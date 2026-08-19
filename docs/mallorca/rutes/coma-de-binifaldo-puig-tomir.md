# 🏔️ Ascensió al Puig Tomir (des de Binifaldó)

Una de les grans meques d'alta muntanya escolta de la Tramuntana nord.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-coma-de-binifaldo-puig-tomir" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_coma_de_binifaldo_puig_tomir() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_coma_de_binifaldo_puig_tomir, 200);
        return;
    }
    
    const trackPoints = [[39.8311, 2.8988]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-coma-de-binifaldo-puig-tomir');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Ascensió al Puig Tomir (des de Binifaldó)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Ascensió al Puig Tomir (des de Binifaldó)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.8311, 2.8988], 14);
        L.marker([39.8311, 2.8988]).addTo(rMap).bindPopup("<b>Ascensió al Puig Tomir (des de Binifaldó)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_coma_de_binifaldo_puig_tomir);
setTimeout(initRouteTrackMap_coma_de_binifaldo_puig_tomir, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Escorca** |
| **Zona / Comarca** | **Tramuntana Nord** |
| **Distància Total** | **10.8 km** |
| **Desnivell Positiu** | **+670 m** |
| **Dificultat Tècnica** | **Exigent** |
| **Durada Estimada** | **4h 30min** |
| **Unitats Recomanades** | **Pioners/Rangers, Rovers/Rutes** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Escorca**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 341** (Pollença - Lluc - Cúber - Port de Sóller (Línia Ma-10)) | Pollença, Lluc (Monestir), Binifaldó, Gorg Blau | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/341) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Cases de Binifaldó
- **Passos per Finques Privades:** Finca de Binifaldó (IBANAT)
- **Punts d'Interès Cultural i Natural:** Cim del Puig Tomir (1.103m), Pas des Regatxo, Cases de Neu del Tomir

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Cadena de seguretat al Pas des Regatxo. Atenció amb vent o pluja.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Cases de Binifaldó (Refugi IBANAT)** | IBANAT (Govern de les Illes Balears) | 30 pers. | **0.00 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/cases-de-binifaldo.md) |
| **Àrea d'Acampada des Pixarells** | IBANAT (Govern de les Illes Balears) | 80 pers. | **0.71 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/es-pixarells-lluc.md) |
| **Àrea d'Acampada de Marjanor** | IBANAT (Govern de les Illes Balears) | 60 pers. | **1.40 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/marjanor-lluc.md) |
| **Refugi de Son Amer** | Consell de Mallorca (Xarxa GR-221) | 52 pers. | **1.46 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/refugi-son-amer.md) |
| **Àrea d'Acampada de Sa Font Coberta** | IBANAT (Govern de les Illes Balears) | 150 pers. | **1.56 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/sa-font-coberta-lluc.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Comuna de Caimari** | **6.1 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/comuna-de-caimari.md) |
| **Monestir de Santa Llúcia** | **9.5 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/monestir-santa-llucia-mancor.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Sa Marjal** | Sa Pobla | **12.8 km** | [Veure Casal](../agrupaments/aeg-sa-marjal.md) |
| **AEG Pedra Viva** | Binissalem | **16.2 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |
