# 🏔️ Puig de Consolació (Santanyí / s'Alqueria Blanca)

Petit puig d'accés fàcil al sud de Mallorca amb panoràmiques marines.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-sanctuari-de-consolacio-santanyi" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_sanctuari_de_consolacio_santanyi() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_sanctuari_de_consolacio_santanyi, 200);
        return;
    }
    
    const trackPoints = [[39.378, 3.162]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-sanctuari-de-consolacio-santanyi');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Puig de Consolació (Santanyí / s'Alqueria Blanca)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Puig de Consolació (Santanyí / s'Alqueria Blanca)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.378, 3.162], 14);
        L.marker([39.378, 3.162]).addTo(rMap).bindPopup("<b>Puig de Consolació (Santanyí / s'Alqueria Blanca)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_sanctuari_de_consolacio_santanyi);
setTimeout(initRouteTrackMap_sanctuari_de_consolacio_santanyi, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Santanyí** |
| **Zona / Comarca** | **Migjorn** |
| **Distància Total** | **3.5 km** |
| **Desnivell Positiu** | **+110 m** |
| **Dificultat Tècnica** | **Molt Fàcil** |
| **Durada Estimada** | **1h 15min** |
| **Unitats Recomanades** | **Castors/Fures, Llops/Daines** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Puig%20de%20Consolaci%C3%B3%20%28Santany%C3%AD%20/%20s%27Alqueria%20Blanca%29)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Santanyí**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 517** (Campos - Santanyí - Cala Mondragó) | Campos, Santanyí, s'Amarador, Cala Mondragó | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/517) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** S'Alqueria Blanca, Santuari de Consolació
- **Passos per Finques Privades:** Camí des Santuari
- **Punts d'Interès Cultural i Natural:** Santuari de Consolació (s. XVI), Vistes al Parc Natural de Mondragó i Cabrera

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Ruta molt accessible.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)

> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.


### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **Grupo Scout Myotragus 684** | Llucmajor | **37.7 km** | [Veure Casal](../agrupaments/gs-myotragus-684.md) |
| **AEG Pedra Viva** | Binissalem | **44.4 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |

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

