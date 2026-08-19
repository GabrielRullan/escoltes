# 🏔️ GR-221 Etapa 8: Son Amer a Pollença

Última etapa del GR-221 que descendeix des de l'alzinar de Binifaldó per la frondosa vall de March fins al Pont Romà de Pollença.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-gr221-etapa-8-son-amer-pollenca" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_gr221_etapa_8_son_amer_pollenca() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_gr221_etapa_8_son_amer_pollenca, 200);
        return;
    }
    
    const trackPoints = [[39.8215, 2.8872], [39.8311, 2.8988], [39.852, 2.948], [39.878, 3.015]];
    const itinerariPassos = [{"pas": 1, "nom": "Sortida de Son Amer", "desc": "Passeig ombrívol fins a les cases de Binifaldó."}, {"pas": 2, "nom": "Coll de sa Batalla a Vall de March", "desc": "Descens suau pel Camí Vell de Pollença."}, {"pas": 3, "nom": "Vall de March", "desc": "Planura de conreu paral·lela al torrent de Sant Jordi."}, {"pas": 4, "nom": "Pont Romà i Pollença", "desc": "Entrada triomfal a Pollença pel Pont Romà."}];
    
    const rMap = L.map('map-route-gr221-etapa-8-son-amer-pollenca');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> GR-221 Etapa 8: Son Amer a Pollença");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> GR-221 Etapa 8: Son Amer a Pollença");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.8215, 2.8872], 14);
        L.marker([39.8215, 2.8872]).addTo(rMap).bindPopup("<b>GR-221 Etapa 8: Son Amer a Pollença</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_gr221_etapa_8_son_amer_pollenca);
setTimeout(initRouteTrackMap_gr221_etapa_8_son_amer_pollenca, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Escorca / Pollença** |
| **Zona / Comarca** | **Tramuntana Nord** |
| **Distància Total** | **16.7 km** |
| **Desnivell Positiu** | **+240 m** |
| **Dificultat Tècnica** | **Fàcil - Moderada** |
| **Durada Estimada** | **4h 45min** |
| **Unitats Recomanades** | **Castors/Fures, Llops/Daines, Pioners/Rangers, Rovers/Rutes** |

---

## 🥾 Itinerari i Rumb de la Ruta Pas a Pas

| Pas | Punt de Referència / Tram | Indicacions i Descripció |
| :---: | :--- | :--- |
| **Pas 1** | **Sortida de Son Amer** | Passeig ombrívol fins a les cases de Binifaldó. |
| **Pas 2** | **Coll de sa Batalla a Vall de March** | Descens suau pel Camí Vell de Pollença. |
| **Pas 3** | **Vall de March** | Planura de conreu paral·lela al torrent de Sant Jordi. |
| **Pas 4** | **Pont Romà i Pollença** | Entrada triomfal a Pollença pel Pont Romà. |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Escorca / Pollença**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 301** (Palma - Inca - Port de Pollença) | Palma, Inca (Estació), Pollença, Port de Pollença | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/301) |
| **TIB 334** (Alcúdia - Port de Pollença - Formentor) | Port de Pollença, Cala Murta, Far de Formentor | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/334) |
| **TIB 341** (Pollença - Lluc - Cúber - Port de Sóller (Línia Ma-10)) | Pollença, Lluc (Monestir), Binifaldó, Gorg Blau | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/341) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Son Amer, Binifaldó, Font de la Sinieta, Pollença vila
- **Passos per Finques Privades:** Camí Vell de Lluc a Pollença (públic)
- **Punts d'Interès Cultural i Natural:** Binifaldó, Puig Tomir, Vall de March, Pont Romà de Pollença

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Etapa còmoda i principalment en descens. Molt indicada per a unitats menudes.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Refugi de Son Amer** | Consell de Mallorca (Xarxa GR-221) | 52 pers. | **0.00 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/refugi-son-amer.md) |
| **Àrea d'Acampada de Marjanor** | IBANAT (Govern de les Illes Balears) | 60 pers. | **0.16 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/marjanor-lluc.md) |
| **Àrea d'Acampada de Sa Font Coberta** | IBANAT (Govern de les Illes Balears) | 150 pers. | **0.45 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/sa-font-coberta-lluc.md) |
| **Àrea d'Acampada des Pixarells** | IBANAT (Govern de les Illes Balears) | 80 pers. | **0.89 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/es-pixarells-lluc.md) |
| **Cases de Binifaldó (Refugi IBANAT)** | IBANAT (Govern de les Illes Balears) | 30 pers. | **1.46 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/cases-de-binifaldo.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Comuna de Caimari** | **5.2 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/comuna-de-caimari.md) |
| **Monestir de Santa Llúcia** | **8.3 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/monestir-santa-llucia-mancor.md) |
| **Refugi de Tossals Verds** | **9.0 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-tossals-verds.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Sa Marjal** | Sa Pobla | **13.1 km** | [Veure Casal](../agrupaments/aeg-sa-marjal.md) |
| **AEG Pedra Viva** | Binissalem | **14.9 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |
