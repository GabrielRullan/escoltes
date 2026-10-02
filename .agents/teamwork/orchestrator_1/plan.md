# Orchestration Plan: Route Comments with Admin Authorization

## Overview
Implement route comment submission without login, admin moderation interface, public display filtering, and deployment verification for the Escoltes Portal project.

## Phased Approach

### Phase 0: Survey & Technical Exploration
- Spawn 3 parallel Explorers:
  - **Explorer 1 (Route Pages & Scripts)**: Explore `scripts/build_wiki_pages.py`, how route pages are structured, current comments/experience implementation, and how HTML/JS is injected.
  - **Explorer 2 (Firestore & Admin Requirements)**: Explore Firebase setup, credentials, SDK usage, Firestore rules, collections (`experiencies`), document schema, and how `docs/mallorca/admin_comentaris.md` should be built.
  - **Explorer 3 (Build, MkDocs & CI/CD)**: Explore `run_phase1.py`, `mkdocs.yml`, nav structure under Escoltisme, GitHub Actions workflow `.github/workflows/deploy_firebase.yml`, and verification procedures.
- Synthesize findings into `PROJECT.md`.

### Phase 1: Milestone 1 — Comment Form & Public Filtering on Route Pages (R1 & R2 Public)
- Explorer -> Worker -> Reviewers (2) -> Challengers (2) -> Auditor -> Gate check.
- Update `scripts/build_wiki_pages.py` to:
  - Include the 6 required fields: Nom, Email, Branca Escolta, Agrupament Escolta, Valoració (1-5 stars), Comentari.
  - Submit directly to Firestore collection `experiencies` with `authorized: false` without login prompt.
  - Display success notification: *"✅ Comentari enviat amb èxit! Està pendent d'autorització per part de l'administrador per ser visible públicament."*
  - Filter public route page comment display to only comments where `authorized: true` (or legacy comments).

### Phase 2: Milestone 2 — Admin Moderation Interface (R2 Admin)
- Explorer -> Worker -> Reviewers (2) -> Challengers (2) -> Auditor -> Gate check.
- Create `docs/mallorca/admin_comentaris.md`:
  - List pending comments (`authorized: false`).
  - Provide "Aprovar" button to set `authorized: true` in Firestore.
  - Provide "Rebutjar / Esborrar" button to delete document from Firestore.
  - List authorized comments with option to revoke/delete.
  - Register page in `mkdocs.yml` under Escoltisme section.

### Phase 3: Milestone 3 — Build Validation, Git Commit & Deployment Verification (R3)
- Run `python run_phase1.py` and `mkdocs build`.
- Verify generated pages, test comment submission & admin approval flow.
- Commit and push to git to trigger `deploy_firebase.yml`.
- Reviewer & Auditor gate verification.

### Phase 4: Final Synthesis & Parent Reporting
- Aggregate all verification artifacts.
- Send completion message to parent.
