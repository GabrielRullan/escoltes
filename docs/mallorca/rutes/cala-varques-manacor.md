# 🏔️ Cala Varques des de les Coves del Pirata (Manacor)

Passejada pineda litoral fins a la verge Cala Varques i el seu pont de roca.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-cala-varques-manacor" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_cala_varques_manacor() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_cala_varques_manacor, 200);
        return;
    }
    
    const trackPoints = [[39.502, 3.285]];
    const itinerariPassos = [];
    
    const rMap = L.map('map-route-cala-varques-manacor');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Cala Varques des de les Coves del Pirata (Manacor)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Cala Varques des de les Coves del Pirata (Manacor)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.502, 3.285], 14);
        L.marker([39.502, 3.285]).addTo(rMap).bindPopup("<b>Cala Varques des de les Coves del Pirata (Manacor)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_cala_varques_manacor);
setTimeout(initRouteTrackMap_cala_varques_manacor, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Manacor** |
| **Zona / Comarca** | **Llevant** |
| **Distància Total** | **6.0 km** |
| **Desnivell Positiu** | **+45 m** |
| **Dificultat Tècnica** | **Fàcil** |
| **Durada Estimada** | **2h 00min** |
| **Unitats Recomanades** | **Llops/Daines, Pioners/Rangers** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Cala%20Varques%20des%20de%20les%20Coves%20del%20Pirata%20%28Manacor%29)** |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Manacor**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 401** (Palma - Manacor - Cala Millor) | Palma, Manacor (Estació), Porto Cristo | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/401) |
| **SFM Línia T3** (Tren Palma - Inca - Sineu - Manacor) | Inca, Sineu, Petra, Manacor (Estació) | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/tren/linia/T3) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Cap punt d'aigua - portar 2L
- **Passos per Finques Privades:** Camí de Cala Varques
- **Punts d'Interès Cultural i Natural:** Cala Varques, Pont natural de roca, Coves de la costa

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Molt calorós a l'estiu. Prohibit fer foc.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)

> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.

### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Puig d'Alanar** | **4.5 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/puig-dalanar-manacor.md) |
| **Sa Murtera** | **8.5 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/sa-murtera-manacor.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Sa Marjal** | Sa Pobla | **37.2 km** | [Veure Casal](../agrupaments/aeg-sa-marjal.md) |
| **AEG Pedra Viva** | Binissalem | **43.4 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |

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

