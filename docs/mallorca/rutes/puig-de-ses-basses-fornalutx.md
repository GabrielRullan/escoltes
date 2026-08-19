# 🏔️ Fornalutx al Coll de sa Bàlitx i Cala Tuent

Descens per la preciosa vall de Bàlitx des de Fornalutx fins a la mar.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-puig-de-ses-basses-fornalutx" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_puig_de_ses_basses_fornalutx() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_puig_de_ses_basses_fornalutx, 200);
        return;
    }
    
    const trackPoints = [[39.782, 2.741]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-puig-de-ses-basses-fornalutx');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Fornalutx al Coll de sa Bàlitx i Cala Tuent");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Fornalutx al Coll de sa Bàlitx i Cala Tuent");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.782, 2.741], 14);
        L.marker([39.782, 2.741]).addTo(rMap).bindPopup("<b>Fornalutx al Coll de sa Bàlitx i Cala Tuent</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_puig_de_ses_basses_fornalutx);
setTimeout(initRouteTrackMap_puig_de_ses_basses_fornalutx, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Fornalutx / Escorca** |
| **Zona / Comarca** | **Tramuntana Central** |
| **Distància Total** | **13.5 km** |
| **Desnivell Positiu** | **+420 m** |
| **Dificultat Tècnica** | **Moderada - Exigent** |
| **Durada Estimada** | **4h 45min** |
| **Unitats Recomanades** | **Pioners/Rangers, Rovers/Rutes** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Fornalutx%20al%20Coll%20de%20sa%20B%C3%A0litx%20i%20Cala%20Tuent)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Fornalutx / Escorca**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 341** (Pollença - Lluc - Cúber - Port de Sóller (Línia Ma-10)) | Pollença, Lluc (Monestir), Binifaldó, Gorg Blau | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/341) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Fornalutx (poble), Bàlitx d'Avall (font)
- **Passos per Finques Privades:** Bàlitx d'Amunt, d'Enmig i d'Avall
- **Punts d'Interès Cultural i Natural:** Poble patrimonial de Fornalutx, Tafona de Bàlitx d'Avall

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Preveure el transport de tornada des de Cala Tuent o Port de Sóller.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)

> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.

### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Sant Ramon de Penyafort** | **2.7 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/sant-ramon-de-penyafort-soller.md) |
| **Refugi de Cúber** | **4.3 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-cuber.md) |
| **Refugi de Muleta** | **4.8 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-muleta.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Capità Angelats** | Sóller | **2.8 km** | [Veure Casal](../agrupaments/aeg-capita-angelats.md) |
| **AEG Pedra Viva** | Binissalem | **13.3 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |

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

