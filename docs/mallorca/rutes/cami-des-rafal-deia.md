# 🏔️ Camí des Rafal i Cova de sa Cauba (Deià)

Ruta boscosa per les terrasses d'oliveres i alzinars sobre Deià.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-cami-des-rafal-deia" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_cami_des_rafal_deia() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_cami_des_rafal_deia, 200);
        return;
    }
    
    const trackPoints = [[39.753, 2.651]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-cami-des-rafal-deia');
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(rMap);
    
    if (trackPoints.length > 1) {
        const polyline = L.polyline(trackPoints, {
            color: '#00897b',
            weight: 5,
            opacity: 0.85,
            lineJoin: 'round'
        }).addTo(rMap);
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Camí des Rafal i Cova de sa Cauba (Deià)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Camí des Rafal i Cova de sa Cauba (Deià)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.753, 2.651], 14);
        L.marker([39.753, 2.651]).addTo(rMap).bindPopup("<b>Camí des Rafal i Cova de sa Cauba (Deià)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_cami_des_rafal_deia);
setTimeout(initRouteTrackMap_cami_des_rafal_deia, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Deià** |
| **Zona / Comarca** | **Tramuntana Central** |
| **Distància Total** | **6.5 km** |
| **Desnivell Positiu** | **+270 m** |
| **Dificultat Tècnica** | **Moderada** |
| **Durada Estimada** | **2h 30min** |
| **Unitats Recomanades** | **Llops/Daines, Pioners/Rangers** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/find.do?q=Cam%C3%AD%20des%20Rafal%20i%20Cova%20de%20sa%20Cauba%20%28Dei%C3%A0%29)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Deià**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 203** (Palma - Valldemossa - Deià - Sóller) | Palma, Valldemossa, Son Marroig, Deià | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/203) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Deià poble
- **Passos per Finques Privades:** Possessió des Rafal
- **Punts d'Interès Cultural i Natural:** Cova de sa Cauba, Alzinars de Deià

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Camí ombrívol ideal per a dies de calor moderada.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Refugi de Can Boi** | Consell de Mallorca (Xarxa GR-221) | 32 pers. | **0.49 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/refugi-can-boi.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Refugi de Son Moragues** | **4.7 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-son-moragues.md) |
| **Refugi de Muleta** | **5.5 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-muleta.md) |
| **Sant Ramon de Penyafort** | **5.7 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/sant-ramon-de-penyafort-soller.md) |

### ⚜️ Agrupaments Escoltes Més Propers a l'Inici de la Ruta (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Capità Angelats** | Sóller | **5.7 km** | [Veure Casal](../agrupaments/aeg-capita-angelats.md) |
| **AEG Nuredduna** | Bunyola / Palmanyola | **11.1 km** | [Veure Casal](../agrupaments/aeg-nuredduna.md) |

---

## 💬 Experiències i Valoracions dels Agrupaments Escoltes

<div id="firebase-exp-wrapper" style="background-color: var(--md-code-bg-color, #f8f9fa); border: 1px solid #e0e0e0; padding: 20px; border-radius: 12px; margin-top: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
    
    <!-- Resum i botó per obrir el formulari -->
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 16px; border-bottom: 1px solid #e0e0e0; padding-bottom: 14px;">
        <div>
            <h3 id="exp-summary-title" style="margin: 0; font-size: 1.2em; color: #00897b; font-weight: bold;">
                💬 Experiències i Consells de Caps
            </h3>
            <p id="exp-summary-subtitle" style="margin: 4px 0 0 0; font-size: 0.88em; color: #666;">
                Compartiu recomanacions d'aigua, ombra, dificultat o estat del camí amb altres agrupaments.
            </p>
        </div>
        <button id="toggle-exp-form-btn" onclick="toggleExpForm()" style="padding: 10px 18px; background-color: #00897b; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; font-size: 0.9em; box-shadow: 0 2px 6px rgba(0,137,123,0.3); transition: background 0.2s;">
            ➕ Afegir la meva experiència 🔥
        </button>
    </div>

    <!-- Formulari interactiu d'enviament a l'administrador (Inicialment ocult) -->
    <div id="exp-form-container" style="display: none; background-color: #ffffff; border: 2px solid #00897b; border-radius: 10px; padding: 18px; margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);">
        <h4 style="margin: 0 0 6px 0; color: #00897b; font-size: 1.05em;">📝 Enviar la teva experiència per a aquesta excursió</h4>
        <p style="margin: 0 0 14px 0; font-size: 0.85em; color: #555;">Qualsevol cap o agrupament pot compartir valoracions. El formulari enviarà les dades per correu electrònic a l'administrador per ser publicades a la fitxa.</p>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; margin-bottom: 12px;">
            <div>
                <label style="font-weight: bold; font-size: 0.85em; display: block; margin-bottom: 4px;">👤 Nom i Llinatges (*):</label>
                <input type="text" id="exp-nom" placeholder="Ex: Joan Bennàssar" style="width: 100%; padding: 8px; border-radius: 6px; border: 1px solid #ccc; box-sizing: border-box;" />
            </div>
            <div>
                <label style="font-weight: bold; font-size: 0.85em; display: block; margin-bottom: 4px;">✉️ El teu Correu Electrònic (*):</label>
                <input type="email" id="exp-email" placeholder="joan@escoltes.cat" style="width: 100%; padding: 8px; border-radius: 6px; border: 1px solid #ccc; box-sizing: border-box;" />
            </div>
            <div>
                <label style="font-weight: bold; font-size: 0.85em; display: block; margin-bottom: 4px;">⚜️ Agrupament Escolta (*):</label>
                <select id="exp-agrupament" onchange="onAgrupamentChange()" style="width: 100%; padding: 8px; border-radius: 6px; border: 1px solid #ccc; box-sizing: border-box;">
                    <option value="">-- Selecciona el teu Agrupament --</option>
                    <optgroup label="🏙️ Agrupaments de Palma de Mallorca">
                        <option value="AEG Eladi Homs">AEG Eladi Homs (Parròquia de Sant Alonso (Palma))</option>
                        <option value="AEG Jaume I">AEG Jaume I (Parròquia de l'Encarnació (Palma))</option>
                        <option value="AEG Ramon Llull">AEG Ramon Llull (Sant Francesc (Centre Històric Palma))</option>
                        <option value="AEG Reina Constança de Mallorca">AEG Reina Constança de Mallorca (Parròquia de Santa Catalina Thomàs (Palma))</option>
                        <option value="AEG Sant Josep Obrer">AEG Sant Josep Obrer (Parròquia de Sant Josep Obrer (Palma))</option>
                        <option value="AEG Son Sardina">AEG Son Sardina (Son Sardina)</option>
                        <option value="AEG Verge de Lluc">AEG Verge de Lluc (Parròquia de l'Encarnació (Palma))</option>
                    </optgroup>
                    <optgroup label="🏡 Agrupaments de Part Forana (Pobles)">
                        <option value="AEG Capità Angelats">AEG Capità Angelats (Sóller)</option>
                        <option value="AEG Nuredduna">AEG Nuredduna (Bunyola / Palmanyola)</option>
                        <option value="AEG Pedra Viva">AEG Pedra Viva (Binissalem)</option>
                        <option value="AEG Sa Marjal">AEG Sa Marjal (Sa Pobla)</option>
                        <option value="AEG Soca-Arrel">AEG Soca-Arrel (Marratxí)</option>
                        <option value="AEG Terra de Pous">AEG Terra de Pous (Santa Maria del Camí)</option>
                        <option value="Grupo Scout Myotragus 684">Grupo Scout Myotragus 684 (Llucmajor)</option>
                    </optgroup>
                    <optgroup label="⛵ Altres Illes i Territoris Escoltes">
                        <option value="Agrupament Escolta de Menorca">Agrupament Escolta de Menorca</option>
                        <option value="Agrupament Escolta d'Eivissa / Formentera">Agrupament Escolta d'Eivissa / Formentera</option>
                        <option value="Agrupament de Catalunya / València">Agrupament de Catalunya / País Valencià</option>
                    </optgroup>
                    <option value="Altre Agrupament Escolta">Altre Agrupament Escolta (especificar)</option>
                </select>
                <div id="exp-altre-agrupament-box" style="display: none; margin-top: 6px;">
                    <input type="text" id="exp-altre-agrupament" placeholder="Escriu el nom del teu agrupament..." style="width: 100%; padding: 8px; border-radius: 6px; border: 1px solid #ccc; font-size: 0.88em; box-sizing: border-box;" />
                </div>
            </div>
            <div>
                <label style="font-weight: bold; font-size: 0.85em; display: block; margin-bottom: 4px;">🎒 Unitat Escolta (*):</label>
                <select id="exp-unitat" style="width: 100%; padding: 8px; border-radius: 6px; border: 1px solid #ccc; box-sizing: border-box;">
                    <option value="Ferrerets">Ferrerets (6-8 anys)</option>
                    <option value="Llops/Daines">Llops / Daines (8-11 anys)</option>
                    <option value="Rangers/Guies">Rangers / Guies o Pioners (11-14 anys)</option>
                    <option value="Pioners/Caravel·les">Pioners / Caravel·les o Rutes (14-17 anys)</option>
                    <option value="Rovers/Rutes">Rovers / Rutes (17-19 anys)</option>
                    <option value="Caps/Equip de Suport">Caps / Responsables / Suport</option>
                </select>
            </div>
            <div>
                <label style="font-weight: bold; font-size: 0.85em; display: block; margin-bottom: 4px;">⭐ Valoració Global:</label>
                <select id="exp-puntuacio" style="width: 100%; padding: 8px; border-radius: 6px; border: 1px solid #ccc; box-sizing: border-box;">
                    <option value="5">⭐⭐⭐⭐⭐ (5/5 - Excel·lent ruta)</option>
                    <option value="4">⭐⭐⭐⭐ (4/5 - Molt bona)</option>
                    <option value="3">⭐⭐⭐ (3/5 - Correcta)</option>
                    <option value="2">⭐⭐ (2/5 - Regular / Amb atenció)</option>
                    <option value="1">⭐ (1/5 - No recomanada)</option>
                </select>
            </div>
            <div>
                <label style="font-weight: bold; font-size: 0.85em; display: block; margin-bottom: 4px;">📅 Data de la Sortida:</label>
                <input type="text" id="exp-data" placeholder="Ex: Febrer 2026" style="width: 100%; padding: 8px; border-radius: 6px; border: 1px solid #ccc; box-sizing: border-box;" />
            </div>
        </div>

        <div style="margin-bottom: 14px;">
            <label style="font-weight: bold; font-size: 0.85em; display: block; margin-bottom: 4px;">💬 Comentaris, consells d'aigua, ombra o recomanacions logístiques (*):</label>
            <textarea id="exp-comentari" rows="3" placeholder="Comentau l'estat del camí, les fonts amb aigua, punts d'ombra, zones d'acampada o recomanacions per a la vostra unitat..." style="width: 100%; padding: 10px; border-radius: 6px; border: 1px solid #ccc; font-family: inherit; font-size: 0.9em; box-sizing: border-box;"></textarea>
        </div>

        <div style="display: flex; justify-content: flex-end; gap: 10px;">
            <button onclick="toggleExpForm()" style="padding: 8px 16px; background-color: #757575; color: white; border: none; border-radius: 6px; cursor: pointer;">Cancel·lar</button>
            <button id="exp-submit-btn" onclick="submitExperience('cami-des-rafal-deia')" style="padding: 8px 20px; background-color: #00897b; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: bold;">✉️ Enviar Experiència per Correu</button>
        </div>
        <div id="exp-status-msg" style="margin-top: 10px; font-weight: bold; font-size: 0.9em;"></div>
    </div>

    <!-- Llista interactiva de ressenyes -->
    <div id="experiences-list-container" style="display: flex; flex-direction: column; gap: 12px;">
        <p style="color: #666; font-style: italic; font-size: 0.88em;">🔄 Carregant experiències d'agrupaments...</p>
    </div>

</div>

<script>
(function() {
    const routeSlug = "cami-des-rafal-deia";
    const routeName = "Camí des Rafal i Cova de sa Cauba (Deià)";
    const staticExperiences = [];

    function escapeHtml(text) {
        if (!text) return '';
        return String(text)
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#039;");
    }

    window.onAgrupamentChange = function() {
        const agrSelect = document.getElementById('exp-agrupament');
        const altreBox = document.getElementById('exp-altre-agrupament-box');
        if (!agrSelect || !altreBox) return;
        altreBox.style.display = (agrSelect.value === 'Altre Agrupament Escolta') ? 'block' : 'none';
    };

    window.toggleExpForm = function() {
        const form = document.getElementById('exp-form-container');
        const btn = document.getElementById('toggle-exp-form-btn');
        if (!form) return;
        if (form.style.display === 'none') {
            form.style.display = 'block';
            btn.innerText = '❌ Tancar formulari';
            btn.style.backgroundColor = '#d32f2f';
        } else {
            form.style.display = 'none';
            btn.innerText = '➕ Afegir la meva experiència 🔥';
            btn.style.backgroundColor = '#00897b';
        }
    };

    window.renderExperiencesList = function(exps) {
        const container = document.getElementById('experiences-list-container');
        const summaryTitle = document.getElementById('exp-summary-title');
        const summarySubtitle = document.getElementById('exp-summary-subtitle');
        if (!container) return;
        
        if (!exps || exps.length === 0) {
            if (summaryTitle) summaryTitle.innerText = "💬 Encara no hi ha experiències enregistrades";
            if (summarySubtitle) summarySubtitle.innerText = "Sigueu els primers a deixar consells sobre aquesta ruta per a altres agrupaments escoltes!";
            container.innerHTML = `
                <div style="text-align: center; padding: 20px; background: white; border-radius: 8px; border: 1px dashed #ccc;">
                    <p style="margin: 0; color: #666;">⛺ Heu fet aquesta excursió? Polsau el botó superior per enviar la vostra experiència per correu a l'administrador.</p>
                </div>
            `;
            return;
        }
        
        const totalScore = exps.reduce((acc, curr) => acc + (Number(curr.puntuacio) || 5), 0);
        const avgScore = (totalScore / exps.length).toFixed(1);
        const starStr = "⭐".repeat(Math.round(avgScore));
        
        if (summaryTitle) summaryTitle.innerText = `Valoració Mitjana: ${starStr} ${avgScore} / 5`;
        if (summarySubtitle) summarySubtitle.innerText = `Basat en ${exps.length} experiències compartides per caps i agrupaments escoltes.`;
        
        let html = '';
        exps.forEach(exp => {
            const score = Math.max(1, Math.min(5, Math.round(Number(exp.puntuacio) || 5)));
            const expStars = "⭐".repeat(score);
            const authorName = exp.nom ? `👤 ${escapeHtml(exp.nom)} - ` : '';
            const agrName = escapeHtml(exp.agrupament || 'Agrupament Escolta');
            const unitatVal = exp.unitat || exp.branca || '';
            const unitatName = unitatVal ? ` (${escapeHtml(unitatVal)})` : '';
            const dataStr = escapeHtml(exp.data || '');
            const comentariText = escapeHtml(exp.comentari || '');
            
            html += `
                <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 14px; background-color: #ffffff; box-shadow: 0 2px 4px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 6px; margin-bottom: 6px;">
                        <span style="font-weight: bold; color: #00897b; font-size: 0.95em;">${authorName}⚜️ ${agrName} <span style="font-weight: normal; color: #666; font-size: 0.9em;">${unitatName}</span></span>
                        <span style="font-size: 0.85em; color: #f57f17; font-weight: bold;">${expStars} <span style="color: #888; font-weight: normal;">(${dataStr})</span></span>
                    </div>
                    <p style="margin: 4px 0 0 0; font-size: 0.9em; color: #333; line-height: 1.45;"><i>"${comentariText}"</i></p>
                </div>
            `;
        });
        container.innerHTML = html;
    };

    window.initExperiences = function() {
        renderExperiencesList(staticExperiences);
    };

    window.submitExperience = async function(slug) {
        const nom = document.getElementById('exp-nom').value.trim();
        const email = document.getElementById('exp-email').value.trim();
        let agrupament = document.getElementById('exp-agrupament').value;
        const unitat = document.getElementById('exp-unitat').value;
        const puntuacio = parseInt(document.getElementById('exp-puntuacio').value, 10);
        const dataVal = document.getElementById('exp-data').value.trim() || 'Recenta';
        const comentari = document.getElementById('exp-comentari').value.trim();
        const statusMsg = document.getElementById('exp-status-msg');
        const submitBtn = document.getElementById('exp-submit-btn');

        if (agrupament === 'Altre Agrupament Escolta') {
            const customAgr = document.getElementById('exp-altre-agrupament')?.value.trim();
            if (customAgr) {
                agrupament = customAgr;
            }
        }

        if (!nom) {
            statusMsg.style.color = '#d32f2f';
            statusMsg.innerText = '⚠️ Si us plau, escriu el teu nom.';
            return;
        }

        if (!email || !email.includes('@')) {
            statusMsg.style.color = '#d32f2f';
            statusMsg.innerText = '⚠️ Si us plau, introdueix un correu electrònic vàlid.';
            return;
        }

        if (!agrupament) {
            statusMsg.style.color = '#d32f2f';
            statusMsg.innerText = '⚠️ Si us plau, selecciona o indica el teu agrupament escolta.';
            return;
        }

        if (!comentari || comentari.length < 5) {
            statusMsg.style.color = '#d32f2f';
            statusMsg.innerText = '⚠️ Si us plau, escriu un comentari o consell rellevant (mínim 5 caràcters).';
            return;
        }

        const mailtoSubject = `[Nova Experiència] ${routeName} - ${agrupament} (${unitat})`;
        const mailtoBody = `Ruta: ${routeName} (${slug})
Nom autor/a: ${nom}
Correu: ${email}
Agrupament: ${agrupament}
Unitat: ${unitat}
Valoració: ${puntuacio} / 5 estrelles
Data sortida: ${dataVal}

Comentaris i consells:
${comentari}`;
        const mailtoUrl = `mailto:escoltesmallorca@gmail.com?subject=${encodeURIComponent(mailtoSubject)}&body=${encodeURIComponent(mailtoBody)}`;

        statusMsg.style.color = '#00897b';
        statusMsg.innerText = '⏳ Enviant comentari per correu electrònic a escoltesmallorca@gmail.com...';
        submitBtn.disabled = true;

        try {
            const response = await fetch("https://formsubmit.co/ajax/escoltesmallorca@gmail.com", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                },
                body: JSON.stringify({
                    _subject: mailtoSubject,
                    _replyto: email,
                    "Ruta": routeName,
                    "Autor": nom,
                    "Correu": email,
                    "Agrupament": agrupament,
                    "Unitat": unitat,
                    "Valoracio": `${puntuacio} / 5 estrelles`,
                    "Data_Sortida": dataVal,
                    "Comentaris": comentari
                })
            });

            if (response.ok) {
                statusMsg.style.color = '#2e7d32';
                statusMsg.innerHTML = "✅ <b>Experiència enviada amb èxit!</b> Hem rebut la teva ressenya per correu a escoltesmallorca@gmail.com. L'administrador la revisarà i l'afegirà a la fitxa pública!";
                document.getElementById('exp-nom').value = '';
                document.getElementById('exp-email').value = '';
                document.getElementById('exp-comentari').value = '';
                document.getElementById('exp-data').value = '';
                setTimeout(() => {
                    toggleExpForm();
                    statusMsg.innerText = '';
                    submitBtn.disabled = false;
                }, 3500);
            } else {
                throw new Error("HTTP error " + response.status);
            }
        } catch (err) {
            console.warn("FormSubmit fetch error, oferint mailto:", err);
            statusMsg.style.color = '#e65100';
            statusMsg.innerHTML = `⚠️ No s'ha pogut tramitar automàticament per xarxa. <a href="${mailtoUrl}" target="_blank" style="color: #00897b; font-weight: bold; text-decoration: underline;">👉 Fes clic aquí per obrir el teu gestor de correu i enviar-ho directament a escoltesmallorca@gmail.com</a>.`;
            submitBtn.disabled = false;
        }
    };

    window.submitFirebaseExperience = window.submitExperience;
    window.initFirebaseExperiences = window.initExperiences;

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', window.initExperiences);
    } else {
        window.initExperiences();
    }

    if (typeof document$ !== 'undefined') {
        document$.subscribe(function() {
            window.initExperiences();
        });
    }
})();
</script>


