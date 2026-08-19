# 🏔️ GR-221 Etapa 6: Sóller a Tossals Verds

Espectacular pujada pel monument d'enginyeria de pedra en sec del Barranc de Biniaraix fins al coll de l'Ofre i l'embassament de Cúber.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-gr221-etapa-6-soller-tossals-verds" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_gr221_etapa_6_soller_tossals_verds() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_gr221_etapa_6_soller_tossals_verds, 200);
        return;
    }
    
    const trackPoints = [[39.7661, 2.7156], [39.758, 2.748], [39.7821, 2.7915], [39.7583, 2.8222]];
    const itinerariPassos = [{"pas": 1, "nom": "Sóller a Biniaraix", "desc": "Passeig des de la plaça de Sóller fins al llogaret de Biniaraix."}, {"pas": 2, "nom": "Barranc de Biniaraix", "desc": "Ascensió pel famós camí empedrat del barranc entre bancals de taronjers i oliveres."}, {"pas": 3, "nom": "Coll de l'Ofre i Cúber", "desc": "Superació del coll de l'Ofre amb vistes a la vall de Sóller i l'embassament de Cúber."}, {"pas": 4, "nom": "Coll des Coloms a Tossals Verds", "desc": "Baixada pel Pas des Llis o Coll des Coloms fins al refugi de Tossals Verds."}];
    
    const rMap = L.map('map-route-gr221-etapa-6-soller-tossals-verds');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> GR-221 Etapa 6: Sóller a Tossals Verds");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> GR-221 Etapa 6: Sóller a Tossals Verds");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.7661, 2.7156], 14);
        L.marker([39.7661, 2.7156]).addTo(rMap).bindPopup("<b>GR-221 Etapa 6: Sóller a Tossals Verds</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_gr221_etapa_6_soller_tossals_verds);
setTimeout(initRouteTrackMap_gr221_etapa_6_soller_tossals_verds, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Sóller / Escorca** |
| **Zona / Comarca** | **Tramuntana Central** |
| **Distància Total** | **15.0 km** |
| **Desnivell Positiu** | **+820 m** |
| **Dificultat Tècnica** | **Exigent** |
| **Durada Estimada** | **5h 30min** |
| **Unitats Recomanades** | **Pioners/Rangers, Rovers/Rutes** |

---

## 🥾 Itinerari i Rumb de la Ruta Pas a Pas

| Pas | Punt de Referència / Tram | Indicacions i Descripció |
| :---: | :--- | :--- |
| **Pas 1** | **Sóller a Biniaraix** | Passeig des de la plaça de Sóller fins al llogaret de Biniaraix. |
| **Pas 2** | **Barranc de Biniaraix** | Ascensió pel famós camí empedrat del barranc entre bancals de taronjers i oliveres. |
| **Pas 3** | **Coll de l'Ofre i Cúber** | Superació del coll de l'Ofre amb vistes a la vall de Sóller i l'embassament de Cúber. |
| **Pas 4** | **Coll des Coloms a Tossals Verds** | Baixada pel Pas des Llis o Coll des Coloms fins al refugi de Tossals Verds. |

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

- **Punts d'Aigua Potable / Recàrrega:** Biniaraix, Font de sa Mula, Refugi Tossals Verds
- **Passos per Finques Privades:** Barranc de Biniaraix (públic d'interès cultural), Coll des Cornadors
- **Punts d'Interès Cultural i Natural:** Barranc de Biniaraix, Coll de l'Ofre, Embassament de Cúber, Pas des Llis

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Pujada contínua i empedrada al Barranc. Portar aigua suficient per a l'ascensió.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Sant Ramon de Penyafort** | Cristians Vall de Sóller | 45 pers. | **0.22 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/sant-ramon-de-penyafort-soller.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Refugi de Muleta** | **4.0 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-muleta.md) |
| **Refugi de Can Boi** | **6.1 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-can-boi.md) |
| **Refugi de Cúber** | **6.7 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-cuber.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Capità Angelats** | Sóller | **0.0 km** | [Veure Casal](../agrupaments/aeg-capita-angelats.md) |
| **AEG Nuredduna** | Bunyola / Palmanyola | **11.9 km** | [Veure Casal](../agrupaments/aeg-nuredduna.md) |
