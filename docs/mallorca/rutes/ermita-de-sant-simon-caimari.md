# 🏔️ Caimari al Coll de sa Batalla pel Camí Vell de Lluc

Subida tradicional des del poble de la oliva Caimari cap a les portes de Lluc.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-ermita-de-sant-simon-caimari" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_ermita_de_sant_simon_caimari() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_ermita_de_sant_simon_caimari, 200);
        return;
    }
    
    const trackPoints = [[39.778, 2.902]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-ermita-de-sant-simon-caimari');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Caimari al Coll de sa Batalla pel Camí Vell de Lluc");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Caimari al Coll de sa Batalla pel Camí Vell de Lluc");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.778, 2.902], 14);
        L.marker([39.778, 2.902]).addTo(rMap).bindPopup("<b>Caimari al Coll de sa Batalla pel Camí Vell de Lluc</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_ermita_de_sant_simon_caimari);
setTimeout(initRouteTrackMap_ermita_de_sant_simon_caimari, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Selva / Caimari** |
| **Zona / Comarca** | **Raiguer** |
| **Distància Total** | **7.8 km** |
| **Desnivell Positiu** | **+410 m** |
| **Dificultat Tècnica** | **Moderada** |
| **Durada Estimada** | **2h 45min** |
| **Unitats Recomanades** | **Llops/Daines, Pioners/Rangers** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Caimari%20al%20Coll%20de%20sa%20Batalla%20pel%20Cam%C3%AD%20Vell%20de%20Lluc)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Selva / Caimari**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 341** (Pollença - Lluc - Cúber - Port de Sóller (Línia Ma-10)) | Pollença, Lluc (Monestir), Binifaldó, Gorg Blau | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/341) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Caimari (poble), Coll de sa Batalla (benzineria/restaurants)
- **Passos per Finques Privades:** Camí Vell de Lluc
- **Punts d'Interès Cultural i Natural:** Cavall Bernat de Caimari, Costa de sa Polla, Forns de calç

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Camí empedrat ben conservat.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Comuna de Caimari** | Ajuntament de Selva | 40 pers. | **0.24 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/comuna-de-caimari.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Monestir de Santa Llúcia** | **4.3 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/monestir-santa-llucia-mancor.md) |
| **Àrea d'Acampada de Marjanor** | **4.9 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/marjanor-lluc.md) |
| **Refugi de Son Amer** | **5.0 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-son-amer.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Sa Marjal** | Sa Pobla | **10.5 km** | [Veure Casal](../agrupaments/aeg-sa-marjal.md) |
| **AEG Pedra Viva** | Binissalem | **10.9 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |

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

