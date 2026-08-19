# 🏔️ Camí Vell de Pollença a Lluc (per la Font del Tomir)

Antiga via de peregrinació cap al santuari de la Patrona de Mallorca.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-monestir-de-lluc-cami-vell" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_monestir_de_lluc_cami_vell() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_monestir_de_lluc_cami_vell, 200);
        return;
    }
    
    const trackPoints = [[39.852, 2.945]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-monestir-de-lluc-cami-vell');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Camí Vell de Pollença a Lluc (per la Font del Tomir)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Camí Vell de Pollença a Lluc (per la Font del Tomir)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.852, 2.945], 14);
        L.marker([39.852, 2.945]).addTo(rMap).bindPopup("<b>Camí Vell de Pollença a Lluc (per la Font del Tomir)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_monestir_de_lluc_cami_vell);
setTimeout(initRouteTrackMap_monestir_de_lluc_cami_vell, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Pollença / Escorca** |
| **Zona / Comarca** | **Tramuntana Nord** |
| **Distància Total** | **12.5 km** |
| **Desnivell Positiu** | **+490 m** |
| **Dificultat Tècnica** | **Moderada** |
| **Durada Estimada** | **4h 00min** |
| **Unitats Recomanades** | **Llops/Daines, Pioners/Rangers** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Pollença / Escorca**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 301** (Palma - Inca - Port de Pollença) | Palma, Inca (Estació), Pollença, Port de Pollença | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/301) |
| **TIB 334** (Alcúdia - Port de Pollença - Formentor) | Port de Pollença, Cala Murta, Far de Formentor | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/334) |
| **TIB 341** (Pollença - Lluc - Cúber - Port de Sóller (Línia Ma-10)) | Pollença, Lluc (Monestir), Binifaldó, Gorg Blau | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/341) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Pollença, Lluc
- **Passos per Finques Privades:** Finca de Muntanya
- **Punts d'Interès Cultural i Natural:** Mare de Déu de Lluc, Coll de sa Batalla

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Atenció als encreuaments de la carretera Ma-10.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)

> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.

### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Cases de Binifaldó (Refugi IBANAT)** | **4.6 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/cases-de-binifaldo.md) |
| **Àrea d'Acampada des Pixarells** | **5.3 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/es-pixarells-lluc.md) |
| **Àrea d'Acampada de Marjanor** | **5.9 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/marjanor-lluc.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Sa Marjal** | Sa Pobla | **11.4 km** | [Veure Casal](../agrupaments/aeg-sa-marjal.md) |
| **AEG Pedra Viva** | Binissalem | **19.9 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |
