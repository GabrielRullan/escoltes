# 🏔️ Torrent de Pareis (Només estiu / temps sec)

La travessa de cañón més famosa de la Mediterrània. Extrema precaució i preparació tècnica.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-torrent-de-pareis" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_torrent_de_pareis() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_torrent_de_pareis, 200);
        return;
    }
    
    const trackPoints = [[39.826, 2.846]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-torrent-de-pareis');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Torrent de Pareis (Només estiu / temps sec)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Torrent de Pareis (Només estiu / temps sec)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.826, 2.846], 14);
        L.marker([39.826, 2.846]).addTo(rMap).bindPopup("<b>Torrent de Pareis (Només estiu / temps sec)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_torrent_de_pareis);
setTimeout(initRouteTrackMap_torrent_de_pareis, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Escorca** |
| **Zona / Comarca** | **Tramuntana Nord** |
| **Distància Total** | **7.2 km** |
| **Desnivell Positiu** | **+50 m** |
| **Dificultat Tècnica** | **Molt Exigent / Tècnica** |
| **Durada Estimada** | **5h 00min** |
| **Unitats Recomanades** | **Rovers/Rutes** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Torrent%20de%20Pareis%20%28Nom%C3%A9s%20estiu%20/%20temps%20sec%29)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Escorca**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 341** (Pollença - Lluc - Cúber - Port de Sóller (Línia Ma-10)) | Pollença, Lluc (Monestir), Binifaldó, Gorg Blau | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/341) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Escorca (inici) - CAP AIGUA EN TOT EL RECORREGUT
- **Passos per Finques Privades:** Entre d'Escorca
- **Punts d'Interès Cultural i Natural:** Entreforc, Cova des Romagueral, Sa Calobra

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> PROHIBIT amb qualsevol risc de pluja (risc de riada mortal). Destresa, cordes de seguretat i 3L d'aigua obligatoris. Només Rovers/Caps.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)

> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.

### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Àrea d'Acampada de Sa Font Coberta** | **3.2 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/sa-font-coberta-lluc.md) |
| **Refugi de Son Amer** | **3.6 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-son-amer.md) |
| **Àrea d'Acampada de Marjanor** | **3.7 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/marjanor-lluc.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Capità Angelats** | Sóller | **13.0 km** | [Veure Casal](../agrupaments/aeg-capita-angelats.md) |
| **AEG Pedra Viva** | Binissalem | **14.9 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |
