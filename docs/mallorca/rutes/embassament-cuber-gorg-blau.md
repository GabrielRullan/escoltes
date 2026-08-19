# 🏔️ Volta a l'Embassament de Cúber i Font de s'Ametler

Passejada accessible al voltant de l'estany de Cúber sota la mirada del Puig Major.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-embassament-cuber-gorg-blau" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_embassament_cuber_gorg_blau() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_embassament_cuber_gorg_blau, 200);
        return;
    }
    
    const trackPoints = [[39.7821, 2.7915]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-embassament-cuber-gorg-blau');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Volta a l'Embassament de Cúber i Font de s'Ametler");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Volta a l'Embassament de Cúber i Font de s'Ametler");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.7821, 2.7915], 14);
        L.marker([39.7821, 2.7915]).addTo(rMap).bindPopup("<b>Volta a l'Embassament de Cúber i Font de s'Ametler</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_embassament_cuber_gorg_blau);
setTimeout(initRouteTrackMap_embassament_cuber_gorg_blau, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Escorca** |
| **Zona / Comarca** | **Tramuntana Nord** |
| **Distància Total** | **5.0 km** |
| **Desnivell Positiu** | **+60 m** |
| **Dificultat Tècnica** | **Molt Fàcil** |
| **Durada Estimada** | **1h 45min** |
| **Unitats Recomanades** | **Castors/Fures, Llops/Daines** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Volta%20a%20l%27Embassament%20de%20C%C3%BAber%20i%20Font%20de%20s%27Ametler)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Escorca**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 341** (Pollença - Lluc - Cúber - Port de Sóller (Línia Ma-10)) | Pollença, Lluc (Monestir), Binifaldó, Gorg Blau | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/341) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Refugi de Cúber
- **Passos per Finques Privades:** Finca Pública de Cúber (Govern Balear)
- **Punts d'Interès Cultural i Natural:** Embassament de Cúber, Puig Major al fons, Rucs i ovelles de la finca

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Ruta plana d'alta muntanya ideal per a branques joves.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Refugi de Cúber** | IBANAT (Govern de les Illes Balears) | 6 pers. | **0.00 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/refugi-cuber.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Refugi de Tossals Verds** | **3.7 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-tossals-verds.md) |
| **Sant Ramon de Penyafort** | **6.7 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/sant-ramon-de-penyafort-soller.md) |
| **Monestir de Santa Llúcia** | **7.8 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/monestir-santa-llucia-mancor.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Capità Angelats** | Sóller | **6.7 km** | [Veure Casal](../agrupaments/aeg-capita-angelats.md) |
| **AEG Pedra Viva** | Binissalem | **10.9 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |

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

