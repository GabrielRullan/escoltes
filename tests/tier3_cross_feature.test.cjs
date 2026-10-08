/**
 * Tier 3: Cross-Feature Interactions
 * Project: Escoltes de les Illes Balears (Balearic Islands Expansion)
 * Reference: PROJECT.md § Feature Inventory & TEST_INFRA.md § Tier 3
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

function getDataset(relPath) {
    const data = safeReadJson(relPath);
    return Array.isArray(data) ? data : [];
}

describe('Tier 3 - Interaction 1: Island Filter + Route Counts Synchronization', () => {
    test('3.1.1: Mallorca filter returns exactly 65 routes', () => {
        const mallorcaRoutes = getDataset('data/rutes_mallorca.json');
        assert(mallorcaRoutes.length === 65, `Expected 65 Mallorca routes, got ${mallorcaRoutes.length}`);
    });

    test('3.1.2: Menorca filter returns 20-22 routes when loaded', () => {
        const exists = fileExists('data/rutes_menorca.json');
        assert(exists, 'Expected data/rutes_menorca.json to exist');
        if (!exists) return;

        const menorcaRoutes = getDataset('data/rutes_menorca.json');
        assert(menorcaRoutes.length >= 20 && menorcaRoutes.length <= 22,
            `Expected 20-22 Menorca routes (GR-223 + variants), got ${menorcaRoutes.length}`);
    });

    test('3.1.3: Eivissa filter returns 7 routes when loaded', () => {
        const exists = fileExists('data/rutes_eivissa.json');
        assert(exists, 'Expected data/rutes_eivissa.json to exist');
        if (!exists) return;

        const eivissaRoutes = getDataset('data/rutes_eivissa.json');
        assert(eivissaRoutes.length >= 7, `Expected at least 7 Eivissa routes, got ${eivissaRoutes.length}`);
    });

    test('3.1.4: Formentera filter returns 3 green routes when loaded', () => {
        const exists = fileExists('data/rutes_formentera.json');
        assert(exists, 'Expected data/rutes_formentera.json to exist');
        if (!exists) return;

        const formenteraRoutes = getDataset('data/rutes_formentera.json');
        assert(formenteraRoutes.length >= 3, `Expected at least 3 Formentera routes, got ${formenteraRoutes.length}`);
    });

    test('3.1.5: Total routes across all Balearic islands equal target 97 routes', () => {
        const m = getDataset('data/rutes_mallorca.json');
        const me = getDataset('data/rutes_menorca.json');
        const e = getDataset('data/rutes_eivissa.json');
        const f = getDataset('data/rutes_formentera.json');

        const total = m.length + me.length + e.length + f.length;
        assert(total >= 65, 'Must have at least Mallorca routes');
        if (me.length > 0 && e.length > 0 && f.length > 0) {
            assertEqual(total, 97, `Target route count across archipelago is 97 (65+22+7+3), got ${total}`);
        }
    });
});

describe('Tier 3 - Interaction 2: Island Filter + Cartographic Bounds Synchronization', () => {
    // Official bounding boxes for Balearic islands
    const islandBounds = {
        Mallorca: { minLat: 39.15, maxLat: 39.95, minLon: 2.30, maxLon: 3.50 },
        Menorca: { minLat: 39.75, maxLat: 40.10, minLon: 3.75, maxLon: 4.35 },
        Eivissa: { minLat: 38.80, maxLat: 39.15, minLon: 1.15, maxLon: 1.65 },
        Formentera: { minLat: 38.60, maxLat: 38.80, minLon: 1.35, maxLon: 1.60 }
    };

    test('3.2.1: Mallorca route coordinates fall within Mallorca bounds', () => {
        const routes = getDataset('data/rutes_mallorca.json');
        assert(routes.length === 65, 'Mallorca routes loaded');
        const b = islandBounds.Mallorca;

        for (const r of routes) {
            assertInRange(r.lat, b.minLat, b.maxLat, `Route ${r.slug} lat (${r.lat}) out of Mallorca bounds`);
            assertInRange(r.lon, b.minLon, b.maxLon, `Route ${r.slug} lon (${r.lon}) out of Mallorca bounds`);
        }
    });

    test('3.2.2: Menorca route coordinates fall within Menorca bounds', () => {
        const exists = fileExists('data/rutes_menorca.json');
        assert(exists, 'Expected data/rutes_menorca.json to exist');
        if (!exists) return;

        const routes = getDataset('data/rutes_menorca.json');
        const b = islandBounds.Menorca;
        for (const r of routes) {
            assertInRange(r.lat, b.minLat, b.maxLat, `Route ${r.slug} lat (${r.lat}) out of Menorca bounds`);
            assertInRange(r.lon, b.minLon, b.maxLon, `Route ${r.slug} lon (${r.lon}) out of Menorca bounds`);
        }
    });

    test('3.2.3: Eivissa route coordinates fall within Eivissa bounds', () => {
        const exists = fileExists('data/rutes_eivissa.json');
        assert(exists, 'Expected data/rutes_eivissa.json to exist');
        if (!exists) return;

        const routes = getDataset('data/rutes_eivissa.json');
        const b = islandBounds.Eivissa;
        for (const r of routes) {
            assertInRange(r.lat, b.minLat, b.maxLat, `Route ${r.slug} lat (${r.lat}) out of Eivissa bounds`);
            assertInRange(r.lon, b.minLon, b.maxLon, `Route ${r.slug} lon (${r.lon}) out of Eivissa bounds`);
        }
    });

    test('3.2.4: Formentera route coordinates fall within Formentera bounds', () => {
        const exists = fileExists('data/rutes_formentera.json');
        assert(exists, 'Expected data/rutes_formentera.json to exist');
        if (!exists) return;

        const routes = getDataset('data/rutes_formentera.json');
        const b = islandBounds.Formentera;
        for (const r of routes) {
            assertInRange(r.lat, b.minLat, b.maxLat, `Route ${r.slug} lat (${r.lat}) out of Formentera bounds`);
            assertInRange(r.lon, b.minLon, b.maxLon, `Route ${r.slug} lon (${r.lon}) out of Formentera bounds`);
        }
    });
});

describe('Tier 3 - Interaction 3: Campsite Capacity + Emergency Access & Transport', () => {
    test('3.3.1: High capacity facilities (>=100 scouts) specify vehicular emergency access', () => {
        const m = getDataset('data/acampada_mallorca.json');
        const me = getDataset('data/acampada_menorca.json');
        const p = getDataset('data/acampada_pitiuses.json');
        const all = [...m, ...me, ...p];

        const largeFacilities = all.filter(c => typeof c.capacitat === 'number' && c.capacitat >= 100);
        assert(largeFacilities.length > 0, 'Must have facilities with capacity >= 100');

        for (const c of largeFacilities) {
            assert(typeof c.acces_emergencia === 'string' && c.acces_emergencia.length > 0,
                `Large facility ${c.slug} (cap=${c.capacitat}) must have explicit emergency vehicle access`);
        }
    });

    test('3.3.2: Menorca campings correlate with local municipalities', () => {
        const me = getDataset('data/acampada_menorca.json');
        const exists = fileExists('data/acampada_menorca.json');
        assert(exists, 'data/acampada_menorca.json exists');
        if (!exists) return;

        const validMunicipalities = ['Maó', 'Ciutadella', 'Ciutadella de Menorca', 'Alaior', 'Es Mercadal', 'Ferreries', 'Es Migjorn Gran', 'Sant Lluís', 'Es Castell'];
        for (const c of me) {
            assert(validMunicipalities.includes(c.municipi) || validMunicipalities.some(m => c.municipi.includes(m)),
                `Campsite ${c.slug} has unrecognized Menorca municipality: ${c.municipi}`);
        }
    });
});

describe('Tier 3 - Interaction 4: Route Difficulty + Scout Unit Suitability', () => {
    test('3.4.1: Demanding ("Exigent") routes do not authorize youngest units without warnings', () => {
        const m = getDataset('data/rutes_mallorca.json');
        const me = getDataset('data/rutes_menorca.json');
        const e = getDataset('data/rutes_eivissa.json');
        const f = getDataset('data/rutes_formentera.json');
        const allRoutes = [...m, ...me, ...e, ...f];

        const demandingRoutes = allRoutes.filter(r => (r.dificultat || '').toLowerCase().includes('exigent'));
        assert(demandingRoutes.length > 0, 'Should find routes classified as Exigent');

        for (const r of demandingRoutes) {
            const units = (r.apte_unitats || []).map(u => u.toLowerCase());
            const hasYoungest = units.some(u => u.includes('castor') || u.includes('ferreret'));
            assert(!hasYoungest, `Exigent route ${r.slug} must not be designated for Castors/Ferrerets unit`);
            // Must specify older units like Pioners or Rutes
            const hasOlder = units.some(u => u.includes('pioner') || u.includes('rànger') || u.includes('ranger') || u.includes('rutes') || u.includes('truc'));
            assert(hasOlder, `Exigent route ${r.slug} must be suitable for older scout branches`);
        }
    });

    test('3.4.2: Easy ("Fàcil" or "Molt fàcil") routes allow younger units', () => {
        const m = getDataset('data/rutes_mallorca.json');
        const me = getDataset('data/rutes_menorca.json');
        const e = getDataset('data/rutes_eivissa.json');
        const f = getDataset('data/rutes_formentera.json');
        const allRoutes = [...m, ...me, ...e, ...f];

        const easyRoutes = allRoutes.filter(r => (r.dificultat || '').toLowerCase().includes('fàcil'));
        assert(easyRoutes.length > 0, 'Should find easy routes');

        for (const r of easyRoutes) {
            const units = (r.apte_unitats || []).map(u => u.toLowerCase());
            const hasLlopsOrCastors = units.some(u => u.includes('llop') || u.includes('daina') || u.includes('castor') || u.includes('ferreret') || u.includes('totes'));
            assert(hasLlopsOrCastors, `Easy route ${r.slug} should be accessible to younger units`);
        }
    });
});

describe('Tier 3 - Interaction 5: Island Filter + Campsites Catalog Partition', () => {
    test('3.5.1: Campsite partitioning across islands preserves Mallorca (45) + expansions (15)', () => {
        const m = getDataset('data/acampada_mallorca.json');
        const me = getDataset('data/acampada_menorca.json');
        const p = getDataset('data/acampada_pitiuses.json');

        assertEqual(m.length, 45, 'Mallorca campsites count must remain exactly 45');
        const existsMe = fileExists('data/acampada_menorca.json');
        const existsP = fileExists('data/acampada_pitiuses.json');
        assert(existsMe, 'acampada_menorca.json exists');
        assert(existsP, 'acampada_pitiuses.json exists');

        if (existsMe && existsP) {
            assert(me.length >= 8, `Expected at least 8 Menorca campsites, got ${me.length}`);
            assert(p.length >= 5, `Expected at least 5 Pitiüses campsites, got ${p.length}`);
            const total = m.length + me.length + p.length;
            assert(total >= 58 && total <= 62, `Total archipelago campsites should be ~60 (45+8+7), got ${total}`);
        }
    });
});

if (require.main === module) {
    const report = harness.printReport();
    process.exit(report.success ? 0 : 1);
}
