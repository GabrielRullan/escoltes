# 🏔️ Tomb pel Bosc del Castell de Bellver (Palma)

El bosc urbà escolta per excel·lència dels agrupaments de la ciutat de Palma.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-castell-de-bellver-bosc-palma" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_castell_de_bellver_bosc_palma() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_castell_de_bellver_bosc_palma, 200);
        return;
    }
    
    const trackPoints = [[39.563, 2.619]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-castell-de-bellver-bosc-palma');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Tomb pel Bosc del Castell de Bellver (Palma)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Tomb pel Bosc del Castell de Bellver (Palma)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.563, 2.619], 14);
        L.marker([39.563, 2.619]).addTo(rMap).bindPopup("<b>Tomb pel Bosc del Castell de Bellver (Palma)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_castell_de_bellver_bosc_palma);
setTimeout(initRouteTrackMap_castell_de_bellver_bosc_palma, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Palma** |
| **Zona / Comarca** | **Palma** |
| **Distància Total** | **4.2 km** |
| **Desnivell Positiu** | **+120 m** |
| **Dificultat Tècnica** | **Molt Fàcil** |
| **Durada Estimada** | **1h 30min** |
| **Unitats Recomanades** | **Castors/Fures, Llops/Daines** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Palma**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **EMT L46 / L4** (EMT Palma - Castell de Bellver) | Plaça d'Espanya, El Terreno, Castell de Bellver | [Consultar Horaris Oficials 🔗](https://www.emtpalma.cat/) |
| **SFM Línia T1** (Tren Palma - Inca (Raiguer)) | Palma (Estació Intermodal), Verge de Lluc, Pont d'Inca, Marratxí | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/tren/linia/T1) |
| **SFM Metro M1 / M2** (Metro de Palma (Palma - UIB / Marratxí)) | Palma Intermodal, Son Costa-Son Forteza, Son Sardina, UIB | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/metro/linia/M1) |
| **Ferrocarril de Sóller** (Tren de Fusta de Sóller (Palma - Bunyola - Sóller)) | Palma (Plaça d'Espanya), Son Sardina, Bunyola, Mirador des Pujol d'en Banya | [Consultar Horaris Oficials 🔗](http://trendesoller.com/) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Fonts públiques del Parc de Bellver
- **Passos per Finques Privades:** Parc Públic del Castell de Bellver
- **Punts d'Interès Cultural i Natural:** Castell circular de Bellver (s. XIV), Vistes a la badia de Palma

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Ideal per a eixides de dissabte horabaixa per a agrupaments de Palma.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)

> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.


### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Reina Constança de Mallorca** | Palma | **2.1 km** | [Veure Casal](../agrupaments/aeg-reina-constanca.md) |
| **AEG Ramon Llull** | Palma | **2.8 km** | [Veure Casal](../agrupaments/aeg-ramon-llull.md) |
