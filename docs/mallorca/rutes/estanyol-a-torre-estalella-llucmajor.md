# 🏔️ s'Estanyol a la Torre de s'Estalella (Llucmajor)

Agradable passejada costera ideal per als més petits que recorre el litoral verge de Llucmajor des del port de s'Estanyol fins a la històrica torre de guaita de s'Estalella.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-estanyol-a-torre-estalella-llucmajor" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_estanyol_a_torre_estalella_llucmajor() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_estanyol_a_torre_estalella_llucmajor, 200);
        return;
    }
    
    const trackPoints = [[39.362, 2.915], [39.358, 2.902], [39.352, 2.891]];
    const itinerariPassos = [{"pas": 1, "nom": "Inici al Port de s'Estanyol", "desc": "Camí litoral que voreja les casetes de pescadors."}, {"pas": 2, "nom": "Far i Jaciments costers", "desc": "Tram pla sobre pedra de marès."}, {"pas": 3, "nom": "Torre de s'Estalella", "desc": "Arribada a la torre defensiva amb vistes a Cabrera."}];
    
    const rMap = L.map('map-route-estanyol-a-torre-estalella-llucmajor');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> s'Estanyol a la Torre de s'Estalella (Llucmajor)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> s'Estanyol a la Torre de s'Estalella (Llucmajor)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.362, 2.915], 14);
        L.marker([39.362, 2.915]).addTo(rMap).bindPopup("<b>s'Estanyol a la Torre de s'Estalella (Llucmajor)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_estanyol_a_torre_estalella_llucmajor);
setTimeout(initRouteTrackMap_estanyol_a_torre_estalella_llucmajor, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Llucmajor** |
| **Zona / Comarca** | **Migjorn** |
| **Distància Total** | **4.2 km** |
| **Desnivell Positiu** | **+20 m** |
| **Dificultat Tècnica** | **Molt Fàcil** |
| **Durada Estimada** | **1h 30min** |
| **Unitats Recomanades** | **Castors/Fures, Llops/Daines, Pioners/Rangers, Rovers/Rutes** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=s%27Estanyol%20a%20la%20Torre%20de%20s%27Estalella%20%28Llucmajor%29)** |
| **Guia Turisme Petit** | **[👶 Veure Guia de Família a Turisme Petit 🔗](https://www.turismepetit.com/excursion/excursion-desde-estanyol-a-torre-estalella/)** |

---

## 🥾 Itinerari i Rumb de la Ruta Pas a Pas

| Pas | Punt de Referència / Tram | Indicacions i Descripció |
| :---: | :--- | :--- |
| **Pas 1** | **Inici al Port de s'Estanyol** | Camí litoral que voreja les casetes de pescadors. |
| **Pas 2** | **Far i Jaciments costers** | Tram pla sobre pedra de marès. |
| **Pas 3** | **Torre de s'Estalella** | Arribada a la torre defensiva amb vistes a Cabrera. |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Llucmajor**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 501** (Palma - Llucmajor - Campos - Felanitx) | Palma, Llucmajor, Campos, Felanitx | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/501) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Poble de s'Estanyol de Migjorn
- **Passos per Finques Privades:** Camí de sa costa (públic)
- **Punts d'Interès Cultural i Natural:** Torre de guaita de s'Estalella (S. XVI), Nidos de metralladora, Far de s'Estalella

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Ruta completament plana sense desnivell. Portar gorra i protecció solar.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **S'Estanyol (Llucmajor)** | Gestió Entitat | 40 pers. | **1.45 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/s-estanyol-llucmajor.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Sant Francesc d'Assís (Colònia de Sant Jordi)** | **8.9 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/sant-francesc-d-assis-ses-salines.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **Grupo Scout Myotragus 684** | Llucmajor | **20.8 km** | [Veure Casal](../agrupaments/gs-myotragus-684.md) |
| **AEG Eladi Homs** | Palma | **32.4 km** | [Veure Casal](../agrupaments/aeg-eladi-homs.md) |

---

## 💬 Experiències i Valoracions dels Agrupaments Escoltes

<div style="background-color: var(--md-code-bg-color, #f8f9fa); border: 1px solid #e0e0e0; padding: 18px; border-radius: 10px; margin-top: 16px;">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
        <div>
            <h3 style="margin: 0; font-size: 1.05em; color: #555;">Encara no hi ha cap experiència registrada per a aquesta ruta.</h3>
            <p style="margin: 4px 0 0 0; font-size: 0.85em; color: #666;">Heu fet aquesta ruta amb la vostra unitat? Sigueu els primers a deixar consells per a altres agrupaments!</p>
        </div>
        <a href="../../sop/enviar_experiencia/" style="padding: 8px 16px; background-color: #00897b; color: white; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 0.85em;">📝 Enviar la primera experiència 🔗</a>
    </div>
</div>

