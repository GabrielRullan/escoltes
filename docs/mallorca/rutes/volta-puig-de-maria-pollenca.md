# 🏔️ Volta al Puig de Maria (Pollença)

Ruta fàcil d'iniciació per a les branques més joves cap al cim del Puig de Maria de Pollença.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-volta-puig-de-maria-pollenca" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_volta_puig_de_maria_pollenca() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_volta_puig_de_maria_pollenca, 200);
        return;
    }
    
    const trackPoints = [[39.8735, 3.018]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-volta-puig-de-maria-pollenca');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Volta al Puig de Maria (Pollença)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Volta al Puig de Maria (Pollença)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.8735, 3.018], 14);
        L.marker([39.8735, 3.018]).addTo(rMap).bindPopup("<b>Volta al Puig de Maria (Pollença)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_volta_puig_de_maria_pollenca);
setTimeout(initRouteTrackMap_volta_puig_de_maria_pollenca, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Pollença** |
| **Zona / Comarca** | **Tramuntana Nord** |
| **Distància Total** | **4.5 km** |
| **Desnivell Positiu** | **+240 m** |
| **Dificultat Tècnica** | **Fàcil** |
| **Durada Estimada** | **1h 45min** |
| **Unitats Recomanades** | **Castors/Fures, Llops/Daines, Pioners/Rangers** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Volta%20al%20Puig%20de%20Maria%20%28Pollen%C3%A7a%29)** |

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

- **Punts d'Aigua Potable / Recàrrega:** Pollença poble, Santuari del Puig de Maria
- **Passos per Finques Privades:** Camí públic pavimentat i empedrat
- **Punts d'Interès Cultural i Natural:** Santuari del segle XIV, Vistes a la badia de Pollença i Alcúdia

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Excel·lent opció per a iniciació de Castors i Llops.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Santuari del Puig de Maria** | Ajuntament de Pollença / Obreria | 25 pers. | **0.00 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/puig-de-maria-santuari-pollenca.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Refugi de Lavanor** | **2.4 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-lavanor-pollenca.md) |
| **Crestatx (Ermita i Terreny)** | **7.6 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/crestatx-sa-pobla.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Sa Marjal** | Sa Pobla | **11.6 km** | [Veure Casal](../agrupaments/aeg-sa-marjal.md) |
| **AEG Pedra Viva** | Binissalem | **25.2 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |
