# 🏔️ Fita del Ram i Ermita de Maristel·la (Esporles)

Excursió boscosa d'alzinar i patrimoni etnogràfic sobre la vila d'Esporles.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-fita-del-ram-maristella" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_fita_del_ram_maristella() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_fita_del_ram_maristella, 200);
        return;
    }
    
    const trackPoints = [[39.664, 2.569]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-fita-del-ram-maristella');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Fita del Ram i Ermita de Maristel·la (Esporles)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Fita del Ram i Ermita de Maristel·la (Esporles)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.664, 2.569], 14);
        L.marker([39.664, 2.569]).addTo(rMap).bindPopup("<b>Fita del Ram i Ermita de Maristel·la (Esporles)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_fita_del_ram_maristella);
setTimeout(initRouteTrackMap_fita_del_ram_maristella, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Esporles** |
| **Zona / Comarca** | **Tramuntana Sud** |
| **Distància Total** | **8.5 km** |
| **Desnivell Positiu** | **+520 m** |
| **Dificultat Tècnica** | **Moderada** |
| **Durada Estimada** | **3h 30min** |
| **Unitats Recomanades** | **Llops/Daines, Pioners/Rangers, Rovers/Rutes** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Fita%20del%20Ram%20i%20Ermita%20de%20Maristel%C2%B7la%20%28Esporles%29)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Esporles**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB / SFM Xarxa General** (Línia d'autobús o tren comarcal (Esporles)) | Esporles | [Consultar Horaris Oficials 🔗](https://www.tib.org/) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Esporles, Font de sa Sínia (Maristel·la)
- **Passos per Finques Privades:** Bosc de sa Granja
- **Punts d'Interès Cultural i Natural:** Ermita de Maristel·la, Cova dels Ermassets, Fita del Ram (833m)

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Terreny de lapiaz (karst) molt irregular a la carena superior.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Maristel·la (Ermita i Terreny)** | Obreria de Maristel·la | 35 pers. | **0.00 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/maristella-esporles.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Refugi de Son Moragues** | **7.6 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-son-moragues.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Son Sardina** | Palma | **9.0 km** | [Veure Casal](../agrupaments/aeg-son-sardina.md) |
| **AEG Nuredduna** | Bunyola / Palmanyola | **11.1 km** | [Veure Casal](../agrupaments/aeg-nuredduna.md) |
