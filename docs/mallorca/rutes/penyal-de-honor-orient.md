# 🏔️ Orient a sa Coma de Santa Maria pel Pas de s'Escaleta

Connexió tradicional de muntanya entre la vall d'Orient i Santa Maria del Camí.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-penyal-de-honor-orient" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_penyal_de_honor_orient() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_penyal_de_honor_orient, 200);
        return;
    }
    
    const trackPoints = [[39.715, 2.785]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-penyal-de-honor-orient');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Orient a sa Coma de Santa Maria pel Pas de s'Escaleta");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Orient a sa Coma de Santa Maria pel Pas de s'Escaleta");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.715, 2.785], 14);
        L.marker([39.715, 2.785]).addTo(rMap).bindPopup("<b>Orient a sa Coma de Santa Maria pel Pas de s'Escaleta</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_penyal_de_honor_orient);
setTimeout(initRouteTrackMap_penyal_de_honor_orient, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Bunyola / Santa Maria** |
| **Zona / Comarca** | **Tramuntana Central** |
| **Distància Total** | **11.5 km** |
| **Desnivell Positiu** | **+390 m** |
| **Dificultat Tècnica** | **Moderada** |
| **Durada Estimada** | **4h 00min** |
| **Unitats Recomanades** | **Llops/Daines, Pioners/Rangers** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Orient%20a%20sa%20Coma%20de%20Santa%20Maria%20pel%20Pas%20de%20s%27Escaleta)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Bunyola / Santa Maria**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 205** (Palma - Bunyola - Orient) | Palma, Raixa, Bunyola, Orient | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/205) |
| **SFM Línia T1** (Tren Palma - Inca (Raiguer)) | Palma (Estació Intermodal), Verge de Lluc, Pont d'Inca, Marratxí | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/tren/linia/T1) |
| **Ferrocarril de Sóller** (Tren de Fusta de Sóller (Palma - Bunyola - Sóller)) | Palma (Plaça d'Espanya), Son Sardina, Bunyola, Mirador des Pujol d'en Banya | [Consultar Horaris Oficials 🔗](http://trendesoller.com/) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Orient, Santa Maria del Camí
- **Passos per Finques Privades:** Finca des Freu
- **Punts d'Interès Cultural i Natural:** Pas de s'Escaleta, Vall de Solleric

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Terreny humit a la tardor.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **S'Olivaret (Alaró)** | Gestió Privada | 40 pers. | **0.42 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/solivaret-alaro.md) |
| **Castell d'Alaró (Hostatgeria i Refugi)** | Fundació Castell d'Alaró / Consell | 30 pers. | **1.50 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/castell-d-alaro-hostatgeria.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Ca n'Arabí** | **5.5 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/ca-narabi-binissalem.md) |
| **Refugi de Tossals Verds** | **5.8 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-tossals-verds.md) |
| **Ca Ses Monges** | **7.2 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/ca-ses-monges-santa-maria.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Pedra Viva** | Binissalem | **5.5 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |
| **AEG Terra de Pous** | Santa Maria del Camí | **7.2 km** | [Veure Casal](../agrupaments/aeg-terra-de-pous.md) |

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

