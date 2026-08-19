# 🏔️ Parc Natural de Mondragó (Santanyí)

Ruta litoral per un dels parcs naturals més frondosos i ben conservats del sud de Mallorca, combinant estanys d'aigua dolça, pinedes i platges verges.

---

## 🗺️ Mapa i Traçat Exacte de la Ruta (Track Polyline)


<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div id="map-route-parc-natural-mondrago" style="width: 100%; height: 380px; border-radius: 10px; border: 1px solid #ccc; box-shadow: 0 4px 12px rgba(0,0,0,0.12); margin-bottom: 16px;"></div>

<script>
function initRouteTrackMap_parc_natural_mondrago() {
    if (typeof L === 'undefined') {
        setTimeout(initRouteTrackMap_parc_natural_mondrago, 200);
        return;
    }
    
    const trackPoints = [[39.352, 3.189], [39.356, 3.192], [39.359, 3.196]];
    const itinerariPassos = [{"pas": 1, "nom": "Centre d'Interpretació", "desc": "Inici al pàrquing de sa Font de n'Alis."}, {"pas": 2, "nom": "Estany i Platja de s'Amarador", "desc": "Sendera de fusta que voreja la marjal."}, {"pas": 3, "nom": "Mirador des Cap des Moro", "desc": "Vistes a les penyes litorals del sud."}];
    
    const rMap = L.map('map-route-parc-natural-mondrago');
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
        
        L.marker(trackPoints[0]).addTo(rMap).bindPopup("<b>🚀 Punt d'Inici:</b> Parc Natural de Mondragó (Santanyí)");
        L.marker(trackPoints[trackPoints.length - 1]).addTo(rMap).bindPopup("<b>🏁 Arribada / Destí:</b> Parc Natural de Mondragó (Santanyí)");
        
        rMap.fitBounds(polyline.getBounds(), { padding: [30, 30] });
    } else {
        rMap.setView([39.352, 3.189], 14);
        L.marker([39.352, 3.189]).addTo(rMap).bindPopup("<b>Parc Natural de Mondragó (Santanyí)</b>");
    }
}

document.addEventListener('DOMContentLoaded', initRouteTrackMap_parc_natural_mondrago);
setTimeout(initRouteTrackMap_parc_natural_mondrago, 400);
</script>


---

## 📊 Fitxa Tècnica

| Paràmetre | Valor |
| :--- | :--- |
| **Municipi / Poble** | **Santanyí** |
| **Zona / Comarca** | **Migjorn** |
| **Distància Total** | **5.2 km** |
| **Desnivell Positiu** | **+40 m** |
| **Dificultat Tècnica** | **Molt Fàcil** |
| **Durada Estimada** | **2h 00min** |
| **Unitats Recomanades** | **Castors/Fures, Llops/Daines, Pioners/Rangers, Rovers/Rutes** |
| **Track a Wikiloc** | **[💚 Cercar Track a Wikiloc 🔗](https://www.wikiloc.com/wikiloc/map.do?q=Parc%20Natural%20de%20Mondrag%C3%B3%20%28Santany%C3%AD%29)** |

---

## 🥾 Itinerari i Rumb de la Ruta Pas a Pas

| Pas | Punt de Referència / Tram | Indicacions i Descripció |
| :---: | :--- | :--- |
| **Pas 1** | **Centre d'Interpretació** | Inici al pàrquing de sa Font de n'Alis. |
| **Pas 2** | **Estany i Platja de s'Amarador** | Sendera de fusta que voreja la marjal. |
| **Pas 3** | **Mirador des Cap des Moro** | Vistes a les penyes litorals del sud. |

---

## 🚌 Transport Públic i Trens Més Propers (TIB / SFM)

A continuació es detallen les línies de bus del TIB i trens de Mallorca (SFM / Sóller) més propers a l'inici del municipi de **Santanyí**:

| Línia TIB / Tren | Trayecte i Parades Clau | Horaris Oficials |
| :--- | :--- | :--- |
| **TIB 517** (Campos - Santanyí - Cala Mondragó) | Campos, Santanyí, s'Amarador, Cala Mondragó | [Consultar Horaris Oficials 🔗](https://www.tib.org/ca/web/ctm/autobus/linia/517) |


---

## 💧 Aigua, Passos i Interès

- **Punts d'Aigua Potable / Recàrrega:** Centre d'Informació del Parc Natural (sa Font de n'Alis)
- **Passos per Finques Privades:** Parc Natural Protegit (públic)
- **Punts d'Interès Cultural i Natural:** Cala Mondragó, s'Amarador, Estany de sa Font de n'Alis, Mirador des Cap des Moro

> [!WARNING]
> **Consells de Seguretat i Prevenció**:
> Portar protecció solar i aigua a l'estiu.

---

## 📍 Relació Realista de Mobilitat i Terrenys d'Acampada

### ⛺ Zones d'Acampada directament accessibles a peu (<= 2.0 km de la ruta)

> [!NOTE]
> **Sense pernoctació directa a peu**: Aquesta ruta no disposa de cap terreny d'acampada ni refugi a menys de 2.0 km de l'inici o del trajecte. Cal preveure transport per al desplaçament a la zona de pernoctació.


### ⚜️ Agrupaments Escoltes Més Propers (Suport Logístic i Emergència)
| Agrupament / Casal | Municipi | Distància | Enllaç |
| :--- | :--- | :---: | :--- |
| **Grupo Scout Myotragus 684** | Llucmajor | **40.9 km** | [Veure Casal](../agrupaments/gs-myotragus-684.md) |
| **AEG Pedra Viva** | Binissalem | **48.1 km** | [Veure Casal](../agrupaments/aeg-pedra-viva.md) |
