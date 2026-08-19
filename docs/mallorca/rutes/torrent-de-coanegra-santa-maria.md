# 🏔️ Torrent de Coanegra i Salt des Freu de Coanegra

Sender boscós ombrívol seguint el llit del torrent de Coanegra.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-torrent-de-coanegra-santa-maria" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_torrent_de_coanegra_santa_maria() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_torrent_de_coanegra_santa_maria, 200);
        return;
    }
    
    const trackPoints = [[39.668, 2.761]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-torrent-de-coanegra-santa-maria');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Torrent de Coanegra i Salt des Freu de Coanegra");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Torrent de Coanegra i Salt des Freu de Coanegra");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.668, 2.761], 14);
        L.marker([39.668, 2.761]).addTo(rMap).bindPopup("<b>Torrent de Coanegra i Salt des Freu de Coanegra</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_torrent_de_coanegra_santa_maria);
setTimeout(initRouteTrackMap_torrent_de_coanegra_santa_maria, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Santa Maria del Camí** |
| **Zona / Comarca** | **Raiguer** |
| **Distància Total** | **9.5 km** |
| **Desnivell Positiu** | **+210 m** |
| **Dificultat Tècnica** | **Moderada** |
| **Durada Estimada** | **3h 15min** |
| **Unitats Recomanades** | **Llops/Daines, Pioners/Rangers** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Torrent%20de%20Coanegra%20i%20Salt%20des%20Freu%20de%20Coanegra)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Santa Maria del Camí**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **SFM Línia T1** (Tren Palma - Inca (Raiguer)) | Palma (Estació Intermodal), Verge de Lluc, Pont d'Inca, Marratxí | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/tren/linia/T1) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Santa Maria del Camí
- **Passos per Finques Privades:** Son Pou / Son Creus
- **Punts d'Interès Cultural i Natural:** Gorg de Can Fumat, Son Pou

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Evitar amb risc de riada en pluges molt torrencials.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)

> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.

### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Ca Ses Monges** | **2.1 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/ca-ses-monges-santa-maria.md) |
| **Castell d'Alaró (Hostatgeria i Refugi)** | **4.6 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/castell-d-alaro-hostatgeria.md) |
| **S'Olivaret (Alaró)** | **5.2 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/solivaret-alaro.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Terra de Pous** | Santa Maria del Camí | **2.1 km** | [Veure Casal](../agrupaments/aeg-terra-de-pous.md) |
| **AEG Soca-Arrel** | Marratxí | **4.3 km** | [Veure Casal](../agrupaments/aeg-soca-arrel.md) |

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

