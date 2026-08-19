# 🏔️ Coll de sa Gramola al Puig de sa Monja (Andratx)

Mirador excepcional sobre els penya-segats del mar d'Andratx.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-coll-de-sa-gramola-ses-basses" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_coll_de_sa_gramola_ses_basses() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_coll_de_sa_gramola_ses_basses, 200);
        return;
    }
    
    const trackPoints = [[39.611, 2.395]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-coll-de-sa-gramola-ses-basses');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Coll de sa Gramola al Puig de sa Monja (Andratx)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Coll de sa Gramola al Puig de sa Monja (Andratx)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.611, 2.395], 14);
        L.marker([39.611, 2.395]).addTo(rMap).bindPopup("<b>Coll de sa Gramola al Puig de sa Monja (Andratx)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_coll_de_sa_gramola_ses_basses);
setTimeout(initRouteTrackMap_coll_de_sa_gramola_ses_basses, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Andratx** |
| **Zona / Comarca** | **Tramuntana Sud** |
| **Distància Total** | **7.5 km** |
| **Desnivell Positiu** | **+280 m** |
| **Dificultat Tècnica** | **Moderada** |
| **Durada Estimada** | **2h 45min** |
| **Unitats Recomanades** | **Llops/Daines, Pioners/Rangers** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Coll%20de%20sa%20Gramola%20al%20Puig%20de%20sa%20Monja%20%28Andratx%29)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Andratx**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 101** (Palma - Andratx - Port d'Andratx) | Palma (Estació Intermodal), Andratx (Grava), Port d'Andratx | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/101) |
| **TIB 102** (Palma - Sant Elm) | Palma, Andratx, Sant Elm (Plaça de na Caragola) | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/102) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Sense punts d'aigua
- **Passos per Finques Privades:** Finca de sa Gramola
- **Punts d'Interès Cultural i Natural:** Vistes a sa Dragonera i els penya-segats de la costa sud-oest

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Portar aigua suficient.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Refugi de Ses Fontanelles** | Gestió Privada / GR-221 | 16 pers. | **0.48 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/ses-fontanelles-sant-elm.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **La Trapa (Zona d'Acampada)** | **3.5 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/la-trapa-andratx.md) |
| **Refugi de la Finca Pública de Galatzó** | **5.8 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/finca-de-galatzo-refugi.md) |
| **Refugi de Sa Coma d'en Vidal** | **6.0 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/sa-coma-den-vidal.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Reina Constança de Mallorca** | Palma | **21.5 km** | [Veure Casal](../agrupaments/aeg-reina-constanca.md) |
| **AEG Son Sardina** | Palma | **22.0 km** | [Veure Casal](../agrupaments/aeg-son-sardina.md) |
