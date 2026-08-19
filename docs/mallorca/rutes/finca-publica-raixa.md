# 🏔️ Tomb per la Finca Pública de Raixa

Possessió senyorial emblemàtica als peus de Bunyola amb jardins monumentals.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-finca-publica-raixa" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_finca_publica_raixa() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_finca_publica_raixa, 200);
        return;
    }
    
    const trackPoints = [[39.648, 2.672]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-finca-publica-raixa');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Tomb per la Finca Pública de Raixa");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Tomb per la Finca Pública de Raixa");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.648, 2.672], 14);
        L.marker([39.648, 2.672]).addTo(rMap).bindPopup("<b>Tomb per la Finca Pública de Raixa</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_finca_publica_raixa);
setTimeout(initRouteTrackMap_finca_publica_raixa, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Bunyola** |
| **Zona / Comarca** | **Tramuntana Central** |
| **Distància Total** | **3.0 km** |
| **Desnivell Positiu** | **+110 m** |
| **Dificultat Tècnica** | **Fàcil** |
| **Durada Estimada** | **1h 15min** |
| **Unitats Recomanades** | **Castors/Fures, Llops/Daines** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Tomb%20per%20la%20Finca%20P%C3%BAblica%20de%20Raixa)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Bunyola**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 205** (Palma - Bunyola - Orient) | Palma, Raixa, Bunyola, Orient | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/205) |
| **Ferrocarril de Sóller** (Tren de Fusta de Sóller (Palma - Bunyola - Sóller)) | Palma (Plaça d'Espanya), Son Sardina, Bunyola, Mirador des Pujol d'en Banya | [Consultar Horaris Oficials 🔗](http://trendesoller.com/) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Centre d'interpretació de Raixa
- **Passos per Finques Privades:** Finca Pública de Raixa (Consell de Mallorca)
- **Punts d'Interès Cultural i Natural:** Jardins històrics, Escalinata del déu Apol·lo, Gran Safareig

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Comprovar horaris d'obertura de la finca abans d'anar-hi.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)

> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.

### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Binicanella (Casa de Colònies)** | **5.8 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/binicanella-bunyola.md) |
| **Refugi de Son Moragues** | **8.3 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-son-moragues.md) |
| **Ca Ses Monges** | **8.6 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/ca-ses-monges-santa-maria.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Nuredduna** | Bunyola / Palmanyola | **2.6 km** | [Veure Casal](../agrupaments/aeg-nuredduna.md) |
| **AEG Son Sardina** | Palma | **4.0 km** | [Veure Casal](../agrupaments/aeg-son-sardina.md) |
