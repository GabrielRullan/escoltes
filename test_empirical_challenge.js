/**
 * Empirical Challenge Verification Harness
 * Challenger Gate 2 - 2
 * 
 * Tests functional and security behaviors for:
 * 1. Comment submission payload (authorized: false, no login, exact notification text)
 * 2. Public route display filtering (authorized === true || undefined, pending strictly blocked)
 * 3. Admin moderation actions (real-time counts, Approve, Revoke, Delete)
 * 4. XSS sanitization & hostile payload injection stress tests
 * 5. Full 65-route static AST and contract integrity audit
 */

const fs = require('fs');
const path = require('path');
const vm = require('vm');
const assert = require('assert');

let passedTests = 0;
let failedTests = 0;
const failures = [];

function test(name, fn) {
    try {
        fn();
        passedTests++;
        console.log(`  ✅ [PASS] ${name}`);
    } catch (e) {
        failedTests++;
        failures.push({ name, error: e.message, stack: e.stack });
        console.log(`  ❌ [FAIL] ${name} -> ${e.message}`);
    }
}

async function asyncTest(name, fn) {
    try {
        await fn();
        passedTests++;
        console.log(`  ✅ [PASS] ${name}`);
    } catch (e) {
        failedTests++;
        failures.push({ name, error: e.message, stack: e.stack });
        console.log(`  ❌ [FAIL] ${name} -> ${e.message}`);
    }
}

console.log('================================================================');
console.log('       GATE 2 - 2 EMPIRICAL CHALLENGE VERIFICATION SUITE        ');
console.log('================================================================\n');

// Load template code from scripts/build_wiki_pages.py and docs/mallorca/admin_comentaris.md
const buildWikiPath = path.resolve(__dirname, 'scripts/build_wiki_pages.py');
const adminPath = path.resolve(__dirname, 'site/mallorca/admin_comentaris/index.html');
const routesDir = path.resolve(__dirname, 'site/mallorca/rutes');

assert(fs.existsSync(buildWikiPath), 'build_wiki_pages.py must exist');
assert(fs.existsSync(adminPath), 'admin_comentaris/index.html must exist');
assert(fs.existsSync(routesDir), 'site/mallorca/rutes must exist');

// -------------------------------------------------------------
// SUITE 1: Comment Submission (submitFirebaseExperience)
// -------------------------------------------------------------
console.log('--- SUITE 1: Comment Submission Functional & Payload Verification ---');

function createMockDOM() {
    const elements = {};
    function getEl(id) {
        if (!elements[id]) {
            elements[id] = {
                id,
                value: '',
                innerText: '',
                innerHTML: '',
                style: {},
                disabled: false
            };
        }
        return elements[id];
    }
    // Pre-populate known element IDs
    [
        'exp-nom', 'exp-email', 'exp-agrupament', 'exp-branca', 'exp-puntuacio',
        'exp-data', 'exp-comentari', 'exp-status-msg', 'exp-submit-btn',
        'exp-form-container', 'toggle-exp-form-btn', 'experiences-list-container',
        'exp-summary-title', 'exp-summary-subtitle',
        'pending-count-badge', 'approved-count-badge',
        'pending-comments-list', 'approved-comments-list'
    ].forEach(id => getEl(id));

    return {
        elements,
        document: {
            getElementById: (id) => getEl(id),
            addEventListener: () => {},
            readyState: 'complete'
        }
    };
}

function extractScriptFromHtml(html, identifier) {
    const scriptRegex = /<script\b[^>]*>([\s\S]*?)<\/script>/gi;
    let match;
    while ((match = scriptRegex.exec(html)) !== null) {
        if (match[1].includes(identifier)) {
            return match[1];
        }
    }
    return null;
}

// Read sample route HTML
const sampleRouteSlug = 'avenc-de-son-pou';
const sampleRouteHtml = fs.readFileSync(path.join(routesDir, sampleRouteSlug, 'index.html'), 'utf8');
const routeScriptCode = extractScriptFromHtml(sampleRouteHtml, 'submitFirebaseExperience');

assert(routeScriptCode, 'Could not extract route comments script from sample route HTML');

// Test 1.1: Syntax validation of the route script
test('Route script parses cleanly into V8 AST', () => {
    new vm.Script(routeScriptCode);
});

// Test 1.2: Simulation of submitFirebaseExperience
(async () => {
    await asyncTest('Submission requires no login, sets authorized: false, and shows notification', async () => {
        const dom = createMockDOM();
        const firestoreCalls = { addedDocs: [] };

        const mockFirebase = {
            apps: [{}],
            firestore: Object.assign(() => ({
                collection: (colName) => ({
                    add: async (doc) => {
                        firestoreCalls.addedDocs.push({ collection: colName, doc });
                        return { id: 'mock-doc-123' };
                    },
                    where: () => ({ onSnapshot: () => {} })
                })
            }), {
                FieldValue: {
                    serverTimestamp: () => 'SERVER_TIMESTAMP'
                }
            })
        };

        const sandbox = {
            window: {},
            document: dom.document,
            firebase: mockFirebase,
            console: { log: () => {}, warn: () => {}, error: () => {} },
            setTimeout: (cb) => cb(),
            Number: Number,
            Math: Math,
            String: String,
            parseInt: parseInt
        };
        sandbox.window = sandbox;

        vm.createContext(sandbox);
        vm.runInContext(routeScriptCode, sandbox);

        // Prepopulate form fields
        dom.elements['exp-nom'].value = 'Pau Rullan';
        dom.elements['exp-email'].value = 'pau@escoltes.cat';
        dom.elements['exp-agrupament'].value = 'AE Serra de Tramuntana';
        dom.elements['exp-branca'].value = 'Pioners/Rangers';
        dom.elements['exp-puntuacio'].value = '5';
        dom.elements['exp-data'].value = 'Abril 2026';
        dom.elements['exp-comentari'].value = 'Ruta excel·lent per a pioners, portau aigua abundant!';

        // Execute submission
        await sandbox.submitFirebaseExperience('avenc-de-son-pou');

        // Check Firestore add call
        assert.strictEqual(firestoreCalls.addedDocs.length, 1, 'Firestore add should be called once');
        const writtenDoc = firestoreCalls.addedDocs[0].doc;

        assert.strictEqual(writtenDoc.ruta_slug, 'avenc-de-son-pou', 'Slug must match');
        assert.strictEqual(writtenDoc.nom, 'Pau Rullan', 'Name must match');
        assert.strictEqual(writtenDoc.email, 'pau@escoltes.cat', 'Email must match');
        assert.strictEqual(writtenDoc.authorized, false, 'Payload MUST strictly have authorized: false');
        assert.strictEqual(typeof writtenDoc.authorized, 'boolean', 'authorized must be boolean');

        // Check Notification Text
        const expectedNotification = "✅ Comentari enviat amb èxit! Està pendent d'autorització per part de l'administrador per ser visible públicament.";
        assert.strictEqual(dom.elements['exp-status-msg'].innerText, '', 'Status msg should be cleared after timeout');
        // Let's test the text right after add by testing without immediate timeout reset
    });

    await asyncTest('Submission displays exact required notification message before clear', async () => {
        const dom = createMockDOM();
        let capturedSuccessText = '';

        const mockFirebase = {
            apps: [{}],
            firestore: Object.assign(() => ({
                collection: () => ({
                    add: async (doc) => ({ id: 'mock-123' })
                })
            }), {
                FieldValue: { serverTimestamp: () => 'TS' }
            })
        };

        const sandbox = {
            window: {},
            document: dom.document,
            firebase: mockFirebase,
            console: { log: () => {}, warn: () => {}, error: () => {} },
            setTimeout: (cb, ms) => {
                // capture status msg before timeout clears it
                capturedSuccessText = dom.elements['exp-status-msg'].innerText;
            },
            Number: Number,
            Math: Math,
            String: String,
            parseInt: parseInt
        };
        sandbox.window = sandbox;

        vm.createContext(sandbox);
        vm.runInContext(routeScriptCode, sandbox);

        dom.elements['exp-nom'].value = 'Marta';
        dom.elements['exp-email'].value = 'marta@escoltes.cat';
        dom.elements['exp-agrupament'].value = 'AE Ciutat';
        dom.elements['exp-branca'].value = 'Llops/Daines';
        dom.elements['exp-puntuacio'].value = '4';
        dom.elements['exp-comentari'].value = 'Bonica excursió de primavera.';

        await sandbox.submitFirebaseExperience('avenc-de-son-pou');

        const expectedText = "✅ Comentari enviat amb èxit! Està pendent d'autorització per part de l'administrador per ser visible públicament.";
        assert.strictEqual(capturedSuccessText, expectedText, `Expected: "${expectedText}", Actual: "${capturedSuccessText}"`);
    });

    await asyncTest('Validation guards prevent submission on missing required fields', async () => {
        const dom = createMockDOM();
        let firestoreCalled = false;

        const mockFirebase = {
            apps: [{}],
            firestore: () => ({
                collection: () => ({
                    add: async () => { firestoreCalled = true; }
                })
            })
        };

        const sandbox = {
            window: {},
            document: dom.document,
            firebase: mockFirebase,
            console: { log: () => {}, warn: () => {}, error: () => {} },
            setTimeout: () => {},
            Number, Math, String, parseInt
        };
        sandbox.window = sandbox;
        vm.createContext(sandbox);
        vm.runInContext(routeScriptCode, sandbox);

        // Missing name
        dom.elements['exp-nom'].value = '';
        await sandbox.submitFirebaseExperience('test-slug');
        assert.strictEqual(firestoreCalled, false, 'Should not submit without name');
        assert(dom.elements['exp-status-msg'].innerText.includes('nom'), 'Must warn about missing name');

        // Invalid email
        dom.elements['exp-nom'].value = 'Test User';
        dom.elements['exp-email'].value = 'invalid-email-without-at';
        await sandbox.submitFirebaseExperience('test-slug');
        assert.strictEqual(firestoreCalled, false, 'Should not submit with invalid email');
        assert(dom.elements['exp-status-msg'].innerText.includes('electrònic'), 'Must warn about invalid email');

        // Short comment
        dom.elements['exp-email'].value = 'valid@email.com';
        dom.elements['exp-agrupament'].value = 'AE Test';
        dom.elements['exp-comentari'].value = 'abc'; // < 5 chars
        await sandbox.submitFirebaseExperience('test-slug');
        assert.strictEqual(firestoreCalled, false, 'Should not submit with comment < 5 chars');
        assert(dom.elements['exp-status-msg'].innerText.includes('mínim 5 caràcters'), 'Must warn about short comment');
    });

    // -------------------------------------------------------------
    // SUITE 2: Public Route Display Filtering
    // -------------------------------------------------------------
    console.log('\n--- SUITE 2: Public Route Display Filtering Verification ---');

    await asyncTest('initFirebaseExperiences strictly filters out pending comments (authorized: false)', async () => {
        const dom = createMockDOM();
        let snapshotCallback = null;

        const mockFirebase = {
            apps: [{}],
            firestore: () => ({
                collection: (col) => ({
                    where: (field, op, val) => {
                        assert.strictEqual(field, 'ruta_slug', 'Query must filter by ruta_slug');
                        assert.strictEqual(op, '==');
                        assert.strictEqual(val, 'avenc-de-son-pou');
                        return {
                            onSnapshot: (cb) => {
                                snapshotCallback = cb;
                            }
                        };
                    }
                })
            })
        };

        const sandbox = {
            window: {},
            document: dom.document,
            firebase: mockFirebase,
            console: { log: () => {}, warn: () => {}, error: () => {} },
            setTimeout: () => {},
            Number, Math, String, parseInt
        };
        sandbox.window = sandbox;
        vm.createContext(sandbox);
        vm.runInContext(routeScriptCode, sandbox);

        assert(typeof snapshotCallback === 'function', 'onSnapshot listener must be registered');

        // Emit snapshot with a mix of comments
        const mockSnapshot = [
            { id: '1', data: () => ({ nom: 'Pending 1', comentari: 'Pending secret comment 1', authorized: false, puntuacio: 5 }) },
            { id: '2', data: () => ({ nom: 'Approved 1', comentari: 'Visible approved comment 1', authorized: true, puntuacio: 5 }) },
            { id: '3', data: () => ({ nom: 'Legacy 1', comentari: 'Visible legacy comment without authorized field', puntuacio: 4 }) }, // authorized undefined
            { id: '4', data: () => ({ nom: 'Invalid String', comentari: 'Should NOT show string authorized', authorized: 'true', puntuacio: 5 }) },
            { id: '5', data: () => ({ nom: 'Null Authorized', comentari: 'Should NOT show null', authorized: null, puntuacio: 5 }) },
            { id: '6', data: () => ({ nom: 'Zero Authorized', comentari: 'Should NOT show zero', authorized: 0, puntuacio: 5 }) },
            { id: '7', data: () => ({ nom: 'Pending 2', comentari: 'Pending secret comment 2', authorized: false, puntuacio: 3 }) }
        ];

        snapshotCallback(mockSnapshot);

        const renderedHtml = dom.elements['experiences-list-container'].innerHTML;

        // Pending comments must strictly NOT appear
        assert(!renderedHtml.includes('Pending secret comment 1'), 'Pending comment 1 must NOT be in public HTML');
        assert(!renderedHtml.includes('Pending secret comment 2'), 'Pending comment 2 must NOT be in public HTML');
        assert(!renderedHtml.includes('Should NOT show string authorized'), 'String authorized must NOT be in public HTML');
        assert(!renderedHtml.includes('Should NOT show null'), 'Null authorized must NOT be in public HTML');
        assert(!renderedHtml.includes('Should NOT show zero'), 'Zero authorized must NOT be in public HTML');

        // Approved and legacy comments MUST appear
        assert(renderedHtml.includes('Visible approved comment 1'), 'Approved comment 1 must be in public HTML');
        assert(renderedHtml.includes('Visible legacy comment without authorized field'), 'Legacy comment must be in public HTML');
    });

    // -------------------------------------------------------------
    // SUITE 3: Admin Moderation Interface
    // -------------------------------------------------------------
    console.log('\n--- SUITE 3: Admin Moderation Panel Verification ---');

    const adminHtml = fs.readFileSync(adminPath, 'utf8');
    const adminScriptCode = extractScriptFromHtml(adminHtml, 'initAdminComments');
    assert(adminScriptCode, 'Could not extract admin script from admin_comentaris/index.html');

    test('Admin moderation script parses cleanly into V8 AST', () => {
        new vm.Script(adminScriptCode);
    });

    await asyncTest('Admin page partitions comments and renders real-time counts correctly', async () => {
        const dom = createMockDOM();
        let snapshotCallback = null;

        const mockFirebase = {
            apps: [{}],
            firestore: Object.assign(() => ({
                collection: (col) => {
                    assert.strictEqual(col, 'experiencies');
                    return {
                        onSnapshot: (cb) => {
                            snapshotCallback = cb;
                        }
                    };
                }
            }), {
                FieldValue: { serverTimestamp: () => 'TS' }
            })
        };

        const sandbox = {
            window: {},
            document: dom.document,
            firebase: mockFirebase,
            console: { log: () => {}, warn: () => {}, error: () => {} },
            confirm: () => true,
            alert: () => {},
            encodeURI: encodeURI,
            encodeURIComponent: encodeURIComponent,
            Number, Math, String, parseInt, Date
        };
        sandbox.window = sandbox;
        vm.createContext(sandbox);
        vm.runInContext(adminScriptCode, sandbox);

        assert(typeof snapshotCallback === 'function', 'Admin onSnapshot listener registered');

        // Snapshot with 3 pending and 2 approved
        const snapshot = [
            { id: 'doc-p1', data: () => ({ nom: 'P1', comentari: 'Pending 1', authorized: false, ruta_slug: 'ruta-1' }) },
            { id: 'doc-p2', data: () => ({ nom: 'P2', comentari: 'Pending 2', authorized: false, ruta_slug: 'ruta-2' }) },
            { id: 'doc-p3', data: () => ({ nom: 'P3', comentari: 'Pending 3 (legacy unreviewed)', ruta_slug: 'ruta-3' }) }, // authorized undefined
            { id: 'doc-a1', data: () => ({ nom: 'A1', comentari: 'Approved 1', authorized: true, ruta_slug: 'ruta-1' }) },
            { id: 'doc-a2', data: () => ({ nom: 'A2', comentari: 'Approved 2', authorized: true, ruta_slug: 'ruta-4' }) }
        ];

        snapshotCallback(snapshot);

        // Check counts
        assert.strictEqual(dom.elements['pending-count-badge'].innerText, '3 pendents');
        assert.strictEqual(dom.elements['approved-count-badge'].innerText, '2 aprovats');

        // Check pending container content
        const pendingHtml = dom.elements['pending-comments-list'].innerHTML;
        assert(pendingHtml.includes('Pending 1'), 'Pending list must contain P1');
        assert(pendingHtml.includes('Pending 2'), 'Pending list must contain P2');
        assert(pendingHtml.includes('Pending 3'), 'Pending list must contain P3');
        assert(pendingHtml.includes('approveComment(\'doc-p1\')'), 'Pending list must contain Approve button');
        assert(pendingHtml.includes('deleteComment(\'doc-p1\')'), 'Pending list must contain Delete button');

        // Check approved container content
        const approvedHtml = dom.elements['approved-comments-list'].innerHTML;
        assert(approvedHtml.includes('Approved 1'), 'Approved list must contain A1');
        assert(approvedHtml.includes('Approved 2'), 'Approved list must contain A2');
        assert(approvedHtml.includes('revokeComment(\'doc-a1\')'), 'Approved list must contain Revoke button');
        assert(approvedHtml.includes('deleteComment(\'doc-a1\')'), 'Approved list must contain Delete button');
    });

    await asyncTest('Admin actions: approveComment updates { authorized: true }', async () => {
        const dom = createMockDOM();
        const updateCalls = [];

        const mockFirebase = {
            apps: [{}],
            firestore: Object.assign(() => ({
                collection: () => ({
                    doc: (id) => ({
                        update: async (data) => updateCalls.push({ id, data })
                    }),
                    onSnapshot: () => {}
                })
            }), {
                FieldValue: { serverTimestamp: () => 'TS' }
            })
        };

        const sandbox = {
            window: {},
            document: dom.document,
            firebase: mockFirebase,
            console: { log: () => {}, warn: () => {}, error: () => {} },
            confirm: () => true,
            alert: () => {},
            Number, Math, String, parseInt, Date
        };
        sandbox.window = sandbox;
        vm.createContext(sandbox);
        vm.runInContext(adminScriptCode, sandbox);

        await sandbox.approveComment('test-doc-99');

        assert.strictEqual(updateCalls.length, 1);
        assert.strictEqual(updateCalls[0].id, 'test-doc-99');
        assert.strictEqual(updateCalls[0].data.authorized, true, 'Must set authorized: true');
        assert.strictEqual(updateCalls[0].data.approvedAt, 'TS', 'Must set approvedAt timestamp');
    });

    await asyncTest('Admin actions: revokeComment updates { authorized: false }', async () => {
        const dom = createMockDOM();
        const updateCalls = [];

        const mockFirebase = {
            apps: [{}],
            firestore: Object.assign(() => ({
                collection: () => ({
                    doc: (id) => ({
                        update: async (data) => updateCalls.push({ id, data })
                    }),
                    onSnapshot: () => {}
                })
            }), {
                FieldValue: { serverTimestamp: () => 'TS' }
            })
        };

        const sandbox = {
            window: {},
            document: dom.document,
            firebase: mockFirebase,
            console: { log: () => {}, warn: () => {}, error: () => {} },
            confirm: () => true,
            alert: () => {},
            Number, Math, String, parseInt, Date
        };
        sandbox.window = sandbox;
        vm.createContext(sandbox);
        vm.runInContext(adminScriptCode, sandbox);

        await sandbox.revokeComment('test-doc-99');

        assert.strictEqual(updateCalls.length, 1);
        assert.strictEqual(updateCalls[0].id, 'test-doc-99');
        assert.strictEqual(updateCalls[0].data.authorized, false, 'Must set authorized: false');
    });

    await asyncTest('Admin actions: deleteComment calls doc.delete()', async () => {
        const dom = createMockDOM();
        const deleteCalls = [];

        const mockFirebase = {
            apps: [{}],
            firestore: Object.assign(() => ({
                collection: () => ({
                    doc: (id) => ({
                        delete: async () => deleteCalls.push(id)
                    }),
                    onSnapshot: () => {}
                })
            }), {
                FieldValue: { serverTimestamp: () => 'TS' }
            })
        };

        const sandbox = {
            window: {},
            document: dom.document,
            firebase: mockFirebase,
            console: { log: () => {}, warn: () => {}, error: () => {} },
            confirm: () => true,
            alert: () => {},
            Number, Math, String, parseInt, Date
        };
        sandbox.window = sandbox;
        vm.createContext(sandbox);
        vm.runInContext(adminScriptCode, sandbox);

        await sandbox.deleteComment('test-doc-99');

        assert.strictEqual(deleteCalls.length, 1);
        assert.strictEqual(deleteCalls[0], 'test-doc-99');
    });

    // -------------------------------------------------------------
    // SUITE 4: Security & Hostile XSS Injection
    // -------------------------------------------------------------
    console.log('\n--- SUITE 4: Security & Hostile XSS Injection Tests ---');

    test('escapeHtml handles null, undefined, numbers, and strings safely', () => {
        // extract escapeHtml function from route script
        const match = routeScriptCode.match(/function escapeHtml\(text\) \{([\s\S]*?)\}/);
        assert(match, 'escapeHtml must be defined');
        const escapeHtml = new Function('text', match[1]);

        assert.strictEqual(escapeHtml(null), '');
        assert.strictEqual(escapeHtml(undefined), '');
        assert.strictEqual(escapeHtml(123), '123');
        assert.strictEqual(escapeHtml('Hello & <World> "Double" \'Single\''), 'Hello &amp; &lt;World&gt; &quot;Double&quot; &#039;Single&#039;');
    });

    test('Hostile XSS payloads are completely neutralized in route page HTML', () => {
        const dom = createMockDOM();
        const sandbox = {
            window: {},
            document: dom.document,
            console: { log: () => {}, warn: () => {}, error: () => {} },
            Number, Math, String, parseInt
        };
        sandbox.window = sandbox;
        vm.createContext(sandbox);
        vm.runInContext(routeScriptCode, sandbox);

        const hostileExperiences = [
            {
                nom: '<script>alert("XSS_NOM")</script>',
                agrupament: '<img src=x onerror=alert("XSS_AGRUPAMENT")>',
                branca: '<svg/onload=alert("XSS_BRANCA")>',
                data: '"><b onmouseover="alert(\'XSS_DATA\')">date</b>',
                comentari: '<iframe src="javascript:alert(\'XSS_COMENTARI\')"></iframe><a href="javascript:alert(1)">click</a>',
                puntuacio: 5
            }
        ];

        sandbox.renderExperiencesList(hostileExperiences);
        const html = dom.elements['experiences-list-container'].innerHTML;

        // Verify that raw hostile HTML tags are escaped and cannot be parsed as executable HTML
        assert(!html.includes('<script>'), 'Must NOT contain raw <script>');
        assert(!html.includes('<img src=x onerror='), 'Must NOT contain raw <img onerror>');
        assert(!html.includes('<svg/onload='), 'Must NOT contain raw <svg/onload>');
        assert(!html.includes('<iframe'), 'Must NOT contain raw <iframe');
        assert(!html.includes('<a href="javascript:'), 'Must NOT contain raw unescaped javascript link in comment');

        // Verify proper entities
        assert(html.includes('&lt;script&gt;'), 'Must have &lt;script&gt;');
        assert(html.includes('&lt;img src=x'), 'Must have &lt;img');
        assert(html.includes('&lt;svg/onload='), 'Must have &lt;svg');
        assert(html.includes('&lt;iframe'), 'Must have &lt;iframe');
    });

    test('Hostile XSS payloads are completely neutralized in admin panel HTML', () => {
        const dom = createMockDOM();
        const sandbox = {
            window: {},
            document: dom.document,
            console: { log: () => {}, warn: () => {}, error: () => {} },
            encodeURI, encodeURIComponent,
            Number, Math, String, parseInt, Date
        };
        sandbox.window = sandbox;
        vm.createContext(sandbox);
        vm.runInContext(adminScriptCode, sandbox);

        // Test with snapshot containing hostile payloads
        let snapshotCb;
        sandbox.firebase = {
            apps: [{}],
            firestore: () => ({
                collection: () => ({
                    onSnapshot: (cb) => { snapshotCb = cb; }
                })
            })
        };
        sandbox.initAdminComments();

        const hostileSnapshot = [
            {
                id: 'bad-id-1',
                data: () => ({
                    nom: '<script>alert("admin_nom")</script>',
                    email: 'attacker" onfocus="alert(1)" x="',
                    agrupament: '<b onfocus=alert(1)>Group</b>',
                    branca: '<script>alert(1)</script>',
                    comentari: '<img src=x onerror=alert("admin_comentari")>',
                    ruta_slug: 'malicious/../slug"><script>alert(1)</script>',
                    authorized: false,
                    puntuacio: 5
                })
            }
        ];

        snapshotCb(hostileSnapshot);

        const pendingHtml = dom.elements['pending-comments-list'].innerHTML;
        assert(!pendingHtml.includes('<script>'), 'Admin pending must NOT contain raw <script>');
        assert(!pendingHtml.includes('<img src=x onerror='), 'Admin pending must NOT contain raw <img onerror>');
        assert(pendingHtml.includes('&lt;script&gt;'), 'Admin pending must escape script tag');
        assert(pendingHtml.includes('&lt;img src=x'), 'Admin pending must escape img tag');
    });

    // -------------------------------------------------------------
    // SUITE 5: Full 65 Routes Static Audit
    // -------------------------------------------------------------
    console.log('\n--- SUITE 5: Static AST & Contract Audit across All 65 Routes ---');

    test('All 65 routes contain exact success notification and valid JS AST', () => {
        const routeDirs = fs.readdirSync(routesDir).filter(f => fs.statSync(path.join(routesDir, f)).isDirectory());
        assert.strictEqual(routeDirs.length, 65, 'Must have exactly 65 route directories');

        const expectedNotification = "✅ Comentari enviat amb èxit! Està pendent d'autorització per part de l'administrador per ser visible públicament.";
        let checked = 0;

        for (const dir of routeDirs) {
            const htmlPath = path.join(routesDir, dir, 'index.html');
            assert(fs.existsSync(htmlPath), `Route index.html must exist: ${dir}`);
            const content = fs.readFileSync(htmlPath, 'utf8');

            // 1. Success notification presence
            assert(content.includes(expectedNotification), `Route ${dir} missing exact notification text`);

            // 2. Double quote syntax fix in script
            assert(content.includes(`statusMsg.innerText = "${expectedNotification}";`), `Route ${dir} does not use double-quote syntax`);

            // 3. Payload authorized: false
            assert(content.includes('authorized: false,'), `Route ${dir} missing authorized: false in payload`);

            // 4. Display filter
            assert(content.includes('data.authorized === true || data.authorized === undefined'), `Route ${dir} missing display filter`);

            // 5. AST parse test
            const script = extractScriptFromHtml(content, 'submitFirebaseExperience');
            assert(script, `Route ${dir} missing script`);
            new vm.Script(script, { filename: `${dir}/index.html` });

            checked++;
        }

        assert.strictEqual(checked, 65, 'All 65 routes audited');
    });

    // -------------------------------------------------------------
    // SUITE 6: Edge Cases & Adversarial Robustness
    // -------------------------------------------------------------
    console.log('\n--- SUITE 6: Edge Cases & Adversarial Robustness ---');

    test('Extreme scores, nulls, and unusual fields do not crash renderers', () => {
        const dom = createMockDOM();
        const sandbox = {
            window: {},
            document: dom.document,
            console: { log: () => {}, warn: () => {}, error: () => {} },
            encodeURI, encodeURIComponent,
            Number, Math, String, parseInt, Date
        };
        sandbox.window = sandbox;
        vm.createContext(sandbox);
        vm.runInContext(routeScriptCode, sandbox);
        vm.runInContext(adminScriptCode, sandbox);

        const edgeCaseComments = [
            { puntuacio: -9999, nom: null, comentari: undefined, data: 123 },
            { puntuacio: 99999999, nom: '', comentari: '', agrupament: null },
            { puntuacio: 'invalid', nom: 'Normal', comentari: 'Valid comment' },
            { puntuacio: NaN, nom: 'NaN Score', comentari: 'Valid comment' },
            { puntuacio: 3.7, createdAt: { seconds: 1700000000, toDate: () => new Date(1700000000000) } }
        ];

        // Should not throw
        sandbox.renderExperiencesList(edgeCaseComments);
        let adminSnapshotCb;
        sandbox.firebase = {
            apps: [{}],
            firestore: () => ({
                collection: () => ({
                    onSnapshot: (cb) => { adminSnapshotCb = cb; }
                })
            })
        };
        sandbox.initAdminComments();
        adminSnapshotCb(edgeCaseComments.map((c, i) => ({ id: `doc-${i}`, data: () => c })));

        const routeHtml = dom.elements['experiences-list-container'].innerHTML;
        assert(routeHtml.includes('⭐'), 'Should render stars safely without memory error');
    });

    // Print Summary
    console.log('\n================================================================');
    console.log(`TOTAL TESTS:   ${passedTests + failedTests}`);
    console.log(`PASSED:        ${passedTests}`);
    console.log(`FAILED:        ${failedTests}`);
    console.log('================================================================\n');

    if (failedTests > 0) {
        console.error('FAILED TEST DETAILS:');
        failures.forEach(f => {
            console.error(`- ${f.name}: ${f.error}`);
        });
        process.exit(1);
    } else {
        console.log(`🎉 ALL ${passedTests} EMPIRICAL TESTS PASSED SUCCESSFULLY WITH ZERO FAILURES.`);
        process.exit(0);
    }
})();
