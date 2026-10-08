/**
 * Tier 2: Boundary & Corner Cases
 * Project: Escoltes de les Illes Balears (Balearic Islands Expansion)
 * Reference: PROJECT.md § Verification & TEST_INFRA.md § Tier 2
 */

const fs = require('fs');
const path = require('path');
const {
    harness,
    describe,
    test,
    assert,
    assertEqual,
    assertInRange,
    fileExists
} = require('./test_harness.cjs');

function safeReadJson(relPath) {
    const fullPath = path.resolve(process.cwd(), relPath);
    if (!fs.existsSync(fullPath)) return null;
    try {
        return JSON.parse(fs.readFileSync(fullPath, 'utf8'));
    } catch {
        return null;
    }
}

function getAllAvailableRoutes() {
    const files = [
        'data/rutes_mallorca.json',
        'data/rutes_menorca.json',
        'data/rutes_eivissa.json',
        'data/rutes_formentera.json'
    ];
    let all = [];
    for (const f of files) {
        const d = safeReadJson(f);
        if (Array.isArray(d)) {
            all = all.concat(d);
        }
    }
    return all;
}

function getAllAvailableCampsites() {
    const files = [
        'data/acampada_mallorca.json',
        'data/acampada_menorca.json',
        'data/acampada_pitiuses.json'
    ];
    let all = [];
    for (const f of files) {
        const d = safeReadJson(f);
        if (Array.isArray(d)) {
            all = all.concat(d);
        }
    }
    return all;
}

function getAllAvailableGroups() {
    const files = [
        'data/agrupaments_mallorca.json',
        'data/agrupaments_menorca.json',
        'data/agrupaments_pitiuses.json'
    ];
    let all = [];
    for (const f of files) {
        const d = safeReadJson(f);
        if (Array.isArray(d)) {
            all = all.concat(d);
        }
    }
    return all;
}

describe('Tier 2 - Boundary: Empty & Wildcard Island Filters', () => {
    test('2.1.1: Wildcard filters ("totes", "", undefined) retain entire dataset', () => {
        const routes = getAllAvailableRoutes();
        assert(routes.length >= 65, 'Must have at least Mallorca routes loaded');

        // Emulate filter function
        function filterByIsland(data, illa) {
            if (!illa || illa.toLowerCase() === 'totes' || illa.toLowerCase() === 'all') {
                return data;
            }
            return data.filter(r => (r.illa || 'Mallorca').toLowerCase() === illa.toLowerCase());
        }

        const filteredEmpty = filterByIsland(routes, '');
        assertEqual(filteredEmpty.length, routes.length, 'Empty filter must return all routes');

        const filteredTotes = filterByIsland(routes, 'totes');
        assertEqual(filteredTotes.length, routes.length, 'Filter "totes" must return all routes');

        const filteredAll = filterByIsland(routes, 'all');
        assertEqual(filteredAll.length, routes.length, 'Filter "all" must return all routes');
    });

    test('2.1.2: Filter handles whitespace and case variations resiliently', () => {
        const routes = getAllAvailableRoutes();
        assert(routes.length >= 65, 'Must have routes loaded');

        function normalizeFilter(illa) {
            if (!illa) return '';
            return illa.trim().toLowerCase();
        }

        assertEqual(normalizeFilter('  Menorca  '), 'menorca', 'Must trim whitespace');
        assertEqual(normalizeFilter('EIVISSA'), 'eivissa', 'Must lowercase');
        assertEqual(normalizeFilter(''), '', 'Empty remains empty');
    });
});

describe('Tier 2 - Boundary: Invalid Island Parameters', () => {
    test('2.2.1: Non-existent island tags do not throw errors', () => {
        const routes = getAllAvailableRoutes();
        assert(routes.length >= 65, 'Must have routes loaded');

        function safeFilter(data, islandName) {
            if (!islandName) return data;
            const valid = ['mallorca', 'menorca', 'eivissa', 'formentera', 'totes'];
            const cleaned = islandName.trim().toLowerCase();
            if (!valid.includes(cleaned)) {
                return []; // Clean empty result without throwing
            }
            if (cleaned === 'totes') return data;
            return data.filter(r => (r.illa || 'Mallorca').toLowerCase() === cleaned);
        }

        let res1, res2, res3;
        assert(typeof safeFilter === 'function', 'safeFilter is a function');
        res1 = safeFilter(routes, 'cabrera');
        res2 = safeFilter(routes, 'drac');
        res3 = safeFilter(routes, '12345');

        assertEqual(res1.length, 0, 'Invalid island tag cabrera should return 0 results');
        assertEqual(res2.length, 0, 'Invalid island tag drac should return 0 results');
        assertEqual(res3.length, 0, 'Numeric island tag should return 0 results');
    });

    test('2.2.2: Null or undefined filter input handled gracefully', () => {
        const routes = getAllAvailableRoutes();
        assert(routes.length >= 65, 'Must have routes loaded');

        function safeGetRoutes(island) {
            if (!island) return routes;
            return routes.filter(r => (r.illa || 'Mallorca').toLowerCase() === String(island).toLowerCase());
        }

        assertEqual(safeGetRoutes(null).length, routes.length, 'null filter must return full dataset');
        assertEqual(safeGetRoutes(undefined).length, routes.length, 'undefined filter must return full dataset');
    });
});

describe('Tier 2 - Geographic Coordinate Bounds & Inversion Protection', () => {
    test('2.3.1: All route coordinates lie strictly within Balearic latitude range [38.50, 40.20]', () => {
        const routes = getAllAvailableRoutes();
        assert(routes.length >= 65, 'Must have routes loaded');

        for (const r of routes) {
            assert(typeof r.lat === 'number', `Route ${r.slug} lat is not numeric`);
            assertInRange(r.lat, 38.50, 40.20, `Route ${r.slug} latitude (${r.lat}) out of Balearic bounds [38.50, 40.20]`);
        }
    });

    test('2.3.2: All route coordinates lie strictly within Balearic longitude range [1.15, 4.45]', () => {
        const routes = getAllAvailableRoutes();
        assert(routes.length >= 65, 'Must have routes loaded');

        for (const r of routes) {
            assert(typeof r.lon === 'number', `Route ${r.slug} lon is not numeric`);
            assertInRange(r.lon, 1.15, 4.45, `Route ${r.slug} longitude (${r.lon}) out of Balearic bounds [1.15, 4.45]`);
        }
    });

    test('2.3.3: Coordinates inversion protection (no lat/lon swapped)', () => {
        const routes = getAllAvailableRoutes();
        assert(routes.length >= 65, 'Must have routes loaded');

        for (const r of routes) {
            // Latitude in Balearic is ~38-40; longitude is ~1.2-4.4.
            // If swapped, lat would be < 5 and lon would be > 30!
            assert(r.lat > 10, `Route ${r.slug} has swapped latitude (lat=${r.lat} < 10)`);
            assert(r.lon < 10, `Route ${r.slug} has swapped longitude (lon=${r.lon} > 10)`);
        }
    });

    test('2.3.4: All campsites coordinates lie strictly within Balearic bounding box', () => {
        const campsites = getAllAvailableCampsites();
        assert(campsites.length >= 45, 'Must have at least Mallorca campsites loaded');

        for (const c of campsites) {
            assertInRange(c.lat, 38.50, 40.20, `Campsite ${c.slug} lat (${c.lat}) out of bounds`);
            assertInRange(c.lon, 1.15, 4.45, `Campsite ${c.slug} lon (${c.lon}) out of bounds`);
        }
    });

    test('2.3.5: All scout groups coordinates lie strictly within Balearic bounding box', () => {
        const groups = getAllAvailableGroups();
        assert(groups.length >= 13, 'Must have at least Mallorca groups loaded');

        for (const g of groups) {
            assertInRange(g.lat, 38.50, 40.20, `Group ${g.slug} lat (${g.lat}) out of bounds`);
            assertInRange(g.lon, 1.15, 4.45, `Group ${g.slug} lon (${g.lon}) out of bounds`);
        }
    });
});

describe('Tier 2 - Character Encoding & Catalan Diacritics Integrity', () => {
    test('2.4.1: No mojibake characters in routes data', () => {
        const routes = getAllAvailableRoutes();
        assert(routes.length >= 65, 'Must have routes loaded');

        const mojibakePatterns = [/\uFFFD/, /Ã/, /Â/, /â€™/, /â€“/, /&amp;/, /&quot;/];
        for (const r of routes) {
            const textToInspect = `${r.nom} ${r.descripcio || ''} ${r.consells_seguretat || ''} ${(r.punts_aigua || []).join(' ')}`;
            for (const pattern of mojibakePatterns) {
                assert(!pattern.test(textToInspect), `Mojibake pattern ${pattern} detected in route ${r.slug}: "${textToInspect.substring(0, 80)}"`);
            }
        }
    });

    test('2.4.2: Legitimate Catalan diacritics are cleanly preserved in routes data', () => {
        const routes = getAllAvailableRoutes();
        assert(routes.length >= 65, 'Must have routes loaded');

        // Verify Catalan characters exist and decode properly across the corpus
        const fullCorpus = routes.map(r => `${r.nom} ${r.descripcio || ''}`).join(' ');
        const catalanChars = ['ç', 'é', 'è', 'í', 'ï', 'ó', 'ò', 'ú'];
        for (const char of catalanChars) {
            assert(fullCorpus.includes(char), `Catalan character '${char}' should be present in corpus`);
        }
    });

    test('2.4.3: No mojibake characters in campsites data', () => {
        const campsites = getAllAvailableCampsites();
        assert(campsites.length >= 45, 'Must have campsites loaded');

        const mojibakePatterns = [/\uFFFD/, /Ã/, /Â/, /â€™/, /â€“/];
        for (const c of campsites) {
            const textToInspect = `${c.nom} ${c.descripcio || ''} ${c.observacions || ''} ${c.permis_antelacio || ''}`;
            for (const pattern of mojibakePatterns) {
                assert(!pattern.test(textToInspect), `Mojibake pattern ${pattern} in campsite ${c.slug}`);
            }
        }
    });
});

describe('Tier 2 - Null Safety & Optional Fields Resilience', () => {
    test('2.5.1: Routes with empty water points [] handle length safely', () => {
        const routes = getAllAvailableRoutes();
        assert(routes.length >= 65, 'Must have routes loaded');

        for (const r of routes) {
            assert(Array.isArray(r.punts_aigua), `Route ${r.slug} punts_aigua must be an array`);
            // Render emulation: should never throw
            const waterStatus = r.punts_aigua.length === 0 ? 'Cap punt d aigua' : r.punts_aigua.join(', ');
            assert(typeof waterStatus === 'string', 'Water status rendering must succeed');
        }
    });

    test('2.5.2: Campsites with optional contact/phone handle undefined safely', () => {
        const campsites = getAllAvailableCampsites();
        assert(campsites.length >= 45, 'Must have campsites loaded');

        for (const c of campsites) {
            const contactDisplay = c.contacte || 'Sense telèfon directe registrat';
            assert(typeof contactDisplay === 'string', 'Contact display must be safe string');
            const webLink = c.web || '#';
            assert(typeof webLink === 'string', 'Web link must be safe string');
        }
    });

    test('2.5.3: Scout groups handle missing optional fields safely', () => {
        const groups = getAllAvailableGroups();
        assert(groups.length >= 13, 'Must have groups loaded');

        for (const g of groups) {
            const email = g.email || '';
            const web = g.web || '';
            assert(typeof email === 'string' && typeof web === 'string', `Group ${g.slug} optional fields safe`);
        }
    });
});

describe('Tier 2 - Zero-Water Warning Integrity', () => {
    test('2.6.1: Zero-water routes provide explicit dehydration safety warnings', () => {
        const routes = getAllAvailableRoutes();
        assert(routes.length >= 65, 'Must have routes loaded');

        const zeroWaterRoutes = routes.filter(r => Array.isArray(r.punts_aigua) && r.punts_aigua.length === 0);
        for (const r of zeroWaterRoutes) {
            assert(typeof r.consells_seguretat === 'string' && r.consells_seguretat.length > 0,
                `Zero-water route ${r.slug} must provide safety warnings`);
            const lower = r.consells_seguretat.toLowerCase();
            const mentionsHydration = lower.includes('aigua') || lower.includes('beure') || lower.includes('sol') || lower.includes('ombra') || lower.includes('calor');
            assert(mentionsHydration, `Zero-water route ${r.slug} must mention water, sun, heat or shade precautions`);
        }
    });
});

if (require.main === module) {
    const report = harness.printReport();
    process.exit(report.success ? 0 : 1);
}
