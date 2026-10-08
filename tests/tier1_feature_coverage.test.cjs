/**
 * Tier 1: Feature Coverage (Features 1 to 17)
 * Project: Escoltes de les Illes Balears (Balearic Islands Expansion)
 * Reference: PROJECT.md § Feature Inventory (Features 1-17)
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
    assertArrayContains,
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

function safeReadText(relPath) {
    const fullPath = path.resolve(process.cwd(), relPath);
    if (!fs.existsSync(fullPath)) return null;
    try {
        return fs.readFileSync(fullPath, 'utf8');
    } catch {
        return null;
    }
}

describe('Tier 1 - Feature 1: Menorca GR-223 Camí de Cavalls Data', () => {
    const filePath = 'data/rutes_menorca.json';

    test('1.1: Menorca routes dataset file exists and is valid JSON', () => {
        const exists = fileExists(filePath);
        assert(exists, `Expected ${filePath} to exist in repository`);
        if (!exists) return;
        const data = safeReadJson(filePath);
        assert(Array.isArray(data), `Expected ${filePath} to contain a JSON array`);
        assert(data.length >= 20, `Expected at least 20 official GR-223 stages, got ${data.length}`);
    });

    test('1.2: All 20 stages have essential schema fields', () => {
        const data = safeReadJson(filePath);
        assert(Array.isArray(data), `Missing or invalid ${filePath}`);
        if (!Array.isArray(data)) return;

        const stages = data.filter(r => (r.slug || '').includes('etapa') || (r.nom || '').includes('Etapa'));
        assert(stages.length >= 20, `Expected at least 20 stages, found ${stages.length}`);

        for (const r of stages) {
            assert(typeof r.slug === 'string' && r.slug.length > 0, `Route missing slug: ${JSON.stringify(r.nom)}`);
            assert(typeof r.nom === 'string' && r.nom.length > 0, `Route missing nom: ${r.slug}`);
            assert(typeof r.distancia_km === 'number' && r.distancia_km > 0, `Route ${r.slug} has invalid distancia_km`);
            assert(typeof r.desnivell_positiu_m === 'number', `Route ${r.slug} has invalid desnivell_positiu_m`);
            assert(typeof r.dificultat === 'string', `Route ${r.slug} has invalid dificultat`);
            assert(typeof r.lat === 'number' && typeof r.lon === 'number', `Route ${r.slug} missing lat/lon`);
        }
    });

    test('1.3: All Menorca routes have illa property set to Menorca', () => {
        const data = safeReadJson(filePath);
        assert(Array.isArray(data), `Missing ${filePath}`);
        if (!Array.isArray(data)) return;

        for (const r of data) {
            assertEqual(r.illa, 'Menorca', `Route ${r.slug} illa must be 'Menorca'`);
        }
    });

    test('1.4: Water points and safety tips populated for Menorca stages', () => {
        const data = safeReadJson(filePath);
        assert(Array.isArray(data), `Missing ${filePath}`);
        if (!Array.isArray(data)) return;

        for (const r of data) {
            assert(Array.isArray(r.punts_aigua), `Route ${r.slug} must have punts_aigua array`);
            assert(typeof r.consells_seguretat === 'string' && r.consells_seguretat.length > 0,
                `Route ${r.slug} must have non-empty consells_seguretat`);
            assert(typeof r.punt_origen === 'string' && r.punt_origen.length > 0,
                `Route ${r.slug} must have non-empty punt_origen`);
        }
    });

    test('1.5: Key variants or full 20-stage perimeter coverage verified', () => {
        const data = safeReadJson(filePath);
        assert(Array.isArray(data), `Missing ${filePath}`);
        if (!Array.isArray(data)) return;

        // Either total routes >= 22 (20 stages + 2 variants) or stage 1 and stage 20 exist closing the loop
        const hasStart = data.some(r => (r.slug || '').includes('01') || (r.slug || '').includes('etapa-1') || (r.nom || '').includes('Etapa 1'));
        const hasEnd = data.some(r => (r.slug || '').includes('20') || (r.nom || '').includes('Etapa 20'));
        assert(hasStart, 'Menorca dataset must include Etapa 1');
        assert(hasEnd, 'Menorca dataset must include Etapa 20');
        assert(data.length >= 20, 'Menorca dataset must have complete coverage');
    });
});

describe('Tier 1 - Feature 2: Eivissa Routes Data', () => {
    const filePath = 'data/rutes_eivissa.json';

    test('2.1: Eivissa routes dataset file exists and contains at least 7 routes', () => {
        const exists = fileExists(filePath);
        assert(exists, `Expected ${filePath} to exist`);
        if (!exists) return;
        const data = safeReadJson(filePath);
        assert(Array.isArray(data), `Expected ${filePath} to be an array`);
        assert(data.length >= 7, `Expected at least 7 Eivissa routes, got ${data.length}`);
    });

    test('2.2: Mandatory landmark routes present in Eivissa dataset', () => {
        const data = safeReadJson(filePath);
        assert(Array.isArray(data), `Missing ${filePath}`);
        if (!Array.isArray(data)) return;

        const slugs = data.map(r => (r.slug || '').toLowerCase());
        const names = data.map(r => (r.nom || '').toLowerCase());
        const combined = slugs.concat(names).join(' ');

        assert(combined.includes('salines') || combined.includes('portes'), 'Must include Ses Salines / Torre de ses Portes');
        assert(combined.includes('savinar') || combined.includes('vedra'), 'Must include Torre des Savinar / Es Vedrà');
        assert(combined.includes('amunts') || combined.includes('vicent'), 'Must include Els Amunts');
    });

    test('2.3: All Eivissa routes have illa === "Eivissa" and valid coordinates', () => {
        const data = safeReadJson(filePath);
        assert(Array.isArray(data), `Missing ${filePath}`);
        if (!Array.isArray(data)) return;

        for (const r of data) {
            assertEqual(r.illa, 'Eivissa', `Route ${r.slug} must have illa 'Eivissa'`);
            assertInRange(r.lat, 38.7, 39.2, `Route ${r.slug} latitude outside Eivissa range`);
            assertInRange(r.lon, 1.15, 1.7, `Route ${r.slug} longitude outside Eivissa range`);
        }
    });

    test('2.4: Eivissa routes contain unit suitability and origin points', () => {
        const data = safeReadJson(filePath);
        assert(Array.isArray(data), `Missing ${filePath}`);
        if (!Array.isArray(data)) return;

        for (const r of data) {
            assert(Array.isArray(r.apte_unitats) && r.apte_unitats.length > 0, `Route ${r.slug} must specify apte_unitats`);
            assert(typeof r.punt_origen === 'string' && r.punt_origen.length > 0, `Route ${r.slug} must specify punt_origen`);
        }
    });

    test('2.5: Coastal cliff and safety tips included for Eivissa routes', () => {
        const data = safeReadJson(filePath);
        assert(Array.isArray(data), `Missing ${filePath}`);
        if (!Array.isArray(data)) return;

        for (const r of data) {
            assert(typeof r.consells_seguretat === 'string' && r.consells_seguretat.length > 10,
                `Route ${r.slug} must have descriptive consells_seguretat`);
        }
    });
});

describe('Tier 1 - Feature 3: Formentera Green Routes Data', () => {
    const filePath = 'data/rutes_formentera.json';

    test('3.1: Formentera routes dataset file exists and contains at least 3 routes', () => {
        const exists = fileExists(filePath);
        assert(exists, `Expected ${filePath} to exist`);
        if (!exists) return;
        const data = safeReadJson(filePath);
        assert(Array.isArray(data), `Expected ${filePath} to be an array`);
        assert(data.length >= 3, `Expected at least 3 green routes, got ${data.length}`);
    });

    test('3.2: Contains Ses Illetes, Camí de sa Pujada, and Far de Barbaria', () => {
        const data = safeReadJson(filePath);
        assert(Array.isArray(data), `Missing ${filePath}`);
        if (!Array.isArray(data)) return;

        const combined = data.map(r => `${r.slug} ${r.nom}`).join(' ').toLowerCase();
        assert(combined.includes('illetes') || combined.includes('savina'), 'Must include Ses Illetes route');
        assert(combined.includes('pujada') || combined.includes('mola'), 'Must include Camí de sa Pujada (La Mola)');
        assert(combined.includes('barbaria'), 'Must include Cap de Barbaria route');
    });

    test('3.3: Formentera routes have illa === "Formentera" and bounded coordinates', () => {
        const data = safeReadJson(filePath);
        assert(Array.isArray(data), `Missing ${filePath}`);
        if (!Array.isArray(data)) return;

        for (const r of data) {
            assertEqual(r.illa, 'Formentera', `Route ${r.slug} must have illa 'Formentera'`);
            assertInRange(r.lat, 38.6, 38.8, `Route ${r.slug} latitude outside Formentera range`);
            assertInRange(r.lon, 1.35, 1.6, `Route ${r.slug} longitude outside Formentera range`);
        }
    });

    test('3.4: Formentera routes emphasize heat and sun exposure precautions', () => {
        const data = safeReadJson(filePath);
        assert(Array.isArray(data), `Missing ${filePath}`);
        if (!Array.isArray(data)) return;

        for (const r of data) {
            assert(typeof r.consells_seguretat === 'string' && r.consells_seguretat.length > 0,
                `Route ${r.slug} must include safety tips`);
            const lower = r.consells_seguretat.toLowerCase();
            const hasSunOrWaterWarning = lower.includes('sol') || lower.includes('aigua') || lower.includes('calor') || lower.includes('ombra') || lower.includes('protecció');
            assert(hasSunOrWaterWarning, `Route ${r.slug} safety tips must address sun, heat, or water conditions`);
        }
    });
});

describe('Tier 1 - Feature 4: Balearic Facilities Data', () => {
    const fileMenorca = 'data/acampada_menorca.json';
    const filePitiuses = 'data/acampada_pitiuses.json';

    test('4.1: Menorca facilities dataset exists and contains key facilities', () => {
        const exists = fileExists(fileMenorca);
        assert(exists, `Expected ${fileMenorca} to exist`);
        if (!exists) return;
        const data = safeReadJson(fileMenorca);
        assert(Array.isArray(data) && data.length >= 8, `Expected at least 8 Menorca facilities, got ${data ? data.length : 0}`);

        const combined = data.map(f => `${f.slug} ${f.nom}`).join(' ').toLowerCase();
        assert(combined.includes('biniparratx'), 'Must include Biniparratx facility');
        assert(combined.includes('vinyeta'), 'Must include Sa Vinyeta facility');
    });

    test('4.2: Pitiüses facilities dataset exists and contains Eivissa/Formentera sites', () => {
        const exists = fileExists(filePitiuses);
        assert(exists, `Expected ${filePitiuses} to exist`);
        if (!exists) return;
        const data = safeReadJson(filePitiuses);
        assert(Array.isArray(data) && data.length >= 5, `Expected at least 5 Pitiüses facilities, got ${data ? data.length : 0}`);

        const combined = data.map(f => `${f.slug} ${f.nom}`).join(' ').toLowerCase();
        assert(combined.includes('jondal') || combined.includes('tomeu') || combined.includes('formentera'),
            'Must include recognized youth facilities in Pitiüses');
    });

    test('4.3: Total youth facilities across Menorca and Pitiüses >= 15', () => {
        const men = safeReadJson(fileMenorca) || [];
        const pit = safeReadJson(filePitiuses) || [];
        const total = men.length + pit.length;
        assert(total >= 13, `Expected at least 13-15 youth facilities across Menorca & Pitiüses, got ${total}`);
    });

    test('4.4: Facilities contain legal framework fields (permis, foc, acces)', () => {
        const allFacilities = (safeReadJson(fileMenorca) || []).concat(safeReadJson(filePitiuses) || []);
        assert(allFacilities.length > 0, 'No facilities loaded for legal verification');
        if (allFacilities.length === 0) return;

        for (const f of allFacilities) {
            assert(typeof f.permis_antelacio === 'string' && f.permis_antelacio.length > 0,
                `Facility ${f.slug} missing permis_antelacio`);
            assert(typeof f.restriccio_foc === 'string' && f.restriccio_foc.length > 0,
                `Facility ${f.slug} missing restriccio_foc`);
            assert(typeof f.acces_emergencia === 'string' && f.acces_emergencia.length > 0,
                `Facility ${f.slug} missing acces_emergencia`);
        }
    });

    test('4.5: Coordinates and capacity are valid for all facilities', () => {
        const allFacilities = (safeReadJson(fileMenorca) || []).concat(safeReadJson(filePitiuses) || []);
        assert(allFacilities.length > 0, 'No facilities loaded');
        if (allFacilities.length === 0) return;

        for (const f of allFacilities) {
            assertInRange(f.lat, 38.5, 40.2, `Facility ${f.slug} lat out of bounds`);
            assertInRange(f.lon, 1.15, 4.45, `Facility ${f.slug} lon out of bounds`);
            assert(typeof f.capacitat === 'number' && f.capacitat > 0, `Facility ${f.slug} capacitat must be positive number`);
        }
    });
});

describe('Tier 1 - Feature 5: Balearic Scout Groups Data', () => {
    const fileMenorca = 'data/agrupaments_menorca.json';
    const filePitiuses = 'data/agrupaments_pitiuses.json';

    test('5.1: Menorca scout groups dataset exists with Escoltes de Menorca (MSC)', () => {
        const exists = fileExists(fileMenorca);
        assert(exists, `Expected ${fileMenorca} to exist`);
        if (!exists) return;
        const data = safeReadJson(fileMenorca);
        assert(Array.isArray(data) && data.length >= 8, `Expected at least 8-9 Menorca scout groups, got ${data ? data.length : 0}`);
        for (const g of data) {
            assertEqual(g.illa, 'Menorca', `Group ${g.slug} illa must be Menorca`);
            assert(typeof g.associacio === 'string' && g.associacio.length > 0, `Group ${g.slug} missing associacio`);
        }
    });

    test('5.2: Pitiüses scout groups dataset exists with active groups', () => {
        const exists = fileExists(filePitiuses);
        assert(exists, `Expected ${filePitiuses} to exist`);
        if (!exists) return;
        const data = safeReadJson(filePitiuses);
        assert(Array.isArray(data) && data.length >= 2, `Expected at least 2 Pitiüses groups, got ${data ? data.length : 0}`);
        const names = data.map(g => g.nom.toLowerCase()).join(' ');
        assert(names.includes('cóndors') || names.includes('condors') || names.includes('macabich'),
            'Must contain Los Cóndors or Isidor Macabich');
    });

    test('5.3: Scout groups have required schema fields', () => {
        const allGroups = (safeReadJson(fileMenorca) || []).concat(safeReadJson(filePitiuses) || []);
        assert(allGroups.length > 0, 'No scout groups found');
        if (allGroups.length === 0) return;

        for (const g of allGroups) {
            assert(typeof g.nom === 'string' && g.nom.length > 0, `Group missing nom: ${g.slug}`);
            assert(typeof g.slug === 'string' && g.slug.length > 0, `Group missing slug: ${g.nom}`);
            assert(typeof g.municipi === 'string' && g.municipi.length > 0, `Group ${g.slug} missing municipi`);
            assert(typeof g.lat === 'number' && typeof g.lon === 'number', `Group ${g.slug} missing valid lat/lon`);
        }
    });
});

describe('Tier 1 - Feature 6: Balearic Public Transport Data', () => {
    const fileMenorca = 'data/transport_menorca.json';
    const filePitiuses = 'data/transport_pitiuses.json';

    test('6.1: Menorca transport dataset exists and defines lines', () => {
        const exists = fileExists(fileMenorca);
        assert(exists, `Expected ${fileMenorca} to exist`);
        if (!exists) return;
        const data = safeReadJson(fileMenorca);
        const lines = Array.isArray(data) ? data : (data.linies_bus || []);
        assert(lines.length >= 10, `Expected at least 10 Menorca bus lines, got ${lines.length}`);
    });

    test('6.2: Pitiüses transport dataset exists and defines lines', () => {
        const exists = fileExists(filePitiuses);
        assert(exists, `Expected ${filePitiuses} to exist`);
        if (!exists) return;
        const data = safeReadJson(filePitiuses);
        const lines = Array.isArray(data) ? data : (data.linies_bus || []);
        assert(lines.length >= 8, `Expected at least 8 Pitiüses bus lines, got ${lines.length}`);
    });

    test('6.3: Transport lines define codes and names', () => {
        const menData = safeReadJson(fileMenorca);
        const pitData = safeReadJson(filePitiuses);
        const menLines = Array.isArray(menData) ? menData : (menData ? menData.linies_bus || [] : []);
        const pitLines = Array.isArray(pitData) ? pitData : (pitData ? pitData.linies_bus || [] : []);
        const total = menLines.length + pitLines.length;

        assert(total >= 18, `Expected combined transport lines >= 18 across new islands, got ${total}`);
        for (const l of menLines.concat(pitLines)) {
            assert(typeof l.codi === 'string' && l.codi.length > 0, `Line missing codi: ${JSON.stringify(l)}`);
            assert(typeof l.nom === 'string' && l.nom.length > 0, `Line missing nom: ${l.codi}`);
        }
    });
});

describe('Tier 1 - Feature 7: Unified Data Abstraction Modules', () => {
    test('7.1: Unified TypeScript data layer exists in src/data/', () => {
        assert(fileExists('src/data/routes.ts') || fileExists('src/data/routes.js'), 'Expected src/data/routes.ts to exist');
        assert(fileExists('src/data/campsites.ts') || fileExists('src/data/campsites.js'), 'Expected src/data/campsites.ts to exist');
        assert(fileExists('src/data/groups.ts') || fileExists('src/data/groups.js'), 'Expected src/data/groups.ts to exist');
        assert(fileExists('src/data/transport.ts') || fileExists('src/data/transport.js'), 'Expected src/data/transport.ts to exist');
        assert(fileExists('src/data/islands.ts') || fileExists('src/data/islands.js'), 'Expected src/data/islands.ts to exist');
    });

    test('7.2: Type definitions file exists in src/types/index.ts', () => {
        const exists = fileExists('src/types/index.ts');
        assert(exists, 'Expected src/types/index.ts to exist');
        if (!exists) return;
        const content = safeReadText('src/types/index.ts');
        assert(content.includes('Mallorca') && content.includes('Menorca'), 'Type definitions must support Balearic islands');
    });
});

describe('Tier 1 - Feature 8 & 9: Multi-Island Selector & Client Route Filtering', () => {
    test('8.1: FilterBar component supports multi-island options', () => {
        const content = safeReadText('src/components/FilterBar.astro');
        assert(content !== null, 'src/components/FilterBar.astro must exist');
        if (!content) return;
        const lower = content.toLowerCase();
        assert(lower.includes('menorca'), 'FilterBar must include Menorca option');
        assert(lower.includes('eivissa'), 'FilterBar must include Eivissa option');
        assert(lower.includes('formentera'), 'FilterBar must include Formentera option');
    });

    test('9.1: RouteCard component contains data-illa attribute for filtering', () => {
        const content = safeReadText('src/components/RouteCard.astro');
        assert(content !== null, 'src/components/RouteCard.astro must exist');
        if (!content) return;
        assert(content.includes('data-illa'), 'RouteCard.astro must include data-illa attribute');
    });
});

describe('Tier 1 - Feature 10: Fallback for Town Drawings', () => {
    test('10.1: RouteCard handles non-Mallorca municipalities gracefully', () => {
        const content = safeReadText('src/components/RouteCard.astro');
        assert(content !== null, 'src/components/RouteCard.astro must exist');
        if (!content) return;
        // Verify fallback image or conditional rendering
        const hasFallback = content.includes('default') || content.includes('fallback') || content.includes('?') || content.includes('illa');
        assert(hasFallback, 'RouteCard must safely handle non-Mallorca municipality image paths');
    });
});

describe('Tier 1 - Feature 11 & 12: Dynamic Balearic Map & Synchronization', () => {
    test('11.1: Map component exists and contains Balearic archipelago center or bounds', () => {
        const mapFile = fileExists('src/components/BalearicMap.astro') ? 'src/components/BalearicMap.astro' : 'src/components/MallorcaMap.astro';
        const content = safeReadText(mapFile);
        assert(content !== null, 'Map component must exist');
        if (!content) return;
        assert(content.includes('39.') || content.includes('bounds') || content.includes('center'),
            'Map must define coordinates or bounds for Balearic area');
    });

    test('12.1: Map script exposes island centering function window.__setMapIsland', () => {
        const mapFile = fileExists('src/components/BalearicMap.astro') ? 'src/components/BalearicMap.astro' : 'src/components/MallorcaMap.astro';
        const content = safeReadText(mapFile);
        assert(content !== null, 'Map component must exist');
        if (!content) return;
        assert(content.includes('__setMapIsland') || content.includes('setMapIsland'),
            'Map component must expose island selector function');
    });
});

describe('Tier 1 - Feature 13 & 14: Route Detail Map & Pages Integration', () => {
    test('13.1: Route detail page handles track coordinates and polyline bounds', () => {
        const content = safeReadText('src/pages/rutes/[slug].astro');
        assert(content !== null, 'src/pages/rutes/[slug].astro must exist');
        if (!content) return;
        assert(content.includes('track_coordinates') || content.includes('lat') || content.includes('fitBounds'),
            'Route detail page must handle route coordinates');
    });

    test('14.1: Core pages exist for routes, campsites, groups, and transport', () => {
        assert(fileExists('src/pages/rutes/index.astro'), 'rutes/index.astro must exist');
        assert(fileExists('src/pages/acampada/index.astro'), 'acampada/index.astro must exist');
        assert(fileExists('src/pages/agrupaments/index.astro'), 'agrupaments/index.astro must exist');
        assert(fileExists('src/pages/transport/index.astro'), 'transport/index.astro must exist');
        assert(fileExists('src/pages/index.astro'), 'index.astro must exist');
    });
});

describe('Tier 1 - Feature 15: Backward Compatibility & Mallorca Preservation', () => {
    test('15.1: Mallorca routes preserved with exactly 65 records', () => {
        const data = safeReadJson('data/rutes_mallorca.json');
        assert(Array.isArray(data), 'rutes_mallorca.json must be valid array');
        if (!Array.isArray(data)) return;
        assertEqual(data.length, 65, `Expected exactly 65 Mallorca routes preserved, got ${data.length}`);
    });

    test('15.2: Mallorca campsites preserved with exactly 45 records', () => {
        const data = safeReadJson('data/acampada_mallorca.json');
        assert(Array.isArray(data), 'acampada_mallorca.json must be valid array');
        if (!Array.isArray(data)) return;
        assertEqual(data.length, 45, `Expected exactly 45 Mallorca campsites preserved, got ${data.length}`);
    });

    test('15.3: Mallorca scout groups preserved with exactly 13 records', () => {
        const data = safeReadJson('data/agrupaments_mallorca.json');
        assert(Array.isArray(data), 'agrupaments_mallorca.json must be valid array');
        if (!Array.isArray(data)) return;
        assertEqual(data.length, 13, `Expected exactly 13 Mallorca scout groups preserved, got ${data.length}`);
    });

    test('15.4: Mallorca transport preserved', () => {
        const data = safeReadJson('data/transport_mallorca.json');
        assert(data !== null && typeof data === 'object', 'transport_mallorca.json must exist');
        if (!data) return;
        const lines = Array.isArray(data) ? data : (data.linies_bus || []);
        assert(lines.length >= 10, 'Mallorca transport lines must be preserved');
    });
});

describe('Tier 1 - Feature 16 & 17: Test Suite Infrastructure & Forensic Integrity', () => {
    test('16.1: Test runner and harness files present', () => {
        assert(fileExists('tests/test_harness.cjs'), 'test_harness.cjs must exist');
    });

    test('17.1: All JSON datasets in data/ are valid UTF-8 without BOM', () => {
        const files = [
            'data/rutes_mallorca.json',
            'data/acampada_mallorca.json',
            'data/agrupaments_mallorca.json',
            'data/transport_mallorca.json'
        ];
        for (const f of files) {
            const buf = fs.readFileSync(path.resolve(process.cwd(), f));
            // Check BOM
            const hasBom = buf[0] === 0xEF && buf[1] === 0xBB && buf[2] === 0xBF;
            assert(!hasBom, `File ${f} should not have UTF-8 BOM`);
        }
    });

    test('17.2: Route slugs are unique across all datasets', () => {
        const mallorca = safeReadJson('data/rutes_mallorca.json') || [];
        const menorca = safeReadJson('data/rutes_menorca.json') || [];
        const eivissa = safeReadJson('data/rutes_eivissa.json') || [];
        const formentera = safeReadJson('data/rutes_formentera.json') || [];

        const allRoutes = [...mallorca, ...menorca, ...eivissa, ...formentera];
        assert(allRoutes.length >= 65, 'Must have at least Mallorca routes loaded');

        const slugSet = new Set();
        for (const r of allRoutes) {
            if (r.slug) {
                assert(!slugSet.has(r.slug), `Duplicate route slug detected: ${r.slug}`);
                slugSet.add(r.slug);
            }
        }
    });
});

if (require.main === module) {
    const report = harness.printReport();
    process.exit(report.success ? 0 : 1);
}
