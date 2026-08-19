# 🏔️ GR-221 Etapa 3: Estellencs a Esporles

Una de les etapes més històriques que recorre l'antic Camí des Correu entre Banyalbufar i Esporles travessant boscos d'alzinar.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-gr221-etapa-3-estellencs-esporles" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_gr221_etapa_3_estellencs_esporles() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_gr221_etapa_3_estellencs_esporles, 200);
        return;
    }
    
    const trackPoints = [[39.638, 2.455], [39.652, 2.481], [39.668, 2.512], [39.6689, 2.5769]];
    const itinerariPassos = [{"pas": 1, "nom": "Estellencs a Banyalbufar", "desc": "Tram pel vell camí de la marjades de Banyalbufar."}, {"pas": 2, "nom": "Banyalbufar Vila", "desc": "Punt de recàrrega d'aigua i menjar al poble."}, {"pas": 3, "nom": "Camí des Correu", "desc": "Pujada tradicional empedrada per l'alzinar d'Esporles."}, {"pas": 4, "nom": "Arribada a Esporles", "desc": "Descens suau fins al passeig d'Esporles."}];
    
    const rMap = L.map('map-route-gr221-etapa-3-estellencs-esporles');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> GR-221 Etapa 3: Estellencs a Esporles");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> GR-221 Etapa 3: Estellencs a Esporles");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.638, 2.455], 14);
        L.marker([39.638, 2.455]).addTo(rMap).bindPopup("<b>GR-221 Etapa 3: Estellencs a Esporles</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_gr221_etapa_3_estellencs_esporles);
setTimeout(initRouteTrackMap_gr221_etapa_3_estellencs_esporles, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Estellencs / Esporles** |
| **Zona / Comarca** | **Tramuntana Sud** |
| **Distància Total** | **15.2 km** |
| **Desnivell Positiu** | **+540 m** |
| **Dificultat Tècnica** | **Moderada** |
| **Durada Estimada** | **5h 15min** |
| **Unitats Recomanades** | **Llops/Daines, Pioners/Rangers, Rovers/Rutes** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=GR-221%20Etapa%203%3A%20Estellencs%20a%20Esporles)** |

---

## 🥾 Itinerari i Rumb de la Ruta Pas a Pas

| Pas | Punt de Referència / Tram | Indicacions i Descripció |
| :---: | :--- | :--- |
| **Pas 1** | **Estellencs a Banyalbufar** | Tram pel vell camí de la marjades de Banyalbufar. |
| **Pas 2** | **Banyalbufar Vila** | Punt de recàrrega d'aigua i menjar al poble. |
| **Pas 3** | **Camí des Correu** | Pujada tradicional empedrada per l'alzinar d'Esporles. |
| **Pas 4** | **Arribada a Esporles** | Descens suau fins al passeig d'Esporles. |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Estellencs / Esporles**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 202** (Palma - Estellencs) | Palma, Puigpunyent, Banyalbufar, Estellencs vila | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/202) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Font de sa Coma (Banyalbufar), Banyalbufar vila, Esporles vila
- **Passos per Finques Privades:** Camí des Correu (públic senyalitzat)
- **Punts d'Interès Cultural i Natural:** Marjades de Banyalbufar, Camí des Correu, Plana de sa Fita del Ram

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Tram molt ben senyalitzat. Cuidar els peus a la terregada de pedres del Camí des Correu.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Refugi de Sa Coma d'en Vidal** | Consell de Mallorca (Xarxa GR-221) | 24 pers. | **0.00 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/sa-coma-den-vidal.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Refugi de la Finca Pública de Galatzó** | **3.7 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/finca-de-galatzo-refugi.md) |
| **Refugi de Ses Fontanelles** | **6.4 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/ses-fontanelles-sant-elm.md) |
| **La Trapa (Zona d'Acampada)** | **9.4 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/la-trapa-andratx.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Son Sardina** | Palma | **17.1 km** | [Veure Casal](../agrupaments/aeg-son-sardina.md) |
| **AEG Reina Constança de Mallorca** | Palma | **17.5 km** | [Veure Casal](../agrupaments/aeg-reina-constanca.md) |
