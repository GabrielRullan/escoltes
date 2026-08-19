# 🏔️ Castell de Santueri (Felanitx)

Imponent castell roquer edificat sobre restes romanes i musulmanes a Felanitx.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-castell-de-santueri-felanitx" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_castell_de_santueri_felanitx() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_castell_de_santueri_felanitx, 200);
        return;
    }
    
    const trackPoints = [[39.442, 3.188]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-castell-de-santueri-felanitx');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Castell de Santueri (Felanitx)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Castell de Santueri (Felanitx)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.442, 3.188], 14);
        L.marker([39.442, 3.188]).addTo(rMap).bindPopup("<b>Castell de Santueri (Felanitx)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_castell_de_santueri_felanitx);
setTimeout(initRouteTrackMap_castell_de_santueri_felanitx, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Felanitx** |
| **Zona / Comarca** | **Migjorn** |
| **Distància Total** | **6.0 km** |
| **Desnivell Positiu** | **+320 m** |
| **Dificultat Tècnica** | **Fàcil - Moderada** |
| **Durada Estimada** | **2h 15min** |
| **Unitats Recomanades** | **Castors/Fures, Llops/Daines, Pioners/Rangers** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Felanitx**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 501** (Palma - Llucmajor - Campos - Felanitx) | Palma, Llucmajor, Campos, Felanitx | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/501) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Aparcament del Castell
- **Passos per Finques Privades:** Camí de Santueri
- **Punts d'Interès Cultural i Natural:** Fortalesa roquera del segle XIV, Vistes a la costa de Santanyí

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Comprovar horaris de visites del castell.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)

> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.


### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **Grupo Scout Myotragus 684** | Llucmajor | **37.9 km** | [Veure Casal](../agrupaments/gs-myotragus-684.md) |
| **AEG Sa Marjal** | Sa Pobla | **39.0 km** | [Veure Casal](../agrupaments/aeg-sa-marjal.md) |
