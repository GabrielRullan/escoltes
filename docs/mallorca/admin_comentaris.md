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
