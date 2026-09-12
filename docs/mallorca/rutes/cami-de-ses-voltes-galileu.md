# 🏔️ Camí de ses Voltes d'en Galileu (Lluc)

Ruta patrimonial que remunta les voltes empedrades cap a les antigues cases de neu de la Tramuntana.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-cami-de-ses-voltes-galileu" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_cami_de_ses_voltes_galileu() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_cami_de_ses_voltes_galileu, 200);
        return;
    }
    
    const trackPoints = [[39.814, 2.875]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-cami-de-ses-voltes-galileu');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Camí de ses Voltes d'en Galileu (Lluc)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Camí de ses Voltes d'en Galileu (Lluc)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.814, 2.875], 14);
        L.marker([39.814, 2.875]).addTo(rMap).bindPopup("<b>Camí de ses Voltes d'en Galileu (Lluc)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_cami_de_ses_voltes_galileu);
setTimeout(initRouteTrackMap_cami_de_ses_voltes_galileu, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Escorca** |
| **Zona / Comarca** | **Tramuntana Nord** |
| **Distància Total** | **9.4 km** |
| **Desnivell Positiu** | **+580 m** |
| **Dificultat Tècnica** | **Moderada - Exigent** |
| **Durada Estimada** | **3h 45min** |
| **Unitats Recomanades** | **Pioners/Rangers, Rovers/Rutes** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Cam%C3%AD%20de%20ses%20Voltes%20d%27en%20Galileu%20%28Lluc%29)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Escorca**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 341** (Pollença - Lluc - Cúber - Port de Sóller (Línia Ma-10)) | Pollença, Lluc (Monestir), Binifaldó, Gorg Blau | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/341) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Son Amer / Lluc
- **Passos per Finques Privades:** Son Massip
- **Punts d'Interès Cultural i Natural:** Cases de Neu d'en Galileu, Ses Voltes empedrades, Vistes a la serra

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Camí en ziga-zaga empedrat. Calçat de muntanya fort necessari.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Àrea d'Acampada de Sa Font Coberta** | IBANAT (Govern de les Illes Balears) | 150 pers. | **1.31 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/sa-font-coberta-lluc.md) |
| **Refugi de Son Amer** | Consell de Mallorca (Xarxa GR-221) | 52 pers. | **1.33 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/refugi-son-amer.md) |
| **Àrea d'Acampada de Marjanor** | IBANAT (Govern de les Illes Balears) | 60 pers. | **1.43 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/marjanor-lluc.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Àrea d'Acampada des Pixarells** | **2.2 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/es-pixarells-lluc.md) |
| **Cases de Binifaldó (Refugi IBANAT)** | **2.8 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/cases-de-binifaldo.md) |
| **Comuna de Caimari** | **4.9 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/comuna-de-caimari.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
---

## 💬 Experiències i Valoracions dels Agrupaments Escoltes

<!-- Firebase SDK compat via CDN -->
<script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore-compat.js"></script>

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

    <!-- Formulari interactiu de publicació Firebase (Inicialment ocult) -->
    <div id="exp-form-container" style="display: none; background-color: #ffffff; border: 2px solid #00897b; border-radius: 10px; padding: 18px; margin-bottom: 20px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);">
        <h4 style="margin: 0 0 12px 0; color: #00897b; font-size: 1.05em;">📝 Enviar la teva experiència per a aquesta excursió</h4>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 12px; margin-bottom: 12px;">
            <div>
                <label style="font-weight: bold; font-size: 0.85em; display: block; margin-bottom: 4px;">⚜️ Agrupament Escolta:</label>
                <select id="exp-agrupament" style="width: 100%; padding: 8px; border-radius: 6px; border: 1px solid #ccc;">
                    <option value="">-- Selecciona el teu Agrupament --</option>
                    <option value="AEG Capità Angelats">AEG Capità Angelats</option>
                    <option value="AEG Pedra Viva">AEG Pedra Viva</option>
                    <option value="AEG Soca-Arrel">AEG Soca-Arrel</option>
                    <option value="AEG Terra de Pous">AEG Terra de Pous</option>
                    <option value="AEG Sa Marjal">AEG Sa Marjal</option>
                    <option value="AEG Son Sardina">AEG Son Sardina</option>
                    <option value="AEG Eladi Homs">AEG Eladi Homs</option>
                    <option value="AEG Jaume I">AEG Jaume I</option>
                    <option value="AEG Verge de Lluc">AEG Verge de Lluc</option>
                    <option value="AEG Ramon Llull">AEG Ramon Llull</option>
                    <option value="AEG Reina Constança de Mallorca">AEG Reina Constança de Mallorca</option>
                    <option value="AEG Sant Josep Obrer">AEG Sant Josep Obrer</option>
                    <option value="AEG Nuredduna">AEG Nuredduna</option>
                    <option value="Grupo Scout Myotragus 684">Grupo Scout Myotragus 684</option>
                    <option value="Altre Agrupament / Grup Escolta">Altre Agrupament / Grup Escolta</option>
                </select>
            </div>
            <div>
                <label style="font-weight: bold; font-size: 0.85em; display: block; margin-bottom: 4px;">🎒 Branca Escolta:</label>
                <select id="exp-branca" style="width: 100%; padding: 8px; border-radius: 6px; border: 1px solid #ccc;">
                    <option value="Castors/Fures">Castors / Fures (6-8 anys)</option>
                    <option value="Llops/Daines">Llops / Daines (8-11 anys)</option>
                    <option value="Pioners/Rangers">Pioners / Rangers (11-14 anys)</option>
                    <option value="Rovers/Rutes">Rovers / Rutes (14-17+ anys)</option>
                    <option value="Caps/Monitors">Caps / Equip de Suport</option>
                </select>
            </div>
            <div>
                <label style="font-weight: bold; font-size: 0.85em; display: block; margin-bottom: 4px;">⭐ Valoració Global:</label>
                <select id="exp-puntuacio" style="width: 100%; padding: 8px; border-radius: 6px; border: 1px solid #ccc;">
                    <option value="5">⭐⭐⭐⭐⭐ (5/5 - Excel·lent ruta)</option>
                    <option value="4">⭐⭐⭐⭐ (4/5 - Molt bona)</option>
                    <option value="3">⭐⭐⭐ (3/5 - Correcta)</option>
                    <option value="2">⭐⭐ (2/5 - Regular / Amb atenció)</option>
                    <option value="1">⭐ (1/5 - No recomanada)</option>
                </select>
            </div>
            <div>
                <label style="font-weight: bold; font-size: 0.85em; display: block; margin-bottom: 4px;">📅 Data de la Sortida:</label>
                <input type="text" id="exp-data" placeholder="Ex: Setembre 2026" style="width: 100%; padding: 8px; border-radius: 6px; border: 1px solid #ccc;" />
            </div>
        </div>

        <div style="margin-bottom: 14px;">
            <label style="font-weight: bold; font-size: 0.85em; display: block; margin-bottom: 4px;">💬 Comentaris, consells d'aigua, ombra o recomanacions logístiques:</label>
            <textarea id="exp-comentari" rows="3" placeholder="Comentau l'estat del camí, les fonts amb aigua, punts d'ombra, zones d'acampada o recomanacions per a la vostra branca..." style="width: 100%; padding: 10px; border-radius: 6px; border: 1px solid #ccc; font-family: inherit; font-size: 0.9em; box-sizing: border-box;"></textarea>
        </div>

        <div style="display: flex; justify-content: flex-end; gap: 10px;">
            <button onclick="toggleExpForm()" style="padding: 8px 16px; background-color: #757575; color: white; border: none; border-radius: 6px; cursor: pointer;">Cancel·lar</button>
            <button id="exp-submit-btn" onclick="submitFirebaseExperience('cami-de-ses-voltes-galileu')" style="padding: 8px 20px; background-color: #00897b; color: white; border: none; border-radius: 6px; cursor: pointer; font-weight: bold;">🚀 Publicar a Firebase</button>
        </div>
        <div id="exp-status-msg" style="margin-top: 10px; font-weight: bold; font-size: 0.9em;"></div>
    </div>

    <!-- Llista interactiva de ressenyes -->
    <div id="experiences-list-container" style="display: flex; flex-direction: column; gap: 12px;">
        <p style="color: #666; font-style: italic; font-size: 0.88em;">🔄 Carregant experiències de Firebase...</p>
    </div>

</div>

<script>
(function() {
    const routeSlug = "cami-de-ses-voltes-galileu";
    const staticExperiences = [];

    // Configurar Firebase Firestore
    const firebaseConfig = {
        projectId: "escoltes-mallorca"
    };

    if (typeof firebase !== 'undefined' && !firebase.apps.length) {
        firebase.initializeApp(firebaseConfig);
    }

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
                    <p style="margin: 0; color: #666;">⛺ Heu fet aquesta excursió? Polsau el botó superior per afegir la teva experiència en temps real.</p>
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
            const score = Number(exp.puntuacio) || 5;
            const expStars = "⭐".repeat(score);
            const agrName = exp.agrupament || 'Agrupament Escolta';
            const brancaName = exp.branca ? ` (${exp.branca})` : '';
            const dataStr = exp.data || '';
            const comentariText = exp.comentari || '';
            
            html += `
                <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 14px; background-color: #ffffff; box-shadow: 0 2px 4px rgba(0,0,0,0.03);">
                    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 6px; margin-bottom: 6px;">
                        <span style="font-weight: bold; color: #00897b; font-size: 0.95em;">⚜️ ${agrName} <span style="font-weight: normal; color: #666; font-size: 0.9em;">${brancaName}</span></span>
                        <span style="font-size: 0.85em; color: #f57f17; font-weight: bold;">${expStars} <span style="color: #888; font-weight: normal;">(${dataStr})</span></span>
                    </div>
                    <p style="margin: 4px 0 0 0; font-size: 0.9em; color: #333; line-height: 1.45;"><i>"${comentariText}"</i></p>
                </div>
            `;
        });
        container.innerHTML = html;
    };

    let liveExperiences = [...staticExperiences];

    window.initFirebaseExperiences = function() {
        renderExperiencesList(liveExperiences);
        
        if (typeof firebase !== 'undefined' && firebase.firestore) {
            try {
                const db = firebase.firestore();
                db.collection("experiencies")
                  .where("ruta_slug", "==", routeSlug)
                  .onSnapshot((snapshot) => {
                      const fetched = [];
                      snapshot.forEach(doc => {
                          fetched.push(doc.data());
                      });
                      
                      if (fetched.length > 0) {
                          const combined = [...fetched];
                          staticExperiences.forEach(st => {
                              if (!combined.some(f => f.comentari === st.comentari && f.agrupament === st.agrupament)) {
                                  combined.push(st);
                              }
                          });
                          liveExperiences = combined;
                          renderExperiencesList(liveExperiences);
                      }
                  }, (err) => {
                      console.warn("Firestore snapshot error/offline, using static exps:", err);
                  });
            } catch(e) {
                console.warn("Firebase init error:", e);
            }
        }
    };

    window.submitFirebaseExperience = async function(slug) {
        const agrupament = document.getElementById('exp-agrupament').value;
        const branca = document.getElementById('exp-branca').value;
        const puntuacio = parseInt(document.getElementById('exp-puntuacio').value, 10);
        const dataVal = document.getElementById('exp-data').value.trim() || 'Recenta';
        const comentari = document.getElementById('exp-comentari').value.trim();
        const statusMsg = document.getElementById('exp-status-msg');
        const submitBtn = document.getElementById('exp-submit-btn');

        if (!agrupament) {
            statusMsg.style.color = '#d32f2f';
            statusMsg.innerText = '⚠️ Si us plau, selecciona el teu agrupament escolta.';
            return;
        }

        if (!comentari || comentari.length < 5) {
            statusMsg.style.color = '#d32f2f';
            statusMsg.innerText = '⚠️ Si us plau, escriu un comentari o consell rellevant (mínim 5 caràcters).';
            return;
        }

        const newExp = {
            ruta_slug: slug,
            agrupament: agrupament,
            branca: branca,
            puntuacio: puntuacio,
            data: dataVal,
            comentari: comentari,
            createdAt: (typeof firebase !== 'undefined' && firebase.firestore) ? firebase.firestore.FieldValue.serverTimestamp() : new Date().toISOString()
        };

        statusMsg.style.color = '#00897b';
        statusMsg.innerText = '⏳ Publicant experiència a Firebase...';
        submitBtn.disabled = true;

        try {
            if (typeof firebase !== 'undefined' && firebase.firestore) {
                const db = firebase.firestore();
                await db.collection("experiencies").add(newExp);
                statusMsg.style.color = '#2e7d32';
                statusMsg.innerText = '✅ Experiència publicada amb èxit en temps real a Firebase!';
            } else {
                liveExperiences.unshift(newExp);
                renderExperiencesList(liveExperiences);
                statusMsg.style.color = '#2e7d32';
                statusMsg.innerText = '✅ Experiència afegida localment!';
            }
            
            document.getElementById('exp-comentari').value = '';
            document.getElementById('exp-data').value = '';
            setTimeout(() => {
                toggleExpForm();
                statusMsg.innerText = '';
                submitBtn.disabled = false;
            }, 1800);
        } catch (error) {
            console.error("Error al publicar a Firebase:", error);
            liveExperiences.unshift(newExp);
            renderExperiencesList(liveExperiences);
            statusMsg.style.color = '#e65100';
            statusMsg.innerText = '✅ Experiència gravada localment (sense connexió directa a Firebase).';
            submitBtn.disabled = false;
        }
    };

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', window.initFirebaseExperiences);
    } else {
        window.initFirebaseExperiences();
    }
})();
</script>


