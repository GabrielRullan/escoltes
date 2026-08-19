# 🏔️ Parc Natural de sa Dragonera (Cala Lledó - Far Vell)

Ruta insular de protecció biològica i vistes espectaculars a la costa de ponent.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-parc-natural-dragonera" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_parc_natural_dragonera() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_parc_natural_dragonera, 200);
        return;
    }
    
    const trackPoints = [[39.584, 2.318]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-parc-natural-dragonera');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Parc Natural de sa Dragonera (Cala Lledó - Far Vell)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Parc Natural de sa Dragonera (Cala Lledó - Far Vell)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.584, 2.318], 14);
        L.marker([39.584, 2.318]).addTo(rMap).bindPopup("<b>Parc Natural de sa Dragonera (Cala Lledó - Far Vell)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_parc_natural_dragonera);
setTimeout(initRouteTrackMap_parc_natural_dragonera, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Andratx** |
| **Zona / Comarca** | **Tramuntana Sud** |
| **Distància Total** | **7.4 km** |
| **Desnivell Positiu** | **+350 m** |
| **Dificultat Tècnica** | **Moderada** |
| **Durada Estimada** | **3h 00min** |
| **Unitats Recomanades** | **Llops/Daines, Pioners/Rangers, Rovers/Rutes** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Parc%20Natural%20de%20sa%20Dragonera%20%28Cala%20Lled%C3%B3%20-%20Far%20Vell%29)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Andratx**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 101** (Palma - Andratx - Port d'Andratx) | Palma (Estació Intermodal), Andratx (Grava), Port d'Andratx | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/101) |
| **TIB 102** (Palma - Sant Elm) | Palma, Andratx, Sant Elm (Plaça de na Caragola) | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/102) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Centre de visitants de Cala Lledó
- **Passos per Finques Privades:** Illa de sa Dragonera (Consell de Mallorca)
- **Punts d'Interès Cultural i Natural:** Far Vell de Na Popia, Sargantanes de Dragonera (Podarcis lilfordi), Cala Lledó

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Cal agafar la barca des de Sant Elm. Sense ombra a la pujada del far.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)

> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.

### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **La Trapa (Zona d'Acampada)** | **3.8 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/la-trapa-andratx.md) |
| **Refugi de Ses Fontanelles** | **6.8 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/ses-fontanelles-sant-elm.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Reina Constança de Mallorca** | Palma | **27.7 km** | [Veure Casal](../agrupaments/aeg-reina-constanca.md) |
| **AEG Ramon Llull** | Palma | **28.5 km** | [Veure Casal](../agrupaments/aeg-ramon-llull.md) |
