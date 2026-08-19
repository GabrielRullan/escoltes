# 🏔️ Cala Boquer i Vall de Boquer (Pollença)

Passejada assequible entre muntanyes fins a una cala verge del nord de Mallorca.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-cala-boquer-pollenca" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_cala_boquer_pollenca() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_cala_boquer_pollenca, 200);
        return;
    }
    
    const trackPoints = [[39.912, 3.084]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-cala-boquer-pollenca');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Cala Boquer i Vall de Boquer (Pollença)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Cala Boquer i Vall de Boquer (Pollença)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.912, 3.084], 14);
        L.marker([39.912, 3.084]).addTo(rMap).bindPopup("<b>Cala Boquer i Vall de Boquer (Pollença)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_cala_boquer_pollenca);
setTimeout(initRouteTrackMap_cala_boquer_pollenca, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Pollença** |
| **Zona / Comarca** | **Tramuntana Nord** |
| **Distància Total** | **5.5 km** |
| **Desnivell Positiu** | **+120 m** |
| **Dificultat Tècnica** | **Fàcil** |
| **Durada Estimada** | **2h 00min** |
| **Unitats Recomanades** | **Castors/Fures, Llops/Daines, Pioners/Rangers** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Pollença**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 301** (Palma - Inca - Port de Pollença) | Palma, Inca (Estació), Pollença, Port de Pollença | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/301) |
| **TIB 334** (Alcúdia - Port de Pollença - Formentor) | Port de Pollença, Cala Murta, Far de Formentor | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/334) |
| **TIB 341** (Pollença - Lluc - Cúber - Port de Sóller (Línia Ma-10)) | Pollença, Lluc (Monestir), Binifaldó, Gorg Blau | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/341) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Port de Pollença (inici)
- **Passos per Finques Privades:** Finca de Boquer
- **Punts d'Interès Cultural i Natural:** Vall verge de Boquer, Cala Boquer, Observació de cavalls i aus de la serra

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Tancat de la finca: tancar sempre les meixantes.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)

> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.

### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Santuari del Puig de Maria** | **7.1 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/puig-de-maria-santuari-pollenca.md) |
| **Refugi de Lavanor** | **7.4 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-lavanor-pollenca.md) |
| **Campament de la Victòria** | **8.6 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/campament-la-victoria-alcudia.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Sa Marjal** | Sa Pobla | **16.6 km** | [Veure Casal](../agrupaments/aeg-sa-marjal.md) |
| **AEG Pedra Viva** | Binissalem | **32.0 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |
