# 🏔️ Avenc de Son Pou (Coanegra / Santa Maria)

Excursió per la vall de Coanegra fins a la cova-avenc amb claraboia natural més gran de Mallorca.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-avenc-de-son-pou" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_avenc_de_son_pou() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_avenc_de_son_pou, 200);
        return;
    }
    
    const trackPoints = [[39.675, 2.768]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-avenc-de-son-pou');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Avenc de Son Pou (Coanegra / Santa Maria)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Avenc de Son Pou (Coanegra / Santa Maria)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.675, 2.768], 14);
        L.marker([39.675, 2.768]).addTo(rMap).bindPopup("<b>Avenc de Son Pou (Coanegra / Santa Maria)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_avenc_de_son_pou);
setTimeout(initRouteTrackMap_avenc_de_son_pou, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Santa Maria del Camí** |
| **Zona / Comarca** | **Raiguer** |
| **Distància Total** | **8.0 km** |
| **Desnivell Positiu** | **+180 m** |
| **Dificultat Tècnica** | **Fàcil - Moderada** |
| **Durada Estimada** | **2h 45min** |
| **Unitats Recomanades** | **Llops/Daines, Pioners/Rangers, Rovers/Rutes** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Avenc%20de%20Son%20Pou%20%28Coanegra%20/%20Santa%20Maria%29)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Santa Maria del Camí**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **SFM Línia T1** (Tren Palma - Inca (Raiguer)) | Palma (Estació Intermodal), Verge de Lluc, Pont d'Inca, Marratxí | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/tren/linia/T1) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Santa Maria del Camí
- **Passos per Finques Privades:** Finca de Son Pou
- **Punts d'Interès Cultural i Natural:** Cova monumental de Son Pou, Vall de Coanegra, Sínia de Son Pou

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Cal portar llanterna o frontal per entrar a la cova.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)

> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.

### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Ca Ses Monges** | **2.7 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/ca-ses-monges-santa-maria.md) |
| **Castell d'Alaró (Hostatgeria i Refugi)** | **3.7 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/castell-d-alaro-hostatgeria.md) |
| **S'Olivaret (Alaró)** | **4.3 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/solivaret-alaro.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Terra de Pous** | Santa Maria del Camí | **2.7 km** | [Veure Casal](../agrupaments/aeg-terra-de-pous.md) |
| **AEG Soca-Arrel** | Marratxí | **5.2 km** | [Veure Casal](../agrupaments/aeg-soca-arrel.md) |

---

## 💬 Experiències i Valoracions dels Agrupaments Escoltes

<div style="background-color: var(--md-code-bg-color, #f8f9fa); border: 1px solid #e0e0e0; padding: 18px; border-radius: 10px; margin-top: 16px;">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
        <div>
            <h3 style="margin: 0; font-size: 1.05em; color: #555;">Encara no hi ha cap experiència registrada per a aquesta ruta.</h3>
            <p style="margin: 4px 0 0 0; font-size: 0.85em; color: #666;">Heu fet aquesta ruta amb la vostra unitat? Sigueu els primers a deixar consells per a altres agrupaments!</p>
        </div>
        <a href="https://docs.google.com/forms/d/e/1FAIpQLScoutsMallorcaRutes/viewform" target="_blank" style="padding: 8px 16px; background-color: #00897b; color: white; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 0.85em;">📝 Enviar la primera experiència 🔗</a>
    </div>
</div>

