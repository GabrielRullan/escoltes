# Project: Balearic Islands Expansion (Escoltes de les Illes Balears)

## Architecture
- **Framework**: Astro v7 (SSG, static directory output to `./site`) with Tailwind CSS v4.
- **Client Interactive Components**: Vanilla TS / Leaflet 1.9.4 loaded via CDN in Layout (`window.L`), avoiding SSR issues.
- **Data Layer**:
  - Independent JSON datasets per island under `data/` preserving existing `data/*_mallorca.json` intact.
  - Unified TypeScript abstraction layer in `src/data/` (`routes.ts`, `campsites.ts`, `groups.ts`, `transport.ts`) providing typed entities with `illa: 'Mallorca' | 'Menorca' | 'Eivissa' | 'Formentera'`.
  - Type definitions in `src/types/index.ts`.
- **UI Architecture**:
  - Multi-island pill tabs / selector integrated into `FilterBar.astro`, `Header.astro`, and `acampada/index.astro`.
  - Dynamic interactive Leaflet map (`MallorcaMap.astro` / `BalearicMap.astro`) centered on the Balearic archipelago with bounding-box jumps per island.
  - Dynamic route detail pages (`src/pages/rutes/[slug].astro`) auto-generating 97 pages (65 Mallorca + 32 new).

## Feature Inventory
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | Menorca GR-223 Data | 20 official stages of Camí de Cavalls + 2 key variants with coordinates, elevation, water points, safety tips, official & Wikiloc links | M1 | survey |
| 2 | Eivissa Routes Data | 7 coastal & heritage routes (Ses Salines, Torre de ses Portes, Torre des Savinar, Els Amunts, Moscarter, Albarca, Comte, Molar) | M1 | survey |
| 3 | Formentera Green Routes Data | 3 green routes (Ses Illetes, Camí de sa Pujada a La Mola, Far de Barbaria) with sun/cliff safety guidelines | M1 | survey |
| 4 | Balearic Facilities Data | 15 legal youth facilities, hostels, and campsites in Menorca, Eivissa, and Formentera (Biniparratx, Sa Vinyeta, Cala des Jondal, etc.) with legal framework | M1 | survey |
| 5 | Balearic Scout Groups Data | 9 Escoltes de Menorca (MSC) groups and 2 Pitiüses groups (Los Cóndors ASDE, AE Isidor Macabich) | M1 | survey |
| 6 | Balearic Transport Data | 25 public transport lines connecting to trailheads and towns across Menorca, Eivissa, and Formentera | M1 | survey |
| 7 | Unified Data Abstraction | TypeScript modules in `src/data/` unifying Mallorca + new islands with strict types | M1 | survey |
| 8 | Multi-Island Selector | Global and page-level island filter (Mallorca, Menorca, Eivissa, Formentera, Totes) in FilterBar and Header | M2 | survey |
| 9 | Client Route Filtering | Fast client-side filtering via `data-illa` attributes and URL param `?illa=` | M2 | survey |
| 10 | Fallback for Town Drawings | Safe fallback image handling in `RouteCard.astro` for non-Mallorca municipalities | M2 | survey |
| 11 | Dynamic Balearic Map | Leaflet map with archipelago bounds `[39.50, 3.00]` zoom 8 and island bounding boxes | M3 | survey |
| 12 | Map & List Synchronization | Marker filtering and `map.flyToBounds` when an island is selected | M3 | survey |
| 13 | Route Detail Map Verification | Ensure individual route maps in `[slug].astro` center and fit polyline bounds for all 32 new routes | M3 | survey |
| 14 | Pages Integration | Update route catalog, campsites, groups, transport, and home pages to render Balearic data | M4 | survey |
| 15 | Static Build & Backward Compatibility | 100% preservation of 65 Mallorca routes & 45 campsites; clean `npm run build` with 0 errors | M4 | survey |
| 16 | E2E Requirement-Driven Test Suite | Automated opaque-box test runner covering Tiers 1-4 with minimum 120 test assertions | E2E-Track | survey |
| 17 | Final E2E Pass & Forensic Audit | Pass 100% of E2E test suite and clean verdict from Forensic Auditor | M5 | survey |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Balearic Data Foundation (`data-balears`) | JSON datasets for Menorca, Eivissa, Formentera routes, campsites, groups, transport + `src/data/` TS layer | none | DONE |
| M2 | Multi-Island UI & Filtering (`ui-multi-island`) | Multi-island selectors, FilterBar tabs, URL params, town drawings fallback | M1 | DONE |
| M3 | Dynamic Balearic Map (`map-cartography`) | Archipelago Leaflet map, per-island bounds, marker synchronization | M1 | DONE |
| M4 | Pages Integration & Build (`pages-integration`) | Astro pages update (`/rutes`, `/acampada`, `/agrupaments`, `/transport`, `/`), clean `npm run build` | M1, M2, M3 | DONE |
| M5 | Final E2E Pass & Audit (`final-e2e-audit`) | Pass 100% E2E test suite (Tiers 1-4) and obtain CLEAN Forensic Audit verdict | M4, TEST_READY | DONE |
| E2E | E2E Testing Track (`e2e-testing-track`) | Test harness, Tiers 1-4 requirement-driven test cases, `TEST_READY.md` publication | Parallel to M1-M4 | DONE |

## Interface Contracts
### Data Layer (`src/data/routes.ts`, `src/data/campsites.ts`, `src/data/groups.ts`, `src/data/transport.ts`)
- `Route`: extends Mallorca route schema with `illa: 'Mallorca' | 'Menorca' | 'Eivissa' | 'Formentera'`.
- `getAllRoutes(): Route[]` returns 97 routes (65 Mallorca + 22 Menorca + 7 Eivissa + 3 Formentera).
- `getRoutesByIsland(illa: string): Route[]`.
- `getAllCampsites(): Campsite[]` returns 60 campsites (45 Mallorca + 8 Menorca + 5 Eivissa + 2 Formentera).
- `getAllGroups(): ScoutGroup[]` returns 24 scout groups (13 Mallorca + 9 Menorca + 2 Eivissa).
- `getAllTransport(): TransportData`.

### UI Component Contracts
- `FilterBar.astro`: accepts `totalRoutes`, `zones`, emits/updates client-side filter events and `data-illa` attributes.
- `MallorcaMap.astro` / `BalearicMap.astro`: exposes global function `window.__setMapIsland(island: string)`.

## Code Layout
- Existing files preserved:
  - `data/rutes_mallorca.json` (DO NOT OVERWRITE)
  - `data/acampada_mallorca.json` (DO NOT OVERWRITE)
  - `data/agrupaments_mallorca.json` (DO NOT OVERWRITE)
  - `data/transport_mallorca.json` (DO NOT OVERWRITE)
- New data files:
  - `data/rutes_menorca.json`
  - `data/rutes_eivissa.json`
  - `data/rutes_formentera.json`
  - `data/acampada_menorca.json`
  - `data/acampada_pitiuses.json`
  - `data/agrupaments_menorca.json`
  - `data/agrupaments_pitiuses.json`
  - `data/transport_menorca.json`
  - `data/transport_pitiuses.json`
- New TypeScript abstraction files:
  - `src/types/index.ts`
  - `src/data/routes.ts`
  - `src/data/campsites.ts`
  - `src/data/groups.ts`
  - `src/data/transport.ts`
  - `src/data/islands.ts`
- Modified Astro UI files:
  - `src/components/FilterBar.astro`
  - `src/components/Header.astro`
  - `src/components/RouteCard.astro`
  - `src/components/MallorcaMap.astro`
  - `src/pages/rutes/index.astro`
  - `src/pages/rutes/[slug].astro`
  - `src/pages/acampada/index.astro`
  - `src/pages/agrupaments/index.astro`
  - `src/pages/transport/index.astro`
  - `src/pages/index.astro`
