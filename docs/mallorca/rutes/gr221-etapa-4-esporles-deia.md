# 🏔️ GR-221 Etapa 4: Esporles a Deià

Espectacular travessa que connecta Esporles amb Valldemossa i ascendeix pel Camí de s'Arxiduc abans de baixar al poble de Deià.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-gr221-etapa-4-esporles-deia" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_gr221_etapa_4_esporles_deia() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_gr221_etapa_4_esporles_deia, 200);
        return;
    }
    
    const trackPoints = [[39.6689, 2.5769], [39.7119, 2.6225], [39.728, 2.635], [39.7491, 2.6483]];
    const itinerariPassos = [{"pas": 1, "nom": "Esporles a Valldemossa", "desc": "Pujada per sa Comuna d'Esporles i baixada cap a Valldemossa."}, {"pas": 2, "nom": "Valldemossa a sa Coma des Cairats", "desc": "Ascensió cap al Pla des Pouet i la serra de s'Arxiduc."}, {"pas": 3, "nom": "Camí de s'Arxiduc", "desc": "Cresta panoràmica sobre la mar de Deià i sa Foradada."}, {"pas": 4, "nom": "Descens a Deià i Refugi Can Boi", "desc": "Baixada de pedra empedrada fins al centre de Deià."}];
    
    const rMap = L.map('map-route-gr221-etapa-4-esporles-deia');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> GR-221 Etapa 4: Esporles a Deià");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> GR-221 Etapa 4: Esporles a Deià");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.6689, 2.5769], 14);
        L.marker([39.6689, 2.5769]).addTo(rMap).bindPopup("<b>GR-221 Etapa 4: Esporles a Deià</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_gr221_etapa_4_esporles_deia);
setTimeout(initRouteTrackMap_gr221_etapa_4_esporles_deia, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Esporles / Valldemossa / Deià** |
| **Zona / Comarca** | **Tramuntana Central** |
| **Distància Total** | **19.6 km** |
| **Desnivell Positiu** | **+890 m** |
| **Dificultat Tècnica** | **Exigent** |
| **Durada Estimada** | **6h 45min** |
| **Unitats Recomanades** | **Pioners/Rangers, Rovers/Rutes** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=GR-221%20Etapa%204%3A%20Esporles%20a%20Dei%C3%A0)** |

---

## 🥾 Itinerari i Rumb de la Ruta Pas a Pas

| Pas | Punt de Referència / Tram | Indicacions i Descripció |
| :---: | :--- | :--- |
| **Pas 1** | **Esporles a Valldemossa** | Pujada per sa Comuna d'Esporles i baixada cap a Valldemossa. |
| **Pas 2** | **Valldemossa a sa Coma des Cairats** | Ascensió cap al Pla des Pouet i la serra de s'Arxiduc. |
| **Pas 3** | **Camí de s'Arxiduc** | Cresta panoràmica sobre la mar de Deià i sa Foradada. |
| **Pas 4** | **Descens a Deià i Refugi Can Boi** | Baixada de pedra empedrada fins al centre de Deià. |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Esporles / Valldemossa / Deià**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 203** (Palma - Valldemossa - Deià - Sóller) | Palma, Valldemossa, Son Marroig, Deià | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/203) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Esporles vila, Valldemossa vila, Deià vila (Refugi Can Boi)
- **Passos per Finques Privades:** Camí de sa Coma des Cairats, Pla des Pouet
- **Punts d'Interès Cultural i Natural:** Muntanya de sa Comuna, Valldemossa, Camí de s'Arxiduc, Son Marroig

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Etapa llarga amb desnivell acusat. Cal estar atents a la boira a la cresta de s'Arxiduc.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Maristel·la (Ermita i Terreny)** | Obreria de Maristel·la | 35 pers. | **0.87 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/maristella-esporles.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Refugi de Son Moragues** | **6.7 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-son-moragues.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Son Sardina** | Palma | **8.8 km** | [Veure Casal](../agrupaments/aeg-son-sardina.md) |
| **AEG Nuredduna** | Bunyola / Palmanyola | **10.4 km** | [Veure Casal](../agrupaments/aeg-nuredduna.md) |

---

## 💬 Experiències i Valoracions dels Agrupaments Escoltes

<div style="background-color: var(--md-code-bg-color, #f8f9fa); border: 1px solid #e0e0e0; padding: 18px; border-radius: 10px; margin-top: 16px;">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
        <div>
            <h3 style="margin: 0; font-size: 1.05em; color: #555;">Encara no hi ha cap experiència registrada per a aquesta ruta.</h3>
            <p style="margin: 4px 0 0 0; font-size: 0.85em; color: #666;">Heu fet aquesta ruta amb la vostra unitat? Sigueu els primers a deixar consells per a altres agrupaments!</p>
        </div>
        <a href="../../sop/enviar_experiencia/" style="padding: 8px 16px; background-color: #00897b; color: white; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 0.85em;">📝 Enviar la primera experiència 🔗</a>
    </div>
</div>

