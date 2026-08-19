# 🏔️ Puig des Teix pel Camí de s'Arxiduc (Valldemossa)

Spectacular camí de la carena construït per l'Arxiduc Lluís Salvador sobre Valldemossa.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-puig-des-teix-valldemossa" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_puig_des_teix_valldemossa() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_puig_des_teix_valldemossa, 200);
        return;
    }
    
    const trackPoints = [[39.712, 2.625]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-puig-des-teix-valldemossa');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Puig des Teix pel Camí de s'Arxiduc (Valldemossa)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Puig des Teix pel Camí de s'Arxiduc (Valldemossa)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.712, 2.625], 14);
        L.marker([39.712, 2.625]).addTo(rMap).bindPopup("<b>Puig des Teix pel Camí de s'Arxiduc (Valldemossa)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_puig_des_teix_valldemossa);
setTimeout(initRouteTrackMap_puig_des_teix_valldemossa, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Valldemossa** |
| **Zona / Comarca** | **Tramuntana Central** |
| **Distància Total** | **14.0 km** |
| **Desnivell Positiu** | **+810 m** |
| **Dificultat Tècnica** | **Exigent** |
| **Durada Estimada** | **5h 15min** |
| **Unitats Recomanades** | **Pioners/Rangers, Rovers/Rutes** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Valldemossa**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 203** (Palma - Valldemossa - Deià - Sóller) | Palma, Valldemossa, Son Marroig, Deià | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/203) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Valldemossa (poble)
- **Passos per Finques Privades:** Muntanya del Voltor (requereix permís gratuït prèvi a Valldemossa)
- **Punts d'Interès Cultural i Natural:** Camí de s'Arxiduc, Cim des Teix (1.064m), Refugi de Son Moragues

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Permís d'accés obligatori per a la Muntanya del Voltor. Vent fort a la carena.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Refugi de Son Moragues** | IBANAT (Govern de les Illes Balears) | 15 pers. | **0.42 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/refugi-son-moragues.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Refugi de Can Boi** | **4.6 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-can-boi.md) |
| **Binicanella (Casa de Colònies)** | **6.8 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/binicanella-bunyola.md) |
| **Maristel·la (Ermita i Terreny)** | **7.2 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/maristella-esporles.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Nuredduna** | Bunyola / Palmanyola | **8.6 km** | [Veure Casal](../agrupaments/aeg-nuredduna.md) |
| **AEG Capità Angelats** | Sóller | **9.8 km** | [Veure Casal](../agrupaments/aeg-capita-angelats.md) |
