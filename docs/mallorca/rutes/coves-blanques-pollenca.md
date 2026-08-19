# 🏔️ Coves Blanques (Cala Sant Vicenç / Pollença)

Ruta històrica construïda durant la Segona Guerra Mundial per presoners que s'endinsa a les cavitats de les Coves Blanques sobre la mar de Cala Sant Vicenç.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-coves-blanques-pollenca" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_coves_blanques_pollenca() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_coves_blanques_pollenca, 200);
        return;
    }
    
    const trackPoints = [[39.921, 3.054], [39.928, 3.061], [39.934, 3.068]];
    const itinerariPassos = [{"pas": 1, "nom": "Cala Molins", "desc": "Inici a la Platja de Cala Molins a Cala Sant Vicenç."}, {"pas": 2, "nom": "Camí dels Presoners", "desc": "Pujada ample en zig-zag amb pineda."}, {"pas": 3, "nom": "Túnels de les Coves Blanques", "desc": "Galeries militars excavades a la roca."}];
    
    const rMap = L.map('map-route-coves-blanques-pollenca');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Coves Blanques (Cala Sant Vicenç / Pollença)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Coves Blanques (Cala Sant Vicenç / Pollença)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.921, 3.054], 14);
        L.marker([39.921, 3.054]).addTo(rMap).bindPopup("<b>Coves Blanques (Cala Sant Vicenç / Pollença)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_coves_blanques_pollenca);
setTimeout(initRouteTrackMap_coves_blanques_pollenca, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Pollença** |
| **Zona / Comarca** | **Tramuntana Nord** |
| **Distància Total** | **5.4 km** |
| **Desnivell Positiu** | **+150 m** |
| **Dificultat Tècnica** | **Fàcil** |
| **Durada Estimada** | **2h 00min** |
| **Unitats Recomanades** | **Castors/Fures, Llops/Daines, Pioners/Rangers, Rovers/Rutes** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Coves%20Blanques%20%28Cala%20Sant%20Vicen%C3%A7%20/%20Pollen%C3%A7a%29)** |
| **Guia Turisme Petit** | **[👶 Veure Guia de Família a Turisme Petit 🔗](https://www.turismepetit.com/excursion/excursion-a-las-coves-blanques-en-pollenca/)** |

---

## 🥾 Itinerari i Rumb de la Ruta Pas a Pas

| Pas | Punt de Referència / Tram | Indicacions i Descripció |
| :---: | :--- | :--- |
| **Pas 1** | **Cala Molins** | Inici a la Platja de Cala Molins a Cala Sant Vicenç. |
| **Pas 2** | **Camí dels Presoners** | Pujada ample en zig-zag amb pineda. |
| **Pas 3** | **Túnels de les Coves Blanques** | Galeries militars excavades a la roca. |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Pollença**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 301** (Palma - Inca - Port de Pollença) | Palma, Inca (Estació), Pollença, Port de Pollença | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/301) |
| **TIB 334** (Alcúdia - Port de Pollença - Formentor) | Port de Pollença, Cala Murta, Far de Formentor | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/334) |
| **TIB 341** (Pollença - Lluc - Cúber - Port de Sóller (Línia Ma-10)) | Pollença, Lluc (Monestir), Binifaldó, Gorg Blau | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/341) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Cala Sant Vicenç
- **Passos per Finques Privades:** Camí dels presoners (històric públic)
- **Punts d'Interès Cultural i Natural:** Coves Blanques (túnels militars), Cala Molins, Cavall Bernat

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Portar llanterna per explorar els túnels excavats a la roca amb precaució.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)

> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.

### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Refugi de Lavanor** | **5.5 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-lavanor-pollenca.md) |
| **Santuari del Puig de Maria** | **6.1 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/puig-de-maria-santuari-pollenca.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Sa Marjal** | Sa Pobla | **17.0 km** | [Veure Casal](../agrupaments/aeg-sa-marjal.md) |
| **AEG Pedra Viva** | Binissalem | **31.3 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |

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

