# 🏔️ S'Alqueria Vella al Campament dels Soldats (Artà)

Ruta històrica i natural pel Parc Natural de Llevant des de les cases de s'Alqueria Vella.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-salquerieta-vella-campament-soldats" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_salquerieta_vella_campament_soldats() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_salquerieta_vella_campament_soldats, 200);
        return;
    }
    
    const trackPoints = [[39.735, 3.342]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-salquerieta-vella-campament-soldats');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> S'Alqueria Vella al Campament dels Soldats (Artà)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> S'Alqueria Vella al Campament dels Soldats (Artà)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.735, 3.342], 14);
        L.marker([39.735, 3.342]).addTo(rMap).bindPopup("<b>S'Alqueria Vella al Campament dels Soldats (Artà)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_salquerieta_vella_campament_soldats);
setTimeout(initRouteTrackMap_salquerieta_vella_campament_soldats, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Artà** |
| **Zona / Comarca** | **Llevant** |
| **Distància Total** | **7.0 km** |
| **Desnivell Positiu** | **+210 m** |
| **Dificultat Tècnica** | **Fàcil - Moderada** |
| **Durada Estimada** | **2h 30min** |
| **Unitats Recomanades** | **Llops/Daines, Pioners/Rangers** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=S%27Alqueria%20Vella%20al%20Campament%20dels%20Soldats%20%28Art%C3%A0%29)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Artà**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 411** (Manacor - Artà - Capdepera - Cala Rajada) | Manacor (Estació), Artà, Cala Rajada | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/411) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Centre d'Informació de s'Alqueria Vella
- **Passos per Finques Privades:** Parc Natural de la Península de Llevant
- **Punts d'Interès Cultural i Natural:** Antic campament de presoners de la Guerra Civil, Puig de sa Tudossa

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Zona molt exposada al sol a l'estiu.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Caseta dels Oguers** | IBANAT (Govern de les Illes Balears) | 10 pers. | **0.93 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/caseta-dels-oguers-arta.md) |
| **Casa de s'Alzina (Albarca)** | IBANAT (Govern de les Illes Balears) | 10 pers. | **1.58 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/casa-de-salzina-albarca.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Refugi de S'Arenalet d'es Verger** | **2.1 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-s-arenalet.md) |
| **Sant Guillem i Sant Antoni** | **2.2 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/sant-guillem-i-sant-antoni-betlem.md) |
| **Betlem (Colònia de Sant Pere)** | **3.2 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/betlem-colonia-sant-pere.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Sa Marjal** | Sa Pobla | **27.4 km** | [Veure Casal](../agrupaments/aeg-sa-marjal.md) |
| **AEG Pedra Viva** | Binissalem | **43.0 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |

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

