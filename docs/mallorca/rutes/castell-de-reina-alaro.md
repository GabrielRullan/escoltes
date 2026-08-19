# 🏔️ Pas des Llop i Cova de sa Campana (Alaró / Escorca)

Ruta tècnica per la cara nord de la serra d'Alaró i les seves cavitats subterrànies.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-castell-de-reina-alaro" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_castell_de_reina_alaro() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_castell_de_reina_alaro, 200);
        return;
    }
    
    const trackPoints = [[39.728, 2.812]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-castell-de-reina-alaro');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Pas des Llop i Cova de sa Campana (Alaró / Escorca)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Pas des Llop i Cova de sa Campana (Alaró / Escorca)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.728, 2.812], 14);
        L.marker([39.728, 2.812]).addTo(rMap).bindPopup("<b>Pas des Llop i Cova de sa Campana (Alaró / Escorca)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_castell_de_reina_alaro);
setTimeout(initRouteTrackMap_castell_de_reina_alaro, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Alaró / Escorca** |
| **Zona / Comarca** | **Raiguer** |
| **Distància Total** | **11.0 km** |
| **Desnivell Positiu** | **+590 m** |
| **Dificultat Tècnica** | **Exigent** |
| **Durada Estimada** | **4h 30min** |
| **Unitats Recomanades** | **Rovers/Rutes** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Alaró / Escorca**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 341** (Pollença - Lluc - Cúber - Port de Sóller (Línia Ma-10)) | Pollença, Lluc (Monestir), Binifaldó, Gorg Blau | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/341) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Font de sa Cova
- **Passos per Finques Privades:** Comuna d'Inca / Clot d'Alaro
- **Punts d'Interès Cultural i Natural:** Pas des Llop, Cova de sa Campana

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Ruta per a caps i Rovers experimentats.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)

> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.

### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **S'Olivaret (Alaró)** | **3.1 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/solivaret-alaro.md) |
| **Castell d'Alaró (Hostatgeria i Refugi)** | **3.3 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/castell-d-alaro-hostatgeria.md) |
| **Refugi de Tossals Verds** | **3.5 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-tossals-verds.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Pedra Viva** | Binissalem | **4.8 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |
| **AEG Terra de Pous** | Santa Maria del Camí | **9.2 km** | [Veure Casal](../agrupaments/aeg-terra-de-pous.md) |
