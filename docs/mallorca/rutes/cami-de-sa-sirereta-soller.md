# 🏔️ Camí de sa Sirereta i Cova de ses Albellons (Sóller)

Itinerari pels horts tradicionals de citrics i oli de la vall de Sóller.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-cami-de-sa-sirereta-soller" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_cami_de_sa_sirereta_soller() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_cami_de_sa_sirereta_soller, 200);
        return;
    }
    
    const trackPoints = [[39.769, 2.718]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-cami-de-sa-sirereta-soller');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Camí de sa Sirereta i Cova de ses Albellons (Sóller)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Camí de sa Sirereta i Cova de ses Albellons (Sóller)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.769, 2.718], 14);
        L.marker([39.769, 2.718]).addTo(rMap).bindPopup("<b>Camí de sa Sirereta i Cova de ses Albellons (Sóller)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_cami_de_sa_sirereta_soller);
setTimeout(initRouteTrackMap_cami_de_sa_sirereta_soller, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Sóller** |
| **Zona / Comarca** | **Tramuntana Central** |
| **Distància Total** | **7.2 km** |
| **Desnivell Positiu** | **+310 m** |
| **Dificultat Tècnica** | **Moderada** |
| **Durada Estimada** | **2h 45min** |
| **Unitats Recomanades** | **Llops/Daines, Pioners/Rangers** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Cam%C3%AD%20de%20sa%20Sirereta%20i%20Cova%20de%20ses%20Albellons%20%28S%C3%B3ller%29)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Sóller**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 203** (Palma - Valldemossa - Deià - Sóller) | Palma, Valldemossa, Son Marroig, Deià | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/203) |
| **TIB 204** (Palma - Sóller - Port de Sóller (Express Túnel)) | Palma (Estació Intermodal), Sóller (Ma-11), Port de Sóller | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/204) |
| **TIB 341** (Pollença - Lluc - Cúber - Port de Sóller (Línia Ma-10)) | Pollença, Lluc (Monestir), Binifaldó, Gorg Blau | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/341) |
| **Ferrocarril de Sóller** (Tren de Fusta de Sóller (Palma - Bunyola - Sóller)) | Palma (Plaça d'Espanya), Son Sardina, Bunyola, Mirador des Pujol d'en Banya | [Consultar Horaris Oficials 🔗](http://trendesoller.com/) |
| **Tramvia de Sóller** (Tranvia Històric de Sóller (Sóller Vila - Port de Sóller)) | Sóller Estació, Mercat de Sóller, Es Control, Sa Torre | [Consultar Horaris Oficials 🔗](http://trendesoller.com/tramvia/) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Sóller poble
- **Passos per Finques Privades:** Horta de Sóller
- **Punts d'Interès Cultural i Natural:** Horta de tarongers de Sóller, Mirador de ses Paises

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Camí molt agradable per a la tardor i la primavera.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Sant Ramon de Penyafort** | Cristians Vall de Sóller | 45 pers. | **0.28 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/sant-ramon-de-penyafort-soller.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Refugi de Muleta** | **3.9 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-muleta.md) |
| **Refugi de Can Boi** | **6.4 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-can-boi.md) |
| **Refugi de Cúber** | **6.4 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-cuber.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Capità Angelats** | Sóller | **0.4 km** | [Veure Casal](../agrupaments/aeg-capita-angelats.md) |
| **AEG Nuredduna** | Bunyola / Palmanyola | **12.3 km** | [Veure Casal](../agrupaments/aeg-nuredduna.md) |

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

