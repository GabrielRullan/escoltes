# 🏔️ Penya de les Sínies i Reserva de Puigpunyent

Itinerari familiar boscós al peu del Galatzó.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-penya-de-sa-foradada-puigpunyent" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_penya_de_sa_foradada_puigpunyent() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_penya_de_sa_foradada_puigpunyent, 200);
        return;
    }
    
    const trackPoints = [[39.623, 2.528]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-penya-de-sa-foradada-puigpunyent');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Penya de les Sínies i Reserva de Puigpunyent");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Penya de les Sínies i Reserva de Puigpunyent");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.623, 2.528], 14);
        L.marker([39.623, 2.528]).addTo(rMap).bindPopup("<b>Penya de les Sínies i Reserva de Puigpunyent</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_penya_de_sa_foradada_puigpunyent);
setTimeout(initRouteTrackMap_penya_de_sa_foradada_puigpunyent, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Puigpunyent** |
| **Zona / Comarca** | **Tramuntana Sud** |
| **Distància Total** | **5.0 km** |
| **Desnivell Positiu** | **+160 m** |
| **Dificultat Tècnica** | **Fàcil** |
| **Durada Estimada** | **2h 00min** |
| **Unitats Recomanades** | **Castors/Fures, Llops/Daines** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Penya%20de%20les%20S%C3%ADnies%20i%20Reserva%20de%20Puigpunyent)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Puigpunyent**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 202** (Palma - Estellencs) | Palma, Puigpunyent, Banyalbufar, Estellencs vila | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/202) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Puigpunyent poble
- **Passos per Finques Privades:** La Reserva de Puigpunyent
- **Punts d'Interès Cultural i Natural:** Bosc de la Tramuntana sud, Salts d'aigua i vegetació

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Apte per a branques joves.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)

> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.

### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Maristel·la (Ermita i Terreny)** | **5.8 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/maristella-esporles.md) |
| **Refugi de la Finca Pública de Galatzó** | **6.0 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/finca-de-galatzo-refugi.md) |
| **Refugi de Sa Coma d'en Vidal** | **6.5 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/sa-coma-den-vidal.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Son Sardina** | Palma | **10.7 km** | [Veure Casal](../agrupaments/aeg-son-sardina.md) |
| **AEG Reina Constança de Mallorca** | Palma | **11.2 km** | [Veure Casal](../agrupaments/aeg-reina-constanca.md) |

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

