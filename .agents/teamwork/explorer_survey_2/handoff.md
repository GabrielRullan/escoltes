# Handoff Report — Explorer 2: Firestore & Admin Interface Architecture

## 1. Observation

### 1.1 Firebase Configuration & SDK Versions
* **Project ID**: Configured as `"escoltes-mallorca"` across:
  * `.firebaserc` (line 3): `"default": "escoltes-mallorca"`
  * `.github/workflows/deploy_firebase.yml` (line 38): `projectId: escoltes-mallorca`
  * `scripts/build_wiki_pages.py` (line 225): `projectId: "escoltes-mallorca"`
  * `docs/mallorca/admin_comentaris.md` (line 45): `projectId: "escoltes-mallorca"`
* **Hosting Config (`firebase.json`)**:
  ```json
  {
    "hosting": {
      "public": "site",
      "ignore": ["firebase.json", "**/.*", "**/node_modules/**"],
      "cleanUrls": true,
      "trailingSlash": true
    }
  }
  ```
  `firebase.json` specifies only the `hosting` target pointing to `site`. There is no `firestore` stanza or rules pointer.
* **Deployment Workflow (`.github/workflows/deploy_firebase.yml`)**:
  Uses `FirebaseExtended/action-hosting-deploy@v0` (lines 33–38) triggered on push to `main`/`master`. It only deploys static hosting files from `site/` using `secrets.FIREBASE_SERVICE_ACCOUNT_ESCOLTES_MALLORCA`. It does not deploy Firestore security rules or indexes.
* **Firebase SDK Version**:
  Universal use of **Firebase JavaScript SDK v10.8.0 Compat libraries via CDN**:
  ```html
  <script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-app-compat.js"></script>
  <script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore-compat.js"></script>
  ```
  Found in `scripts/build_wiki_pages.py` (lines 134–135) and `docs/mallorca/admin_comentaris.md` (lines 9–10).
  * Syntax style: Uses namespaced compat API (`firebase.initializeApp(...)`, `firebase.firestore()`, `db.collection("experiencies")`, `firebase.firestore.FieldValue.serverTimestamp()`).

### 1.2 `experiencies` Collection Schema & Current Data
* **Static Seed Data (`data/experiencies_rutes.json`)**: Contains 8 sample reviews (all labeled `[PROVA / DEMO]`), covering fields: `ruta_slug`, `agrupament`, `branca`, `puntuacio`, `data`, `comentari`.
* **Form Submission (`scripts/build_wiki_pages.py`, lines 363–374)** creates documents in `experiencies` with:
  ```javascript
  const newExp = {
      ruta_slug: slug,
      nom: nom,
      email: email,
      agrupament: agrupament,
      branca: branca,
      puntuacio: puntuacio,
      data: dataVal,
      comentari: comentari,
      authorized: false,
      createdAt: (typeof firebase !== 'undefined' && firebase.firestore) ? firebase.firestore.FieldValue.serverTimestamp() : new Date().toISOString()
  };
  ```
* **Public Route Query (`scripts/build_wiki_pages.py`, lines 302–305)**:
  ```javascript
  db.collection("experiencies")
    .where("ruta_slug", "==", routeSlug)
    .where("authorized", "==", true)
    .onSnapshot(...)
  ```
* **Admin Moderation Updates (`docs/mallorca/admin_comentaris.md`, lines 86–89, 100–102, 113)**:
  * Approve: `db.collection("experiencies").doc(docId).update({ authorized: true, approvedAt: firebase.firestore.FieldValue.serverTimestamp() })`
  * Revoke: `db.collection("experiencies").doc(docId).update({ authorized: false })`
  * Delete: `db.collection("experiencies").doc(docId).delete()`

### 1.3 Firestore Security Rules
* There is **no `firestore.rules` file** in the repository.
* Neither `firebase.json` nor `.github/workflows/deploy_firebase.yml` manages or deploys security rules.
* Security rules are configured directly in the Firebase Console for project `escoltes-mallorca`.

### 1.4 Admin Interface (`docs/mallorca/admin_comentaris.md`)
* An implementation already exists as an untracked file `docs/mallorca/admin_comentaris.md` (221 lines).
* It is registered in `mkdocs.yml` under `nav` -> `Escoltisme a Mallorca` -> `Moderació de Comentaris: mallorca/admin_comentaris.md` (line 65).
* Running `python -m mkdocs build` compiles cleanly into `site/mallorca/admin_comentaris/index.html` (exit code 0).

### 1.5 Critical Syntax Bug Observed in `scripts/build_wiki_pages.py`
In `scripts/build_wiki_pages.py` lines 401–410:
```python
        }} catch (error) {{
            console.error("Error al enviar a Firebase:", error);
            statusMsg.style.color = '#e65100';
            statusMsg.innerText = '✅ Comentari gravat localment. Està pendent d\'autorització per l\'administrador.';
            submitBtn.disabled = false;
        }}
    }};
            submitBtn.disabled = false;
        }}
    }};
```
The dangling lines 407–409 contain extra closing braces (`submitBtn.disabled = false; }};`) which inject invalid JavaScript into all 65 generated route markdown files in `docs/mallorca/rutes/*.md`. Confirmed by viewing `docs/mallorca/rutes/cami-des-rafal-deia.md` lines 402–404.

---

## 2. Logic Chain

1. **SDK Choice & Justification**: MkDocs is a static site generator compiling Markdown to HTML without a Node.js bundling pipeline (such as Vite or Webpack). Using modular Firebase v9/v10 (`import { initializeApp } from 'firebase/app'`) in raw Markdown scripts requires `<script type="module">` and ES module CDNs or build toolchains. The Firebase v10.8.0 compat bundle (`firebase-app-compat.js` + `firebase-firestore-compat.js`) provides standard browser globals (`firebase`) and namespace methods, making it completely stable, self-contained, and compatible across all static MkDocs templates.
2. **Collection Schema & Field Types**:
   * `ruta_slug` (string): Identifies route page association.
   * `nom` (string) & `email` (string): Reviewer personal details captured without user login.
   * `agrupament` (string) & `branca` (string): Scout structure identity.
   * `puntuacio` (number 1–5): Rating score used for star calculations.
   * `data` (string): Date/season of hike.
   * `comentari` (string): User advice.
   * `authorized` (boolean): Key gatekeeper for public display. When `false`, ignored by public query; when `true`, included in public query.
   * `createdAt` (timestamp): Created upon submission.
   * `approvedAt` (timestamp): Added when approved.
3. **Firestore Indexing Logic**:
   * Public route query uses: `.where("ruta_slug", "==", routeSlug).where("authorized", "==", true)`. In Firestore, multiple equality (`==`) filters are merged automatically using single-field indexes; no manual composite index is required.
   * In `docs/mallorca/admin_comentaris.md`, listening to `db.collection("experiencies").onSnapshot(...)` without chained filters avoids any indexing requirement and allows client-side segregation into pending and approved buckets in real time.
4. **Security Rules Reasoning**:
   * Because the portal operates as a fully static site with no Firebase Authentication (no user login required to submit, and no admin login barrier), all Firestore writes, updates, and reads come from unauthenticated browser clients.
   * If Firestore rules are set to require authentication (`request.auth != null`), both public submission and the admin page would fail with permission errors.
   * Therefore, rules in the Firebase Console must allow unauthenticated create with `authorized == false`, unauthenticated read for `authorized == true`, and unauthenticated read/update/delete for the moderation interface (or open read/write on `/experiencies`).
5. **State Transition Logic**:
   * **Submit**: User submits form on route page -> Document created with `authorized: false` -> Not returned by public query (`where("authorized", "==", true)`).
   * **Approve**: Admin clicks "Aprovar" -> `.update({ authorized: true, approvedAt: serverTimestamp() })` -> Public route snapshot listener fires immediately and renders comment; admin listener moves item from pending to approved card.
   * **Revoke**: Admin clicks "Desautoritzar" -> `.update({ authorized: false })` -> Comment disappears immediately from public route page; admin listener moves item back to pending queue.
   * **Delete**: Admin clicks "Esborrar" -> `.delete()` -> Permanently removed from Firestore and UI.

---

## 3. Caveats

1. **Unauthenticated Admin Access**: Anyone with access to the URL `/mallorca/admin_comentaris/` can view and moderate comments because there is no Firebase Authentication login screen or route guarding on MkDocs static pages. In production, this can be secured behind basic authentication, HTTP auth on hosting, or Firebase Auth.
2. **Missing `firestore.rules` in Repo**: Since `firestore.rules` is not tracked in git and not deployed by `.github/workflows/deploy_firebase.yml`, rule management remains external (in the Firebase Console). Adding a tracked `firestore.rules` file is recommended for reproducibility.
3. **Firestore Quotas & Free Tier**: `db.collection("experiencies").onSnapshot(...)` on the admin page reads all documents in the collection upon opening. For an internal scout portal with hundreds of comments, this easily remains well within the Firebase free tier (50,000 reads/day).

---

## 4. Conclusion & Architecture Specifications

### 4.1 Verified Firestore Document Schema
| Field Name | Type | Value Example | Required by Form | Notes |
| :--- | :--- | :--- | :--- | :--- |
| `ruta_slug` | String | `"cami-des-rafal-deia"` | Yes | Matches route markdown slug |
| `nom` | String | `"Joan Bennàssar"` | Yes | Input text |
| `email` | String | `"joan@escoltes.cat"` | Yes | Validated with `@` |
| `agrupament` | String | `"AEG Eladi Homs"` | Yes | Select dropdown |
| `branca` | String | `"Llops/Daines"` | Yes | Select dropdown (5 branches) |
| `puntuacio` | Number | `5` | Yes | 1 to 5 stars |
| `data` | String | `"Setembre 2026"` | Optional | Excursion date |
| `comentari` | String | `"Camí amb bona ombra..."` | Yes | Min 5 characters |
| `authorized` | Boolean | `false` (default) / `true` | System | Controls public visibility |
| `createdAt` | Timestamp | `serverTimestamp()` | System | Time of submission |
| `approvedAt` | Timestamp | `serverTimestamp()` | System | Time of admin approval |

### 4.2 Security Rules Specification (`firestore.rules`)
```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /experiencies/{commentId} {
      // 1. Unauthenticated creation: Only allow new comments with authorized == false
      allow create: if request.resource.data.authorized == false
                    && request.resource.data.nom is string
                    && request.resource.data.email is string
                    && request.resource.data.comentari is string;

      // 2. Public read: Anyone can read approved comments
      allow read: if resource.data.authorized == true;

      // 3. Admin moderation operations (open access until Firebase Auth is integrated):
      allow read, update, delete: if true;
    }
  }
}
```

### 4.3 Proposed Implementation of `docs/mallorca/admin_comentaris.md`
The admin page should include robust XSS sanitization, safe star rendering, date formatting, clickable route links, and instant navigation hooks:

```markdown
# 🛡️ Administració i Moderació de Comentaris de Rutes

Benvinguts al panell de moderació dels Escoltes de Mallorca. Aquí els administradors i responsables poden revisar, autoritzar o esborrar els comentaris i ressenyes d'excursions enviats pels agrupaments.

!!! info "Panell de Moderació i Seguretat Escolta"
    Tots els comentaris nous s'enregistren per defecte amb l'estat pendent d'autorització (`authorized: false`). Només apareixeran a la web pública de la ruta quan hagin estat aprovats des d'aquest panell.

---

<script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore-compat.js"></script>

<div id="admin-panel-container" style="margin-top: 20px;">

    <!-- Secció 1: Comentaris Pendents -->
    <div style="background-color: #fff8e1; border: 2px solid #ffa000; border-radius: 12px; padding: 20px; margin-bottom: 24px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; flex-wrap: wrap; gap: 8px;">
            <h2 style="margin: 0; color: #b78103; font-size: 1.3em;">⏳ Comentaris Pendents d'Autorització</h2>
            <span id="pending-count-badge" style="background-color: #ffa000; color: white; padding: 4px 12px; border-radius: 20px; font-weight: bold; font-size: 0.9em;">0 pendents</span>
        </div>
        <p style="margin-top: 0; color: #666; font-size: 0.9em;">Aquests comentaris no són visibles a la fitxa pública de l'excursió fins que no premis <b>Aprovar</b>.</p>

        <div id="pending-comments-list" style="display: flex; flex-direction: column; gap: 14px; margin-top: 16px;">
            <p style="color: #888; font-style: italic;">🔄 Carregant comentaris pendents de Firebase...</p>
        </div>
    </div>

    <!-- Secció 2: Comentaris Autoritzats -->
    <div style="background-color: #f0f7f4; border: 1px solid #00897b; border-radius: 12px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; flex-wrap: wrap; gap: 8px;">
            <h2 style="margin: 0; color: #00897b; font-size: 1.3em;">✅ Comentaris Autoritzats Públicament</h2>
            <span id="approved-count-badge" style="background-color: #00897b; color: white; padding: 4px 12px; border-radius: 20px; font-weight: bold; font-size: 0.9em;">0 aprovats</span>
        </div>
        <p style="margin-top: 0; color: #666; font-size: 0.9em;">Aquests comentaris estan actualment visibles per a tots els visitants del portal.</p>

        <div id="approved-comments-list" style="display: flex; flex-direction: column; gap: 14px; margin-top: 16px;">
            <p style="color: #888; font-style: italic;">🔄 Carregant comentaris aprovats de Firebase...</p>
        </div>
    </div>

</div>

<script>
(function() {
    const firebaseConfig = {
        projectId: "escoltes-mallorca"
    };

    if (typeof firebase !== 'undefined' && !firebase.apps.length) {
        firebase.initializeApp(firebaseConfig);
    }

    function escapeHtml(text) {
        if (!text) return '';
        return String(text)
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }

    function sortDesc(items) {
        return items.sort((a, b) => {
            const timeA = a.createdAt?.seconds ? a.createdAt.seconds * 1000 : (new Date(a.createdAt || a.data || 0).getTime() || 0);
            const timeB = b.createdAt?.seconds ? b.createdAt.seconds * 1000 : (new Date(b.createdAt || b.data || 0).getTime() || 0);
            return timeB - timeA;
        });
    }

    window.initAdminComments = function() {
        if (typeof firebase === 'undefined' || !firebase.firestore) {
            console.error("Firebase Firestore no està disponible.");
            return;
        }

        const db = firebase.firestore();

        db.collection("experiencies").onSnapshot((snapshot) => {
            const pendingList = [];
            const approvedList = [];

            snapshot.forEach(doc => {
                const data = doc.data();
                const item = { id: doc.id, ...data };
                if (data.authorized === true) {
                    approvedList.push(item);
                } else {
                    pendingList.push(item);
                }
            });

            sortDesc(pendingList);
            sortDesc(approvedList);

            renderPendingComments(pendingList);
            renderApprovedComments(approvedList);
        }, (err) => {
            console.error("Error carregar comentaris Firestore:", err);
            const pCont = document.getElementById('pending-comments-list');
            if (pCont) pCont.innerHTML = `<p style="color: #d32f2f;">❌ Error en connectar amb Firestore: ${escapeHtml(err.message)}</p>`;
        });
    };

    window.approveComment = async function(docId) {
        if (!confirm("Vols autoritzar aquest comentari per a la seva publicació immediata?")) return;
        try {
            const db = firebase.firestore();
            await db.collection("experiencies").doc(docId).update({
                authorized: true,
                approvedAt: firebase.firestore.FieldValue.serverTimestamp()
            });
            alert("✅ Comentari autoritzat amb èxit!");
        } catch (e) {
            alert("❌ Error en autoritzar: " + e.message);
        }
    };

    window.revokeComment = async function(docId) {
        if (!confirm("Vols desautoritzar aquest comentari? Tornarà a l'estat pendent.")) return;
        try {
            const db = firebase.firestore();
            await db.collection("experiencies").doc(docId).update({
                authorized: false
            });
            alert("⚠️ Comentari mogut a pendents.");
        } catch (e) {
            alert("❌ Error en desautoritzar: " + e.message);
        }
    };

    window.deleteComment = async function(docId) {
        if (!confirm("⚠️ Esteu segur de voler esborrar finalment aquest comentari? L'acció no es pot desfer.")) return;
        try {
            const db = firebase.firestore();
            await db.collection("experiencies").doc(docId).delete();
            alert("🗑️ Comentari eliminat de Firebase.");
        } catch (e) {
            alert("❌ Error en eliminar: " + e.message);
        }
    };

    function renderPendingComments(items) {
        const container = document.getElementById('pending-comments-list');
        const badge = document.getElementById('pending-count-badge');
        if (!container) return;

        badge.innerText = `${items.length} pendents`;

        if (items.length === 0) {
            container.innerHTML = `<p style="color: #666; font-style: italic; margin: 0;">🎉 Genial! No hi ha cap comentari pendent d'autorització.</p>`;
            return;
        }

        let html = '';
        items.forEach(item => {
            const safeScore = Math.max(1, Math.min(5, Math.round(Number(item.puntuacio) || 5)));
            const stars = "⭐".repeat(safeScore);
            const rawRoute = item.ruta_slug || '';
            const routeDisplay = rawRoute ? `<a href="../rutes/${encodeURIComponent(rawRoute)}/" target="_blank" style="color: #d84315; text-decoration: underline; font-weight: bold;">📍 Ruta: ${escapeHtml(rawRoute)} ↗</a>` : '<span style="color: #888;">📍 Ruta Desconeguda</span>';
            const name = escapeHtml(item.nom || 'Anònim');
            const emailHtml = item.email ? ` (<a href="mailto:${encodeURI(item.email)}" style="color: #00897b;">${escapeHtml(item.email)}</a>)` : '';
            const group = escapeHtml(item.agrupament || 'Sense Agrupament');
            const unit = item.branca ? ` | Branca: ${escapeHtml(item.branca)}` : '';
            const comment = escapeHtml(item.comentari || '');
            let dateStr = escapeHtml(item.data || '');
            if (item.createdAt && item.createdAt.toDate) {
                dateStr += (dateStr ? ' · ' : '') + item.createdAt.toDate().toLocaleDateString('ca-ES');
            }

            html += `
                <div style="background: white; border: 1px solid #ffe082; border-radius: 8px; padding: 14px; box-shadow: 0 2px 4px rgba(0,0,0,0.04);">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 8px; margin-bottom: 8px;">
                        <div>
                            <div>${routeDisplay}</div>
                            <div style="font-size: 0.9em; color: #333; margin-top: 4px;">
                                👤 <b>${name}</b>${emailHtml} | ⚜️ <b>${group}</b>${unit}
                            </div>
                        </div>
                        <span style="color: #f57f17; font-weight: bold; font-size: 0.9em;">${stars} ${dateStr ? `(${dateStr})` : ''}</span>
                    </div>
                    <p style="background: #fffde7; padding: 10px; border-radius: 6px; border-left: 4px solid #ffb300; margin: 8px 0 12px 0; font-size: 0.95em; line-height: 1.4;">
                        "${comment}"
                    </p>
                    <div style="display: flex; justify-content: flex-end; gap: 10px;">
                        <button onclick="deleteComment('${escapeHtml(item.id)}')" style="padding: 6px 14px; background-color: #d32f2f; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 0.85em;">🗑️ Esborrar</button>
                        <button onclick="approveComment('${escapeHtml(item.id)}')" style="padding: 6px 18px; background-color: #2e7d32; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 0.85em;">✅ Aprovar / Autoritzar</button>
                    </div>
                </div>
            `;
        });
        container.innerHTML = html;
    }

    function renderApprovedComments(items) {
        const container = document.getElementById('approved-comments-list');
        const badge = document.getElementById('approved-count-badge');
        if (!container) return;

        badge.innerText = `${items.length} aprovats`;

        if (items.length === 0) {
            container.innerHTML = `<p style="color: #666; font-style: italic; margin: 0;">Encara no hi ha cap comentari aprovat a Firebase.</p>`;
            return;
        }

        let html = '';
        items.forEach(item => {
            const safeScore = Math.max(1, Math.min(5, Math.round(Number(item.puntuacio) || 5)));
            const stars = "⭐".repeat(safeScore);
            const rawRoute = item.ruta_slug || '';
            const routeDisplay = rawRoute ? `<a href="../rutes/${encodeURIComponent(rawRoute)}/" target="_blank" style="color: #00897b; text-decoration: underline; font-weight: bold;">📍 Ruta: ${escapeHtml(rawRoute)} ↗</a>` : '<span style="color: #888;">📍 Ruta Desconeguda</span>';
            const name = escapeHtml(item.nom || 'Anònim');
            const emailHtml = item.email ? ` (${escapeHtml(item.email)})` : '';
            const group = escapeHtml(item.agrupament || 'Sense Agrupament');
            const unit = item.branca ? ` | Branca: ${escapeHtml(item.branca)}` : '';
            const comment = escapeHtml(item.comentari || '');
            let dateStr = escapeHtml(item.data || '');
            if (item.createdAt && item.createdAt.toDate) {
                dateStr += (dateStr ? ' · ' : '') + item.createdAt.toDate().toLocaleDateString('ca-ES');
            }

            html += `
                <div style="background: white; border: 1px solid #b2dfdb; border-radius: 8px; padding: 14px; box-shadow: 0 2px 4px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 8px; margin-bottom: 8px;">
                        <div>
                            <div>${routeDisplay}</div>
                            <div style="font-size: 0.88em; color: #444; margin-top: 4px;">
                                👤 <b>${name}</b>${emailHtml} | ⚜️ <b>${group}</b>${unit}
                            </div>
                        </div>
                        <span style="color: #f57f17; font-weight: bold; font-size: 0.88em;">${stars} ${dateStr ? `(${dateStr})` : ''}</span>
                    </div>
                    <p style="margin: 6px 0 10px 0; font-size: 0.92em; color: #333; line-height: 1.4;">
                        "${comment}"
                    </p>
                    <div style="display: flex; justify-content: flex-end; gap: 10px;">
                        <button onclick="revokeComment('${escapeHtml(item.id)}')" style="padding: 5px 12px; background-color: #ef6c00; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 0.8em;">⚠️ Desautoritzar</button>
                        <button onclick="deleteComment('${escapeHtml(item.id)}')" style="padding: 5px 12px; background-color: #c62828; color: white; border: none; border-radius: 6px; cursor: pointer; font-size: 0.8em;">🗑️ Esborrar</button>
                    </div>
                </div>
            `;
        });
        container.innerHTML = html;
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', window.initAdminComments);
    } else {
        window.initAdminComments();
    }

    if (typeof document$ !== 'undefined') {
        document$.subscribe(function() {
            window.initAdminComments();
        });
    }
})();
</script>
```

### 4.4 Remediation Needed in `scripts/build_wiki_pages.py`
Before running `python run_phase1.py`, lines 406–409 in `scripts/build_wiki_pages.py` must be cleaned:
```diff
         }} catch (error) {{
             console.error("Error al enviar a Firebase:", error);
             statusMsg.style.color = '#e65100';
             statusMsg.innerText = '✅ Comentari gravat localment. Està pendent d\'autorització per l\'administrador.';
             submitBtn.disabled = false;
         }}
     }};
-            submitBtn.disabled = false;
-        }}
-    }};
 
     if (document.readyState === 'loading') {{
```

---

## 5. Verification Method

To independently verify all findings and confirm the system functions:

1. **Verify Syntax in `scripts/build_wiki_pages.py`**:
   Inspect lines 400–415 in `scripts/build_wiki_pages.py` to confirm the duplicate braces are removed.
2. **Re-generate Wiki Pages and Build Site**:
   Execute the project pipeline:
   ```powershell
   python scripts/build_wiki_pages.py
   python -m mkdocs build --clean
   ```
   *Expected Result*: Zero build warnings, clean compilation of `site/mallorca/admin_comentaris/index.html`.
3. **Verify Nav Registration in `mkdocs.yml`**:
   Check line 65 of `mkdocs.yml`:
   ```powershell
   Select-String -Path mkdocs.yml -Pattern "admin_comentaris.md"
   ```
   *Expected Result*: Found in `nav` under `Escoltisme a Mallorca`.
4. **Inspect Generated HTML for Admin Page**:
   Open `site/mallorca/admin_comentaris/index.html` and verify:
   * Script tags load `firebase-app-compat.js` and `firebase-firestore-compat.js`.
   * Pending container (`pending-comments-list`) and Approved container (`approved-comments-list`) are present.
   * `approveComment`, `revokeComment`, and `deleteComment` functions are defined.
5. **Invalidation Conditions**:
   * If Firebase modular SDK v9+ (without compat) were introduced without a module bundler, MkDocs pages would fail to run Firebase in ordinary browsers.
   * If Firestore security rules in Firebase Console enforce `request.auth != null`, client-side updates/deletes and unauthenticated comment creations will fail with `FirebaseError: Missing or insufficient permissions`.
