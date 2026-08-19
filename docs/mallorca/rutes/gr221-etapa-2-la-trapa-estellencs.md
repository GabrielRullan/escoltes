# 🏔️ GR-221 Etapa 2: La Trapa a Estellencs

Etapa de transició de la Tramuntana sud que travessa el Coll de sa Gramola i les faldilles del puig de s'Esclop fins al poble d'Estellencs.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-gr221-etapa-2-la-trapa-estellencs" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_gr221_etapa_2_la_trapa_estellencs() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_gr221_etapa_2_la_trapa_estellencs, 200);
        return;
    }
    
    const trackPoints = [[39.598, 2.358], [39.608, 2.391], [39.621, 2.428], [39.638, 2.455]];
    const itinerariPassos = [{"pas": 1, "nom": "Sortida de la Trapa", "desc": "Ascensió pel pas de s'Escapçat fins a recuperar el camí alt."}, {"pas": 2, "nom": "Coll de sa Gramola", "desc": "Creuament de la carretera Ma-10 a la zona del coll de sa Gramola."}, {"pas": 3, "nom": "Ses Fontanelles", "desc": "Pas pel refugi privat de ses Fontanelles i ascens cap a la Coma d'en Vidal."}, {"pas": 4, "nom": "Arribada a Estellencs", "desc": "Baixada entre marjades d'oliveres fins al poble d'Estellencs."}];
    
    const rMap = L.map('map-route-gr221-etapa-2-la-trapa-estellencs');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> GR-221 Etapa 2: La Trapa a Estellencs");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> GR-221 Etapa 2: La Trapa a Estellencs");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.598, 2.358], 14);
        L.marker([39.598, 2.358]).addTo(rMap).bindPopup("<b>GR-221 Etapa 2: La Trapa a Estellencs</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_gr221_etapa_2_la_trapa_estellencs);
setTimeout(initRouteTrackMap_gr221_etapa_2_la_trapa_estellencs, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Andratx / Estellencs** |
| **Zona / Comarca** | **Tramuntana Sud** |
| **Distància Total** | **14.5 km** |
| **Desnivell Positiu** | **+620 m** |
| **Dificultat Tècnica** | **Exigent** |
| **Durada Estimada** | **5h 45min** |
| **Unitats Recomanades** | **Pioners/Rangers, Rovers/Rutes** |

---

## 🥾 Itinerari i Rumb de la Ruta Pas a Pas

| Pas | Punt de Referència / Tram | Indicacions i Descripció |
| :---: | :--- | :--- |
| **Pas 1** | **Sortida de la Trapa** | Ascensió pel pas de s'Escapçat fins a recuperar el camí alt. |
| **Pas 2** | **Coll de sa Gramola** | Creuament de la carretera Ma-10 a la zona del coll de sa Gramola. |
| **Pas 3** | **Ses Fontanelles** | Pas pel refugi privat de ses Fontanelles i ascens cap a la Coma d'en Vidal. |
| **Pas 4** | **Arribada a Estellencs** | Baixada entre marjades d'oliveres fins al poble d'Estellencs. |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Andratx / Estellencs**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 101** (Palma - Andratx - Port d'Andratx) | Palma (Estació Intermodal), Andratx (Grava), Port d'Andratx | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/101) |
| **TIB 102** (Palma - Sant Elm) | Palma, Andratx, Sant Elm (Plaça de na Caragola) | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/102) |
| **TIB 202** (Palma - Estellencs) | Palma, Puigpunyent, Banyalbufar, Estellencs vila | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/202) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Font de ses Fontanelles, Vila d'Estellencs
- **Passos per Finques Privades:** Pas de s'Escapçat, Ses Fontanelles (passos habilitats)
- **Punts d'Interès Cultural i Natural:** Coll de sa Gramola, Puig de s'Esclop, Vall d'Estellencs

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Atenció a la baixada del Pas de s'Escapçat amb terregada descomposada.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **La Trapa (Zona d'Acampada)** | GOB Mallorca | 25 pers. | **0.00 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/la-trapa-andratx.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Refugi de Ses Fontanelles** | **3.0 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/ses-fontanelles-sant-elm.md) |
| **Refugi de la Finca Pública de Galatzó** | **8.9 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/finca-de-galatzo-refugi.md) |
| **Refugi de Sa Coma d'en Vidal** | **9.4 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/sa-coma-den-vidal.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Reina Constança de Mallorca** | Palma | **24.4 km** | [Veure Casal](../agrupaments/aeg-reina-constanca.md) |
| **AEG Ramon Llull** | Palma | **25.2 km** | [Veure Casal](../agrupaments/aeg-ramon-llull.md) |
