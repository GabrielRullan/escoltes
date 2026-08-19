# 🏔️ Ruta Litoral de la Finca Pública de Son Real

Ruta arqueològica verge vora mar a la badia d'Alcúdia.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-son-real-can-picafort" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_son_real_can_picafort() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_son_real_can_picafort, 200);
        return;
    }
    
    const trackPoints = [[39.751, 3.19]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-son-real-can-picafort');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Ruta Litoral de la Finca Pública de Son Real");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Ruta Litoral de la Finca Pública de Son Real");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.751, 3.19], 14);
        L.marker([39.751, 3.19]).addTo(rMap).bindPopup("<b>Ruta Litoral de la Finca Pública de Son Real</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_son_real_can_picafort);
setTimeout(initRouteTrackMap_son_real_can_picafort, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Santa Margalida** |
| **Zona / Comarca** | **Pla de Mallorca** |
| **Distància Total** | **8.5 km** |
| **Desnivell Positiu** | **+25 m** |
| **Dificultat Tècnica** | **Molt Fàcil** |
| **Durada Estimada** | **2h 30min** |
| **Unitats Recomanades** | **Castors/Fures, Llops/Daines, Pioners/Rangers** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Ruta%20Litoral%20de%20la%20Finca%20P%C3%BAblica%20de%20Son%20Real)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Santa Margalida**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 302** (Can Picafort - Son Real - Alcúdia) | Can Picafort, Son Real, Alcúdia | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/302) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Cases de Son Real (centre d'interpretació)
- **Passos per Finques Privades:** Finca Pública de Son Real (Govern Balear)
- **Punts d'Interès Cultural i Natural:** Necròpolis talaiòtica de Son Real, Illa des Porros, Torres de defensa

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Ruta ideal per a senderisme arqueològic i Castors/Llops.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Son Real (Refugi i Cases)** | IBANAT (Govern de les Illes Balears) | 12 pers. | **0.00 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/son-real-refugi-ibanat.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **S'Hort de Son Serra** | **6.8 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/short-de-son-serra.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Sa Marjal** | Sa Pobla | **14.3 km** | [Veure Casal](../agrupaments/aeg-sa-marjal.md) |
| **AEG Pedra Viva** | Binissalem | **30.5 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |

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

