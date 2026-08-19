# 🏔️ Camí de ses Voltes d'en Galileu (Lluc)

Ruta patrimonial que remunta les voltes empedrades cap a les antigues cases de neu de la Tramuntana.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-cami-de-ses-voltes-galileu" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_cami_de_ses_voltes_galileu() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_cami_de_ses_voltes_galileu, 200);
        return;
    }
    
    const trackPoints = [[39.814, 2.875]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-cami-de-ses-voltes-galileu');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Camí de ses Voltes d'en Galileu (Lluc)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Camí de ses Voltes d'en Galileu (Lluc)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.814, 2.875], 14);
        L.marker([39.814, 2.875]).addTo(rMap).bindPopup("<b>Camí de ses Voltes d'en Galileu (Lluc)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_cami_de_ses_voltes_galileu);
setTimeout(initRouteTrackMap_cami_de_ses_voltes_galileu, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Escorca** |
| **Zona / Comarca** | **Tramuntana Nord** |
| **Distància Total** | **9.4 km** |
| **Desnivell Positiu** | **+580 m** |
| **Dificultat Tècnica** | **Moderada - Exigent** |
| **Durada Estimada** | **3h 45min** |
| **Unitats Recomanades** | **Pioners/Rangers, Rovers/Rutes** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Cam%C3%AD%20de%20ses%20Voltes%20d%27en%20Galileu%20%28Lluc%29)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Escorca**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 341** (Pollença - Lluc - Cúber - Port de Sóller (Línia Ma-10)) | Pollença, Lluc (Monestir), Binifaldó, Gorg Blau | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/341) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Son Amer / Lluc
- **Passos per Finques Privades:** Son Massip
- **Punts d'Interès Cultural i Natural:** Cases de Neu d'en Galileu, Ses Voltes empedrades, Vistes a la serra

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Camí en ziga-zaga empedrat. Calçat de muntanya fort necessari.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Àrea d'Acampada de Sa Font Coberta** | IBANAT (Govern de les Illes Balears) | 150 pers. | **1.31 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/sa-font-coberta-lluc.md) |
| **Refugi de Son Amer** | Consell de Mallorca (Xarxa GR-221) | 52 pers. | **1.33 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/refugi-son-amer.md) |
| **Àrea d'Acampada de Marjanor** | IBANAT (Govern de les Illes Balears) | 60 pers. | **1.43 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/marjanor-lluc.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Àrea d'Acampada des Pixarells** | **2.2 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/es-pixarells-lluc.md) |
| **Cases de Binifaldó (Refugi IBANAT)** | **2.8 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/cases-de-binifaldo.md) |
| **Comuna de Caimari** | **4.9 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/comuna-de-caimari.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Sa Marjal** | Sa Pobla | **13.7 km** | [Veure Casal](../agrupaments/aeg-sa-marjal.md) |
| **AEG Pedra Viva** | Binissalem | **13.9 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |

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

