# 🏔️ Esporles a Banyalbufar pel Camí des Correu

El camí històric medieval més popular de la Tramuntana sud.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-puig-des-teix-espolres" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_puig_des_teix_espolres() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_puig_des_teix_espolres, 200);
        return;
    }
    
    const trackPoints = [[39.668, 2.548]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-puig-des-teix-espolres');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Esporles a Banyalbufar pel Camí des Correu");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Esporles a Banyalbufar pel Camí des Correu");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.668, 2.548], 14);
        L.marker([39.668, 2.548]).addTo(rMap).bindPopup("<b>Esporles a Banyalbufar pel Camí des Correu</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_puig_des_teix_espolres);
setTimeout(initRouteTrackMap_puig_des_teix_espolres, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Esporles / Banyalbufar** |
| **Zona / Comarca** | **Tramuntana Sud** |
| **Distància Total** | **8.2 km** |
| **Desnivell Positiu** | **+280 m** |
| **Dificultat Tècnica** | **Fàcil - Moderada** |
| **Durada Estimada** | **2h 45min** |
| **Unitats Recomanades** | **Castors/Fures, Llops/Daines, Pioners/Rangers** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Esporles%20a%20Banyalbufar%20pel%20Cam%C3%AD%20des%20Correu)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Esporles / Banyalbufar**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 202** (Palma - Estellencs) | Palma, Puigpunyent, Banyalbufar, Estellencs vila | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/202) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Esporles, Banyalbufar
- **Passos per Finques Privades:** Camí des Correu públic
- **Punts d'Interès Cultural i Natural:** Empedrat medieval des Correu, Vistes al mar de Banyalbufar

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Ruta lineal de fàcil orientació.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Maristel·la (Ermita i Terreny)** | Obreria de Maristel·la | 35 pers. | **1.85 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/maristella-esporles.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Refugi de Son Moragues** | **8.6 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-son-moragues.md) |
| **Refugi de Sa Coma d'en Vidal** | **8.6 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/sa-coma-den-vidal.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Son Sardina** | Palma | **10.7 km** | [Veure Casal](../agrupaments/aeg-son-sardina.md) |
| **AEG Nuredduna** | Bunyola / Palmanyola | **12.9 km** | [Veure Casal](../agrupaments/aeg-nuredduna.md) |
