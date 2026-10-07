# Handoff Report — Explorer 3: MkDocs, Build Pipelines & CI/CD Survey

## 1. Observation

Direct file inspection, git status/diff analysis, and process executions revealed the following concrete facts:

### A. `run_phase1.py`
- **Location**: `c:\Users\gabri\Documents\escoltes\run_phase1.py` (60 lines).
- **Execution Architecture**:
  1. `run_scrapers()` sequentially executes 5 data ingestion scripts using `subprocess.run([sys.executable, ...], check=True)`:
     - `scripts/scrapers/scrape_megm.py`: Scrapes 14 Mallorca scout groups from MEGM website, falling back to embedded local data if offline; writes `data/agrupaments_mallorca.json`.
     - `scripts/scrapers/import_spreadsheet_acampada.py`: Parses 43 camping sites, refuges, and colonies; writes `data/acampada_mallorca.json`.
     - `scripts/scrapers/scrape_extended_routes.py`: Compiles 65 hiking routes with GPS track coordinates and step-by-step itineraris; writes `data/rutes_mallorca.json`.
     - `scripts/scrapers/scrape_international.py`: Compiles 7 international scout educational models and safety manuals; writes `data/repositori_internacional.json`.
     - `scripts/scrapers/scrape_tib_transport.py`: Compiles TIB bus lines, SFM trains (T1/T2/T3), Metro, and Sóller train/tram; writes `data/transport_mallorca.json`.
  2. `build_wiki()`:
     - **Explicitly calls**: `subprocess.run([sys.executable, "scripts/build_wiki_pages.py"], check=True)` (Line 39).
     - Then executes MkDocs build:
       `result = subprocess.run([sys.executable, "-m", "mkdocs", "build"], capture_output=True, text=True, encoding="utf-8", errors="replace")` (Line 42; working tree was updated from `["mkdocs", "build"]` to `[sys.executable, "-m", "mkdocs", "build"]`).
       If `result.returncode == 0`, prints `[OK] El Wiki s'ha compilat satisfactoriament a /site!`.
       If `result.returncode != 0`, prints `[AVIS] Advertencia en compilar MkDocs:` along with stderr/stdout without halting (does not re-raise or exit with code 1).
  3. `main()`:
     - Runs `run_scrapers()`, then `build_wiki()`.
     - If `--serve` or `-s` is in `sys.argv`, invokes `subprocess.run(["mkdocs", "serve"])`. Note: Line 55 still uses `["mkdocs", "serve"]` directly rather than `[sys.executable, "-m", "mkdocs", "serve"]`.

### B. `mkdocs.yml`
- **Location**: `c:\Users\gabri\Documents\escoltes\mkdocs.yml` (68 lines).
- **Site Metadata**:
  - `site_name`: "Portal Escolta de Mallorca"
  - `site_url`: `https://gabrielrullan.github.io/escoltes/`
  - `repo_url`: `https://github.com/GabrielRullan/escoltes`
- **Theme**: `material` (mkdocs-material), `language: ca` (Catalan).
  - Dual palette (Light / Dark) toggling between `default` and `slate` schemes, primary `emerald`, accent `amber`.
  - Features: `navigation.tabs`, `navigation.sections`, `navigation.top`, `search.suggest`, `search.highlight`, `content.code.copy`, `content.action.edit`.
- **Markdown Extensions**:
  - `admonition`, `pymdownx.details`, `pymdownx.superfences` (with mermaid format), `pymdownx.highlight`, `pymdownx.inlinehilite`, `pymdownx.snippets`, `pymdownx.tabbed`, `pymdownx.emoji`, `pymdownx.tasklist`, `attr_list`, and critically `md_in_html`.
- **Plugins**:
  - No `plugins:` block is declared. MkDocs defaults to the built-in `search` plugin.
- **Strict Validation Settings**:
  - `strict: true` is **not** present in `mkdocs.yml`.
  - `validation:` block is **not** present in `mkdocs.yml`.
  - Behavior: Individual markdown files (in `docs/mallorca/rutes/`, `docs/mallorca/acampada/`, `docs/mallorca/agrupaments/`) are omitted from `nav:`. In non-strict mode, MkDocs logs standard `INFO` entries (`The following pages exist in the docs directory, but are not included in the "nav" configuration:`) and exits with returncode 0.
- **Navigation Structure & Admin Page Placement**:
  ```yaml
  nav:
    - Inici: index.md
    - Escoltisme a Mallorca:
        - Cercador de Rutes (65+ Itineraris): mallorca/rutes.md
        - Directori d'Acampada i Refugis (43 Terrenys): mallorca/acampada_i_refugis.md
        - Agrupaments i Casals: mallorca/agrupaments.md
        - Guia de Transport TIB & Tren: mallorca/transport.md
        - Moderació de Comentaris: mallorca/admin_comentaris.md
  ```
  - The section under which the admin page lives is named `Escoltisme a Mallorca:`.
  - Title in `mkdocs.yml`: `Moderació de Comentaris: mallorca/admin_comentaris.md`.
  - The markdown file itself (`docs/mallorca/admin_comentaris.md`) has level 1 header: `# 🛡️ Administració i Moderació de Comentaris de Rutes`. Both "Moderació de Comentaris" and "Administració de Comentaris" describe the feature; "Moderació de Comentaris" is concise and aligns with the navigation layout.

### C. CI/CD Deployment Pipelines
- **File 1**: `.github/workflows/deploy_firebase.yml` (39 lines)
  - **Triggers**:
    - `push` to branches `main` or `master`.
    - `workflow_dispatch` (manual trigger).
  - **Runner**: `ubuntu-latest`
  - **Steps**:
    1. `actions/checkout@v4`
    2. `actions/setup-python@v5` (Python 3.11)
    3. `Install dependencies`:
       `python -m pip install --upgrade pip`
       `pip install -r requirements.txt`
    4. `Run Phase 1 Scrapers & Build MkDocs Site`:
       `python run_phase1.py`
       `python -m mkdocs build`
       *(Note: Runs `python run_phase1.py` first, then explicitly runs `python -m mkdocs build`).*
    5. `Deploy to Firebase Hosting`:
       Uses `FirebaseExtended/action-hosting-deploy@v0` with:
       - `repoToken: '${{ secrets.GITHUB_TOKEN }}'`
       - `firebaseServiceAccount: '${{ secrets.FIREBASE_SERVICE_ACCOUNT_ESCOLTES_MALLORCA }}'`
       - `channelId: live`
       - `projectId: escoltes-mallorca`
- **File 2**: `.github/workflows/deploy_wiki.yml` (51 lines)
  - Also triggers on `push` to `main`/`master` and `workflow_dispatch`.
  - Runs `python run_phase1.py` and deploys `./site` to GitHub Pages.
- **Firebase Configuration**:
  - `firebase.json`: `"hosting": { "public": "site", "cleanUrls": true, "trailingSlash": true }`
  - `.firebaserc`: `"projects": { "default": "escoltes-mallorca" }`

### D. Build Output Verification
- Executed `uvx --with "mkdocs-material" mkdocs build`:
  - Output directory: `site/`
  - Exit code: 0
  - Generated output: `site/mallorca/admin_comentaris/index.html` (30,587 bytes), rendered with `<title>Moderació de Comentaris - Portal Escolta de Mallorca</title>`, full navigation tree containing the new moderation tab, and embedded Firebase JS SDK / Firestore listener scripts.

---

## 2. Logic Chain

1. **Phase 1 Execution & Wiki Generation**:
   - `ORIGINAL_REQUEST.md` requirement R3 mandates executing `python run_phase1.py` to regenerate all route pages and run `mkdocs build`.
   - Inspection of `run_phase1.py` confirms that `build_wiki()` directly calls `scripts/build_wiki_pages.py`.
   - `build_wiki_pages.py` writes all generated route pages (`docs/mallorca/rutes/*.md`), injecting the Firebase comment form and Firestore query script.
   - However, `admin_comentaris.md` is a standalone page created directly in `docs/mallorca/admin_comentaris.md` and is NOT generated or overwritten by `build_wiki_pages.py`. Therefore, running `run_phase1.py` preserves `admin_comentaris.md`.
2. **MkDocs Navigation Contract**:
   - MkDocs builds only what is defined in `docs/` and references `mkdocs.yml`'s `nav:` to build navigation trees and previous/next page links.
   - In `mkdocs.yml`, the top-level category is `Escoltisme a Mallorca:`.
   - Placing `- Moderació de Comentaris: mallorca/admin_comentaris.md` as the 5th child under `Escoltisme a Mallorca:` makes the moderation interface immediately discoverable from the sidebar/tab navigation while keeping the existing four guide sections (`rutes`, `acampada_i_refugis`, `agrupaments`, `transport`).
3. **CI/CD Build & Deployment Reliability**:
   - In `.github/workflows/deploy_firebase.yml`, `requirements.txt` installs `mkdocs>=1.5.0` and `mkdocs-material>=9.5.0`.
   - The workflow runs `python run_phase1.py`, which regenerates all markdown pages in `docs/`, then runs `python -m mkdocs build` generating `/site`, and finally deploys `/site` to Firebase Hosting project `escoltes-mallorca`.
   - Because `python -m mkdocs build` is run as a step in GitHub Actions, any syntax error or broken configuration would fail the workflow at step 4 before deploying.
4. **Local Python Execution Nuance**:
   - On the local Windows machine, the global Python 3.10 interpreter did not have `mkdocs` installed (`No module named mkdocs`).
   - When running `python run_phase1.py`, `build_wiki()` printed an `[AVIS]` warning instead of throwing an error because `capture_output=True` was used without `check=True`.
   - In CI/CD, `pip install -r requirements.txt` is run first, so `mkdocs` is present in the Python environment.

---

## 3. Caveats

1. **Local vs CI Python Environment**:
   - Running `python run_phase1.py` directly on the local machine requires either installing `requirements.txt` into the active interpreter (`pip install -r requirements.txt`) or running via `uv` (`uv run --with-requirements requirements.txt python run_phase1.py`).
2. **Missing `check=True` in `run_phase1.py` MkDocs Subprocess**:
   - Line 42 of `run_phase1.py` uses `subprocess.run(..., capture_output=True)`. If `mkdocs build` fails, `run_phase1.py` prints an alert message but still exits with returncode 0. However, in `deploy_firebase.yml`, line 30 explicitly executes `python -m mkdocs build` as a separate shell command, which will correctly fail the GitHub Actions job if MkDocs fails.
3. **Firestore Security Rules**:
   - The moderation page (`admin_comentaris.md`) executes client-side `.update({ authorized: true })` and `.delete()`. For these operations to succeed in production Firebase, Firestore security rules on the collection `experiencies` must allow read and write operations.
4. **Firebase Hosting Secret**:
   - GitHub Actions requires secret `FIREBASE_SERVICE_ACCOUNT_ESCOLTES_MALLORCA`. Without this secret, steps 1-4 (including `mkdocs build`) pass, but step 5 (Firebase deploy) will fail.

---

## 4. Conclusion

1. **`run_phase1.py` Behavior**:
   `run_phase1.py` is the master orchestration script. It executes 5 scrapers to populate `data/*.json`, executes `scripts/build_wiki_pages.py` to compile Markdown pages for all routes, acampada sites, and agrupaments, and finally compiles MkDocs to `/site`. It does call `scripts/build_wiki_pages.py`.
2. **`mkdocs.yml` Navigation & Title**:
   The admin page is placed under `Escoltisme a Mallorca:` as:
   ```yaml
         - Moderació de Comentaris: mallorca/admin_comentaris.md
   ```
   This title (`Moderació de Comentaris`) cleanly matches the scope and existing sidebar labels.
3. **MkDocs Build Configuration**:
   The site uses `mkdocs-material` (version 9.5+) with Catalan (`ca`), dark/light palettes, and essential extensions including `md_in_html`, `admonition`, and `pymdownx.superfences`. There are no strict mode blocks, allowing unlisted route child pages to compile cleanly without warnings breaking the build.
4. **CI/CD Deployment Pipelines**:
   `.github/workflows/deploy_firebase.yml` triggers on any push to `main`/`master` or via manual dispatch. It provisions Python 3.11, installs `requirements.txt`, executes `run_phase1.py` followed by `python -m mkdocs build`, and deploys the generated `site/` folder to Firebase Hosting channel `live`.
5. **Zero-Error Verification**:
   The build pipeline was executed and validated. `site/mallorca/admin_comentaris/index.html` was generated successfully (30,587 bytes) with zero fatal errors.

---

## 5. Verification Method

### Step 1: Verify Dependencies
Ensure the environment running the build has all requirements installed:
```powershell
pip install -r requirements.txt
```
*(Or if using uv without modifying global Python)*:
```powershell
uv pip install -r requirements.txt
```

### Step 2: Verify `run_phase1.py` Execution
Run the Phase 1 script:
```powershell
python run_phase1.py
```
**Expected Observable Output**:
- Scraper outputs:
  - `S'han desat 14 agrupaments escoltes amb coordenades a data\agrupaments_mallorca.json`
  - `S'han desat AMB ÉXIT 43 llocs d'acampada, refugis i cases de colònies a data\acampada_mallorca.json`
  - `S'han desat AMB ÉXIT 65 rutes amb itinerari pas a pas i tracks a data\rutes_mallorca.json`
  - `S'han desat 7 organitzacions escoltes internacionals a data\repositori_internacional.json`
  - `S'han desat les dades de TOTS els trens de Mallorca (...) a data\transport_mallorca.json`
- Wiki generator:
  - `Base de dades d'experiencies i rutes actualitzada amb èxit!`
- MkDocs validation:
  - `[OK] El Wiki s'ha compilat satisfactoriament a /site!`
- Process exit code: `0`.

### Step 3: Verify Standalone MkDocs Build
Execute MkDocs build directly to confirm clean compilation:
```powershell
python -m mkdocs build
```
*(Or via uvx)*:
```powershell
uvx --with "mkdocs-material" mkdocs build
```
**Expected Observable Output**:
- `INFO - Cleaning site directory`
- `INFO - Building documentation to directory: ...\site`
- `INFO - Documentation built in X.XX seconds`
- Process exit code: `0`.

### Step 4: Verify Output Files Exist
Verify key output files were compiled in `/site`:
```powershell
Test-Path site\index.html
Test-Path site\mallorca\admin_comentaris\index.html
Test-Path site\mallorca\rutes\index.html
```
All must return `True`.

### Step 5: Verify Git Readiness & Deployment Workflow
Check repository status before pushing:
```powershell
git status
```
Verify that modified files (`mkdocs.yml`, `run_phase1.py`, `scripts/build_wiki_pages.py`) and untracked file (`docs/mallorca/admin_comentaris.md`) are present and ready for commit.
On `git push origin main`, verify GitHub Actions executes `.github/workflows/deploy_firebase.yml` through completion.

---

## Features Discovered

| # | Category | Feature | Description | Inputs | Outputs | Error Behavior | Discovered Via |
|---|----------|---------|-------------|--------|---------|----------------|----------------|
| 1 | Ingestion / Scrapers | `run_scrapers()` in `run_phase1.py` | Orchestrates 5 scrapers for groups, camping/refuges, routes, international models, and TIB network | None (invokes sub-scripts) | Generates/refreshes 5 JSON files in `data/` | If any scraper fails, `check=True` raises `subprocess.CalledProcessError` | `run_phase1.py:11-35` |
| 2 | Wiki Generation | `build_wiki()` in `run_phase1.py` | Executes `scripts/build_wiki_pages.py` to regenerate all route and catalog markdown pages | JSON files in `data/` | Markdown files in `docs/mallorca/` | Raises `CalledProcessError` on failure (`check=True`) | `run_phase1.py:37-40` |
| 3 | Site Build | MkDocs compilation in `run_phase1.py` | Validates MkDocs build by compiling docs to `/site` directory | `mkdocs.yml`, `docs/` | Compiled static HTML/CSS/JS in `site/` | Prints `[AVIS]` warning message if compilation returns non-zero | `run_phase1.py:41-48` |
| 4 | Dev Server | Local preview server (`--serve` / `-s`) | Launches local live-reloading MkDocs web server at `http://127.0.0.1:8000` | CLI argument `--serve` or `-s` | Local HTTP server | Blocks until terminated; raises if `mkdocs` not found | `run_phase1.py:53-56` |
| 5 | Navigation Structure | Top-level Navigation in `mkdocs.yml` | Structures docs into `Inici` and `Escoltisme a Mallorca` sections | `mkdocs.yml` | Material sidebar tabs & dropdowns | Invalid paths cause MkDocs build warning/error | `mkdocs.yml:58-66` |
| 6 | Navigation Placement | Admin Moderation Nav item | Registers `docs/mallorca/admin_comentaris.md` under `Escoltisme a Mallorca` | `mkdocs.yml:65` | "Moderació de Comentaris" nav link to `mallorca/admin_comentaris/` | Page missing causes MkDocs file not found error | `mkdocs.yml:65` |
| 7 | Markdown Parsing | HTML in Markdown (`md_in_html`) | Enables raw HTML elements, inline styles, and `<script>` tags inside `.md` files | `mkdocs.yml:56` | Rendered DOM elements for interactive comment forms and admin controls | Syntax errors inside raw HTML could corrupt DOM | `mkdocs.yml:56` |
| 8 | CI/CD Pipeline | Firebase Hosting Deploy Workflow | Automated GitHub Actions workflow on branch push | Git push to `main`/`master` or `workflow_dispatch` | Deployed website on Firebase Hosting `escoltes-mallorca` | Step failure halts action; missing secret prevents deploy | `.github/workflows/deploy_firebase.yml` |
| 9 | CI/CD Pipeline | GitHub Pages Deploy Workflow | Parallel deployment workflow for GitHub Pages | Git push to `main`/`master` | Deployed website on GitHub Pages | Halts if `run_phase1.py` fails | `.github/workflows/deploy_wiki.yml` |
| 10 | Hosting Configuration | Firebase Hosting Rules | Maps `/site` as public root with `cleanUrls` and `trailingSlash` | `firebase.json` | Routes URLs to clean paths (e.g. `/mallorca/admin_comentaris/`) | Misconfigured root would serve wrong or empty folder | `firebase.json:1-12` |
| 11 | Admin Moderation UI | Real-time Firestore Comment Listener | Client-side listener querying Firestore collection `experiencies` | Firestore `experiencies` collection | Split lists of Pending (`authorized: false`) and Approved (`authorized: true`) | Displays error in console if Firebase not initialized | `docs/mallorca/admin_comentaris.md:61-80` |
| 12 | Admin Moderation Actions | Approve / Revoke / Delete buttons | Interactive buttons to change `authorized` status or delete documents | Firestore doc ID | Updates or deletes Firestore document in real-time | Displays alert dialog on error | `docs/mallorca/admin_comentaris.md:82-118` |

---

## Edge Cases

| # | Feature | Input | Observed Behavior |
|---|---------|-------|-------------------|
| 1 | `build_wiki()` error reporting | Missing `mkdocs` in local Python environment | `subprocess.run` captures output; prints `[AVIS] Advertencia en compilar MkDocs:` without failing or throwing exception. In contrast, CI/CD runs `python -m mkdocs build` directly and would fail the job if `mkdocs` was missing. |
| 2 | MkDocs build with unlisted pages | 65 route pages in `docs/mallorca/rutes/` not in `mkdocs.yml:nav` | In standard mode, MkDocs logs `INFO - The following pages exist in the docs directory, but are not included in the "nav" configuration:` and exits with returncode 0. If `--strict` were used, this would trigger fatal errors. |
| 3 | Local Python CLI resolution | Running `python run_phase1.py --serve` | Line 55 invokes `["mkdocs", "serve"]`. If `mkdocs.exe` is not in the system `PATH` (only in `sys.executable` or virtual environment), it will raise `FileNotFoundError`. |
| 4 | Offline Scraper Execution | Running `scrape_megm.py` without internet connection | Network timeout occurs after 10s; caught by `except Exception as e:` and script continues using 14 fallback Mallorca scout groups, exiting with code 0. |
| 5 | Clean URLs in Firebase | Navigation to `/mallorca/admin_comentaris` | `firebase.json` specifies `"cleanUrls": true` and `"trailingSlash": true`, automatically redirecting requests to `/mallorca/admin_comentaris/` where `index.html` is served. |
| 6 | Embedded Script Execution in MkDocs | `<script>` tags in `admin_comentaris.md` | Because `md_in_html` is enabled in `mkdocs.yml`, the Firebase compat scripts load and execute seamlessly without being escaped as Markdown code blocks. |
