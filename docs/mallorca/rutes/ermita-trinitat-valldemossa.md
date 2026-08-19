# 🏔️ Ermita de la Trinitat i Miradors de Valldemossa

Ruta de pau i espiritualitat pels boscos d'alzinars de Valldemossa.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-ermita-trinitat-valldemossa" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_ermita_trinitat_valldemossa() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_ermita_trinitat_valldemossa, 200);
        return;
    }
    
    const trackPoints = [[39.718, 2.612]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-ermita-trinitat-valldemossa');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Ermita de la Trinitat i Miradors de Valldemossa");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Ermita de la Trinitat i Miradors de Valldemossa");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.718, 2.612], 14);
        L.marker([39.718, 2.612]).addTo(rMap).bindPopup("<b>Ermita de la Trinitat i Miradors de Valldemossa</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_ermita_trinitat_valldemossa);
setTimeout(initRouteTrackMap_ermita_trinitat_valldemossa, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Valldemossa** |
| **Zona / Comarca** | **Tramuntana Central** |
| **Distància Total** | **5.8 km** |
| **Desnivell Positiu** | **+220 m** |
| **Dificultat Tècnica** | **Fàcil** |
| **Durada Estimada** | **2h 15min** |
| **Unitats Recomanades** | **Castors/Fures, Llops/Daines, Pioners/Rangers** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Ermita%20de%20la%20Trinitat%20i%20Miradors%20de%20Valldemossa)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Valldemossa**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 203** (Palma - Valldemossa - Deià - Sóller) | Palma, Valldemossa, Son Marroig, Deià | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/203) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Valldemossa / Ermita de la Trinitat
- **Passos per Finques Privades:** Bosc de sa Coma
- **Punts d'Interès Cultural i Natural:** Ermita dels Ermitans de Sant Pau, Miranda des Lledoner

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Respectar el silenci i la tranquil·litat dels ermitans.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Refugi de Son Moragues** | IBANAT (Govern de les Illes Balears) | 15 pers. | **1.41 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/refugi-son-moragues.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Refugi de Can Boi** | **4.6 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-can-boi.md) |
| **Maristel·la (Ermita i Terreny)** | **7.0 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/maristella-esporles.md) |
| **Binicanella (Casa de Colònies)** | **8.0 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/binicanella-bunyola.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Nuredduna** | Bunyola / Palmanyola | **9.8 km** | [Veure Casal](../agrupaments/aeg-nuredduna.md) |
| **AEG Capità Angelats** | Sóller | **10.3 km** | [Veure Casal](../agrupaments/aeg-capita-angelats.md) |
