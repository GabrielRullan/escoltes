# 🏔️ GR-221 Etapa 7: Tossals Verds a Son Amer (Lluc)

El sostre del GR-221. Travessa les altures de la serra entre el Puig de Massanella i les Voltes d'en Galileu fins al Santuari de Lluc.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-gr221-etapa-7-tossals-verds-son-amer" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_gr221_etapa_7_tossals_verds_son_amer() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_gr221_etapa_7_tossals_verds_son_amer, 200);
        return;
    }
    
    const trackPoints = [[39.7583, 2.8222], [39.791, 2.845], [39.808, 2.869], [39.8215, 2.8872]];
    const itinerariPassos = [{"pas": 1, "nom": "Sortida de Tossals Verds", "desc": "Camí cap a la Font des Prat per la frondosa vall d'Escorca."}, {"pas": 2, "nom": "Ascens al Coll des Prat", "desc": "Pujada sostinguda fins al punt més alt del GR-221 a 1.205 metres d'altitud."}, {"pas": 3, "nom": "Ses Voltes d'en Galileu", "desc": "Baixada espectacular pel zigzag empedrat de les cases de neu d'en Galileu."}, {"pas": 4, "nom": "Arribada a Son Amer (Lluc)", "desc": "Entrada a la vall de Lluc i refugi de Son Amer."}];
    
    const rMap = L.map('map-route-gr221-etapa-7-tossals-verds-son-amer');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> GR-221 Etapa 7: Tossals Verds a Son Amer (Lluc)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> GR-221 Etapa 7: Tossals Verds a Son Amer (Lluc)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.7583, 2.8222], 14);
        L.marker([39.7583, 2.8222]).addTo(rMap).bindPopup("<b>GR-221 Etapa 7: Tossals Verds a Son Amer (Lluc)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_gr221_etapa_7_tossals_verds_son_amer);
setTimeout(initRouteTrackMap_gr221_etapa_7_tossals_verds_son_amer, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Escorca** |
| **Zona / Comarca** | **Tramuntana Nord** |
| **Distància Total** | **14.8 km** |
| **Desnivell Positiu** | **+830 m** |
| **Dificultat Tècnica** | **Exigent** |
| **Durada Estimada** | **5h 45min** |
| **Unitats Recomanades** | **Pioners/Rangers, Rovers/Rutes** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=GR-221%20Etapa%207%3A%20Tossals%20Verds%20a%20Son%20Amer%20%28Lluc%29)** |

---

## 🥾 Itinerari i Rumb de la Ruta Pas a Pas

| Pas | Punt de Referència / Tram | Indicacions i Descripció |
| :---: | :--- | :--- |
| **Pas 1** | **Sortida de Tossals Verds** | Camí cap a la Font des Prat per la frondosa vall d'Escorca. |
| **Pas 2** | **Ascens al Coll des Prat** | Pujada sostinguda fins al punt més alt del GR-221 a 1.205 metres d'altitud. |
| **Pas 3** | **Ses Voltes d'en Galileu** | Baixada espectacular pel zigzag empedrat de les cases de neu d'en Galileu. |
| **Pas 4** | **Arribada a Son Amer (Lluc)** | Entrada a la vall de Lluc i refugi de Son Amer. |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Escorca**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 341** (Pollença - Lluc - Cúber - Port de Sóller (Línia Ma-10)) | Pollença, Lluc (Monestir), Binifaldó, Gorg Blau | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/341) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Refugi Tossals Verds, Font des Prat, Font de sa Coma de sa Vinya, Son Amer / Lluc
- **Passos per Finques Privades:** Coll des Prat, Coll de sa Batalla
- **Punts d'Interès Cultural i Natural:** Coll des Prat, Puig de Massanella, Ses Voltes d'en Galileu, Monestir de Lluc

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Punt més alt del GR-221 (Coll des Prat, 1.205m). Atenció a les nevades a l'hivern i vent fort.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Refugi de Tossals Verds** | Consell de Mallorca (Xarxa GR-221) | 30 pers. | **0.00 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/refugi-tossals-verds.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Refugi de Cúber** | **3.7 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-cuber.md) |
| **Monestir de Santa Llúcia** | **4.3 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/monestir-santa-llucia-mancor.md) |
| **S'Olivaret (Alaró)** | **6.2 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/solivaret-alaro.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Pedra Viva** | Binissalem | **7.6 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |
| **AEG Capità Angelats** | Sóller | **9.2 km** | [Veure Casal](../agrupaments/aeg-capita-angelats.md) |

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

