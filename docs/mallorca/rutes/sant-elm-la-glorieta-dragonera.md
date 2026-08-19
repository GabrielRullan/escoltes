# 🏔️ Cala en Basset i Torre de sa Salve des de Sant Elm

Passejada litoral fins a la torre de defensa amb vistes a sa Dragonera.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-sant-elm-la-glorieta-dragonera" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_sant_elm_la_glorieta_dragonera() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_sant_elm_la_glorieta_dragonera, 200);
        return;
    }
    
    const trackPoints = [[39.581, 2.352]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-sant-elm-la-glorieta-dragonera');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Cala en Basset i Torre de sa Salve des de Sant Elm");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Cala en Basset i Torre de sa Salve des de Sant Elm");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.581, 2.352], 14);
        L.marker([39.581, 2.352]).addTo(rMap).bindPopup("<b>Cala en Basset i Torre de sa Salve des de Sant Elm</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_sant_elm_la_glorieta_dragonera);
setTimeout(initRouteTrackMap_sant_elm_la_glorieta_dragonera, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Andratx** |
| **Zona / Comarca** | **Tramuntana Sud** |
| **Distància Total** | **5.2 km** |
| **Desnivell Positiu** | **+140 m** |
| **Dificultat Tècnica** | **Fàcil** |
| **Durada Estimada** | **2h 00min** |
| **Unitats Recomanades** | **Castors/Fures, Llops/Daines** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Cala%20en%20Basset%20i%20Torre%20de%20sa%20Salve%20des%20de%20Sant%20Elm)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Andratx**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 101** (Palma - Andratx - Port d'Andratx) | Palma (Estació Intermodal), Andratx (Grava), Port d'Andratx | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/101) |
| **TIB 102** (Palma - Sant Elm) | Palma, Andratx, Sant Elm (Plaça de na Caragola) | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/102) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Sant Elm
- **Passos per Finques Privades:** Camí de sa Torre
- **Punts d'Interès Cultural i Natural:** Torre de Cala en Basset (s. XVI), Vistes a la Dragonera

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Molt assequible per a Castors i Llops.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **La Trapa (Zona d'Acampada)** | GOB Mallorca | 25 pers. | **1.96 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/la-trapa-andratx.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Refugi de Ses Fontanelles** | **4.5 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/ses-fontanelles-sant-elm.md) |
| **Refugi de la Finca Pública de Galatzó** | **9.8 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/finca-de-galatzo-refugi.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Reina Constança de Mallorca** | Palma | **24.8 km** | [Veure Casal](../agrupaments/aeg-reina-constanca.md) |
| **AEG Ramon Llull** | Palma | **25.6 km** | [Veure Casal](../agrupaments/aeg-ramon-llull.md) |

---

## 💬 Experiències i Valoracions dels Agrupaments Escoltes

<div style="background-color: var(--md-code-bg-color, #f8f9fa); border: 1px solid #e0e0e0; padding: 18px; border-radius: 10px; margin-top: 16px;">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
        <div>
            <h3 style="margin: 0; font-size: 1.05em; color: #555;">Encara no hi ha cap experiència registrada per a aquesta ruta.</h3>
            <p style="margin: 4px 0 0 0; font-size: 0.85em; color: #666;">Heu fet aquesta ruta amb la vostra unitat? Sigueu els primers a deixar consells per a altres agrupaments!</p>
        </div>
        <a href="../../sop/enviar_experiencia/" style="padding: 8px 16px; background-color: #00897b; color: white; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 0.85em;">📝 Enviar la primera experiència 🔗</a>
    </div>
</div>

