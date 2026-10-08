# Test Infrastructure: Balearic Islands Expansion E2E Suite

**Project**: Escoltes de les Illes Balears  
**Component**: End-to-End Requirement-Driven Verification Harness  
**Author**: E2E Testing Specialist  
**Standard**: Node.js CommonJS Native TAP v13 Runner  

---

## 1. Overview & Objective

The Balearic Islands Expansion E2E Test Suite provides an automated, opaque-box, requirement-driven verification mechanism for all 17 features outlined in `PROJECT.md` and `ORIGINAL_REQUEST.md`.

It enforces:
1. Complete data coverage across Menorca (GR-223 20 stages + variants), Eivissa, and Formentera.
2. 100% backward compatibility of existing Mallorca datasets (65 routes, 45 campsites, 13 groups).
3. Type and interface integrity of the unified TypeScript data layer (`src/data/`).
4. Multi-island UI responsiveness (`FilterBar.astro`, `RouteCard.astro`, `Header.astro`, `MallorcaMap.astro`).
5. Leaflet map centering, bounding box management (`window.__setMapIsland`), and route polyline fitting.
6. Real-world scout pedagogical safety constraints (water rationing, heat protection, legal camping authorization under Llei 10/2022).

---

## 2. Directory Layout & Architecture

```
tests/
├── test_harness.cjs                    # Core harness: test registry, assertion engine, TAP reporter
├── run_e2e_tests.cjs                   # Master test runner executable
├── tier1_feature_coverage.test.cjs     # Tier 1: Feature coverage (Features 1-17, >=85 tests)
├── tier2_boundary_corner.test.cjs      # Tier 2: Boundary & edge cases (6 categories, >=30 tests)
├── tier3_cross_feature.test.cjs        # Tier 3: Pairwise cross-feature interactions (>=25 tests)
└── tier4_real_world_scenarios.test.cjs # Tier 4: Scout operational scenarios (5 missions, >=20 tests)
```

### Core Harness Components (`tests/test_harness.cjs`)
- **Zero Third-Party Runtime Dependencies**: Uses Node.js standard library (`fs`, `path`, `assert`, `vm`). Can be run in any standard Node.js (v18+) environment without installing extra npm packages.
- **Assertion Tracking**: Counts individual assertions executed to guarantee the minimum threshold of 120 assertions.
- **Dual Reporting**:
  - **Formatted Terminal Output**: Grouped by test suite with colorized status badges (`✅ PASS`, `❌ FAIL`).
  - **TAP v13 Stream**: Standardized machine-readable Test Anything Protocol output.
- **Deterministic Exit Codes**:
  - Exit code `0`: All tests passed.
  - Exit code `1`: One or more tests failed.

---

## 3. How to Run the Tests

### 3.1 Complete Test Run (All Tiers)
```bash
node tests/run_e2e_tests.cjs
```

### 3.2 Running Specific Tiers
```bash
# Run only Tier 1 (Feature Coverage)
node tests/run_e2e_tests.cjs --tier=1

# Run only Tier 2 (Boundary & Corner Cases)
node tests/run_e2e_tests.cjs --tier=2

# Run only Tier 3 (Cross-Feature Combinations)
node tests/run_e2e_tests.cjs --tier=3

# Run only Tier 4 (Real-World Scenarios)
node tests/run_e2e_tests.cjs --tier=4
```

### 3.3 TAP Output Mode
```bash
node tests/run_e2e_tests.cjs --tap
```

---

## 4. Test Suite Specification (4 Tiers)

### Tier 1: Feature Coverage (Features 1 to 17)
Covers all 17 features from `PROJECT.md`:
1. `Feature 1`: Menorca GR-223 Data (20 official stages + 2 variants).
2. `Feature 2`: Eivissa Routes Data (7 coastal and heritage routes).
3. `Feature 3`: Formentera Green Routes Data (3 green routes).
4. `Feature 4`: Balearic Facilities Data (15 legal youth facilities, hostels, campsites).
5. `Feature 5`: Balearic Scout Groups Data (9 Menorca + 2 Pitiüses).
6. `Feature 6`: Balearic Transport Data (25 public transport lines).
7. `Feature 7`: Unified Data Abstraction (`src/data/` modules).
8. `Feature 8`: Multi-Island Selector (all islands pill tabs / filter).
9. `Feature 9`: Client Route Filtering (`data-illa` attributes, `?illa=` query param).
10. `Feature 10`: Fallback for Town Drawings (non-Mallorca safe fallback).
11. `Feature 11`: Dynamic Balearic Map (Archipelago bounds `[39.50, 3.00]` zoom 8).
12. `Feature 12`: Map & List Synchronization (`window.__setMapIsland`).
13. `Feature 13`: Route Detail Map Verification (polyline bounds fitting).
14. `Feature 14`: Pages Integration (`/rutes`, `/acampada`, `/agrupaments`, `/transport`, `/`).
15. `Feature 15`: Static Build & Backward Compatibility (65 Mallorca routes preserved, clean build).
16. `Feature 16`: E2E Requirement-Driven Test Suite (executable, TAP output, >=120 assertions).
17. `Feature 17`: Final E2E Pass & Forensic Audit Readiness.

### Tier 2: Boundary & Corner Cases
1. Empty and wildcard island filter (`""`, `"totes"`).
2. Invalid island tags (`?illa=cabrera`, `?illa=invalid`).
3. Geographic coordinate boundaries (`lat: 38.50..40.20`, `lon: 1.15..4.45`).
4. Catalan diacritic character encoding (UTF-8 clean, no mojibake, no `\uFFFD`).
5. Null safety and optional fields resiliency.
6. Zero-water point stages handling and explicit safety warnings.

### Tier 3: Cross-Feature Interactions
1. Island filter + Route cards visible count synchronization.
2. Island filter + Leaflet bounding box jump (`__setMapIsland`).
3. Campsite capacity + Transport line proximity.
4. Route difficulty + Scout unit pedagogical suitability.
5. Island filter + Campsites catalog synchronization.

### Tier 4: Real-World Scout Application Scenarios
1. Castors unit (6-8 yrs) day route (< 5km, flat, water accessible).
2. Truc / Rovers expedition on Menorca North Coast (Etapes 6-7, Biniparratx basecamp, water protocol).
3. Eivissa coastal hike with direct TIB bus connection (car-free scouting).
4. Formentera heat protection and water rationing compliance.
5. Multi-day South Coast Menorca trek with legal campsite overnight stay.

---

## 5. Verification Metrics & Thresholds

| Metric | Target | Enforced Threshold |
|---|---|---|
| Total Test Cases | >= 150 | >= 100 |
| Total Test Assertions | >= 200 | **>= 120 (MANDATORY)** |
| Tier 1 Features Covered | 17 / 17 | 100% |
| Mallorca Backward Compatibility | 65 routes / 45 campsites | 100% byte & count preservation |
| Character Encoding | UTF-8 | 0 encoding errors |

---

## 6. Exit Codes & CI/CD Integration

In automated build pipelines (GitHub Actions, Firebase Deploy):
```bash
node tests/run_e2e_tests.cjs
```
- If any assertion fails, the process exits with `code 1`, halting the deployment and printing the exact failure diff.
- Once all worker milestones (M1 through M4) are complete, `node tests/run_e2e_tests.cjs` exits with `code 0`.
