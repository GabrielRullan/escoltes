# 🏔️ Finca Pública de Planícia (Banyalbufar)

Ruta semicircular per una de les possessions públiques més emblemàtiques de la serra de Tramuntana, entre alzinars centenaris, fonts i l'antiga tafona d'oli.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-finca-publica-planicia-banyalbufar" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_finca_publica_planicia_banyalbufar() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_finca_publica_planicia_banyalbufar, 200);
        return;
    }
    
    const trackPoints = [[39.678, 2.498], [39.685, 2.508], [39.692, 2.516]];
    const itinerariPassos = [{"pas": 1, "nom": "Entrada de la Ma-10", "desc": "Aparcament a l'accés de la Finca de Planícia."}, {"pas": 2, "nom": "Cases de Planícia", "desc": "Arribada al nucli històric i tafona de la finca."}, {"pas": 3, "nom": "Font de sa Mentida", "desc": "Retorn circular per l'alzinar alt."}];
    
    const rMap = L.map('map-route-finca-publica-planicia-banyalbufar');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Finca Pública de Planícia (Banyalbufar)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Finca Pública de Planícia (Banyalbufar)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.678, 2.498], 14);
        L.marker([39.678, 2.498]).addTo(rMap).bindPopup("<b>Finca Pública de Planícia (Banyalbufar)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_finca_publica_planicia_banyalbufar);
setTimeout(initRouteTrackMap_finca_publica_planicia_banyalbufar, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Banyalbufar** |
| **Zona / Comarca** | **Tramuntana Sud** |
| **Distància Total** | **9.2 km** |
| **Desnivell Positiu** | **+320 m** |
| **Dificultat Tècnica** | **Moderada** |
| **Durada Estimada** | **3h 15min** |
| **Unitats Recomanades** | **Llops/Daines, Pioners/Rangers, Rovers/Rutes** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Finca%20P%C3%BAblica%20de%20Plan%C3%ADcia%20%28Banyalbufar%29)** |
| **Guia Turisme Petit** | **[👶 Veure Guia de Família a Turisme Petit 🔗](https://www.turismepetit.com/excursion/excursion-semicircular-por-la-finca-publica-de-planicia/)** |

---

## 🥾 Itinerari i Rumb de la Ruta Pas a Pas

| Pas | Punt de Referència / Tram | Indicacions i Descripció |
| :---: | :--- | :--- |
| **Pas 1** | **Entrada de la Ma-10** | Aparcament a l'accés de la Finca de Planícia. |
| **Pas 2** | **Cases de Planícia** | Arribada al nucli històric i tafona de la finca. |
| **Pas 3** | **Font de sa Mentida** | Retorn circular per l'alzinar alt. |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Banyalbufar**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 202** (Palma - Estellencs) | Palma, Puigpunyent, Banyalbufar, Estellencs vila | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/202) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Font de Planícia, Cases de Planícia
- **Passos per Finques Privades:** Finca Pública de Planícia (Govern de les Illes Balears)
- **Punts d'Interès Cultural i Natural:** Cases de Planícia, Alabern, Font de sa Mentida, Tafona tradicional

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Finca pública de gran extensió. Seguir els itineraris senyalitzats.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)

> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.

### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Refugi de Sa Coma d'en Vidal** | **5.8 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/sa-coma-den-vidal.md) |
| **Maristel·la (Ermita i Terreny)** | **6.3 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/maristella-esporles.md) |
| **Refugi de la Finca Pública de Galatzó** | **8.7 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/finca-de-galatzo-refugi.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Son Sardina** | Palma | **14.9 km** | [Veure Casal](../agrupaments/aeg-son-sardina.md) |
| **AEG Reina Constança de Mallorca** | Palma | **17.0 km** | [Veure Casal](../agrupaments/aeg-reina-constanca.md) |

---

## 💬 Experiències i Valoracions dels Agrupaments Escoltes

<div style="background-color: var(--md-code-bg-color, #f8f9fa); border: 1px solid #e0e0e0; padding: 18px; border-radius: 10px; margin-top: 16px;">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 16px; border-bottom: 1px solid #e0e0e0; padding-bottom: 12px;">
        <div>
            <h3 style="margin: 0; font-size: 1.15em; color: #00897b;">Valoració Mitjana: ⭐⭐⭐⭐ 4.0 / 5</h3>
            <p style="margin: 4px 0 0 0; font-size: 0.85em; color: #666;">Basat en <b>1 experiències</b> compartides per caps escoltes.</p>
        </div>
        <a href="https://docs.google.com/forms/d/e/1FAIpQLScoutsMallorcaRutes/viewform" target="_blank" style="padding: 8px 16px; background-color: #00897b; color: white; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 0.85em; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">📝 Compartir la meva experiència i consells 🔗</a>
    </div>
    <div style="display: flex; flex-direction: column; gap: 12px;">
        <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 12px; background-color: #ffffff;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 6px; margin-bottom: 6px;">
                <span style="font-weight: bold; color: #333; font-size: 0.9em;">⚜️ AEG Verge de Lluc <span style="font-weight: normal; color: #666;">(Pioners/Rangers)</span></span>
                <span style="font-size: 0.8em; color: #f57f17; font-weight: bold;">⭐⭐⭐⭐ (Tardor 2025)</span>
            </div>
            <p style="margin: 0; font-size: 0.85em; color: #444; line-height: 1.4;"><i>"Finca pública de l'IBANAT molt completa amb albellons, aljubs i cases senyorials. Bona ombra i pistes amples."</i></p>
        </div>
    </div>
</div>

