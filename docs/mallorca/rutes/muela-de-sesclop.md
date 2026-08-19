# 🏔️ Muela de s'Esclop (des de sa Vinya de Galatzó)

Ruta d'alta muntanya cap a la taula rocosa de s'Esclop, on el físic Arago va mesurar el meridià de París.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-muela-de-sesclop" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_muela_de_sesclop() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_muela_de_sesclop, 200);
        return;
    }
    
    const trackPoints = [[39.598, 2.451]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-muela-de-sesclop');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Muela de s'Esclop (des de sa Vinya de Galatzó)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Muela de s'Esclop (des de sa Vinya de Galatzó)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.598, 2.451], 14);
        L.marker([39.598, 2.451]).addTo(rMap).bindPopup("<b>Muela de s'Esclop (des de sa Vinya de Galatzó)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_muela_de_sesclop);
setTimeout(initRouteTrackMap_muela_de_sesclop, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Calvià / Andratx** |
| **Zona / Comarca** | **Tramuntana Sud** |
| **Distància Total** | **12.8 km** |
| **Desnivell Positiu** | **+690 m** |
| **Dificultat Tècnica** | **Exigent** |
| **Durada Estimada** | **5h 00min** |
| **Unitats Recomanades** | **Pioners/Rangers, Rovers/Rutes** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Muela%20de%20s%27Esclop%20%28des%20de%20sa%20Vinya%20de%20Galatz%C3%B3%29)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Calvià / Andratx**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 101** (Palma - Andratx - Port d'Andratx) | Palma (Estació Intermodal), Andratx (Grava), Port d'Andratx | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/101) |
| **TIB 102** (Palma - Sant Elm) | Palma, Andratx, Sant Elm (Plaça de na Caragola) | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/102) |
| **TIB 108** (Palma - Calvià - Es Capdellà) | Palma, Calvià, Es Capdellà (sa Vinya) | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/108) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Es Capdellà / sa Vinya
- **Passos per Finques Privades:** Finca Pública de Galatzó
- **Punts d'Interès Cultural i Natural:** Caseta de François Arago, Cim de s'Esclop (926m), Pas des Cap Cornell

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Orientació complexa si hi ha boira.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Refugi de la Finca Pública de Galatzó** | Consell de Mallorca / Aj. Calvià | 50 pers. | **1.22 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/finca-de-galatzo-refugi.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Refugi de Sa Coma d'en Vidal** | **4.5 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/sa-coma-den-vidal.md) |
| **Refugi de Ses Fontanelles** | **5.3 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/ses-fontanelles-sant-elm.md) |
| **La Trapa (Zona d'Acampada)** | **8.0 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/la-trapa-andratx.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Reina Constança de Mallorca** | Palma | **16.5 km** | [Veure Casal](../agrupaments/aeg-reina-constanca.md) |
| **AEG Son Sardina** | Palma | **17.3 km** | [Veure Casal](../agrupaments/aeg-son-sardina.md) |

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

