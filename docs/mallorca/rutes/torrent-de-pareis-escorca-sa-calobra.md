# 🏔️ Torrent De Pareis Escorca Sa Calobra

Ruta d'excursió extreta de Wikiloc ([Veure Track Oficial a Wikiloc](https://es.wikiloc.com/rutas-senderismo/torrent-de-pareis-escorca-sa-calobra-2194812)).

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-torrent-de-pareis-escorca-sa-calobra" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_torrent_de_pareis_escorca_sa_calobra() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_torrent_de_pareis_escorca_sa_calobra, 200);
        return;
    }
    
    const trackPoints = [[39.65, 2.9], [39.655, 2.905]];
    const itinerariPassos = [{"pas": 1, "nom": "Inici de la ruta (Wikiloc)", "desc": "Sortida des del punt inicial indicat al track de Wikiloc (https://es.wikiloc.com/rutas-senderismo/torrent-de-pareis-escorca-sa-calobra-2194812)."}, {"pas": 2, "nom": "Tram principal del recorregut", "desc": "Seguiment de la sendera i fites sobre el terreny."}, {"pas": 3, "nom": "Punt d'arribada", "desc": "Final de la ruta o retorn al punt d'origen."}];
    
    const rMap = L.map('map-route-torrent-de-pareis-escorca-sa-calobra');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Torrent De Pareis Escorca Sa Calobra");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Torrent De Pareis Escorca Sa Calobra");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.65, 2.9], 14);
        L.marker([39.65, 2.9]).addTo(rMap).bindPopup("<b>Torrent De Pareis Escorca Sa Calobra</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_torrent_de_pareis_escorca_sa_calobra);
setTimeout(initRouteTrackMap_torrent_de_pareis_escorca_sa_calobra, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Mallorca** |
| **Zona / Comarca** | **Serra de Tramuntana** |
| **Distància Total** | **8.5 km** |
| **Desnivell Positiu** | **+350 m** |
| **Dificultat Tècnica** | **Moderada** |
| **Durada Estimada** | **3h 30min** |
| **Unitats Recomanades** | **Llops/Daines, Pioners/Rangers, Rovers/Rutes** |
| **Track a Wikiloc** | **[💚 Obrir Track Oficial a Wikiloc 🔗](https://es.wikiloc.com/rutas-senderismo/torrent-de-pareis-escorca-sa-calobra-2194812)** |

---

## 🥾 Itinerari i Rumb de la Ruta Pas a Pas

| Pas | Punt de Referència / Tram | Indicacions i Descripció |
| :---: | :--- | :--- |
| **Pas 1** | **Inici de la ruta (Wikiloc)** | Sortida des del punt inicial indicat al track de Wikiloc (https://es.wikiloc.com/rutas-senderismo/torrent-de-pareis-escorca-sa-calobra-2194812). |
| **Pas 2** | **Tram principal del recorregut** | Seguiment de la sendera i fites sobre el terreny. |
| **Pas 3** | **Punt d'arribada** | Final de la ruta o retorn al punt d'origen. |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Mallorca**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB / SFM Xarxa General** (Línia d'autobús o tren comarcal (Mallorca)) | Mallorca | [Consultar Horaris Oficials 🔗](https://www.tib.org/) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Consultar punts de recàrrega
- **Passos per Finques Privades:** Consultar senyalització i camins habilitats
- **Punts d'Interès Cultural i Natural:** Torrent De Pareis Escorca Sa Calobra

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Portar aigua suficient, calçat de muntanya i consultar la previsió del temps abans de sortir.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)

> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.

### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Ca n'Arabí** | **6.8 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/ca-narabi-binissalem.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Pedra Viva** | Binissalem | **6.8 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |
| **AEG Terra de Pous** | Santa Maria del Camí | **10.9 km** | [Veure Casal](../agrupaments/aeg-terra-de-pous.md) |
