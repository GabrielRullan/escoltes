/**
 * Adversarial Stress & Invariant Test Suite for Milestone 1
 * Project: Escoltes de les Illes Balears (Balearic Islands Expansion)
 * Author: Challenger 1 (Empirical Challenger)
 * Standard: Node.js CommonJS Native TAP v13 & ANSI Formatted Runner
 */

const fs = require('fs');
const path = require('path');
const { createServer } = require('vite');
const {
    harness,
    describe,
    test,
    assert,
    assertEqual,
    assertInRange
} = require('./test_harness.cjs');

function safeReadJson(relPath) {
    const fullPath = path.resolve(process.cwd(), relPath);
    if (!fs.existsSync(fullPath)) return null;
    return JSON.parse(fs.readFileSync(fullPath, 'utf8'));
}

// Bounding box definitions per island
const BOUNDS = {
    Mallorca: { latMin: 39.15, latMax: 40.00, lonMin: 2.30, lonMax: 3.55 },
    Menorca: { latMin: 39.75, latMax: 40.10, lonMin: 3.75, lonMax: 4.35 },
    Eivissa: { latMin: 38.80, latMax: 39.15, lonMin: 1.15, lonMax: 1.65 },
    Formentera: { latMin: 38.60, latMax: 38.80, lonMin: 1.35, lonMax: 1.60 },
    Balears: { latMin: 38.50, latMax: 40.20, lonMin: 1.15, lonMax: 4.45 }
};

async function runAdversarialSuite() {
    // -------------------------------------------------------------
    // SUITE 1: 97 Routes Data Invariants
    // -------------------------------------------------------------
    describe('Adversarial 1: All 97 Routes Data Invariants', () => {
        const rMallorca = safeReadJson('data/rutes_mallorca.json') || [];
        const rMenorca = safeReadJson('data/rutes_menorca.json') || [];
        const rEivissa = safeReadJson('data/rutes_eivissa.json') || [];
        const rFormentera = safeReadJson('data/rutes_formentera.json') || [];

        const allRoutes = [
            ...rMallorca.map(r => ({ ...r, illa: r.illa || 'Mallorca' })),
            ...rMenorca.map(r => ({ ...r, illa: r.illa || 'Menorca' })),
            ...rEivissa.map(r => ({ ...r, illa: r.illa || 'Eivissa' })),
            ...rFormentera.map(r => ({ ...r, illa: r.illa || 'Formentera' }))
        ];

        test('1.1: Exact Route Counts and Archipelago Partitioning', () => {
            assertEqual(rMallorca.length, 65, 'Mallorca routes count must be exactly 65');
            assertEqual(rMenorca.length, 22, 'Menorca routes count must be exactly 22 (20 GR-223 + 2 variants)');
            assertEqual(rEivissa.length, 7, 'Eivissa routes count must be exactly 7');
            assertEqual(rFormentera.length, 3, 'Formentera routes count must be exactly 3');
            assertEqual(allRoutes.length, 97, 'Total archipelago routes count must be exactly 97');
        });

        test('1.2: Slug Uniqueness & Strict URL-Safe Format Across All 97 Routes', () => {
            const slugMap = new Map();
            const urlSafeRegex = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;

            for (const r of allRoutes) {
                assert(typeof r.slug === 'string' && r.slug.length > 0, `Route must have non-empty slug: ${JSON.stringify(r.nom)}`);
                assert(urlSafeRegex.test(r.slug), `Route slug must be strictly lowercase kebab-case: "${r.slug}"`);
                assert(!slugMap.has(r.slug), `Duplicate slug detected! Slug "${r.slug}" found in ${slugMap.get(r.slug)} and ${r.illa}`);
                slugMap.set(r.slug, r.illa);
            }
            assertEqual(slugMap.size, 97, 'All 97 slugs must be completely unique');
        });

        test('1.3: Distance & Positive Elevation Gain Invariants', () => {
            for (const r of allRoutes) {
                // Distance must be a positive, finite number > 0
                assert(typeof r.distancia_km === 'number' && !isNaN(r.distancia_km), `distancia_km must be number for ${r.slug}`);
                assert(r.distancia_km > 0, `distancia_km must be > 0 for ${r.slug}, got ${r.distancia_km}`);
                assertInRange(r.distancia_km, 0.5, 55.0, `distancia_km out of realistic hiking range for ${r.slug}: ${r.distancia_km}`);

                // Elevation gain must be a positive number >= 0
                assert(typeof r.desnivell_positiu_m === 'number' && !isNaN(r.desnivell_positiu_m), `desnivell_positiu_m must be number for ${r.slug}`);
                assert(r.desnivell_positiu_m >= 0, `desnivell_positiu_m must be >= 0 for ${r.slug}, got ${r.desnivell_positiu_m}`);
                assertInRange(r.desnivell_positiu_m, 0, 2000, `desnivell_positiu_m out of realistic range for ${r.slug}: ${r.desnivell_positiu_m}`);
            }
        });

        test('1.4: Geographical Coordinate Bounds & Coordinate Inversion Protection', () => {
            for (const r of allRoutes) {
                const b = BOUNDS[r.illa];
                assert(b, `Unknown island ${r.illa} for route ${r.slug}`);

                // Origin coordinates check
                assert(typeof r.lat === 'number' && !isNaN(r.lat), `lat must be number for ${r.slug}`);
                assert(typeof r.lon === 'number' && !isNaN(r.lon), `lon must be number for ${r.slug}`);
                assertInRange(r.lat, b.latMin, b.latMax, `lat out of ${r.illa} bounds for ${r.slug}: ${r.lat}`);
                assertInRange(r.lon, b.lonMin, b.lonMax, `lon out of ${r.illa} bounds for ${r.slug}: ${r.lon}`);

                // Lat/Lon inversion check
                assert(r.lat > r.lon, `Latitude must be greater than longitude in Balearics for ${r.slug} (lat: ${r.lat}, lon: ${r.lon})`);

                // Track coordinates check
                if (Array.isArray(r.track_coordinates) && r.track_coordinates.length > 0) {
                    for (let i = 0; i < r.track_coordinates.length; i++) {
                        const pt = r.track_coordinates[i];
                        assert(Array.isArray(pt) && pt.length === 2, `Track point ${i} must be [lat, lon] array in ${r.slug}`);
                        const [tLat, tLon] = pt;
                        assertInRange(tLat, b.latMin, b.latMax, `Track pt ${i} lat out of bounds in ${r.slug}: ${tLat}`);
                        assertInRange(tLon, b.lonMin, b.lonMax, `Track pt ${i} lon out of bounds in ${r.slug}: ${tLon}`);
                        assert(tLat > tLon, `Track pt ${i} lat/lon inverted in ${r.slug}`);
                    }
                }
            }
        });

        test('1.5: Safety Tips Non-Emptiness & Essential Content Invariants', () => {
            for (const r of allRoutes) {
                const tips = r.consells_seguretat;
                assert(typeof tips === 'string', `consells_seguretat must be string for ${r.slug}`);
                assert(tips.trim().length >= 15, `consells_seguretat too short (<15 chars) for ${r.slug}: "${tips}"`);

                // No placeholder text
                const lowerTips = tips.toLowerCase();
                assert(!lowerTips.includes('todo') && !lowerTips.includes('lorem ipsum') && !lowerTips.includes('tbd'),
                    `Placeholder text found in safety tips for ${r.slug}: "${tips}"`);

                // Formentera specific: sun/heat or cliff warning
                if (r.illa === 'Formentera') {
                    const hasSunOrCliff = lowerTips.includes('sol') || lowerTips.includes('calor') ||
                        lowerTips.includes('insolació') || lowerTips.includes('penya-segat') ||
                        lowerTips.includes('deshidratació') || lowerTips.includes('aigua');
                    assert(hasSunOrCliff, `Formentera route ${r.slug} must include sun/heat/cliff safety warning`);
                }

                // Zero water routes: must warn
                if (Array.isArray(r.punts_aigua) && r.punts_aigua.length === 0) {
                    const warnsWater = lowerTips.includes('aigua') || lowerTips.includes('hidratació') || lowerTips.includes('sense font');
                    assert(warnsWater, `Route ${r.slug} has zero water points but no water warning in consells_seguretat`);
                }
            }
        });

        test('1.6: Scout Unit Suitability Invariants', () => {
            for (const r of allRoutes) {
                assert(Array.isArray(r.apte_unitats), `apte_unitats must be an array for ${r.slug}`);
                assert(r.apte_unitats.length > 0, `apte_unitats cannot be empty for ${r.slug}`);

                // Demanding routes should not admit Castors without explicit warnings
                if (r.dificultat === 'Exigent') {
                    const admitsCastors = r.apte_unitats.some(u => u.toLowerCase().includes('castor'));
                    assert(!admitsCastors, `Exigent route ${r.slug} must not be recommended for Castors`);
                }
            }
        });
    });

    // -------------------------------------------------------------
    // SUITE 2: Campsites, Groups, and Transport Invariants
    // -------------------------------------------------------------
    describe('Adversarial 2: Facilities, Groups, and Transport Invariants', () => {
        const cMallorca = safeReadJson('data/acampada_mallorca.json') || [];
        const cMenorca = safeReadJson('data/acampada_menorca.json') || [];
        const cPitiuses = safeReadJson('data/acampada_pitiuses.json') || [];
        const allCampsites = [
            ...cMallorca.map(c => ({ ...c, illa: c.illa || 'Mallorca' })),
            ...cMenorca.map(c => ({ ...c, illa: c.illa || 'Menorca' })),
            ...cPitiuses.map(c => ({ ...c, illa: c.illa || 'Eivissa' }))
        ];

        const gMallorca = safeReadJson('data/agrupaments_mallorca.json') || [];
        const gMenorca = safeReadJson('data/agrupaments_menorca.json') || [];
        const gPitiuses = safeReadJson('data/agrupaments_pitiuses.json') || [];
        const allGroups = [
            ...gMallorca.map(g => ({ ...g, illa: g.illa || 'Mallorca' })),
            ...gMenorca.map(g => ({ ...g, illa: g.illa || 'Menorca' })),
            ...gPitiuses.map(g => ({ ...g, illa: g.illa || 'Eivissa' }))
        ];

        const tMallorca = safeReadJson('data/transport_mallorca.json') || {};
        const tMenorca = safeReadJson('data/transport_menorca.json') || {};
        const tPitiuses = safeReadJson('data/transport_pitiuses.json') || {};

        test('2.1: Campsite Record Counts and Field Invariants', () => {
            assertEqual(cMallorca.length, 45, 'Mallorca campsites count must be 45');
            assertEqual(cMenorca.length, 8, 'Menorca campsites count must be 8');
            assertEqual(cPitiuses.length, 7, 'Pitiüses campsites count must be 7 (5 Eivissa + 2 Formentera)');
            assertEqual(allCampsites.length, 60, 'Archipelago campsites count must be 60');

            const slugMap = new Map();
            for (const c of allCampsites) {
                assert(typeof c.slug === 'string' && c.slug.length > 0, `Campsite must have slug: ${c.nom}`);
                assert(!slugMap.has(c.slug), `Duplicate campsite slug: ${c.slug}`);
                slugMap.set(c.slug, c.illa);

                assert(typeof c.capacitat === 'number' && c.capacitat > 0, `Capacity must be > 0 for ${c.slug}`);

                const b = BOUNDS[c.illa];
                assertInRange(c.lat, b.latMin, b.latMax, `Campsite lat out of bounds for ${c.slug}: ${c.lat}`);
                assertInRange(c.lon, b.lonMin, b.lonMax, `Campsite lon out of bounds for ${c.slug}: ${c.lon}`);

                // New islands must satisfy Balearic legal framework
                if (c.illa !== 'Mallorca') {
                    assert(typeof c.permis_antelacio === 'string' && c.permis_antelacio.length > 5, `Missing permis_antelacio in ${c.slug}`);
                    assert(typeof c.restriccio_foc === 'string' && c.restriccio_foc.length > 5, `Missing restriccio_foc in ${c.slug}`);
                    assert(typeof c.acces_emergencia === 'string' && c.acces_emergencia.length > 5, `Missing acces_emergencia in ${c.slug}`);
                }
            }
        });

        test('2.2: Scout Groups Counts and Invariants', () => {
            assertEqual(gMallorca.length, 13, 'Mallorca groups must be 13');
            assertEqual(gMenorca.length, 9, 'Menorca groups must be 9');
            assertEqual(gPitiuses.length, 2, 'Pitiüses groups must be 2');
            assertEqual(allGroups.length, 24, 'Total scout groups must be 24');

            const slugMap = new Map();
            for (const g of allGroups) {
                assert(typeof g.slug === 'string' && g.slug.length > 0, `Group must have slug: ${g.nom}`);
                assert(!slugMap.has(g.slug), `Duplicate group slug: ${g.slug}`);
                slugMap.set(g.slug, g.illa);

                const b = BOUNDS[g.illa];
                assertInRange(g.lat, b.latMin, b.latMax, `Group lat out of bounds for ${g.slug}: ${g.lat}`);
                assertInRange(g.lon, b.lonMin, b.lonMax, `Group lon out of bounds for ${g.slug}: ${g.lon}`);
            }
        });

        test('2.3: Public Transport Lines and Coverage', () => {
            const mBus = tMallorca.linies_bus || [];
            const mTrain = tMallorca.linies_tren || [];
            const meBus = tMenorca.linies_bus || [];
            const pBus = tPitiuses.linies_bus || [];

            assertEqual(mBus.length, 18, 'Mallorca bus lines must be 18');
            assertEqual(mTrain.length, 6, 'Mallorca train lines must be 6');
            assertEqual(meBus.length, 12, 'Menorca bus lines must be 12');
            assertEqual(pBus.length, 13, 'Pitiüses bus lines must be 13 (9 Eivissa + 4 Formentera)');

            const totalBus = mBus.length + meBus.length + pBus.length;
            assertEqual(totalBus, 43, 'Total bus lines must be 43');

            for (const line of [...mBus, ...meBus, ...pBus]) {
                assert(typeof line.codi === 'string' && line.codi.length > 0, `Bus line missing codi: ${JSON.stringify(line)}`);
                assert(typeof line.nom === 'string' && line.nom.length > 0, `Bus line missing nom: ${line.codi}`);
            }
        });
    });

    // -------------------------------------------------------------
    // SUITE 3: Dynamic Stress Testing of src/data/*.ts Modules
    // -------------------------------------------------------------
    let viteServer = null;
    let routesMod, campsitesMod, groupsMod, transportMod, islandsMod;

    try {
        viteServer = await createServer({ server: { middlewareMode: true } });
        routesMod = await viteServer.ssrLoadModule('./src/data/routes.ts');
        campsitesMod = await viteServer.ssrLoadModule('./src/data/campsites.ts');
        groupsMod = await viteServer.ssrLoadModule('./src/data/groups.ts');
        transportMod = await viteServer.ssrLoadModule('./src/data/transport.ts');
        islandsMod = await viteServer.ssrLoadModule('./src/data/islands.ts');
    } catch (err) {
        console.error('Failed to load Vite modules:', err);
        throw err;
    }

    describe('Adversarial 3: Dynamic Stress Testing of src/data/*.ts Modules', () => {
        test('3.1: Adversarial getRouteBySlug Edge Cases', () => {
            const { getRouteBySlug } = routesMod;

            // Valid slugs
            const r1 = getRouteBySlug('gr221-etapa-1-port-andratx-trapa');
            assert(r1 && r1.nom.includes('Port d\'Andratx'), 'Should return correct Mallorca route');

            const r2 = getRouteBySlug('gr223-etapa-01-mao-es-grau');
            assert(r2 && r2.nom.includes('Maó'), 'Should return correct Menorca route');

            const r3 = getRouteBySlug('eivissa-ses-salines-torre-portes');
            assert(r3 && r3.illa === 'Eivissa', 'Should return correct Eivissa route');

            const r4 = getRouteBySlug('formentera-cami-sa-pujada-la-mola');
            assert(r4 && r4.illa === 'Formentera', 'Should return correct Formentera route');

            // Adversarial inputs must NOT throw and must return undefined
            assertEqual(getRouteBySlug(''), undefined, 'Empty slug returns undefined');
            assertEqual(getRouteBySlug(null), undefined, 'null slug returns undefined');
            assertEqual(getRouteBySlug(undefined), undefined, 'undefined slug returns undefined');
            assertEqual(getRouteBySlug('non-existent-slug-12345'), undefined, 'Unknown slug returns undefined');
            assertEqual(getRouteBySlug('<script>alert("xss")</script>'), undefined, 'XSS string returns undefined');
            assertEqual(getRouteBySlug('../../../etc/passwd'), undefined, 'Path traversal string returns undefined');
            assertEqual(getRouteBySlug('   '), undefined, 'Spaces only returns undefined');
        });

        test('3.2: Adversarial getRoutesByIsland Case & Whitespace Variations', () => {
            const { getRoutesByIsland, getAllRoutes } = routesMod;
            assertEqual(getAllRoutes().length, 97, 'getAllRoutes returns 97');

            // Standard island names
            assertEqual(getRoutesByIsland('Mallorca').length, 65, 'Mallorca returns 65');
            assertEqual(getRoutesByIsland('Menorca').length, 22, 'Menorca returns 22');
            assertEqual(getRoutesByIsland('Eivissa').length, 7, 'Eivissa returns 7');
            assertEqual(getRoutesByIsland('Formentera').length, 3, 'Formentera returns 3');

            // Case insensitivity
            assertEqual(getRoutesByIsland('mallorca').length, 65, 'lowercase mallorca returns 65');
            assertEqual(getRoutesByIsland('MALLORCA').length, 65, 'UPPERCASE MALLORCA returns 65');
            assertEqual(getRoutesByIsland('mAlLoRcA').length, 65, 'mIxEdCaSe mAlLoRcA returns 65');
            assertEqual(getRoutesByIsland('menorca').length, 22, 'lowercase menorca returns 22');
            assertEqual(getRoutesByIsland('MENORCA').length, 22, 'UPPERCASE MENORCA returns 22');
            assertEqual(getRoutesByIsland('eivissa').length, 7, 'lowercase eivissa returns 7');
            assertEqual(getRoutesByIsland('EIVISSA').length, 7, 'UPPERCASE EIVISSA returns 7');
            assertEqual(getRoutesByIsland('formentera').length, 3, 'lowercase formentera returns 3');
            assertEqual(getRoutesByIsland('FORMENTERA').length, 3, 'UPPERCASE FORMENTERA returns 3');

            // Whitespace handling on island names
            assertEqual(getRoutesByIsland('  Mallorca  ').length, 65, 'Trimmed Mallorca returns 65');
            assertEqual(getRoutesByIsland(' Menorca ').length, 22, 'Trimmed Menorca returns 22');
            assertEqual(getRoutesByIsland('   Eivissa   ').length, 7, 'Trimmed Eivissa returns 7');
            assertEqual(getRoutesByIsland(' Formentera ').length, 3, 'Trimmed Formentera returns 3');

            // Wildcard / All filters
            assertEqual(getRoutesByIsland('totes').length, 97, 'totes returns all 97');
            assertEqual(getRoutesByIsland('TOTES').length, 97, 'TOTES returns all 97');
            assertEqual(getRoutesByIsland('all').length, 97, 'all returns all 97');
            assertEqual(getRoutesByIsland('ALL').length, 97, 'ALL returns all 97');
            assertEqual(getRoutesByIsland('').length, 97, 'empty string returns all 97');
            assertEqual(getRoutesByIsland(undefined).length, 97, 'undefined returns all 97');

            // Non-existent islands return empty array safely without error
            assertEqual(getRoutesByIsland('Atlantis').length, 0, 'Atlantis returns []');
            assertEqual(getRoutesByIsland('Cabrera').length, 0, 'Cabrera returns []');
            assertEqual(getRoutesByIsland('Narnia').length, 0, 'Narnia returns []');
        });

        test('3.3: Adversarial getCampsitesByIsland & getCampsiteBySlug', () => {
            const { getCampsitesByIsland, getCampsiteBySlug, getAllCampsites } = campsitesMod;
            assertEqual(getAllCampsites().length, 60, 'getAllCampsites returns 60');

            // Lookups
            const c1 = getCampsiteBySlug('alberg-sa-vinyeta');
            assert(c1 && c1.illa === 'Menorca', 'Lookup Sa Vinyeta returns Menorca campsite');

            const c2 = getCampsiteBySlug('campament-cala-des-jondal');
            assert(c2 && c2.illa === 'Eivissa', 'Lookup Cala des Jondal returns Eivissa campsite');

            const c3 = getCampsiteBySlug('centre-can-marroig');
            assert(c3 && c3.illa === 'Formentera', 'Lookup Can Marroig returns Formentera campsite');

            // Invalid lookups
            assertEqual(getCampsiteBySlug(''), undefined, 'Empty slug returns undefined');
            assertEqual(getCampsiteBySlug(null), undefined, 'null slug returns undefined');
            assertEqual(getCampsiteBySlug('fake-campsite'), undefined, 'fake campsite returns undefined');

            // Counts per island
            assertEqual(getCampsitesByIsland('Mallorca').length, 45, 'Mallorca campsites 45');
            assertEqual(getCampsitesByIsland('Menorca').length, 8, 'Menorca campsites 8');
            assertEqual(getCampsitesByIsland('Eivissa').length, 5, 'Eivissa campsites 5');
            assertEqual(getCampsitesByIsland('Formentera').length, 2, 'Formentera campsites 2');
            assertEqual(getCampsitesByIsland('totes').length, 60, 'totes campsites 60');
            assertEqual(getCampsitesByIsland('').length, 60, 'empty campsites 60');
            assertEqual(getCampsitesByIsland('   Eivissa   ').length, 5, 'Trimmed Eivissa campsites 5');
        });

        test('3.4: Adversarial getGroupsByIsland & getGroupBySlug', () => {
            const { getGroupsByIsland, getGroupBySlug, getAllGroups } = groupsMod;
            assertEqual(getAllGroups().length, 24, 'getAllGroups returns 24');

            // Lookups
            const g1 = getGroupBySlug('ae-sant-francesc-ferreries');
            assert(g1 && g1.illa === 'Menorca', 'Lookup Ferreries returns Menorca group');

            const g2 = getGroupBySlug('ae-isidor-macabich');
            assert(g2 && g2.illa === 'Eivissa', 'Lookup Macabich returns Eivissa group');

            // Invalid lookups
            assertEqual(getGroupBySlug(''), undefined, 'Empty slug returns undefined');
            assertEqual(getGroupBySlug('fake-group'), undefined, 'Fake group returns undefined');

            // Counts
            assertEqual(getGroupsByIsland('Mallorca').length, 13, 'Mallorca groups 13');
            assertEqual(getGroupsByIsland('Menorca').length, 9, 'Menorca groups 9');
            assertEqual(getGroupsByIsland('Eivissa').length, 2, 'Eivissa groups 2');
            assertEqual(getGroupsByIsland('Formentera').length, 0, 'Formentera groups 0 (none currently active)');
            assertEqual(getGroupsByIsland('totes').length, 24, 'totes groups 24');
        });

        test('3.5: Adversarial getBusLinesByIsland & Transport', () => {
            const { getBusLinesByIsland, getAllBusLines, getAllTrainLines, getAllTransport } = transportMod;
            assertEqual(getAllBusLines().length, 43, 'getAllBusLines returns 43');
            assertEqual(getAllTrainLines().length, 6, 'getAllTrainLines returns 6');
            assertEqual(getAllTransport().linies_bus.length, 43, 'getAllTransport has 43 bus lines');

            assertEqual(getBusLinesByIsland('Mallorca').length, 18, 'Mallorca bus 18');
            assertEqual(getBusLinesByIsland('Menorca').length, 12, 'Menorca bus 12');
            assertEqual(getBusLinesByIsland('Eivissa').length, 9, 'Eivissa bus 9');
            assertEqual(getBusLinesByIsland('Formentera').length, 4, 'Formentera bus 4');
            assertEqual(getBusLinesByIsland('totes').length, 43, 'totes bus 43');
            assertEqual(getBusLinesByIsland('NonExistent').length, 0, 'NonExistent bus 0');
        });

        test('3.6: Adversarial getIslandById', () => {
            const { getIslandById, getIslands } = islandsMod;
            assertEqual(getIslands().length, 4, 'Archipelago defines exactly 4 islands');

            assert(getIslandById('Mallorca')?.name === 'Mallorca', 'Mallorca lookup');
            assert(getIslandById('menorca')?.name === 'Menorca', 'menorca lowercase lookup');
            assert(getIslandById('  Eivissa  ')?.name === 'Eivissa', 'Trimmed Eivissa lookup');
            assert(getIslandById('FORMENTERA')?.name === 'Formentera', 'UPPERCASE Formentera lookup');

            assertEqual(getIslandById(''), undefined, 'Empty string returns undefined');
            assertEqual(getIslandById('cabrera'), undefined, 'Uninhabited/Unsupported island returns undefined');
        });
    });

    if (viteServer) {
        await viteServer.close();
    }

    // -------------------------------------------------------------
    // SUITE 4: Character Encoding, BOM, & Catalan Toponymy Integrity
    // -------------------------------------------------------------
    describe('Adversarial 4: Encoding & Catalan Linguistic Integrity', () => {
        const dataFiles = [
            'data/rutes_mallorca.json',
            'data/rutes_menorca.json',
            'data/rutes_eivissa.json',
            'data/rutes_formentera.json',
            'data/acampada_mallorca.json',
            'data/acampada_menorca.json',
            'data/acampada_pitiuses.json',
            'data/agrupaments_mallorca.json',
            'data/agrupaments_menorca.json',
            'data/agrupaments_pitiuses.json',
            'data/transport_mallorca.json',
            'data/transport_menorca.json',
            'data/transport_pitiuses.json'
        ];

        test('4.1: Strict Absence of UTF-8 BOM in All 13 Datasets', () => {
            for (const relPath of dataFiles) {
                const fullPath = path.resolve(process.cwd(), relPath);
                const buf = fs.readFileSync(fullPath);
                const hasBom = buf.length >= 3 && buf[0] === 0xef && buf[1] === 0xbb && buf[2] === 0xbf;
                assert(!hasBom, `UTF-8 BOM detected in file: ${relPath}`);
            }
        });

        test('4.2: Zero Mojibake Corruption Across Datasets', () => {
            const mojibakePatterns = [/Ã/, /Â/, /â€/, /ï¿½/, /\ufffd/, /&amp;/];

            for (const relPath of dataFiles) {
                const raw = fs.readFileSync(path.resolve(process.cwd(), relPath), 'utf8');
                for (const pat of mojibakePatterns) {
                    assert(!pat.test(raw), `Mojibake corruption pattern ${pat} detected in ${relPath}`);
                }
            }
        });

        test('4.3: Authentic Catalan Diacritics Presence', () => {
            const menorcaRaw = fs.readFileSync(path.resolve(process.cwd(), 'data/rutes_menorca.json'), 'utf8');
            assert(menorcaRaw.includes('Maó'), 'Maó with accent must be preserved');
            assert(menorcaRaw.includes('Camí de Cavalls'), 'Camí with accent must be preserved');

            const eivissaRaw = fs.readFileSync(path.resolve(process.cwd(), 'data/rutes_eivissa.json'), 'utf8');
            assert(eivissaRaw.includes('Eivissa'), 'Eivissa must be preserved');
            assert(eivissaRaw.includes('Albarca') || eivissaRaw.includes('Salines'), 'Eivissa toponyms preserved');

            const formenteraRaw = fs.readFileSync(path.resolve(process.cwd(), 'data/rutes_formentera.json'), 'utf8');
            assert(formenteraRaw.includes('Camí de sa Pujada'), 'Camí de sa Pujada preserved');
        });
    });

    const report = harness.printReport();
    return report.success;
}

if (require.main === module) {
    runAdversarialSuite().then((success) => {
        process.exit(success ? 0 : 1);
    }).catch((err) => {
        console.error('Adversarial suite crashed:', err);
        process.exit(1);
    });
}
