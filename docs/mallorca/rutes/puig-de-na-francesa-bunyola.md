# 🏔️ Puig de na Francessa (Bunyola)

Atalaia panoràmica sobre la vall de Bunyola i el Pla de Palma.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-puig-de-na-francesa-bunyola" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_puig_de_na_francesa_bunyola() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_puig_de_na_francesa_bunyola, 200);
        return;
    }
    
    const trackPoints = [[39.691, 2.712]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-puig-de-na-francesa-bunyola');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Puig de na Francessa (Bunyola)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Puig de na Francessa (Bunyola)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.691, 2.712], 14);
        L.marker([39.691, 2.712]).addTo(rMap).bindPopup("<b>Puig de na Francessa (Bunyola)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_puig_de_na_francesa_bunyola);
setTimeout(initRouteTrackMap_puig_de_na_francesa_bunyola, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Bunyola** |
| **Zona / Comarca** | **Tramuntana Central** |
| **Distància Total** | **8.0 km** |
| **Desnivell Positiu** | **+430 m** |
| **Dificultat Tècnica** | **Moderada** |
| **Durada Estimada** | **3h 00min** |
| **Unitats Recomanades** | **Pioners/Rangers, Rovers/Rutes** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Puig%20de%20na%20Francessa%20%28Bunyola%29)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Bunyola**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 205** (Palma - Bunyola - Orient) | Palma, Raixa, Bunyola, Orient | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/205) |
| **Ferrocarril de Sóller** (Tren de Fusta de Sóller (Palma - Bunyola - Sóller)) | Palma (Plaça d'Espanya), Son Sardina, Bunyola, Mirador des Pujol d'en Banya | [Consultar Horaris Oficials 🔗](http://trendesoller.com/) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Bunyola poble
- **Passos per Finques Privades:** Camí de sa Coma
- **Punts d'Interès Cultural i Natural:** Cim de na Francessa (754m), Vistes a la vall de Sóller i Palma

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Pujada directa amb fort pendent.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Binicanella (Casa de Colònies)** | Fundació Pere Tarrés | 80 pers. | **1.04 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/binicanella-bunyola.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **S'Olivaret (Alaró)** | **6.4 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/solivaret-alaro.md) |
| **Ca Ses Monges** | **6.8 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/ca-ses-monges-santa-maria.md) |
| **Castell d'Alaró (Hostatgeria i Refugi)** | **6.9 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/castell-d-alaro-hostatgeria.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Nuredduna** | Bunyola / Palmanyola | **3.7 km** | [Veure Casal](../agrupaments/aeg-nuredduna.md) |
| **AEG Soca-Arrel** | Marratxí | **5.4 km** | [Veure Casal](../agrupaments/aeg-soca-arrel.md) |

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

