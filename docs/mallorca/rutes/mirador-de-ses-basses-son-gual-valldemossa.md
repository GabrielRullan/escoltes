# 🏔️ Mirador de ses Basses i Son Gual (Valldemossa)

Ruta panoràmica des de Valldemossa que ascendeix per l'alzinar fins als miradors naturals de ses Basses i Son Gual amb vistes directes a la Cartoixa.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-mirador-de-ses-basses-son-gual-valldemossa" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_mirador_de_ses_basses_son_gual_valldemossa() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_mirador_de_ses_basses_son_gual_valldemossa, 200);
        return;
    }
    
    const trackPoints = [[39.712, 2.623], [39.718, 2.631], [39.724, 2.639]];
    const itinerariPassos = [{"pas": 1, "nom": "Inici a Valldemossa", "desc": "Sortida des de la part alta del poble cap al bosc."}, {"pas": 2, "nom": "Alzinar des Cairats", "desc": "Pujada amena a l'ombra de les alzines centenàries."}, {"pas": 3, "nom": "Mirador de Son Gual", "desc": "Balcó natural amb vistes impressionants a tota la vall."}];
    
    const rMap = L.map('map-route-mirador-de-ses-basses-son-gual-valldemossa');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Mirador de ses Basses i Son Gual (Valldemossa)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Mirador de ses Basses i Son Gual (Valldemossa)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.712, 2.623], 14);
        L.marker([39.712, 2.623]).addTo(rMap).bindPopup("<b>Mirador de ses Basses i Son Gual (Valldemossa)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_mirador_de_ses_basses_son_gual_valldemossa);
setTimeout(initRouteTrackMap_mirador_de_ses_basses_son_gual_valldemossa, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Valldemossa** |
| **Zona / Comarca** | **Tramuntana Central** |
| **Distància Total** | **6.8 km** |
| **Desnivell Positiu** | **+290 m** |
| **Dificultat Tècnica** | **Fàcil** |
| **Durada Estimada** | **2h 30min** |
| **Unitats Recomanades** | **Castors/Fures, Llops/Daines, Pioners/Rangers, Rovers/Rutes** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Mirador%20de%20ses%20Basses%20i%20Son%20Gual%20%28Valldemossa%29)** |
| **Guia Turisme Petit** | **[👶 Veure Guia de Família a Turisme Petit 🔗](https://www.turismepetit.com/excursion/excursion-al-mirador-de-ses-basses-y-mirador-de-son-gual/)** |

---

## 🥾 Itinerari i Rumb de la Ruta Pas a Pas

| Pas | Punt de Referència / Tram | Indicacions i Descripció |
| :---: | :--- | :--- |
| **Pas 1** | **Inici a Valldemossa** | Sortida des de la part alta del poble cap al bosc. |
| **Pas 2** | **Alzinar des Cairats** | Pujada amena a l'ombra de les alzines centenàries. |
| **Pas 3** | **Mirador de Son Gual** | Balcó natural amb vistes impressionants a tota la vall. |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Valldemossa**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 203** (Palma - Valldemossa - Deià - Sóller) | Palma, Valldemossa, Son Marroig, Deià | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/203) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Vila de Valldemossa
- **Passos per Finques Privades:** Miradors públics de sa Comuna de Valldemossa
- **Punts d'Interès Cultural i Natural:** Mirador de ses Basses, Mirador de Son Gual, Panoràmica de Valldemossa

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Bosc frondós d'alzinar. Atenció als nins a la vora del mirador penjat.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Refugi de Son Moragues** | IBANAT (Govern de les Illes Balears) | 15 pers. | **0.54 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/refugi-son-moragues.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Refugi de Can Boi** | **4.7 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-can-boi.md) |
| **Binicanella (Casa de Colònies)** | **6.9 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/binicanella-bunyola.md) |
| **Maristel·la (Ermita i Terreny)** | **7.1 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/maristella-esporles.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Nuredduna** | Bunyola / Palmanyola | **8.7 km** | [Veure Casal](../agrupaments/aeg-nuredduna.md) |
| **AEG Capità Angelats** | Sóller | **9.9 km** | [Veure Casal](../agrupaments/aeg-capita-angelats.md) |
