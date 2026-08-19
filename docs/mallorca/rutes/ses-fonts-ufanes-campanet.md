# 🏔️ Ses Fonts Ufanes (Campanet)

Ruta circular plana per la finca pública de Gabellí Petit per admirar l'únic fenomen hidrogeològic de les Fonts Ufanes quan l'aigua brota de l'alzinar.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-ses-fonts-ufanes-campanet" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_ses_fonts_ufanes_campanet() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_ses_fonts_ufanes_campanet, 200);
        return;
    }
    
    const trackPoints = [[39.789, 2.964], [39.792, 2.968], [39.795, 2.971]];
    const itinerariPassos = [{"pas": 1, "nom": "Ermita de Sant Miquel", "desc": "Inici a la fita d'entrada de la finca Gabellí Petit."}, {"pas": 2, "nom": "Camí de l'Alzinar", "desc": "Passejada adapada per a totes les edats."}, {"pas": 3, "nom": "Brollador de les Ufanes", "desc": "Punt on l'aigua s'anega entre els arbres en dies de pluja."}];
    
    const rMap = L.map('map-route-ses-fonts-ufanes-campanet');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Ses Fonts Ufanes (Campanet)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Ses Fonts Ufanes (Campanet)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.789, 2.964], 14);
        L.marker([39.789, 2.964]).addTo(rMap).bindPopup("<b>Ses Fonts Ufanes (Campanet)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_ses_fonts_ufanes_campanet);
setTimeout(initRouteTrackMap_ses_fonts_ufanes_campanet, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Campanet** |
| **Zona / Comarca** | **Raiguer** |
| **Distància Total** | **3.8 km** |
| **Desnivell Positiu** | **+60 m** |
| **Dificultat Tècnica** | **Molt Fàcil** |
| **Durada Estimada** | **1h 15min** |
| **Unitats Recomanades** | **Castors/Fures, Llops/Daines, Pioners/Rangers, Rovers/Rutes** |

---

## 🥾 Itinerari i Rumb de la Ruta Pas a Pas

| Pas | Punt de Referència / Tram | Indicacions i Descripció |
| :---: | :--- | :--- |
| **Pas 1** | **Ermita de Sant Miquel** | Inici a la fita d'entrada de la finca Gabellí Petit. |
| **Pas 2** | **Camí de l'Alzinar** | Passejada adapada per a totes les edats. |
| **Pas 3** | **Brollador de les Ufanes** | Punt on l'aigua s'anega entre els arbres en dies de pluja. |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Campanet**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 312** (Sa Pobla - Campanet - Inca) | Inca, Campanet, Sa Pobla | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/312) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Centre de Visitors de Gabellí Petit
- **Passos per Finques Privades:** Finca Pública de Gabellí Petit (Govern)
- **Punts d'Interès Cultural i Natural:** Fenomen hidrogeològic de les Fonts Ufanes, Ermita de Sant Miquel, Alzinar de Gabellí

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Ideal després d'episodis de pluja intensa per veure brotar l'aigua del terra.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)

> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.

### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Crestatx (Ermita i Terreny)** | **4.7 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/crestatx-sa-pobla.md) |
| **Comuna de Caimari** | **5.4 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/comuna-de-caimari.md) |
| **Cases de Binifaldó (Refugi IBANAT)** | **7.3 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/cases-de-binifaldo.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Sa Marjal** | Sa Pobla | **5.6 km** | [Veure Casal](../agrupaments/aeg-sa-marjal.md) |
| **AEG Pedra Viva** | Binissalem | **15.0 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |
