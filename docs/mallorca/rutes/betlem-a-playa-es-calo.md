# 🏔️ Excursió de Betlem a Platja des Caló (Artà)

Plàcida passejada litoral per la costa nord d'Artà que connecta les darreres cases de Betlem amb la platja verge i refugi de pescadors des Caló.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-betlem-a-playa-es-calo" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_betlem_a_playa_es_calo() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_betlem_a_playa_es_calo, 200);
        return;
    }
    
    const trackPoints = [[39.755, 3.328], [39.761, 3.341], [39.769, 3.355]];
    const itinerariPassos = [{"pas": 1, "nom": "Inici a la urbanització de Betlem", "desc": "Fi de l'asfalt al carrer de la badia de Betlem."}, {"pas": 2, "nom": "Camí de sa Cova des Pescadors", "desc": "Sendera plana que discorre entre la pineda i la mar."}, {"pas": 3, "nom": "Arribada a es Caló", "desc": "Embarcador tradicional de fusta i platja verge."}];
    
    const rMap = L.map('map-route-betlem-a-playa-es-calo');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Excursió de Betlem a Platja des Caló (Artà)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Excursió de Betlem a Platja des Caló (Artà)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.755, 3.328], 14);
        L.marker([39.755, 3.328]).addTo(rMap).bindPopup("<b>Excursió de Betlem a Platja des Caló (Artà)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_betlem_a_playa_es_calo);
setTimeout(initRouteTrackMap_betlem_a_playa_es_calo, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Artà** |
| **Zona / Comarca** | **Llevant** |
| **Distància Total** | **7.0 km** |
| **Desnivell Positiu** | **+80 m** |
| **Dificultat Tècnica** | **Molt Fàcil** |
| **Durada Estimada** | **2h 15min** |
| **Unitats Recomanades** | **Castors/Fures, Llops/Daines, Pioners/Rangers, Rovers/Rutes** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Excursi%C3%B3%20de%20Betlem%20a%20Platja%20des%20Cal%C3%B3%20%28Art%C3%A0%29)** |
| **Guia Turisme Petit** | **[👶 Veure Guia de Família a Turisme Petit 🔗](https://www.turismepetit.com/excursion/excursion-de-betlem-a-playa-es-calo/)** |

---

## 🥾 Itinerari i Rumb de la Ruta Pas a Pas

| Pas | Punt de Referència / Tram | Indicacions i Descripció |
| :---: | :--- | :--- |
| **Pas 1** | **Inici a la urbanització de Betlem** | Fi de l'asfalt al carrer de la badia de Betlem. |
| **Pas 2** | **Camí de sa Cova des Pescadors** | Sendera plana que discorre entre la pineda i la mar. |
| **Pas 3** | **Arribada a es Caló** | Embarcador tradicional de fusta i platja verge. |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Artà**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 411** (Manacor - Artà - Capdepera - Cala Rajada) | Manacor (Estació), Artà, Cala Rajada | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/411) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Llogaret de Betlem
- **Passos per Finques Privades:** Sender públic del Parc Natural de Llevant
- **Punts d'Interès Cultural i Natural:** Platja verge des Caló, Llogaret de Betlem, Vistes a la Badia d'Alcúdia

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Ruta molt accessible amb ombres parcials. Ideal per a la branca de Castors i Llops.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)
| Refugi / Zona d'Acampada | Titularitat | Capacitat | Distància a peu | Enllaç |
| :--- | :--- | :---: | :---: | :--- |
| **Betlem (Colònia de Sant Pere)** | Ajuntament d'Artà | 40 pers. | **1.11 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/betlem-colonia-sant-pere.md) |
| **Casa de s'Alzina (Albarca)** | IBANAT (Govern de les Illes Balears) | 10 pers. | **1.15 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/casa-de-salzina-albarca.md) |
| **Sant Guillem i Sant Antoni** | Gestió Entitat | 35 pers. | **1.68 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/sant-guillem-i-sant-antoni-betlem.md) |
| **Refugi de S'Arenalet d'es Verger** | IBANAT / Parc Natural de Llevant | 22 pers. | **2.00 km** (🟢 Accessible a peu) | [Veure Refugi](../acampada/refugi-s-arenalet.md) |
### 🚌 Refugis/Acampades que requereixen transport (> 2.0 km)
| Refugi | Distància | Recomanació Logística | Enllaç |
| :--- | :---: | :--- | :--- |
| **Caseta dels Oguers** | **2.2 km** | Requereix autocar/vehicle de suport des de la ruta | [Veure Refugi](../acampada/caseta-dels-oguers-arta.md) |

### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **AEG Sa Marjal** | Sa Pobla | **26.0 km** | [Veure Casal](../agrupaments/aeg-sa-marjal.md) |
| **AEG Pedra Viva** | Binissalem | **42.1 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |

---

## 💬 Experiències i Valoracions dels Agrupaments Escoltes

<div style="background-color: var(--md-code-bg-color, #f8f9fa); border: 1px solid #e0e0e0; padding: 18px; border-radius: 10px; margin-top: 16px;">
    <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-bottom: 16px; border-bottom: 1px solid #e0e0e0; padding-bottom: 12px;">
        <div>
            <h3 style="margin: 0; font-size: 1.15em; color: #00897b;">Valoració Mitjana: ⭐⭐⭐⭐⭐ 5.0 / 5</h3>
            <p style="margin: 4px 0 0 0; font-size: 0.85em; color: #666;">Basat en <b>1 experiències</b> compartides per caps escoltes.</p>
        </div>
        <a href="../../sop/enviar_experiencia/" style="padding: 8px 16px; background-color: #00897b; color: white; border-radius: 6px; text-decoration: none; font-weight: bold; font-size: 0.85em; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">📝 Compartir la meva experiència i consells 🔗</a>
    </div>
    <div style="display: flex; flex-direction: column; gap: 12px;">
        <div style="border: 1px solid #e0e0e0; border-radius: 8px; padding: 12px; background-color: #ffffff;">
            <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 6px; margin-bottom: 6px;">
                <span style="font-weight: bold; color: #333; font-size: 0.9em;">⚜️ [PROVA / DEMO] AEG Sa Marjal <span style="font-weight: normal; color: #666;">(Llops/Daines)</span></span>
                <span style="font-size: 0.8em; color: #f57f17; font-weight: bold;">⭐⭐⭐⭐⭐ (Abril 2025 (Exemple))</span>
            </div>
            <p style="margin: 0; font-size: 0.85em; color: #444; line-height: 1.4;"><i>"[EXEMPLE DE PROVA] Comentari de prova del cercador. Ruta litoral preciosa a la Colònia de Sant Pere / Artà."</i></p>
        </div>
    </div>
</div>

