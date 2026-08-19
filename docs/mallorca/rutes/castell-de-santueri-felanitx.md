# 🏔️ Castell de Santueri (Felanitx)

Imponent castell roquer edificat sobre restes romanes i musulmanes a Felanitx.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-castell-de-santueri-felanitx" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_castell_de_santueri_felanitx() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_castell_de_santueri_felanitx, 200);
        return;
    }
    
    const trackPoints = [[39.442, 3.188]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-castell-de-santueri-felanitx');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Castell de Santueri (Felanitx)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Castell de Santueri (Felanitx)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.442, 3.188], 14);
        L.marker([39.442, 3.188]).addTo(rMap).bindPopup("<b>Castell de Santueri (Felanitx)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_castell_de_santueri_felanitx);
setTimeout(initRouteTrackMap_castell_de_santueri_felanitx, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Felanitx** |
| **Zona / Comarca** | **Migjorn** |
| **Distància Total** | **6.0 km** |
| **Desnivell Positiu** | **+320 m** |
| **Dificultat Tècnica** | **Fàcil - Moderada** |
| **Durada Estimada** | **2h 15min** |
| **Unitats Recomanades** | **Castors/Fures, Llops/Daines, Pioners/Rangers** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Castell%20de%20Santueri%20%28Felanitx%29)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Felanitx**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 501** (Palma - Llucmajor - Campos - Felanitx) | Palma, Llucmajor, Campos, Felanitx | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/501) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Aparcament del Castell
- **Passos per Finques Privades:** Camí de Santueri
- **Punts d'Interès Cultural i Natural:** Fortalesa roquera del segle XIV, Vistes a la costa de Santanyí

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Comprovar horaris de visites del castell.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)

> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.


### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **Grupo Scout Myotragus 684** | Llucmajor | **37.9 km** | [Veure Casal](../agrupaments/gs-myotragus-684.md) |
| **AEG Sa Marjal** | Sa Pobla | **39.0 km** | [Veure Casal](../agrupaments/aeg-sa-marjal.md) |

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

