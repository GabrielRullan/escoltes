# Project: Route Comments with Admin Authorization

## Architecture
- **Static Wiki Generator**: `scripts/build_wiki_pages.py` parses `data/rutes_mallorca.json`, `data/experiencies_rutes.json`, and other data files to generate markdown route pages in `docs/mallorca/rutes/{slug}.md`.
- **Frontend Storage & Sync**: Firebase Firestore (SDK v10.8.0 Compat) with Project ID `escoltes-mallorca`.
  - Public route pages submit unauthenticated reviews to collection `experiencies` with `authorized: false`.
  - Public route pages query collection `experiencies` filtering for approved reviews (`authorized === true || authorized === undefined`).
- **Admin Moderation Interface**: `docs/mallorca/admin_comentaris.md` listens to collection `experiencies` in real-time, displays pending and authorized reviews, and provides Approve, Revoke, and Delete actions.
- **Documentation Engine**: MkDocs with `mkdocs-material` (Catalan language `ca`, `md_in_html` enabled) compiling `docs/` to `site/`.
- **CI/CD & Deployment**: GitHub Actions workflow `.github/workflows/deploy_firebase.yml` running `python run_phase1.py` and `python -m mkdocs build` before deploying `/site` to Firebase Hosting channel `live`.

## Feature Inventory
| # | Feature | Description | Milestone | Source | Status |
|---|---------|-------------|-----------|--------|--------|
| 1 | Comment Form on Route Pages (R1) | Add/verify 6 input fields (Nom, Email, Branca Escolta, Agrupament, Valoració 1-5, Comentari) without requiring user login | M1 | ORIGINAL_REQUEST §R1 | VERIFIED (Gate 2 PASS) |
| 2 | Unauthenticated Submission (R1) | Submits review to Firestore `experiencies` collection with `authorized: false` | M1 | ORIGINAL_REQUEST §R1 | VERIFIED (Gate 2 PASS) |
| 3 | User Notification on Submit (R1) | Displays: "✅ Comentari enviat amb èxit! Està pendent d'autorització per part de l'administrador per ser visible públicament." | M1 | ORIGINAL_REQUEST §R1 | VERIFIED (Gate 2 PASS) |
| 4 | Fix Script Syntax Error in Route Pages | Remove stray closing tokens & double-quote Catalan string at line 397 in `scripts/build_wiki_pages.py` | M1 | Survey & Reviewers | VERIFIED (Gate 2 PASS) |
| 5 | Public Comment Filtering & Legacy Support (R2) | Public route queries display only comments where `authorized == true` or legacy comments | M1 | ORIGINAL_REQUEST §R2 | VERIFIED (Gate 2 PASS) |
| 6 | Restore Agrupaments Table Rows | Restore missing 2 nearest scout groups table rows in `scripts/build_wiki_pages.py` line 557 | M1 | Survey (Explorer 1) | VERIFIED (Gate 2 PASS) |
| 7 | Admin Moderation Page (R2) | Create/update `docs/mallorca/admin_comentaris.md` with realtime Firestore listener | M2 | ORIGINAL_REQUEST §R2 | VERIFIED (Gate 2 PASS) |
| 8 | Admin Approve Action (R2) | Single-click button to update doc to `authorized: true` (and `approvedAt`), immediately visible on route pages | M2 | ORIGINAL_REQUEST §R2 | VERIFIED (Gate 2 PASS) |
| 9 | Admin Delete / Reject Action (R2) | Single-click button to permanently delete pending or authorized comment from Firestore | M2 | ORIGINAL_REQUEST §R2 | VERIFIED (Gate 2 PASS) |
| 10 | Admin Authorized List & Revoke Action (R2) | List of already authorized comments with option to revoke (`authorized: false`) or delete | M2 | ORIGINAL_REQUEST §R2 | VERIFIED (Gate 2 PASS) |
| 11 | MkDocs Navigation Registration (R2) | Register admin page in `mkdocs.yml` under `Escoltisme a Mallorca:` as `Moderació de Comentaris: mallorca/admin_comentaris.md` | M2 | ORIGINAL_REQUEST §R2 & MkDocs | VERIFIED (Gate 2 PASS) |
| 12 | XSS Protection & UX Polish | Escape all user input before rendering in DOM, safe star rendering, and clean route links | M1, M2 | Survey (Explorer 1 & 2) | VERIFIED (Gate 2 PASS) |
| 13 | Phase 1 & Wiki Regeneration (R3) | Execute `python run_phase1.py` to regenerate route pages and build wiki with zero errors | M3 | ORIGINAL_REQUEST §R3 | VERIFIED (Gate 2 PASS) |
| 14 | MkDocs Site Compilation (R3) | Validate `mkdocs build` compiles cleanly into `site/` with zero errors | M3 | ORIGINAL_REQUEST §R3 | VERIFIED (Gate 2 PASS) |
| 15 | Git Commit & Deployment Trigger (R3) | Commit all changes and push to git to trigger GitHub Actions `deploy_firebase.yml` | M3 | ORIGINAL_REQUEST §R3 | VERIFIED (Gate 2 PASS) |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | Comment Form on Route Pages & Public Filtering (R1 & R2 Public) | Fix syntax error & table bug in `scripts/build_wiki_pages.py`, verify/update 6 fields form, unauthenticated write (`authorized: false`), notification text, and public query filtering. Regenerate route pages. | none | DONE |
| 2 | Admin Moderation Interface & Navigation (R2 Admin) | Complete `docs/mallorca/admin_comentaris.md` with pending/approved lists, approve/revoke/delete actions, XSS escaping, and verify registration in `mkdocs.yml` under Escoltisme. | M1 | DONE |
| 3 | Build Validation, Phase 1 Execution, Git Commit & Deployment (R3) | Run `python run_phase1.py` and `python -m mkdocs build`, verify generated artifacts in `site/`, commit to git, and verify GitHub Actions deployment. | M1, M2 | DONE |

## Interface Contracts
### Route Pages (`scripts/build_wiki_pages.py`) ↔ Firestore (`experiencies`)
- **Collection**: `experiencies`
- **Document Payload on Submit**:
  ```javascript
  {
    ruta_slug: String,      // Route slug matching markdown filename
    nom: String,            // Author name (mandatory)
    email: String,          // Author email (mandatory)
    agrupament: String,     // Scout group name (mandatory)
    branca: String,         // Scout unit: Castors/Fures, Llops/Daines, Pioners/Rangers, Rovers/Rutes, Caps/Monitors
    puntuacio: Number,      // Rating (1-5)
    data: String,           // Optional date/season string
    comentari: String,      // Review text (mandatory, >= 5 chars)
    authorized: Boolean,    // Initial value: false
    createdAt: Timestamp    // firebase.firestore.FieldValue.serverTimestamp()
  }
  ```
- **Public Query**:
  `db.collection("experiencies").where("ruta_slug", "==", routeSlug)` with client-side filter `data.authorized === true || data.authorized === undefined` to include authorized and legacy reviews while excluding pending reviews.

### Admin Moderation (`docs/mallorca/admin_comentaris.md`) ↔ Firestore (`experiencies`)
- **Listener**: `db.collection("experiencies").onSnapshot(...)`
- **Actions**:
  - `Aprovar`: `db.collection("experiencies").doc(docId).update({ authorized: true, approvedAt: serverTimestamp() })`
  - `Desautoritzar`: `db.collection("experiencies").doc(docId).update({ authorized: false })`
  - `Esborrar`: `db.collection("experiencies").doc(docId).delete()`

## Code Layout
- `scripts/build_wiki_pages.py`: Generates route pages in `docs/mallorca/rutes/*.md`.
- `docs/mallorca/admin_comentaris.md`: Admin moderation interface page.
- `mkdocs.yml`: Documentation configuration and navigation tree.
- `run_phase1.py`: Master orchestration script executing scrapers, wiki generation, and MkDocs build.
- `.github/workflows/deploy_firebase.yml`: Deployment CI/CD workflow.
