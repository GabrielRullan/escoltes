# 🏔️ Penya Rotja i Ermita de la Victòria (Alcúdia)

Niu d'àliga defensiu a la península de la Victòria d'Alcúdia.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-penya-rotja-alcudia" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_penya_rotja_alcudia() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_penya_rotja_alcudia, 200);
        return;
    }
    
    const trackPoints = [[39.871, 3.172]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-penya-rotja-alcudia');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Penya Rotja i Ermita de la Victòria (Alcúdia)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Penya Rotja i Ermita de la Victòria (Alcúdia)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.871, 3.172], 14);
        L.marker([39.871, 3.172]).addTo(rMap).bindPopup("<b>Penya Rotja i Ermita de la Victòria (Alcúdia)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_penya_rotja_alcudia);
setTimeout(initRouteTrackMap_penya_rotja_alcudia, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Alcúdia** |
| **Zona / Comarca** | **Raiguer** |
| **Distància Total** | **6.8 km** |
| **Desnivell Positiu** | **+310 m** |
| **Dificultat Tècnica** | **Moderada** |
| **Durada Estimada** | **2h 45min** |
| **Unitats Recomanades** | **Llops/Daines, Pioners/Rangers** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Alcúdia**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 302** (Can Picafort - Son Real - Alcúdia) | Can Picafort, Son Real, Alcúdia | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/302) |
| **TIB 334** (Alcúdia - Port de Pollença - Formentor) | Port de Pollença, Cala Murta, Far de Formentor | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/334) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Ermita de la Victòria
- **Passos per Finques Privades:** Finca pública de la Victòria
- **Punts d'Interès Cultural i Natural:** Antic canó de guaita de Penya Rotja, Ermita de la Victòria, Badia de Pollença

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Tram d'escala amb barana de seguretat.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Campament de la Victòria** | IBJOVE (Govern de les Illes Balears) | 200 pers. | **0.20 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/campament-la-victoria-alcudia.md) |
| **Refugi del Coll Baix** | IBANAT (Govern de les Illes Balears) | 6 pers. | **1.60 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/refugi-coll-baix-alcudia.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Sa Marjal** | Sa Pobla | **16.9 km** | [Veure Casal](../agrupaments/aeg-sa-marjal.md) |
| **AEG Pedra Viva** | Binissalem | **34.5 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |
