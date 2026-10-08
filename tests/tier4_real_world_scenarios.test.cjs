/**
 * Tier 4: Real-World Scout Application Scenarios
 * Project: Escoltes de les Illes Balears (Balearic Islands Expansion)
 * Reference: PROJECT.md & TEST_INFRA.md § Tier 4
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

describe('Tier 4 - Scenario 1: Castors Unit (6-8 yrs) Day Outing', () => {
    test('4.1.1: Find child-friendly day route (<=5.5 km, low elevation, easy)', () => {
        const m = getDataset('data/rutes_mallorca.json');
        const me = getDataset('data/rutes_menorca.json');
        const e = getDataset('data/rutes_eivissa.json');
        const f = getDataset('data/rutes_formentera.json');
        const allRoutes = [...m, ...me, ...e, ...f];

        assert(allRoutes.length >= 65, 'Routes dataset available');

        // Castors require: distance <= 5.5 km, desnivell <= 120m, Fàcil
        const castorRoutes = allRoutes.filter(r =>
            typeof r.distancia_km === 'number' && r.distancia_km <= 5.5 &&
            typeof r.desnivell_positiu_m === 'number' && r.desnivell_positiu_m <= 120 &&
            (r.dificultat || '').toLowerCase().includes('fàcil')
        );

        assert(castorRoutes.length >= 3, `Expected at least 3 child-friendly routes, found ${castorRoutes.length}`);
    });

    test('4.1.2: Child-friendly routes have accessible origin or water points', () => {
        const m = getDataset('data/rutes_mallorca.json');
        const f = getDataset('data/rutes_formentera.json');
        const all = [...m, ...f];

        const shortEasy = all.filter(r => r.distancia_km <= 5.5 && (r.dificultat || '').toLowerCase().includes('fàcil'));
        assert(shortEasy.length > 0, 'Must find short easy routes');

        for (const r of shortEasy) {
            assert(typeof r.punt_origen === 'string' || typeof r.municipi === 'string',
                `Route ${r.slug} must specify clear start point for young unit logistical drop-off`);
        }
    });
});

describe('Tier 4 - Scenario 2: Truc / Rovers Menorca North Coast Expedition', () => {
    test('4.2.1: Menorca North Coast rugged stages classified as Exigent', () => {
        const exists = fileExists('data/rutes_menorca.json');
        assert(exists, 'Expected data/rutes_menorca.json to exist');
        if (!exists) return;

        const menorca = getDataset('data/rutes_menorca.json');
        const northCoastRugged = menorca.filter(r =>
            (r.nom || '').includes('Binimel·là') ||
            (r.nom || '').includes('Alocs') ||
            (r.slug || '').includes('06') ||
            (r.slug || '').includes('07')
        );

        assert(northCoastRugged.length > 0, 'North coast rugged stages must exist');
        for (const r of northCoastRugged) {
            const dif = (r.dificultat || '').toLowerCase();
            assert(dif.includes('exigent') || dif.includes('moderada'),
                `North coast stage ${r.slug} must reflect rugged difficulty`);
        }
    });

    test('4.2.2: Menorca basecamp facilities support scout troop lodging', () => {
        const exists = fileExists('data/acampada_menorca.json');
        assert(exists, 'Expected data/acampada_menorca.json to exist');
        if (!exists) return;

        const menorcaFacilities = getDataset('data/acampada_menorca.json');
        const basecamps = menorcaFacilities.filter(f =>
            (f.slug || '').includes('biniparratx') ||
            (f.slug || '').includes('vinyeta')
        );

        assert(basecamps.length >= 1, 'Must find Biniparratx or Sa Vinyeta basecamp facility');
        for (const f of basecamps) {
            assert(typeof f.capacitat === 'number' && f.capacitat >= 50,
                `Basecamp facility ${f.slug} must have capacity >= 50 for large scout units`);
        }
    });

    test('4.2.3: North coast stage safety notes mandate high water carrying protocol', () => {
        const exists = fileExists('data/rutes_menorca.json');
        assert(exists, 'Expected data/rutes_menorca.json to exist');
        if (!exists) return;

        const menorca = getDataset('data/rutes_menorca.json');
        const etapa6 = menorca.find(r => (r.slug || '').includes('06') || (r.nom || '').includes('Binimel·là'));
        if (etapa6) {
            const tips = (etapa6.consells_seguretat || '').toLowerCase();
            const hasWaterRule = tips.includes('aigua') || tips.includes('litre') || tips.includes('2') || tips.includes('3');
            assert(hasWaterRule, 'Etapa 6 safety tips must highlight water carrying requirements');
        }
    });
});

describe('Tier 4 - Scenario 3: Eivissa Coastal Hike with Public Bus Connection', () => {
    test('4.3.1: Eivissa coastal routes have defined public transport bus lines', () => {
        const routesExists = fileExists('data/rutes_eivissa.json');
        const transExists = fileExists('data/transport_pitiuses.json');
        assert(routesExists, 'Expected data/rutes_eivissa.json to exist');
        assert(transExists, 'Expected data/transport_pitiuses.json to exist');
        if (!routesExists || !transExists) return;

        const eivissaRoutes = getDataset('data/rutes_eivissa.json');
        const pitiusesTransport = safeReadJson('data/transport_pitiuses.json');
        const lines = Array.isArray(pitiusesTransport) ? pitiusesTransport : (pitiusesTransport.linies_bus || []);

        assert(eivissaRoutes.length >= 7, 'Eivissa routes loaded');
        assert(lines.length >= 5, 'Eivissa transport lines loaded');

        // Look for bus line servicing Ses Salines or Portinatx or Sant Joan
        const coastalServiced = lines.some(l => {
            const towns = (l.municipis_coberts || []).concat(l.parades_clau || []).join(' ').toLowerCase();
            return towns.includes('salines') || towns.includes('portinatx') || towns.includes('josep') || towns.includes('joan');
        });
        assert(coastalServiced, 'At least one public bus line must service Eivissa hiking trailheads');
    });

    test('4.3.2: Eivissa hike origin specifies recognizable public transit point', () => {
        const routesExists = fileExists('data/rutes_eivissa.json');
        assert(routesExists, 'Expected data/rutes_eivissa.json to exist');
        if (!routesExists) return;

        const eivissaRoutes = getDataset('data/rutes_eivissa.json');
        for (const r of eivissaRoutes) {
            assert(typeof r.punt_origen === 'string' && r.punt_origen.length > 5,
                `Route ${r.slug} must have informative punt_origen for transit planning`);
        }
    });
});

describe('Tier 4 - Scenario 4: Formentera Sun & Dehydration Safety Protocol', () => {
    test('4.4.1: Exposed Formentera routes identify lack of natural shade', () => {
        const exists = fileExists('data/rutes_formentera.json');
        assert(exists, 'Expected data/rutes_formentera.json to exist');
        if (!exists) return;

        const formentera = getDataset('data/rutes_formentera.json');
        const barbaria = formentera.find(r => (r.slug || '').includes('barbaria'));
        if (barbaria) {
            const safety = (barbaria.consells_seguretat || '').toLowerCase();
            const warnsShadeOrSun = safety.includes('ombra') || safety.includes('sol') || safety.includes('calor');
            assert(warnsShadeOrSun, 'Barbaria route must warn about lack of shade or sun intensity');
        }
    });

    test('4.4.2: Cliff edge safety explicitly addressed for Formentera routes', () => {
        const exists = fileExists('data/rutes_formentera.json');
        assert(exists, 'Expected data/rutes_formentera.json to exist');
        if (!exists) return;

        const formentera = getDataset('data/rutes_formentera.json');
        const cliffRoutes = formentera.filter(r => (r.slug || '').includes('barbaria') || (r.slug || '').includes('pujada'));
        for (const r of cliffRoutes) {
            const safety = (r.consells_seguretat || '').toLowerCase();
            const mentionsCliffs = safety.includes('penya') || safety.includes('foradada') || safety.includes('caiguda') || safety.includes('supervisió') || safety.includes('perill') || safety.includes('precaució');
            assert(mentionsCliffs, `Route ${r.slug} must include cliff safety advice`);
        }
    });
});

describe('Tier 4 - Scenario 5: Multi-Day Trek with Legal Camping Regulations', () => {
    test('4.5.1: Legal camping regulations (Llei 10/2022) reflected in facility metadata', () => {
        const m = getDataset('data/acampada_mallorca.json');
        const me = getDataset('data/acampada_menorca.json');
        const p = getDataset('data/acampada_pitiuses.json');
        const allFacilities = [...m, ...me, ...p];

        assert(allFacilities.length >= 45, 'Campsites dataset loaded');
        for (const f of allFacilities) {
            // Every facility must have fire restriction guidance
            assert(typeof f.restriccio_foc === 'string' && f.restriccio_foc.length > 0,
                `Facility ${f.slug} must state fire restriction compliance`);
        }
    });

    test('4.5.2: Advance reservation authorization required for scout camps', () => {
        const m = getDataset('data/acampada_mallorca.json');
        const me = getDataset('data/acampada_menorca.json');
        const p = getDataset('data/acampada_pitiuses.json');
        const allFacilities = [...m, ...me, ...p];

        const facilitiesWithPermit = allFacilities.filter(f =>
            typeof f.permis_antelacio === 'string' && f.permis_antelacio.length > 0
        );
        assert(facilitiesWithPermit.length >= 45, 'All youth camping facilities must document permit requirements');
    });
});

if (require.main === module) {
    const report = harness.printReport();
    process.exit(report.success ? 0 : 1);
}
