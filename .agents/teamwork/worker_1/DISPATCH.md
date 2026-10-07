# Dispatch to Worker 1

Implement R1 (Comment Form on Route Pages), R2 (Admin Moderation & Display Filtering), and R3 (Build Validation, Git Commit, and Deployment Verification) per ORIGINAL_REQUEST.md and the survey handoffs from Explorer 1, 2, and 3.

Read the detailed instructions in your dispatch prompt and record all changes and verification outputs in `handoff.md`.

## 2026-10-02T06:07:38Z
You are Worker 1 for Route Comments with Admin Authorization.
Your working directory is: c:\Users\gabri\Documents\escoltes\.agents\teamwork\worker_1
Parent conversation ID: dcb42897-fdd4-46e4-b072-4c35d17ef50c

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

MANDATORY INPUT:
Read the authoritative user request at:
c:\Users\gabri\Documents\escoltes\.agents\teamwork\ORIGINAL_REQUEST.md

SURVEY HANDOFFS TO CONSULT:
- Explorer 1 (Route pages & build_wiki_pages.py): c:\Users\gabri\Documents\escoltes\.agents\teamwork\explorer_survey_1\handoff.md
- Explorer 2 (Firestore & Admin interface): c:\Users\gabri\Documents\escoltes\.agents\teamwork\explorer_survey_2\handoff.md
- Explorer 3 (MkDocs & Build pipelines): c:\Users\gabri\Documents\escoltes\.agents\teamwork\explorer_survey_3\handoff.md

FILE OWNERSHIP:
You exclusively own and may edit/create:
- `scripts/build_wiki_pages.py`
- `docs/mallorca/admin_comentaris.md`
- `mkdocs.yml`
- Execution of `run_phase1.py` and `mkdocs build`
- Git commit and git push

DETAILED IMPLEMENTATION TASKS:

1. Update `scripts/build_wiki_pages.py`:
   - Fix syntax error: Remove the stray tokens at lines 407–409 (`submitBtn.disabled = false; } };`).
   - Fix nearest scout groups table at line 557: Restore the loop:
     ```python
     for dist, agr in agrupaments_amb_dist[:2]:
         md += f"| **{agr['nom']}** | {agr['municipi']} | **{dist:.1f} km** | [Veure Casal](../agrupaments/{agr['slug']}.md) |\n"
     ```
   - Ensure the comment form (`get_firebase_experiences_section_html`) captures all 6 required fields without requiring user login:
     * Nom (Name)
     * Email (Email address)
     * Branca Escolta (Scout Unit dropdown: Castors/Fures, Llops/Daines, Pioners/Rangers, Rovers/Rutes, Caps/Monitors)
     * Agrupament Escolta (Scout Group)
     * Valoració (Rating 1-5 stars)
     * Comentari (Comment text)
   - On submission, write entry to Firebase Firestore collection `experiencies` with `authorized: false` and `createdAt: serverTimestamp()`.
   - Ensure the notification message upon submission is exactly:
     "✅ Comentari enviat amb èxit! Està pendent d'autorització per part de l'administrador per ser visible públicament."
   - In catch block, show accurate error ("❌ Error en enviar el comentari: Si us plau, comprova la teva connexió.") instead of misleading success.
   - Sanitize user inputs with HTML escaping before DOM insertion.
   - In `initFirebaseExperiences` (lines 302–310), query by `.where("ruta_slug", "==", routeSlug)` and filter client-side:
     `if (data.authorized === true || data.authorized === undefined) { fetched.push(data); }`
     This ensures approved comments (`authorized == true`) AND legacy comments without `authorized` field are shown publicly, while pending comments (`authorized == false`) are strictly hidden.

2. Create/Update Admin Moderation Interface (`docs/mallorca/admin_comentaris.md`):
   - Implement the complete, secure, responsive admin interface specified in Explorer 2 handoff Section 4.3:
     * Connect to Firestore (`escoltes-mallorca`) using Firebase Compat SDK v10.8.0.
     * Section 1: Pending Comments (`authorized: false`) with real-time counter badge.
     * Section 2: Approved Comments (`authorized: true`) with real-time counter badge.
     * Action "Aprovar": Updates Firestore doc to `authorized: true` and `approvedAt: serverTimestamp()`.
     * Action "Rebutjar / Esborrar": Deletes the document from Firestore.
     * In Approved section: Action "Desautoritzar" (updates doc to `authorized: false`) and "Esborrar" (deletes doc).
     * Card rendering with author name, email, scout group, scout unit, stars (1-5), submission date, comment text, and clickable route link to `../rutes/{slug}/`.
     * Full XSS escaping (`escapeHtml()`) on all displayed fields.
     * MkDocs Material theme integration (`document$.subscribe(window.initAdminComments)`).

3. Verify `mkdocs.yml`:
   - Ensure `docs/mallorca/admin_comentaris.md` is registered under `nav` -> `Escoltisme a Mallorca:` as:
     `- Moderació de Comentaris: mallorca/admin_comentaris.md`

4. Build Validation:
   - Run `python run_phase1.py` and verify all scrapers run, `scripts/build_wiki_pages.py` regenerates all route pages, and the script exits with 0 errors.
   - Run `python -m mkdocs build` and confirm site compiles cleanly to `/site` with 0 errors.
   - Verify that `site/mallorca/admin_comentaris/index.html` and route pages (e.g. `site/mallorca/rutes/es-salt-des-freu-orient/index.html`) exist and are non-empty.

5. Git Commit & Push:
   - Run `git status` and `git diff` to review all modified and new files.
   - Stage all relevant changes (`git add`).
   - Commit with a clear, descriptive commit message.
   - Push to git remote (`git push origin main` or current tracking branch) to trigger `.github/workflows/deploy_firebase.yml`.

6. Documentation & Report:
   - Write a complete handoff report to `c:\Users\gabri\Documents\escoltes\.agents\teamwork\worker_1\handoff.md` with:
     * Observation: Files modified, exact changes made.
     * Verification: Commands executed, terminal outputs, exit codes.
     * Status of Acceptance Criteria: Form & Data Model, Admin & Public Visibility, Build & Deployment.
   - Send a completion message back to parent when done.
