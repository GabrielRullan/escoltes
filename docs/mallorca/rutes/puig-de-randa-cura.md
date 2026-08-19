# 🏔️ Puig de Randa i Santuari de Cura (Algaida)

Muntanya sagrada del centre de Mallorca associada a la figura de Ramon Llull.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-puig-de-randa-cura" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_puig_de_randa_cura() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_puig_de_randa_cura, 200);
        return;
    }
    
    const trackPoints = [[39.528, 2.926]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-puig-de-randa-cura');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Puig de Randa i Santuari de Cura (Algaida)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Puig de Randa i Santuari de Cura (Algaida)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.528, 2.926], 14);
        L.marker([39.528, 2.926]).addTo(rMap).bindPopup("<b>Puig de Randa i Santuari de Cura (Algaida)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_puig_de_randa_cura);
setTimeout(initRouteTrackMap_puig_de_randa_cura, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Algaida** |
| **Zona / Comarca** | **Pla de Mallorca** |
| **Distància Total** | **9.0 km** |
| **Desnivell Positiu** | **+410 m** |
| **Dificultat Tècnica** | **Moderada** |
| **Durada Estimada** | **3h 00min** |
| **Unitats Recomanades** | **Llops/Daines, Pioners/Rangers, Rovers/Rutes** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Puig%20de%20Randa%20i%20Santuari%20de%20Cura%20%28Algaida%29)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Algaida**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB / SFM Xarxa General** (Línia d'autobús o tren comarcal (Algaida)) | Algaida | [Consultar Horaris Oficials 🔗](https://www.tib.org/) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Randa, Santuari de Cura
- **Passos per Finques Privades:** Camí vell de Randa
- **Punts d'Interès Cultural i Natural:** Santuari de Gràcia, Santuari de Sant Honorat, Santuari de Cura (543m)

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Punts de pas per carretera d'accés.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Santuari de Cura** | Ordre de Franciscans | 50 pers. | **0.00 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/santuari-de-cura-algaida.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Puig de Sant Miquel (Kcodril)** | **7.5 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/puig-de-sant-miquel-montuiri-alberg.md) |
| **Santuari de Monti-Sion** | **9.3 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/santuari-monti-sion-porreres.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **Grupo Scout Myotragus 684** | Llucmajor | **15.1 km** | [Veure Casal](../agrupaments/gs-myotragus-684.md) |
| **AEG Terra de Pous** | Santa Maria del Camí | **19.0 km** | [Veure Casal](../agrupaments/aeg-terra-de-pous.md) |

---

## 💬 Experiències i Valoracions dels Agrupaments Escoltes

<div style="background-color: var(--md-code-bg-color, #f8f9fa); border: 1px solid #e0e0e0; padding: 18px; border-radius: 10px; margin-top: 16px;">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
        <div>
            <h3 style="margin: 0; font-size: 1.05em; color: #555;">Encara no hi ha cap experiència registrada per a aquesta ruta.</h3>
            <p style="margin: 4px 0 0 0; font-size: 0.85em; color: #666;">Heu fet aquesta ruta amb la vostra unitat? Sigueu els primers a deixar consells per a altres agrupaments!</p>
        </div>
        <a href="https://docs.google.com/forms/d/e/1FAIpQLScoutsMallorcaRutes/viewform" target="_blank" style="padding: 8px 16px; background-color: #00897b; color: white; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 0.85em;">📝 Enviar la primera experiència 🔗</a>
    </div>
</div>

