# 🏔️ Puig de Galatzó (des de la Font des Pi)

Ascensió al cim piramidal més emblemàtic del ponent mallorquí.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-puig-de-galatzo-font-des-pi" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_puig_de_galatzo_font_des_pi() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_puig_de_galatzo_font_des_pi, 200);
        return;
    }
    
    const trackPoints = [[39.621, 2.478]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-puig-de-galatzo-font-des-pi');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Puig de Galatzó (des de la Font des Pi)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Puig de Galatzó (des de la Font des Pi)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.621, 2.478], 14);
        L.marker([39.621, 2.478]).addTo(rMap).bindPopup("<b>Puig de Galatzó (des de la Font des Pi)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_puig_de_galatzo_font_des_pi);
setTimeout(initRouteTrackMap_puig_de_galatzo_font_des_pi, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Puigpunyent / Estellencs** |
| **Zona / Comarca** | **Tramuntana Sud** |
| **Distància Total** | **11.2 km** |
| **Desnivell Positiu** | **+780 m** |
| **Dificultat Tècnica** | **Exigent** |
| **Durada Estimada** | **4h 45min** |
| **Unitats Recomanades** | **Pioners/Rangers, Rovers/Rutes** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Puig%20de%20Galatz%C3%B3%20%28des%20de%20la%20Font%20des%20Pi%29)** |
| **Guia Turisme Petit** | **[👶 Veure Guia de Família a Turisme Petit 🔗](https://www.turismepetit.com/excursion/excursion-a-la-finca-publica-de-galatzo/)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Puigpunyent / Estellencs**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 202** (Palma - Estellencs) | Palma, Puigpunyent, Banyalbufar, Estellencs vila | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/202) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Font des Pi (no sempre pot)
- **Passos per Finques Privades:** Finca Pública de Galatzó
- **Punts d'Interès Cultural i Natural:** Cim del Puig de Galatzó (1.027m), Ses Sínies, Pas de sa Sabata

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Tram final de grimpa rocosa. Prohibit en boira espessa o gel.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)

> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.

### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Refugi de la Finca Pública de Galatzó** | **2.2 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/finca-de-galatzo-refugi.md) |
| **Refugi de Sa Coma d'en Vidal** | **2.7 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/sa-coma-den-vidal.md) |
| **Refugi de Ses Fontanelles** | **7.6 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/ses-fontanelles-sant-elm.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Son Sardina** | Palma | **14.9 km** | [Veure Casal](../agrupaments/aeg-son-sardina.md) |
| **AEG Reina Constança de Mallorca** | Palma | **15.0 km** | [Veure Casal](../agrupaments/aeg-reina-constanca.md) |

---

## 💬 Experiències i Valoracions dels Agrupaments Escoltes

<div style="background-color: var(--md-code-bg-color, #f8f9fa); border: 1px solid #e0e0e0; padding: 18px; border-radius: 10px; margin-top: 16px;">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 16px; border-bottom: 1px solid #e0e0e0; padding-bottom: 12px;">
        <div>
            <h3 style="margin: 0; font-size: 1.15em; color: #00897b;">Valoració Mitjana: ⭐⭐⭐⭐⭐ 5.0 / 5</h3>
            <p style="margin: 4px 0 0 0; font-size: 0.85em; color: #666;">Basat en <b>1 experiències</b> compartides per caps escoltes.</p>
        </div>
        <a href="https://docs.google.com/forms/d/e/1FAIpQLScoutsMallorcaRutes/viewform" target="_blank" style="padding: 8px 16px; background-color: #00897b; color: white; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 0.85em; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">📝 Compartir la meva experiència i consells 🔗</a>
    </div>
    <div style="display: flex; flex-direction: column; gap: 12px;">
        <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 12px; background-color: #ffffff;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 6px; margin-bottom: 6px;">
                <span style="font-weight: bold; color: #333; font-size: 0.9em;">⚜️ [PROVA / DEMO] AEG Reina Constança <span style="font-weight: normal; color: #666;">(Rovers/Rutes)</span></span>
                <span style="font-size: 0.8em; color: #f57f17; font-weight: bold;">⭐⭐⭐⭐⭐ (Febrer 2026 (Exemple))</span>
            </div>
            <p style="margin: 0; font-size: 0.85em; color: #444; line-height: 1.4;"><i>"[EXEMPLE DE PROVA] Entrada de prova de demostració del formulari. Pujada exigent però molt agraïda."</i></p>
        </div>
    </div>
</div>

