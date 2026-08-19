# 🏔️ Parc Natural de s'Albufera de Mallorca

La major zona humida de les Balears, ideal per a tallers d'observació d'aus i ecologia.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-parc-natural-albufera-mallorca" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_parc_natural_albufera_mallorca() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_parc_natural_albufera_mallorca, 200);
        return;
    }
    
    const trackPoints = [[39.792, 3.118]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-parc-natural-albufera-mallorca');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Parc Natural de s'Albufera de Mallorca");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Parc Natural de s'Albufera de Mallorca");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.792, 3.118], 14);
        L.marker([39.792, 3.118]).addTo(rMap).bindPopup("<b>Parc Natural de s'Albufera de Mallorca</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_parc_natural_albufera_mallorca);
setTimeout(initRouteTrackMap_parc_natural_albufera_mallorca, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Sa Pobla / Muro** |
| **Zona / Comarca** | **Pla de Mallorca** |
| **Distància Total** | **6.2 km** |
| **Desnivell Positiu** | **+10 m** |
| **Dificultat Tècnica** | **Molt Fàcil** |
| **Durada Estimada** | **2h 00min** |
| **Unitats Recomanades** | **Castors/Fures, Llops/Daines, Pioners/Rangers** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Parc%20Natural%20de%20s%27Albufera%20de%20Mallorca)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Sa Pobla / Muro**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 302** (Can Picafort - Son Real - Alcúdia) | Can Picafort, Son Real, Alcúdia | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/302) |
| **TIB 312** (Sa Pobla - Campanet - Inca) | Inca, Campanet, Sa Pobla | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/312) |
| **SFM Línia T2** (Tren Palma - Inca - Sa Pobla) | Inca, Llubí, Muro, Sa Pobla | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/tren/linia/T2) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Centre de visitants Sa Roca
- **Passos per Finques Privades:** Parc Natural de s'Albufera
- **Punts d'Interès Cultural i Natural:** Observatoris d'aus, Gran Canal, PONT dels Anglesos

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Prohibit circular fora dels itineraris senyalitzats. Silenci en els observatoris.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)

> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.

### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **S'Hort de Son Serra** | **6.7 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/short-de-son-serra.md) |
| **Son Real (Refugi i Cases)** | **7.7 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/son-real-refugi-ibanat.md) |
| **Crestatx (Ermita i Terreny)** | **8.9 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/crestatx-sa-pobla.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Sa Marjal** | Sa Pobla | **8.4 km** | [Veure Casal](../agrupaments/aeg-sa-marjal.md) |
| **AEG Pedra Viva** | Binissalem | **26.1 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |
