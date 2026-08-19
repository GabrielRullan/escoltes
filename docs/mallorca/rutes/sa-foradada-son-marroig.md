# 🏔️ Sa Foradada des de Son Marroig (Deià)

Baixada clàssica cap a la singular península rocosa foradada de la costa nord.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-sa-foradada-son-marroig" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_sa_foradada_son_marroig() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_sa_foradada_son_marroig, 200);
        return;
    }
    
    const trackPoints = [[39.751, 2.628]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-sa-foradada-son-marroig');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Sa Foradada des de Son Marroig (Deià)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Sa Foradada des de Son Marroig (Deià)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.751, 2.628], 14);
        L.marker([39.751, 2.628]).addTo(rMap).bindPopup("<b>Sa Foradada des de Son Marroig (Deià)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_sa_foradada_son_marroig);
setTimeout(initRouteTrackMap_sa_foradada_son_marroig, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Deià** |
| **Zona / Comarca** | **Tramuntana Central** |
| **Distància Total** | **7.0 km** |
| **Desnivell Positiu** | **+290 m** |
| **Dificultat Tècnica** | **Moderada** |
| **Durada Estimada** | **2h 45min** |
| **Unitats Recomanades** | **Llops/Daines, Pioners/Rangers, Rovers/Rutes** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Deià**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 203** (Palma - Valldemossa - Deià - Sóller) | Palma, Valldemossa, Son Marroig, Deià | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/203) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Son Marroig (cafeteria)
- **Passos per Finques Privades:** Possessió de Son Marroig (Arxiduc Lluís Salvador)
- **Punts d'Interès Cultural i Natural:** Roca foradada de sa Foradada, Embarcador de l'Arxiduc

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Pujada de tornada sota el sol. Aigua necessària.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Refugi de Can Boi** | Consell de Mallorca (Xarxa GR-221) | 32 pers. | **1.75 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/refugi-can-boi.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Refugi de Son Moragues** | **4.0 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-son-moragues.md) |
| **Refugi de Muleta** | **7.0 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-muleta.md) |
| **Sant Ramon de Penyafort** | **7.7 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/sant-ramon-de-penyafort-soller.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Capità Angelats** | Sóller | **7.7 km** | [Veure Casal](../agrupaments/aeg-capita-angelats.md) |
| **AEG Nuredduna** | Bunyola / Palmanyola | **11.8 km** | [Veure Casal](../agrupaments/aeg-nuredduna.md) |
