# 🏔️ Pujada a l'Ermita de Bonany des de Petra

El mirador del Pla de Mallorca des del poble de Petra.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-ermita-bonany-petra" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_ermita_bonany_petra() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_ermita_bonany_petra, 200);
        return;
    }
    
    const trackPoints = [[39.605, 3.102]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-ermita-bonany-petra');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Pujada a l'Ermita de Bonany des de Petra");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Pujada a l'Ermita de Bonany des de Petra");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.605, 3.102], 14);
        L.marker([39.605, 3.102]).addTo(rMap).bindPopup("<b>Pujada a l'Ermita de Bonany des de Petra</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_ermita_bonany_petra);
setTimeout(initRouteTrackMap_ermita_bonany_petra, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Petra** |
| **Zona / Comarca** | **Pla de Mallorca** |
| **Distància Total** | **7.0 km** |
| **Desnivell Positiu** | **+220 m** |
| **Dificultat Tècnica** | **Fàcil** |
| **Durada Estimada** | **2h 15min** |
| **Unitats Recomanades** | **Castors/Fures, Llops/Daines** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Petra**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **SFM Línia T3** (Tren Palma - Inca - Sineu - Manacor) | Inca, Sineu, Petra, Manacor (Estació) | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/tren/linia/T3) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Petra (poble), Ermita de Bonany
- **Passos per Finques Privades:** Camí de Bonany
- **Punts d'Interès Cultural i Natural:** Ermita de la Mare de Déu de Bonany (317m), Vistes a tot el Pla de Mallorca

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Ideal per a sortides d'un dia de Castors i Llops.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)

> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.


### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Sa Marjal** | Sa Pobla | **19.4 km** | [Veure Casal](../agrupaments/aeg-sa-marjal.md) |
| **AEG Pedra Viva** | Binissalem | **24.2 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |
