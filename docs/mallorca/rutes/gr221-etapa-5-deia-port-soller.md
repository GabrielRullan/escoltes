# 🏔️ GR-221 Etapa 5: Deià al Port de Sóller

Una de les etapes més amables del GR-221 que discorre per la costa nord entre hortes d'oliveres centenàries i vistes al mar mediterrani.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-gr221-etapa-5-deia-port-soller" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_gr221_etapa_5_deia_port_soller() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_gr221_etapa_5_deia_port_soller, 200);
        return;
    }
    
    const trackPoints = [[39.7491, 2.6483], [39.761, 2.662], [39.782, 2.678], [39.7942, 2.6869]];
    const itinerariPassos = [{"pas": 1, "nom": "Sortida de Deià (Can Boi)", "desc": "Camí baix cap a les hortes de Deià i Llucalcari."}, {"pas": 2, "nom": "Pintors i Son Mico", "desc": "Travessa de la finca tradicional de Son Mico."}, {"pas": 3, "nom": "Camí de Muleta", "desc": "Sendera flanquejada de fites fins a la pineda del Cap Gros."}, {"pas": 4, "nom": "Refugi de Muleta", "desc": "Arribada al far i refugi de Muleta sobre la badia del Port de Sóller."}];
    
    const rMap = L.map('map-route-gr221-etapa-5-deia-port-soller');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> GR-221 Etapa 5: Deià al Port de Sóller");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> GR-221 Etapa 5: Deià al Port de Sóller");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.7491, 2.6483], 14);
        L.marker([39.7491, 2.6483]).addTo(rMap).bindPopup("<b>GR-221 Etapa 5: Deià al Port de Sóller</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_gr221_etapa_5_deia_port_soller);
setTimeout(initRouteTrackMap_gr221_etapa_5_deia_port_soller, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Deià / Sóller** |
| **Zona / Comarca** | **Tramuntana Central** |
| **Distància Total** | **10.2 km** |
| **Desnivell Positiu** | **+310 m** |
| **Dificultat Tècnica** | **Fàcil - Moderada** |
| **Durada Estimada** | **3h 30min** |
| **Unitats Recomanades** | **Castors/Fures, Llops/Daines, Pioners/Rangers, Rovers/Rutes** |

---

## 🥾 Itinerari i Rumb de la Ruta Pas a Pas

| Pas | Punt de Referència / Tram | Indicacions i Descripció |
| :---: | :--- | :--- |
| **Pas 1** | **Sortida de Deià (Can Boi)** | Camí baix cap a les hortes de Deià i Llucalcari. |
| **Pas 2** | **Pintors i Son Mico** | Travessa de la finca tradicional de Son Mico. |
| **Pas 3** | **Camí de Muleta** | Sendera flanquejada de fites fins a la pineda del Cap Gros. |
| **Pas 4** | **Refugi de Muleta** | Arribada al far i refugi de Muleta sobre la badia del Port de Sóller. |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Deià / Sóller**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 203** (Palma - Valldemossa - Deià - Sóller) | Palma, Valldemossa, Son Marroig, Deià | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/203) |
| **TIB 204** (Palma - Sóller - Port de Sóller (Express Túnel)) | Palma (Estació Intermodal), Sóller (Ma-11), Port de Sóller | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/204) |
| **TIB 341** (Pollença - Lluc - Cúber - Port de Sóller (Línia Ma-10)) | Pollença, Lluc (Monestir), Binifaldó, Gorg Blau | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/341) |
| **Ferrocarril de Sóller** (Tren de Fusta de Sóller (Palma - Bunyola - Sóller)) | Palma (Plaça d'Espanya), Son Sardina, Bunyola, Mirador des Pujol d'en Banya | [Consultar Horaris Oficials 🔗](http://trendesoller.com/) |
| **Tramvia de Sóller** (Tranvia Històric de Sóller (Sóller Vila - Port de Sóller)) | Sóller Estació, Mercat de Sóller, Es Control, Sa Torre | [Consultar Horaris Oficials 🔗](http://trendesoller.com/tramvia/) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Deià (Can Boi), Son Mico (cafè/aigua), Port de Sóller (Refugi Muleta)
- **Passos per Finques Privades:** Camí des Pintors, Son Mico (obert)
- **Punts d'Interès Cultural i Natural:** Cala Deià, Llucalcari, Finca de Son Mico, Cap Gros i Far de Muleta

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Ideal per a totes les unitats escoltes. Ruta amena entre oliveres i mar.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Refugi de Can Boi** | Consell de Mallorca (Xarxa GR-221) | 32 pers. | **0.00 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/refugi-can-boi.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Refugi de Son Moragues** | **4.2 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-son-moragues.md) |
| **Refugi de Muleta** | **6.0 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-muleta.md) |
| **Sant Ramon de Penyafort** | **6.1 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/sant-ramon-de-penyafort-soller.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Capità Angelats** | Sóller | **6.0 km** | [Veure Casal](../agrupaments/aeg-capita-angelats.md) |
| **AEG Nuredduna** | Bunyola / Palmanyola | **10.8 km** | [Veure Casal](../agrupaments/aeg-nuredduna.md) |
