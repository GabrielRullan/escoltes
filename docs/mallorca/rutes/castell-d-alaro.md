# 🏔️ Excursió al Castell d'Alaró (des d'Orient o Es Verger)

Excursió clàssica de l'escoltisme mallorquí cap a la fortalesa rocosa del Castell d'Alaró.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-castell-d-alaro" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_castell_d_alaro() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_castell_d_alaro, 200);
        return;
    }
    
    const trackPoints = [[39.7025, 2.7915]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-castell-d-alaro');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Excursió al Castell d'Alaró (des d'Orient o Es Verger)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Excursió al Castell d'Alaró (des d'Orient o Es Verger)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.7025, 2.7915], 14);
        L.marker([39.7025, 2.7915]).addTo(rMap).bindPopup("<b>Excursió al Castell d'Alaró (des d'Orient o Es Verger)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_castell_d_alaro);
setTimeout(initRouteTrackMap_castell_d_alaro, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Alaró** |
| **Zona / Comarca** | **Raiguer** |
| **Distància Total** | **8.0 km** |
| **Desnivell Positiu** | **+450 m** |
| **Dificultat Tècnica** | **Moderada** |
| **Durada Estimada** | **3h 00min** |
| **Unitats Recomanades** | **Llops/Daines, Pioners/Rangers, Rovers/Rutes** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Excursi%C3%B3%20al%20Castell%20d%27Alar%C3%B3%20%28des%20d%27Orient%20o%20Es%20Verger%29)** |
| **Guia Turisme Petit** | **[👶 Veure Guia de Família a Turisme Petit 🔗](https://www.turismepetit.com/excursion/el-castell-dalaro/)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Alaró**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB / SFM Xarxa General** (Línia d'autobús o tren comarcal (Alaró)) | Alaró | [Consultar Horaris Oficials 🔗](https://www.tib.org/) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Orient / Es Verger, Hostal del Castell d'Alaró
- **Passos per Finques Privades:** Camí del Castell
- **Punts d'Interès Cultural i Natural:** Castell d'Alaró, Hospederia, Vistes panoràmiques del Pla i la Serra

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Compte amb les pedres resbaladisses en dies de pluja.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Castell d'Alaró (Hostatgeria i Refugi)** | Fundació Castell d'Alaró / Consell | 30 pers. | **0.00 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/castell-d-alaro-hostatgeria.md) |
| **S'Olivaret (Alaró)** | Gestió Privada | 40 pers. | **1.33 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/solivaret-alaro.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Ca n'Arabí** | **4.5 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/ca-narabi-binissalem.md) |
| **Ca Ses Monges** | **5.9 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/ca-ses-monges-santa-maria.md) |
| **Refugi de Tossals Verds** | **6.7 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-tossals-verds.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Pedra Viva** | Binissalem | **4.5 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |
| **AEG Terra de Pous** | Santa Maria del Camí | **5.9 km** | [Veure Casal](../agrupaments/aeg-terra-de-pous.md) |
