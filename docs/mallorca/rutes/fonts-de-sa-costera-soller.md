# 🏔️ Ruta de les Fonts de sa Costera (Sóller - Cala Tuent)

Una de les rutes litorals més maragda i majestuoses de la costa nord de Mallorca.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-fonts-de-sa-costera-soller" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_fonts_de_sa_costera_soller() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_fonts_de_sa_costera_soller, 200);
        return;
    }
    
    const trackPoints = [[39.785, 2.735]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-fonts-de-sa-costera-soller');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Ruta de les Fonts de sa Costera (Sóller - Cala Tuent)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Ruta de les Fonts de sa Costera (Sóller - Cala Tuent)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.785, 2.735], 14);
        L.marker([39.785, 2.735]).addTo(rMap).bindPopup("<b>Ruta de les Fonts de sa Costera (Sóller - Cala Tuent)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_fonts_de_sa_costera_soller);
setTimeout(initRouteTrackMap_fonts_de_sa_costera_soller, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Sóller / Escorca** |
| **Zona / Comarca** | **Tramuntana Central** |
| **Distància Total** | **12.0 km** |
| **Desnivell Positiu** | **+380 m** |
| **Dificultat Tècnica** | **Moderada** |
| **Durada Estimada** | **4h 00min** |
| **Unitats Recomanades** | **Pioners/Rangers, Rovers/Rutes** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Ruta%20de%20les%20Fonts%20de%20sa%20Costera%20%28S%C3%B3ller%20-%20Cala%20Tuent%29)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Sóller / Escorca**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 203** (Palma - Valldemossa - Deià - Sóller) | Palma, Valldemossa, Son Marroig, Deià | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/203) |
| **TIB 204** (Palma - Sóller - Port de Sóller (Express Túnel)) | Palma (Estació Intermodal), Sóller (Ma-11), Port de Sóller | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/204) |
| **TIB 341** (Pollença - Lluc - Cúber - Port de Sóller (Línia Ma-10)) | Pollença, Lluc (Monestir), Binifaldó, Gorg Blau | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/341) |
| **Ferrocarril de Sóller** (Tren de Fusta de Sóller (Palma - Bunyola - Sóller)) | Palma (Plaça d'Espanya), Son Sardina, Bunyola, Mirador des Pujol d'en Banya | [Consultar Horaris Oficials 🔗](http://trendesoller.com/) |
| **Tramvia de Sóller** (Tranvia Històric de Sóller (Sóller Vila - Port de Sóller)) | Sóller Estació, Mercat de Sóller, Es Control, Sa Torre | [Consultar Horaris Oficials 🔗](http://trendesoller.com/tramvia/) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Biniaraix / Mirador de ses Barques, Font de sa Costera
- **Passos per Finques Privades:** Finca de sa Costera
- **Punts d'Interès Cultural i Natural:** Central hidroelèctrica de sa Costera, Cala Tuent, Vistes al mar de Tramuntana

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Ruta lineal. Cal organitzar el retorn amb barca o autocar des de Cala Tuent.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)

> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.

### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Sant Ramon de Penyafort** | **2.5 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/sant-ramon-de-penyafort-soller.md) |
| **Refugi de Muleta** | **4.2 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-muleta.md) |
| **Refugi de Cúber** | **4.8 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-cuber.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Capità Angelats** | Sóller | **2.7 km** | [Veure Casal](../agrupaments/aeg-capita-angelats.md) |
| **AEG Pedra Viva** | Binissalem | **13.8 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |

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

