# 🏔️ Puig de Sant Miquel (Montuïri)

Passejada rural pel Pla de Mallorca fins a l'ermita de Sant Miquel.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-puig-de-sant-miquel-montuiri" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_puig_de_sant_miquel_montuiri() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_puig_de_sant_miquel_montuiri, 200);
        return;
    }
    
    const trackPoints = [[39.578, 2.985]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-puig-de-sant-miquel-montuiri');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Puig de Sant Miquel (Montuïri)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Puig de Sant Miquel (Montuïri)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.578, 2.985], 14);
        L.marker([39.578, 2.985]).addTo(rMap).bindPopup("<b>Puig de Sant Miquel (Montuïri)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_puig_de_sant_miquel_montuiri);
setTimeout(initRouteTrackMap_puig_de_sant_miquel_montuiri, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Montuïri** |
| **Zona / Comarca** | **Pla de Mallorca** |
| **Distància Total** | **5.2 km** |
| **Desnivell Positiu** | **+160 m** |
| **Dificultat Tècnica** | **Fàcil** |
| **Durada Estimada** | **1h 45min** |
| **Unitats Recomanades** | **Castors/Fures, Llops/Daines** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Montuïri**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 514** (Felanitx - Porreres - Vilafranca) | Felanitx, Porreres, Vilafranca, Montuïri | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/514) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Montuïri poble
- **Passos per Finques Privades:** Camí des Puig
- **Punts d'Interès Cultural i Natural:** Ermita de Sant Miquel (s. XIV), Vistes al Pla de Mallorca

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Ruta serena de baixa dificultat.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Puig de Sant Miquel (Kcodril)** | Kcodril / Gestió Entitat | 40 pers. | **0.00 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/puig-de-sant-miquel-montuiri-alberg.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Santuari de Cura** | **7.5 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/santuari-de-cura-algaida.md) |
| **Santuari de Monti-Sion** | **8.7 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/santuari-monti-sion-porreres.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Pedra Viva** | Binissalem | **17.6 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |
| **AEG Terra de Pous** | Santa Maria del Camí | **19.9 km** | [Veure Casal](../agrupaments/aeg-terra-de-pous.md) |
