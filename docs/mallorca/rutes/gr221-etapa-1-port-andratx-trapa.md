# 🏔️ GR-221 Etapa 1: Port d'Andratx a La Trapa

Primer tram de la Ruta de Pedra en Sec GR-221 que voreja els penya-segats del sud-oest de Mallorca des del Port d'Andratx fins a l'antic monestir trapenc de la Trapa.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-gr221-etapa-1-port-andratx-trapa" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_gr221_etapa_1_port_andratx_trapa() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_gr221_etapa_1_port_andratx_trapa, 200);
        return;
    }
    
    const trackPoints = [[39.544, 2.38], [39.561, 2.369], [39.578, 2.361], [39.598, 2.358]];
    const itinerariPassos = [{"pas": 1, "nom": "Inici al Port d'Andratx", "desc": "Sortida des de la zona del port cap al camí del Coll des Pal."}, {"pas": 2, "nom": "Ascens al Coll des Pal", "desc": "Punyada de pujada per sender de pedra amb vistes a la badia d'Andratx."}, {"pas": 3, "nom": "Cala en Basset i Mirador", "desc": "Desviament cap al mirador de sa Dragonera i de la torre de Cala en Basset."}, {"pas": 4, "nom": "Arribada a la Trapa", "desc": "Descens cap a les cases i marjades del monestir de la Trapa."}];
    
    const rMap = L.map('map-route-gr221-etapa-1-port-andratx-trapa');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> GR-221 Etapa 1: Port d'Andratx a La Trapa");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> GR-221 Etapa 1: Port d'Andratx a La Trapa");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.544, 2.38], 14);
        L.marker([39.544, 2.38]).addTo(rMap).bindPopup("<b>GR-221 Etapa 1: Port d'Andratx a La Trapa</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_gr221_etapa_1_port_andratx_trapa);
setTimeout(initRouteTrackMap_gr221_etapa_1_port_andratx_trapa, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Andratx** |
| **Zona / Comarca** | **Tramuntana Sud** |
| **Distància Total** | **11.8 km** |
| **Desnivell Positiu** | **+480 m** |
| **Dificultat Tècnica** | **Moderada** |
| **Durada Estimada** | **4h 30min** |
| **Unitats Recomanades** | **Pioners/Rangers, Rovers/Rutes** |

---

## 🥾 Itinerari i Rumb de la Ruta Pas a Pas

| Pas | Punt de Referència / Tram | Indicacions i Descripció |
| :---: | :--- | :--- |
| **Pas 1** | **Inici al Port d'Andratx** | Sortida des de la zona del port cap al camí del Coll des Pal. |
| **Pas 2** | **Ascens al Coll des Pal** | Punyada de pujada per sender de pedra amb vistes a la badia d'Andratx. |
| **Pas 3** | **Cala en Basset i Mirador** | Desviament cap al mirador de sa Dragonera i de la torre de Cala en Basset. |
| **Pas 4** | **Arribada a la Trapa** | Descens cap a les cases i marjades del monestir de la Trapa. |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Andratx**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 101** (Palma - Andratx - Port d'Andratx) | Palma (Estació Intermodal), Andratx (Grava), Port d'Andratx | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/101) |
| **TIB 102** (Palma - Sant Elm) | Palma, Andratx, Sant Elm (Plaça de na Caragola) | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/102) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Port d'Andratx (abans de sortir), Sant Elm
- **Passos per Finques Privades:** Pas de sa Gramola (camí públic), Coll des Pal (obert)
- **Punts d'Interès Cultural i Natural:** Coll des Pal, Cala en Basset, Monestir de la Trapa, Vistes a sa Dragonera

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Tram sense ombra a la primera meitat. Evitar hores centrals de sol a l'estiu.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)

> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.

### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **La Trapa (Zona d'Acampada)** | **6.3 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/la-trapa-andratx.md) |
| **Refugi de Ses Fontanelles** | **7.2 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/ses-fontanelles-sant-elm.md) |
| **Refugi de la Finca Pública de Galatzó** | **9.8 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/finca-de-galatzo-refugi.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Reina Constança de Mallorca** | Palma | **22.6 km** | [Veure Casal](../agrupaments/aeg-reina-constanca.md) |
| **AEG Ramon Llull** | Palma | **23.3 km** | [Veure Casal](../agrupaments/aeg-ramon-llull.md) |
