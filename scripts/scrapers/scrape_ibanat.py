import os
import json

def get_ibanat_and_camping_data():
    refugis_and_camping = [
        {
            "slug": "refugi-tossals-verds",
            "nom": "Refugi de Tossals Verds",
            "titularitat": "Consell de Mallorca (Xarxa GR-221)",
            "municipi": "Escorca",
            "capacitat": 30,
            "serveis": ["Aigua potable", "Dormitoris", "Menjador", "Dutxes aigua calenta", "Calefacció"],
            "permis_antelacio": "Fins a 60 dies abans",
            "contacte": "971 17 37 00 / reserves@caminsdemallorca.cat",
            "restriccio_foc": "Estricta. Prohibit fer foc a l'exterior.",
            "acces_emergencia": "Camí rural accessible 4x4 des de la carretera de Lluc/Inca (Ma-2130)",
            "lat": 39.7583, "lon": 2.8222,
            "descripcio": "Refugi clau de la xarxa del GR-221 situat a la finca de Tossals Verds, punt estratègic per a la travessa de la Serra de Tramuntana."
        },
        {
            "slug": "refugi-son-amer",
            "nom": "Refugi de Son Amer",
            "titularitat": "Consell de Mallorca (Xarxa GR-221)",
            "municipi": "Escorca (Lluc)",
            "capacitat": 52,
            "serveis": ["Aigua potable", "Habitacions compartides", "Servei de menjador", "Dutxes", "Wi-Fi", "Accessibilitat reduïda"],
            "permis_antelacio": "Fins a 60 dies abans",
            "contacte": "971 51 71 09 / reserves@caminsdemallorca.cat",
            "restriccio_foc": "Prohibit fer foc.",
            "acces_emergencia": "Accés directe per vehicle des de Lluc Ma-10",
            "lat": 39.8215, "lon": 2.8872,
            "descripcio": "El refugi més gran del GR-221, situat sobre el puig de Son Amer amb vistes a la vall de Lluc i la serra de les Caubelles."
        },
        {
            "slug": "refugi-can-boi",
            "nom": "Refugi de Can Boi",
            "titularitat": "Consell de Mallorca (Xarxa GR-221)",
            "municipi": "Deià",
            "capacitat": 32,
            "serveis": ["Aigua potable", "Cuina", "Dutxes", "Calefacció", "Tafona històrica"],
            "permis_antelacio": "Fins a 60 dies abans",
            "contacte": "971 63 61 86 / reserves@caminsdemallorca.cat",
            "restriccio_foc": "Prohibit fer foc.",
            "acces_emergencia": "Accés vehicle urbà des del poble de Deià",
            "lat": 39.7491, "lon": 2.6483,
            "descripcio": "Antiga casa urbana de Deià rehabilitada com a refugi del GR-221 amb una tafona d'oli tradicional conservada."
        },
        {
            "slug": "refugi-muleta",
            "nom": "Refugi de Muleta",
            "titularitat": "Consell de Mallorca (Xarxa GR-221)",
            "municipi": "Sóller (Port de Sóller)",
            "capacitat": 30,
            "serveis": ["Aigua potable", "Dormitori", "Dutxes", "Servei àpats", "Vistes al mar"],
            "permis_antelacio": "Fins a 60 dies abans",
            "contacte": "971 63 19 02 / reserves@caminsdemallorca.cat",
            "restriccio_foc": "Prohibit fer foc.",
            "acces_emergencia": "Accés per camí del far de Muleta",
            "lat": 39.7942, "lon": 2.6869,
            "descripcio": "Ubicat a la península de Muleta al costat del Cap Gros, oferint vistes panoràmiques sobre la badia del Port de Sóller."
        },
        {
            "slug": "cases-de-binifaldo",
            "nom": "Cases de Binifaldó",
            "titularitat": "IBANAT (Govern de les Illes Balears)",
            "municipi": "Escorca",
            "capacitat": 30,
            "serveis": ["Aigua no tractada (cal bullir)", "Habitacions", "Cuina equipada", "Electricitat solar", "Lavabos"],
            "permis_antelacio": "60 dies a través de la web IBANAT",
            "contacte": "971 17 76 52 / refugis@ibanat.caib.es",
            "restriccio_foc": "Prohibit l'1 maig - 15 d'octubre. Ús exclusiu de fogons habilitats a l'hivern.",
            "acces_emergencia": "Pista forestal des de la Ma-10 (Lluc - Pollença)",
            "lat": 39.8311, "lon": 2.8988,
            "descripcio": "Refugi de l'IBANAT al peu del Puig Tomir, ideal per a acampades i estades de grups escoltes en plena natura."
        },
        {
            "slug": "binifaldo-petit",
            "nom": "Binifaldó Petit",
            "titularitat": "IBANAT (Govern de les Illes Balears)",
            "municipi": "Escorca",
            "capacitat": 10,
            "serveis": ["Aigua", "Llar de foc interna", "Dormitori diàfan", "Lavabo"],
            "permis_antelacio": "60 dies via IBANAT web",
            "contacte": "971 17 76 52 / refugis@ibanat.caib.es",
            "restriccio_foc": "Normativa forestal IBANAT",
            "acces_emergencia": "Pista de Binifaldó",
            "lat": 39.8320, "lon": 2.8995,
            "descripcio": "Petita caseta forestal per a grups reduïts o equips de caps al costat de les Cases de Binifaldó."
        },
        {
            "slug": "refugi-cuber",
            "nom": "Refugi de Cúber",
            "titularitat": "IBANAT (Govern de les Illes Balears)",
            "municipi": "Escorca",
            "capacitat": 6,
            "serveis": ["Refugi de muntanya bàsic", "Taula", "Bancs", "Aixopluc"],
            "permis_antelacio": "60 dies via IBANAT web",
            "contacte": "971 17 76 52 / refugis@ibanat.caib.es",
            "restriccio_foc": "Estricta prohibició d'encendre foc a l'exterior",
            "acces_emergencia": "Aparcament de l'embassament de Cúber (Ma-10)",
            "lat": 39.7821, "lon": 2.7915,
            "descripcio": "Refugi lliure/bàsic d'alta muntanya situat a la vorera de l'embassament de Cúber."
        },
        {
            "slug": "refugi-gorg-blau",
            "nom": "Refugi de Gorg Blau",
            "titularitat": "IBANAT (Govern de les Illes Balears)",
            "municipi": "Escorca",
            "capacitat": 8,
            "serveis": ["Refugi bàsic de muntanya", "Taules"],
            "permis_antelacio": "60 dies via IBANAT web",
            "contacte": "971 17 76 52 / refugis@ibanat.caib.es",
            "restriccio_foc": "Estricta prohibició de foc",
            "acces_emergencia": "Carretera Ma-10 embassament Gorg Blau",
            "lat": 39.7994, "lon": 2.8250,
            "descripcio": "Refugi bàsic prop de l'embassament del Gorg Blau i la font de sa Calobra."
        },
        {
            "slug": "refugi-s-arenalet",
            "nom": "Refugi de S'Arenalet",
            "titularitat": "IBANAT / Parc Natural de Llevant",
            "municipi": "Artà",
            "capacitat": 22,
            "serveis": ["Aigua", "Dutxes", "Cuina", "Proximitat a la platja verge"],
            "permis_antelacio": "60 dies via IBANAT web",
            "contacte": "971 17 76 52 / refugis@ibanat.caib.es",
            "restriccio_foc": "Prohibit encendre qualsevol tipus de foc.",
            "acces_emergencia": "A peu (2h30 des de s'Alqueria Vella) o vehicle autoritzat de protecció civil",
            "lat": 39.7528, "lon": 3.3512,
            "descripcio": "Un dels refugis més aïllats de Mallorca, situat a la platja verge de s'Arenalet des Verger a Artà."
        },
        {
            "slug": "area-recreativa-caubet",
            "nom": "Àrea Recreativa de Caubet",
            "titularitat": "IBANAT",
            "municipi": "Marratxí",
            "capacitat": 150,
            "serveis": ["Taules de fusta", "Fogons (ús hivern)", "Aigua no potable", "Aparcament"],
            "permis_antelacio": "Accés lliure (grup escolta >20 persones requereix comunicació IBANAT)",
            "contacte": "971 17 76 52",
            "restriccio_foc": "Prohibit l'1 maig - 15 d'octubre",
            "acces_emergencia": "Carretera de Palma a Sóller (Ma-11)",
            "lat": 39.6380, "lon": 2.6840,
            "descripcio": "Gran àrea recreativa als peus de la Serra de Tramuntana, molt utilitzada per a trobades de branques joves (Castors i Llops)."
        },
        {
            "slug": "area-recreativa-sa-coma-binifaldo",
            "nom": "Àrea Recreativa de Sa Coma de Binifaldó",
            "titularitat": "IBANAT",
            "municipi": "Escorca",
            "capacitat": 100,
            "serveis": ["Taules", "Ombra d'alzinar", "Punts d'aigua"],
            "permis_antelacio": "Accés lliure / Comunicació prèvia per a grups",
            "contacte": "971 17 76 52",
            "restriccio_foc": "Prohibit l'1 maig - 15 d'octubre",
            "acces_emergencia": "Des de Lluc per pista de Binifaldó",
            "lat": 39.8300, "lon": 2.8950,
            "descripcio": "Espai boscós d'alzinar vell ideal per a dinars i jocs de bosc durant les excursions a Lluc."
        },
        {
            "slug": "campament-lluc-s-alquerieta",
            "nom": "Campament de s'Alquerieta (Lluc)",
            "titularitat": "Monestir de Lluc / IBANAT",
            "municipi": "Escorca",
            "capacitat": 200,
            "serveis": ["Zona acampada escolta", "Serveis higiènics", "Font d'aigua potable", "Aparcament autocar"],
            "permis_antelacio": "Sol·licitud 30 dies abans al Monestir i IBANAT",
            "contacte": "971 87 15 25 / espai.lluc@lluc.net",
            "restriccio_foc": "Estricta",
            "acces_emergencia": "Accés directe carretera Ma-10",
            "lat": 39.8230, "lon": 2.8840,
            "descripcio": "El terreny d'acampada escolta històric per excel·lència a Mallorca, situat al costat del Monestir de Lluc."
        }
    ]
    return refugis_and_camping

def main():
    os.makedirs("data", exist_ok=True)
    data = get_ibanat_and_camping_data()
    output_path = os.path.join("data", "acampada_mallorca.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"S'han desat {len(data)} llocs d'acampada i refugis amb coordenades a {output_path}")

if __name__ == "__main__":
    main()
