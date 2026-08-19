# 🏔️ Cami del Far de Formentor a Cala Murta (Pollença)

Ruta litoral per la península de Formentor finalitzant a la cala verge de Cala Murta.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-penyal-des-migdia-formentor" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_penyal_des_migdia_formentor() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_penyal_des_migdia_formentor, 200);
        return;
    }
    
    const trackPoints = [[39.948, 3.178]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-penyal-des-migdia-formentor');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Cami del Far de Formentor a Cala Murta (Pollença)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Cami del Far de Formentor a Cala Murta (Pollença)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.948, 3.178], 14);
        L.marker([39.948, 3.178]).addTo(rMap).bindPopup("<b>Cami del Far de Formentor a Cala Murta (Pollença)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_penyal_des_migdia_formentor);
setTimeout(initRouteTrackMap_penyal_des_migdia_formentor, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Pollença** |
| **Zona / Comarca** | **Tramuntana Nord** |
| **Distància Total** | **6.8 km** |
| **Desnivell Positiu** | **+190 m** |
| **Dificultat Tècnica** | **Fàcil - Moderada** |
| **Durada Estimada** | **2h 30min** |
| **Unitats Recomanades** | **Llops/Daines, Pioners/Rangers, Rovers/Rutes** |

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

- **Punts d'Aigua Potable / Recàrrega:** Cala Murta (cases de la fundació)
- **Passos per Finques Privades:** Fundació Rotger-Villalonga (Cala Murta)
- **Punts d'Interès Cultural i Natural:** Cala Figuera, Cala Murta, Possessió de Formentor

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Restriccions de trànsit a la carretera de Formentor a l'estiu (usar bus TIB).

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)

> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.

### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Campament de la Victòria** | **8.5 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/campament-la-victoria-alcudia.md) |
| **Refugi del Coll Baix** | **9.3 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-coll-baix-alcudia.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Sa Marjal** | Sa Pobla | **23.8 km** | [Veure Casal](../agrupaments/aeg-sa-marjal.md) |
| **AEG Pedra Viva** | Binissalem | **40.4 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |
