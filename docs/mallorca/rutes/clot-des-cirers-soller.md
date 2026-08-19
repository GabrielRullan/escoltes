# 🏔️ Clot des Cirers des del Port de Sóller

Vall secreta d'oliveres i maquis sobre el Port de Sóller.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-clot-des-cirers-soller" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_clot_des_cirers_soller() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_clot_des_cirers_soller, 200);
        return;
    }
    
    const trackPoints = [[39.789, 2.695]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-clot-des-cirers-soller');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Clot des Cirers des del Port de Sóller");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Clot des Cirers des del Port de Sóller");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.789, 2.695], 14);
        L.marker([39.789, 2.695]).addTo(rMap).bindPopup("<b>Clot des Cirers des del Port de Sóller</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_clot_des_cirers_soller);
setTimeout(initRouteTrackMap_clot_des_cirers_soller, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Sóller** |
| **Zona / Comarca** | **Tramuntana Central** |
| **Distància Total** | **9.8 km** |
| **Desnivell Positiu** | **+480 m** |
| **Dificultat Tècnica** | **Moderada** |
| **Durada Estimada** | **3h 45min** |
| **Unitats Recomanades** | **Llops/Daines, Pioners/Rangers** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Clot%20des%20Cirers%20des%20del%20Port%20de%20S%C3%B3ller)** |

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

- **Punts d'Aigua Potable / Recàrrega:** Port de Sóller, Muleta
- **Passos per Finques Privades:** Finca de sa Figuera
- **Punts d'Interès Cultural i Natural:** Vall amagada del Clot des Cirers, Oliveres mil·lenàries

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Respectar la tranquil·litat de les finques agràries.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Refugi de Muleta** | Consell de Mallorca (Xarxa GR-221) | 30 pers. | **0.90 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/refugi-muleta.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Sant Ramon de Penyafort** | **2.9 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/sant-ramon-de-penyafort-soller.md) |
| **Refugi de Can Boi** | **6.0 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-can-boi.md) |
| **Refugi de Cúber** | **8.3 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-cuber.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Capità Angelats** | Sóller | **3.1 km** | [Veure Casal](../agrupaments/aeg-capita-angelats.md) |
| **AEG Nuredduna** | Bunyola / Palmanyola | **14.4 km** | [Veure Casal](../agrupaments/aeg-nuredduna.md) |

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

