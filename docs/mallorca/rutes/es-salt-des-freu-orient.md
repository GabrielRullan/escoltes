# 🏔️ Es Salt des Freu (Orient / Bunyola)

Una de les excursions de família i escoltes més populars de Mallorca. Un passeig plàcid per l'alzinar que condueix a les espectaculars cascades del Salt des Freu.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-es-salt-des-freu-orient" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_es_salt_des_freu_orient() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_es_salt_des_freu_orient, 200);
        return;
    }
    
    const trackPoints = [[39.721, 2.768], [39.725, 2.772], [39.729, 2.778]];
    const itinerariPassos = [{"pas": 1, "nom": "Inici a la carretera d'Orient", "desc": "Aparcament al km 8.5 de la Ma-2100."}, {"pas": 2, "nom": "Pineda i Alzinar des Freu", "desc": "Sender ample en descens suau."}, {"pas": 3, "nom": "Cascada des Salt des Freu", "desc": "Arribada a les pozes i salts d'aigua."}];
    
    const rMap = L.map('map-route-es-salt-des-freu-orient');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Es Salt des Freu (Orient / Bunyola)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Es Salt des Freu (Orient / Bunyola)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.721, 2.768], 14);
        L.marker([39.721, 2.768]).addTo(rMap).bindPopup("<b>Es Salt des Freu (Orient / Bunyola)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_es_salt_des_freu_orient);
setTimeout(initRouteTrackMap_es_salt_des_freu_orient, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Bunyola** |
| **Zona / Comarca** | **Tramuntana Central** |
| **Distància Total** | **4.5 km** |
| **Desnivell Positiu** | **+120 m** |
| **Dificultat Tècnica** | **Molt Fàcil** |
| **Durada Estimada** | **1h 45min** |
| **Unitats Recomanades** | **Castors/Fures, Llops/Daines, Pioners/Rangers, Rovers/Rutes** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Es%20Salt%20des%20Freu%20%28Orient%20/%20Bunyola%29)** |

---

## 🥾 Itinerari i Rumb de la Ruta Pas a Pas

| Pas | Punt de Referència / Tram | Indicacions i Descripció |
| :---: | :--- | :--- |
| **Pas 1** | **Inici a la carretera d'Orient** | Aparcament al km 8.5 de la Ma-2100. |
| **Pas 2** | **Pineda i Alzinar des Freu** | Sender ample en descens suau. |
| **Pas 3** | **Cascada des Salt des Freu** | Arribada a les pozes i salts d'aigua. |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Bunyola**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 205** (Palma - Bunyola - Orient) | Palma, Raixa, Bunyola, Orient | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/205) |
| **Ferrocarril de Sóller** (Tren de Fusta de Sóller (Palma - Bunyola - Sóller)) | Palma (Plaça d'Espanya), Son Sardina, Bunyola, Mirador des Pujol d'en Banya | [Consultar Horaris Oficials 🔗](http://trendesoller.com/) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Font de Cals Reis (Orient)
- **Passos per Finques Privades:** Camí des Freu (públic)
- **Punts d'Interès Cultural i Natural:** Salt d'aigua des Freu, Bosc de la Comuna de Bunyola, Vila d'Orient

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Atenció a les pedres resbaladisses devora el torrent en època de pluges.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **S'Olivaret (Alaró)** | Gestió Privada | 40 pers. | **1.56 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/solivaret-alaro.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Castell d'Alaró (Hostatgeria i Refugi)** | **2.9 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/castell-d-alaro-hostatgeria.md) |
| **Refugi de Tossals Verds** | **6.2 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/refugi-tossals-verds.md) |
| **Binicanella (Casa de Colònies)** | **6.4 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/binicanella-bunyola.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Capità Angelats** | Sóller | **6.8 km** | [Veure Casal](../agrupaments/aeg-capita-angelats.md) |
| **AEG Pedra Viva** | Binissalem | **7.1 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |

---

## 💬 Experiències i Valoracions dels Agrupaments Escoltes

<div style="background-color: var(--md-code-bg-color, #f8f9fa); border: 1px solid #e0e0e0; padding: 18px; border-radius: 10px; margin-top: 16px;">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 16px; border-bottom: 1px solid #e0e0e0; padding-bottom: 12px;">
        <div>
            <h3 style="margin: 0; font-size: 1.15em; color: #00897b;">Valoració Mitjana: ⭐⭐⭐⭐ 4.5 / 5</h3>
            <p style="margin: 4px 0 0 0; font-size: 0.85em; color: #666;">Basat en <b>2 experiències</b> compartides per caps escoltes.</p>
        </div>
        <a href="../../sop/enviar_experiencia/" style="padding: 8px 16px; background-color: #00897b; color: white; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 0.85em; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">📝 Compartir la meva experiència i consells 🔗</a>
    </div>
    <div style="display: flex; flex-direction: column; gap: 12px;">
        <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 12px; background-color: #ffffff;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 6px; margin-bottom: 6px;">
                <span style="font-weight: bold; color: #333; font-size: 0.9em;">⚜️ [PROVA / DEMO] AEG Eladi Homs <span style="font-weight: normal; color: #666;">(Llops/Daines)</span></span>
                <span style="font-size: 0.8em; color: #f57f17; font-weight: bold;">⭐⭐⭐⭐⭐ (Novembre 2025 (Exemple))</span>
            </div>
            <p style="margin: 0; font-size: 0.85em; color: #444; line-height: 1.4;"><i>"[EXEMPLE DE PROVA] Ruta de mostra per provar la interfície. El bosc d'alzines ofereix molta ombra i el camí és fàcil de seguir. Si ha plogut els dies anteriors, el Salt des Freu porta molta aigua."</i></p>
        </div>
        <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 12px; background-color: #ffffff;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 6px; margin-bottom: 6px;">
                <span style="font-weight: bold; color: #333; font-size: 0.9em;">⚜️ [PROVA / DEMO] AEG Jaume I <span style="font-weight: normal; color: #666;">(Pioners/Rangers)</span></span>
                <span style="font-size: 0.8em; color: #f57f17; font-weight: bold;">⭐⭐⭐⭐ (Octubre 2025 (Exemple))</span>
            </div>
            <p style="margin: 0; font-size: 0.85em; color: #444; line-height: 1.4;"><i>"[EXEMPLE DE PROVA] Comentari de mostra per testar el sistema de ressenyes d'agrupaments. Recomanam dur calçat de recanvi per si s'ha de creuar el torrent."</i></p>
        </div>
    </div>
</div>

