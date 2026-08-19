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
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Cam%C3%AD%20des%20Rafal%20i%20Cova%20de%20sa%20Cauba%20%28Dei%C3%A0%29)** |

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

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Capità Angelats** | Sóller | **5.7 km** | [Veure Casal](../agrupaments/aeg-capita-angelats.md) |
| **AEG Nuredduna** | Bunyola / Palmanyola | **11.1 km** | [Veure Casal](../agrupaments/aeg-nuredduna.md) |

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

