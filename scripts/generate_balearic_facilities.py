#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator script for Balearic Islands facilities and scout groups datasets.
Expands the portal to Menorca, Eivissa, and Formentera while strictly
preserving existing Mallorca datasets untouched.

Generates:
- data/acampada_menorca.json (8 facilities)
- data/acampada_pitiuses.json (7 facilities: 5 Eivissa, 2 Formentera)
- data/agrupaments_menorca.json (9 active groups, Escoltes de Menorca - MSC)
- data/agrupaments_pitiuses.json (2 active groups in Eivissa)
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# ---------------------------------------------------------------------------
# 1. Menorca Facilities (8 facilities)
# ---------------------------------------------------------------------------
ACAMPADA_MENORCA = [
    {
        "slug": "campament-de-biniparratx",
        "nom": "Campament de Biniparratx",
        "categoria": "Zona d'Acampada Menorca",
        "municipi": "Sant Lluís",
        "illa": "Menorca",
        "titularitat": "Institut Balear de la Joventut (IBJOVE) / INJOVE Menorca",
        "contacte": "971 36 50 73 / reserves@injovemenorca.com",
        "web": "https://www.injovemenorca.es",
        "observacions": "Instal·lació de lleure educatiu de referència amb 4 zones d'acampada modulars en pinar i esplanades per a tendes de patrulla. Prioritat per a agrupaments escoltes i entitats juvenils registrades.",
        "capacitat": 120,
        "serveis": [
            "Aigua potable",
            "Lavabos i dutxes accessibles",
            "Piscina amb socorrista",
            "Menjador exterior cobert",
            "Pistes poliesportives",
            "Aparcament"
        ],
        "permis_antelacio": "Sol·licitud prèvia telemàtica a INJOVE Menorca amb un mínim de 15 dies d'antelació segons el Decret 23/2018",
        "restriccio_foc": "Prohibició absoluta de fer foc fora de les zones de cuina habilitades.",
        "acces_emergencia": "Camí de Biniparratx Petit, accés viari asfaltat directe per a vehicles d'emergència i bombers des de la carretera Me-10",
        "lat": 39.8322,
        "lon": 4.2258,
        "descripcio": "Campament juvenil referent a Menorca, ubicat al sud-est de l'illa molt a prop del Camí de Cavalls (etapes 18 i 19) i de cala Biniparratx.",
        "punt_origen": "Camí de Biniparratx Petit s/n, entre Binidalí i Cap d'en Font (Sant Lluís)"
    },
    {
        "slug": "casa-colonies-biniparratx",
        "nom": "Casa de Colònies de Biniparratx",
        "categoria": "Cases de Colònies i Albergs",
        "municipi": "Sant Lluís",
        "illa": "Menorca",
        "titularitat": "Institut Balear de la Joventut (IBJOVE) / INJOVE Menorca",
        "contacte": "971 36 50 73 / reserves@injovemenorca.com",
        "web": "https://www.injovemenorca.es",
        "observacions": "Edifici de colònies situat al mateix recinte de Biniparratx, adaptat per a estades educatives escoltes durant tot l'any.",
        "capacitat": 50,
        "serveis": [
            "Habitacions col·lectives amb lliteres",
            "Menjador interior",
            "Cuina industrial equipada",
            "Calefacció",
            "Banys i dutxes adaptats"
        ],
        "permis_antelacio": "Sol·licitud prèvia a través del registre d'INJOVE Menorca amb 15 dies d'antelació mínima",
        "restriccio_foc": "Prohibició total de foc exterior.",
        "acces_emergencia": "Accés per carretera asfaltada des de la Me-10, apte per a ambulàncies i bombers",
        "lat": 39.8325,
        "lon": 4.2255,
        "descripcio": "Casa de colònies integrada a l'espai de Biniparratx, ideal com a base d'operacions per a unitats escoltes i trobades formatives.",
        "punt_origen": "Camí de Biniparratx Petit s/n, Sant Lluís"
    },
    {
        "slug": "alberg-sa-vinyeta",
        "nom": "Alberg Juvenil de Sa Vinyeta",
        "categoria": "Cases de Colònies i Albergs",
        "municipi": "Ciutadella de Menorca",
        "illa": "Menorca",
        "titularitat": "Institut Balear de la Joventut (IBJOVE) / Xarxa REAJ",
        "contacte": "971 48 77 63 / savinyeta@injovemenorca.com",
        "web": "https://www.injovemenorca.es",
        "observacions": "Alberg oficial de joventut en finca rústica del segle XVIII rehabilitada amb pavellons moderns. Accessible per a persones amb mobilitat reduïda.",
        "capacitat": 80,
        "serveis": [
            "Dormitoris comunitaris",
            "Banys complets",
            "Esmorzar inclòs",
            "Pista poliesportiva",
            "Connexió Wifi",
            "Zona de jocs"
        ],
        "permis_antelacio": "Reserva a través d'INJOVE Menorca / central de reserves REAJ amb antelació mínima de 15 dies",
        "restriccio_foc": "No permès fer foc a l'exterior.",
        "acces_emergencia": "Camí Vell de Sa Farola, accés rodat òptim per a ambulàncies i vehicles d'emergència des del nucli urbà de Ciutadella",
        "lat": 40.0051,
        "lon": 3.8402,
        "descripcio": "Instal·lació clau per a grups escoltes com a base de pernocta o inici de la travessa de la costa nord i oest del Camí de Cavalls.",
        "punt_origen": "Camí Vell de Sa Farola s/n, Ciutadella de Menorca"
    },
    {
        "slug": "torre-de-son-ganxo",
        "nom": "Torre de Son Ganxo",
        "categoria": "Cases de Colònies i Albergs",
        "municipi": "Sant Lluís",
        "illa": "Menorca",
        "titularitat": "INJOVE Menorca / Institut Balear de la Joventut",
        "contacte": "971 36 50 73 / reserves@injovemenorca.com",
        "web": "https://www.injovemenorca.es",
        "observacions": "Torre de defensa costanera del segle XVIII restaurada com a alberg juvenil singular vora la mar, a tocar del Camí de Cavalls (etapa 19).",
        "capacitat": 28,
        "serveis": [
            "Lliteres",
            "Cuina bàsica",
            "Lavabos i dutxes",
            "Terrassa panoràmica",
            "Electricitat solar"
        ],
        "permis_antelacio": "Sol·licitud de reserva prèvia a INJOVE Menorca amb 15 dies d'antelació",
        "restriccio_foc": "Prohibició estricta de foc tant a l'interior com a l'exterior.",
        "acces_emergencia": "Passeig de Son Ganxo, accés rodat des de la urbanització de Punta Prima (Sant Lluís) per a vehicles d'emergència",
        "lat": 39.8142,
        "lon": 4.2628,
        "descripcio": "Allotjament juvenil històric en una torre de defensa costanera amb vistes a l'Illa de l'Aire.",
        "punt_origen": "Passeig de Son Ganxo, Punta Prima (Sant Lluís)"
    },
    {
        "slug": "casa-colonies-santa-eularieta",
        "nom": "Casa de Colònies Santa Eularieta",
        "categoria": "Cases de Colònies i Albergs",
        "municipi": "Es Migjorn Gran",
        "illa": "Menorca",
        "titularitat": "INJOVE Menorca / Institut Balear de la Joventut",
        "contacte": "971 36 50 73 / reserves@injovemenorca.com",
        "web": "https://www.injovemenorca.es",
        "observacions": "Finca rústica menorquina habilitada per a trobades de lleure educatiu i colònies escoltes en un entorn d'alt valor natural i tranquil·litat.",
        "capacitat": 40,
        "serveis": [
            "Dormitoris amb lliteres",
            "Cuina menjador",
            "Serveis sanitaris",
            "Espai exterior ampli",
            "Zona d'esbarjo"
        ],
        "permis_antelacio": "Sol·licitud davant INJOVE Menorca amb 15 dies d'antelació mínima",
        "restriccio_foc": "Prohibit fer foc a l'exterior durant tot l'any segons normativa de prevenció d'incendis.",
        "acces_emergencia": "Camí rural asfaltat des d'Es Migjorn Gran, accés garantit per a ambulàncies i bombers",
        "lat": 39.9458,
        "lon": 4.0412,
        "descripcio": "Instal·lació de lleure situada al terme d'Es Migjorn Gran, enllaç perfecte amb els barrancs del sud i la platja de Sant Tomàs.",
        "punt_origen": "Carretera d'Es Migjorn Gran a Sant Tomàs, desviació Santa Eularieta"
    },
    {
        "slug": "casa-colonies-es-torreto",
        "nom": "Casa de Colònies Es Torretó",
        "categoria": "Cases de Colònies i Albergs",
        "municipi": "Maó",
        "illa": "Menorca",
        "titularitat": "Escoltes de Menorca (MSC)",
        "contacte": "971 35 15 20 / torreto@escoltesmenorca.org",
        "web": "https://www.escoltesmenorca.org",
        "observacions": "Espai propi gestionat per l'associació Escoltes de Menorca (MSC) destinat a formacions d'educadors, sortides d'unitats i acollida de grups federats.",
        "capacitat": 35,
        "serveis": [
            "Sales d'activitats",
            "Habitacions per a grups",
            "Cuina equipada",
            "Lavabos complets",
            "Pati tancat"
        ],
        "permis_antelacio": "Sol·licitud a la Secretaria d'Escoltes de Menorca amb antelació prèvia de 20 dies",
        "restriccio_foc": "Prohibit fer foc a l'exterior.",
        "acces_emergencia": "Accés viari complet per carrer pavimentat des de Maó, apte per a vehicles d'emergència",
        "lat": 39.8890,
        "lon": 4.2610,
        "descripcio": "Casa de colònies de referència de l'escoltisme menorquí, punt de trobada per a activitats educatives i associatives.",
        "punt_origen": "Camí de Malbúger s/n, Maó"
    },
    {
        "slug": "camping-son-bou",
        "nom": "Càmping Son Bou",
        "categoria": "Zona d'Acampada Menorca",
        "municipi": "Alaior",
        "illa": "Menorca",
        "titularitat": "Privat (Habilitat Lleure Educatiu)",
        "contacte": "971 37 27 27 / info@campingsonbou.com",
        "web": "https://www.campingsonbou.com",
        "observacions": "Càmping equipat de primera categoria amb zona reservada per a acampada d'entitats juvenils i escoltes sota arbreda de pins.",
        "capacitat": 300,
        "serveis": [
            "Parcel·les per a tendes",
            "Piscina",
            "Supermercat",
            "Blocs de dutxes i wc",
            "Pistes esportives",
            "Restaurant"
        ],
        "permis_antelacio": "Reserva prèvia amb la direcció del càmping indicant grup escolta o juvenil",
        "restriccio_foc": "Ús exclusiu de fogons a les zones habilitades de pícnic. Prohibit foc a terra.",
        "acces_emergencia": "Carretera de Son Bou (Me-12), accés viari ample per a vehicles de bombers i ambulàncies",
        "lat": 39.9078,
        "lon": 4.0722,
        "descripcio": "Gran espai d'acampada situat a la costa sud d'Alaior, estratègic per a les etapes 15 i 16 del Camí de Cavalls.",
        "punt_origen": "Carretera de Son Bou km 3.5, 07730 Alaior"
    },
    {
        "slug": "camping-satalaia",
        "nom": "Càmping S'Atalaia",
        "categoria": "Zona d'Acampada Menorca",
        "municipi": "Ferreries",
        "illa": "Menorca",
        "titularitat": "Privat (Habilitat Lleure Educatiu)",
        "contacte": "971 37 42 32 / info@campingsatalaia.com",
        "web": "https://www.campingsatalaia.com",
        "observacions": "Càmping d'ambient tranquil en bosc natural de pins a prop de Cala Galdana. Acull habitualment grups escoltes en ruta pel Camí de Cavalls.",
        "capacitat": 200,
        "serveis": [
            "Zona d'acampada en pinar",
            "Sanitaris i dutxes amb aigua calenta",
            "Piscina",
            "Bar cafeteria",
            "Bugaderia",
            "Recepció"
        ],
        "permis_antelacio": "Reserva anticipada recomanada amb un mínim de 15 dies per a grups",
        "restriccio_foc": "Prohibit encendre foc o barbacoes fora dels espais autoritzats.",
        "acces_emergencia": "Carretera de Cala Galdana (Me-22) km 4.5, accés rodat directe per a vehicles d'emergència i camions de bombers",
        "lat": 39.9542,
        "lon": 3.9785,
        "descripcio": "Càmping situat al terme de Ferreries, al migjorn de Menorca, proper a Cala Mitjana i Cala Galdana (etapes 13 i 14 del Camí de Cavalls).",
        "punt_origen": "Carretera Ferreries - Cala Galdana km 4.5, Ferreries"
    }
]

# ---------------------------------------------------------------------------
# 2. Pitiüses Facilities (7 facilities: 5 Eivissa, 2 Formentera)
# ---------------------------------------------------------------------------
ACAMPADA_PITIUSES = [
    {
        "slug": "campament-cala-des-jondal",
        "nom": "Campament de sa Cala des Jondal",
        "categoria": "Zona d'Acampada Eivissa",
        "municipi": "Sant Josep de sa Talaia",
        "illa": "Eivissa",
        "titularitat": "Consell Insular d'Eivissa (Departament de Joventut)",
        "contacte": "971 19 59 00 (ext. 1422) / cij.eivissa@conselldeivissa.es",
        "web": "https://www.conselldeivissa.es",
        "observacions": "Instal·lació pública de lleure educatiu per a entitats juvenils en pinar coster a la Punta des Jondal. Disposa de tendes de campanya i serveis centrals. Operatiu principalment de maig a setembre.",
        "capacitat": 150,
        "serveis": [
            "Zona de tendes en plataformes",
            "Sanitaris i dutxes",
            "Menjador",
            "Zona de tallers",
            "Espais poliesportius",
            "Accés directe a la costa"
        ],
        "permis_antelacio": "Sol·licitud de reserva al Departament de Joventut del Consell Insular d'Eivissa amb 1 mes d'antelació segons el Decret 23/2018",
        "restriccio_foc": "Prohibició absoluta de foc durant tota l'època d'alt risc d'incendi (1 de maig al 15 d'octubre).",
        "acces_emergencia": "Camí des Jondal des de la carretera PM-803 / des Porroig, accés rodat apte per a vehicles d'emergència i bombers",
        "lat": 38.8685,
        "lon": 1.3142,
        "descripcio": "Instal·lació pública d'acampada juvenil de referència a Eivissa, situada a prop de la Reserva Natural de Ses Salines.",
        "punt_origen": "Punta des Jondal, Cala des Jondal (Sant Josep de sa Talaia)"
    },
    {
        "slug": "casa-colonies-can-tomeu",
        "nom": "Casa de Colònies Can Tomeu",
        "categoria": "Cases de Colònies i Albergs",
        "municipi": "Eivissa",
        "illa": "Eivissa",
        "titularitat": "Ajuntament d'Eivissa",
        "contacte": "971 39 76 00 / joventut@eivissa.es",
        "web": "https://www.eivissa.es",
        "observacions": "Instal·lació municipal per a activitats de lleure educatiu, colònies escoltes i trobades juvenils.",
        "capacitat": 38,
        "serveis": [
            "Dormitoris amb lliteres",
            "Menjador",
            "Cuina equipada",
            "Lavabos i dutxes",
            "Zona exterior de jocs"
        ],
        "permis_antelacio": "Sol·licitud registrada a l'Ajuntament d'Eivissa amb 20 dies d'antelació",
        "restriccio_foc": "Prohibit fer foc a l'exterior.",
        "acces_emergencia": "Camí Vell de Sant Mateu, accés viari urbà asfaltat per a ambulàncies i bombers",
        "lat": 38.9056,
        "lon": 1.4198,
        "descripcio": "Casa de colònies situada als afores de la ciutat d'Eivissa, ideal per a caps de setmana i campaments base.",
        "punt_origen": "Camí Vell de Sant Mateu s/n, Eivissa"
    },
    {
        "slug": "alberg-amistat-island",
        "nom": "Alberg Juvenil Amistat Island",
        "categoria": "Cases de Colònies i Albergs",
        "municipi": "Sant Antoni de Portmany",
        "illa": "Eivissa",
        "titularitat": "Privat / Xarxa REAJ Habilitat",
        "contacte": "971 34 89 22 / info@amistathostels.com",
        "web": "https://www.amistathostels.com",
        "observacions": "Alberg juvenil homologat per la Xarxa Espanyola d'Albergs Juvenils (REAJ) a Sant Antoni de Portmany, amb habitacions per a grups.",
        "capacitat": 110,
        "serveis": [
            "Habitacions compartides i privades",
            "Piscina",
            "Cuina d'ús comunitari",
            "Wifi gratuït",
            "Zona chill-out",
            "Recepció 24h"
        ],
        "permis_antelacio": "Reserva prèvia amb antelació per a grups a través de la xarxa REAJ",
        "restriccio_foc": "Prohibició de foc en tot el recinte.",
        "acces_emergencia": "Carrer de Santa Rosalia, casc urbà de Sant Antoni, accés directe per a vehicles d'emergència i ambulàncies",
        "lat": 38.9832,
        "lon": 1.3025,
        "descripcio": "Allotjament juvenil urbà al municipi de Sant Antoni de Portmany, amb connexió ràpida a les rutes de ponent.",
        "punt_origen": "Carrer de Santa Rosalia 25, 07820 Sant Antoni de Portmany"
    },
    {
        "slug": "camping-cala-nova",
        "nom": "Càmping Cala Nova",
        "categoria": "Zona d'Acampada Eivissa",
        "municipi": "Santa Eulària des Riu",
        "illa": "Eivissa",
        "titularitat": "Privat (Habilitat Lleure Educatiu)",
        "contacte": "971 33 17 74 / info@campingcalanova.com",
        "web": "https://www.campingcalanova.com",
        "observacions": "Càmping costaner tradicional amb pinar a 50 metres de la platja de Cala Nova. Disposa de zona d'acampada per a grups juvenils i escoltes.",
        "capacitat": 250,
        "serveis": [
            "Parcel·les d'acampada",
            "Sanitaris i dutxes",
            "Bar cafeteria",
            "Rentadores",
            "Electricitat a les parcel·les",
            "Supermercat proper"
        ],
        "permis_antelacio": "Reserva prèvia imprescindible per a grups escoltes amb un mínim de 15 dies d'antelació",
        "restriccio_foc": "Prohibit estrictament fer foc lliure a les parcel·les.",
        "acces_emergencia": "Carretera de Cala Nova, accés per carretera pavimentada per a ambulàncies i bombers",
        "lat": 39.0068,
        "lon": 1.5832,
        "descripcio": "Instal·lació d'acampada a l'est d'Eivissa, propera a les rutes de la costa de Santa Eulària i les torres de defensa.",
        "punt_origen": "Platja de Cala Nova, Es Canar (Santa Eulària des Riu)"
    },
    {
        "slug": "camping-la-playa-ibiza",
        "nom": "Càmping La Playa Ibiza",
        "categoria": "Zona d'Acampada Eivissa",
        "municipi": "Santa Eulària des Riu",
        "illa": "Eivissa",
        "titularitat": "Privat (Habilitat Lleure Educatiu)",
        "contacte": "971 33 85 25 / info@campinglaplayaibiza.com",
        "web": "https://www.campinglaplayaibiza.com",
        "observacions": "Càmping situat vora la mar a Cala Martina, envoltat de pins, apte per a pernoctes de grups itinerants escoltes.",
        "capacitat": 180,
        "serveis": [
            "Zona d'acampada lliure",
            "Serveis higiènics i dutxes",
            "Wifi",
            "Àrea de rentat",
            "Accés directe a la platja"
        ],
        "permis_antelacio": "Reserva de grup anticipada requerida amb almenys 15 dies d'antelació",
        "restriccio_foc": "Prohibició absoluta de fer foc a l'exterior segons normativa balear.",
        "acces_emergencia": "Avinguda de Cala Martina, accés asfaltat per a bombers i serveis sanitaris d'urgència",
        "lat": 38.9950,
        "lon": 1.5780,
        "descripcio": "Espai d'acampada situat a la costa oriental d'Eivissa vora Cala Martina, ideal per a activitats marines escoltes.",
        "punt_origen": "Cala Martina, Es Canar (Santa Eulària des Riu)"
    },
    {
        "slug": "casa-colonies-formentera",
        "nom": "Casa de Colònies de Formentera",
        "categoria": "Cases de Colònies i Albergs",
        "municipi": "Sant Francesc Xavier",
        "illa": "Formentera",
        "titularitat": "Consell Insular de Formentera / Institut Balear de la Joventut (IBJOVE)",
        "contacte": "971 17 89 34 / reserves@ibjove.caib.es",
        "web": "https://ibjove.caib.es",
        "observacions": "Única instal·lació d'allotjament juvenil públic a l'illa de Formentera. Capacitat màxima de 32 places. Mínim de reserva per grup: 20 places.",
        "capacitat": 32,
        "serveis": [
            "4 habitacions de lliteres (8 places cadascuna)",
            "Cuina equipada comunitària",
            "Sala polivalent",
            "Pati exterior",
            "Dutxes amb aigua calenta"
        ],
        "permis_antelacio": "Sol·licitud centralitzada a l'IBJOVE amb alta antelació (mínim 30 dies)",
        "restriccio_foc": "Prohibit qualsevol tipus de foc exterior a tota l'illa de Formentera degut a la màxima protecció ambiental.",
        "acces_emergencia": "Nucli urbà de Sant Francesc Xavier, accés directe per vehicles d'emergència i ambulàncies",
        "lat": 38.7058,
        "lon": 1.4285,
        "descripcio": "Equipament clau i imprescindible per a qualsevol sortida o campament escolta a Formentera degut a la prohibició total d'acampada lliure a l'illa.",
        "punt_origen": "Carrer de Portossalè / nucli de Sant Francesc Xavier, Formentera"
    },
    {
        "slug": "centre-can-marroig",
        "nom": "Centre Can Marroig",
        "categoria": "Refugi de Muntanya / Comuna",
        "municipi": "Sant Francesc Xavier",
        "illa": "Formentera",
        "titularitat": "Espais Naturals CAIB / IBANAT",
        "contacte": "971 30 14 60 / parcsnaturals@caib.es",
        "web": "https://www.caib.es/sites/espaisnaturals/",
        "observacions": "Centre d'interpretació del Parc Natural de ses Salines d'Eivissa i Formentera amb espai d'acollida per a grups educatius i activitats ambientals de dia.",
        "capacitat": 20,
        "serveis": [
            "Centre d'interpretació",
            "Lavabos públics",
            "Àrea de pícnic exterior",
            "Punt d'aigua potable",
            "Panells divulgatius"
        ],
        "permis_antelacio": "Autorització prèvia a la direcció del Parc Natural de ses Salines per a grups educatius",
        "restriccio_foc": "Prohibició absoluta de fer foc en tot el Parc Natural.",
        "acces_emergencia": "Camí de Can Marroig, accés rodat forestal apte per a vehicles 4x4 d'emergència i bombers",
        "lat": 38.7230,
        "lon": 1.4050,
        "descripcio": "Finca pública i centre d'educació ambiental del Parc Natural de ses Salines a Formentera, base per a rutes pedagògiques pel nord-oest de l'illa.",
        "punt_origen": "Finca de Can Marroig, carretera de Porto-salè, Formentera"
    }
]

# ---------------------------------------------------------------------------
# 3. Menorca Scout Groups (9 groups, Escoltes de Menorca - MSC)
# ---------------------------------------------------------------------------
AGRUPAMENTS_MENORCA = [
    {
        "slug": "ae-tramuntana-mao",
        "nom": "AE Tramuntana",
        "associacio": "Escoltes de Menorca (MSC)",
        "municipi": "Maó",
        "illa": "Menorca",
        "zona": "Llevant",
        "ubicacio_detall": "Dalt Sant Joan, Maó",
        "lat": 39.8885,
        "lon": 4.2635,
        "email": "tramuntana@escoltesmenorca.org",
        "web": "https://www.escoltesmenorca.org",
        "descripcio": "Agrupament escolta històric de la ciutat de Maó, integrat a Escoltes de Menorca (MSC) i dinamitzador del barri de Dalt Sant Joan."
    },
    {
        "slug": "ae-sant-antoni-claret",
        "nom": "AE Sant Antoni Maria Claret",
        "associacio": "Escoltes de Menorca (MSC)",
        "municipi": "Ciutadella de Menorca",
        "illa": "Menorca",
        "zona": "Ponent",
        "ubicacio_detall": "Carrer del Roser, Ciutadella",
        "lat": 40.0012,
        "lon": 3.8378,
        "email": "santantoni@escoltesmenorca.org",
        "web": "https://www.escoltesmenorca.org",
        "descripcio": "Agrupament escolta de referència a Ciutadella de Menorca, amb llarga trajectòria en projectes comunitaris i campaments a la costa nord."
    },
    {
        "slug": "ae-sant-miquel-ciutadella",
        "nom": "AE Sant Miquel",
        "associacio": "Escoltes de Menorca (MSC)",
        "municipi": "Ciutadella de Menorca",
        "illa": "Menorca",
        "zona": "Ponent",
        "ubicacio_detall": "Parròquia de Sant Miquel, Ciutadella",
        "lat": 39.9985,
        "lon": 3.8410,
        "email": "santmiquel@escoltesmenorca.org",
        "web": "https://www.escoltesmenorca.org",
        "descripcio": "Agrupament actiu a Ciutadella vinculat a la parròquia de Sant Miquel, promotor de l'educació en el lleure i el servei comunitari."
    },
    {
        "slug": "ae-pare-bartomeu-pou",
        "nom": "AE Pare Bartomeu Pou",
        "associacio": "Escoltes de Menorca (MSC)",
        "municipi": "Alaior",
        "illa": "Menorca",
        "zona": "Centre",
        "ubicacio_detall": "Carrer Nou, Alaior",
        "lat": 39.9340,
        "lon": 4.1402,
        "email": "bartomeupou@escoltesmenorca.org",
        "web": "https://www.escoltesmenorca.org",
        "descripcio": "Agrupament escolta d'Alaior amb una forta implicació en l'entorn natural de la conca de Son Bou i el Camí d'en Kane."
    },
    {
        "slug": "ae-sant-francesc-ferreries",
        "nom": "AE Sant Francesc",
        "associacio": "Escoltes de Menorca (MSC)",
        "municipi": "Ferreries",
        "illa": "Menorca",
        "zona": "Centre",
        "ubicacio_detall": "Plaça de l'Església, Ferreries",
        "lat": 39.9830,
        "lon": 4.0115,
        "email": "santfrancesc@escoltesmenorca.org",
        "web": "https://www.escoltesmenorca.org",
        "descripcio": "Agrupament de Ferreries molt arrelat a les tradicions locals i a les excursions pel barranc d'Algendar i la costa de Santa Galdana."
    },
    {
        "slug": "ae-es-castell",
        "nom": "AE Es Castell",
        "associacio": "Escoltes de Menorca (MSC)",
        "municipi": "Es Castell",
        "illa": "Menorca",
        "zona": "Llevant",
        "ubicacio_detall": "Carrer Stuart, Es Castell",
        "lat": 39.8805,
        "lon": 4.2865,
        "email": "escastell@escoltesmenorca.org",
        "web": "https://www.escoltesmenorca.org",
        "descripcio": "Agrupament escolta d'Es Castell (Villacarlos), situat a la boca del port de Maó, amb forta participació en activitats de costa."
    },
    {
        "slug": "ae-sant-lluis",
        "nom": "AE Sant Lluís",
        "associacio": "Escoltes de Menorca (MSC)",
        "municipi": "Sant Lluís",
        "illa": "Menorca",
        "zona": "Llevant",
        "ubicacio_detall": "Casal de Joves, Sant Lluís",
        "lat": 39.8515,
        "lon": 4.2588,
        "email": "santlluis@escoltesmenorca.org",
        "web": "https://www.escoltesmenorca.org",
        "descripcio": "Agrupament del municipi de Sant Lluís, estretament lligat a les activitats juvenils de Biniparratx i la costa de Migjorn."
    },
    {
        "slug": "ae-mercadal",
        "nom": "AE Mercadal",
        "associacio": "Escoltes de Menorca (MSC)",
        "municipi": "Es Mercadal",
        "illa": "Menorca",
        "zona": "Centre",
        "ubicacio_detall": "Carrer Major, Es Mercadal",
        "lat": 39.9868,
        "lon": 4.0934,
        "email": "mercadal@escoltesmenorca.org",
        "web": "https://www.escoltesmenorca.org",
        "descripcio": "Agrupament situat als peus del Toro, al bell mig de l'illa, dinamitzador clau de trobades de branques de tota Menorca."
    },
    {
        "slug": "ae-fornells",
        "nom": "AE Fornells",
        "associacio": "Escoltes de Menorca (MSC)",
        "municipi": "Es Mercadal",
        "illa": "Menorca",
        "zona": "Nord",
        "ubicacio_detall": "Port de Fornells, Es Mercadal",
        "lat": 40.0545,
        "lon": 4.1310,
        "email": "fornells@escoltesmenorca.org",
        "web": "https://www.escoltesmenorca.org",
        "descripcio": "Agrupament de la badia de Fornells, especialitzat en activitats marines, descoberta del litoral nord i protecció del medi aquàtic."
    }
]

# ---------------------------------------------------------------------------
# 4. Pitiüses Scout Groups (2 active groups in Eivissa)
# ---------------------------------------------------------------------------
AGRUPAMENTS_PITIUSES = [
    {
        "slug": "ae-los-condors",
        "nom": "AE Los Cóndors",
        "associacio": "ASDE Scouts de Baleares / Scouts de España",
        "municipi": "Eivissa",
        "illa": "Eivissa",
        "zona": "Eivissa Ciutat",
        "ubicacio_detall": "Can Misses / Ca n'Escandell, Eivissa",
        "lat": 38.9102,
        "lon": 1.4245,
        "email": "ibiza@scoutsdebaleares.org",
        "web": "https://scoutsdebaleares.org",
        "descripcio": "Grup scout històric d'Eivissa fundat als anys 80, membre d'ASDE Scouts de Baleares, actiu en projectes d'educació ambiental i ciutadania."
    },
    {
        "slug": "ae-isidor-macabich",
        "nom": "AE Isidor Macabich",
        "associacio": "Escoltes de Balears (MSC)",
        "municipi": "Eivissa",
        "illa": "Eivissa",
        "zona": "Eivissa Ciutat",
        "ubicacio_detall": "Avinguda d'Isidor Macabich, Eivissa",
        "lat": 38.9135,
        "lon": 1.4310,
        "email": "isidormacabich@escoltesbalears.org",
        "web": "https://www.vilajove.eivissa.es",
        "descripcio": "Agrupament escolta d'Eivissa ciutat federat al Moviment Scout Catòlic (MSC), actiu en activitats d'excursionisme a ses Salines i els Amunts."
    }
]


def write_json_clean(filepath: Path, data):
    """Write cleanly formatted UTF-8 JSON without BOM."""
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Generated {filepath.relative_to(BASE_DIR)}: {len(data)} records")


def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Menorca Facilities
    file_acampada_menorca = DATA_DIR / "acampada_menorca.json"
    write_json_clean(file_acampada_menorca, ACAMPADA_MENORCA)

    # 2. Pitiüses Facilities
    file_acampada_pitiuses = DATA_DIR / "acampada_pitiuses.json"
    write_json_clean(file_acampada_pitiuses, ACAMPADA_PITIUSES)

    # 3. Menorca Scout Groups
    file_agrupaments_menorca = DATA_DIR / "agrupaments_menorca.json"
    write_json_clean(file_agrupaments_menorca, AGRUPAMENTS_MENORCA)

    # 4. Pitiüses Scout Groups
    file_agrupaments_pitiuses = DATA_DIR / "agrupaments_pitiuses.json"
    write_json_clean(file_agrupaments_pitiuses, AGRUPAMENTS_PITIUSES)

    print("\nAll 4 datasets generated successfully!")


if __name__ == "__main__":
    main()
