# 🏔️ Sa Comuna de Lloret de Vistalegre

Bosc pla ideal per a la primera acampada o jornada de jocs de les branques més petites.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-sa-comuna-de-lloret-de-vistalegre" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_sa_comuna_de_lloret_de_vistalegre() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_sa_comuna_de_lloret_de_vistalegre, 200);
        return;
    }
    
    const trackPoints = [[39.612, 2.975]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-sa-comuna-de-lloret-de-vistalegre');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Sa Comuna de Lloret de Vistalegre");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Sa Comuna de Lloret de Vistalegre");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.612, 2.975], 14);
        L.marker([39.612, 2.975]).addTo(rMap).bindPopup("<b>Sa Comuna de Lloret de Vistalegre</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_sa_comuna_de_lloret_de_vistalegre);
setTimeout(initRouteTrackMap_sa_comuna_de_lloret_de_vistalegre, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Lloret de Vistalegre** |
| **Zona / Comarca** | **Pla de Mallorca** |
| **Distància Total** | **4.0 km** |
| **Desnivell Positiu** | **+45 m** |
| **Dificultat Tècnica** | **Molt Fàcil** |
| **Durada Estimada** | **1h 30min** |
| **Unitats Recomanades** | **Castors/Fures, Llops/Daines** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Lloret de Vistalegre**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB / SFM Xarxa General** (Línia d'autobús o tren comarcal (Lloret de Vistalegre)) | Lloret de Vistalegre | [Consultar Horaris Oficials 🔗](https://www.tib.org/) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Lloret de Vistalegre
- **Passos per Finques Privades:** Bosc Públic de la Comuna de Lloret
- **Punts d'Interès Cultural i Natural:** Cova d'en sa Garriga, Pineda de la Comuna, Caseta de fusta de natura

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Ideal per a jocs de pista i Castors/Llops.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)

> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.

### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Puig de Sant Miquel (Kcodril)** | **3.9 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/puig-de-sant-miquel-montuiri-alberg.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Pedra Viva** | Binissalem | **14.4 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |
| **AEG Terra de Pous** | Santa Maria del Camí | **17.9 km** | [Veure Casal](../agrupaments/aeg-terra-de-pous.md) |
