#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generator script for Eivissa and Formentera scout hiking routes datasets.
Generates:
- data/rutes_eivissa.json (7 routes)
- data/rutes_formentera.json (3 green routes)

Preserves existing data/rutes_mallorca.json 100% untouched.
Outputs strictly valid UTF-8 JSON without BOM.
"""

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# ---------------------------------------------------------------------------
# 1. Eivissa Routes (7 authentic routes)
# ---------------------------------------------------------------------------
RUTES_EIVISSA = [
    {
        "slug": "eivissa-ses-salines-torre-portes",
        "nom": "Ses Salines i Torre de ses Portes",
        "municipi": "Sant Josep de sa Talaia",
        "zona": "Parc Natural de ses Salines / Sud",
        "illa": "Eivissa",
        "distancia_km": 4.8,
        "desnivell_positiu_m": 35,
        "dificultat": "Fàcil",
        "durada_estimada": "1h 30min",
        "apte_unitats": [
            "Castors/Fures",
            "Llops/Daines",
            "Pioners/Rangers",
            "Rutes i guies"
        ],
        "punts_aigua": [
            "Platja de ses Salines (inici/final, serveis i xiringuitos)",
            "Es Cavallet (temporada estival)"
        ],
        "consells_seguretat": "Nul·la ombra durant tot el recorregut. Forta calor i reflex del sol sobre les salines i la sorra blanca. Portar barret, protecció solar alta i mínim 1.5L d'aigua per persona. Respectar estrictament els cordons dunars de protecció i anar amb compte a les roques baixes properes a la torre davant Es Freus.",
        "descripcio": "Itinerari planer pel Parc Natural de ses Salines d'Eivissa i Formentera que recorre les platges verges de ses Salines i es Cavallet fins a l'estratègica Torre de ses Portes (segle XVI), guaitant el pas marítim des Freus.",
        "lat": 38.8415,
        "lon": 1.3980,
        "punt_origen": "Aparcament de la Platja de ses Salines (parada bus L11)",
        "font": "Consell Insular d'Eivissa",
        "wikiloc_url": "https://www.wikiloc.com/rutas-senderismo/torre-ses-portes-ses-salines-eivissa-10928374",
        "track_coordinates": [
            [38.8415, 1.3980],
            [38.8350, 1.4010],
            [38.8310, 1.4050],
            [38.8335, 1.4075]
        ],
        "punts_interes": [
            "Platja de ses Salines",
            "Estanys saliners protegits",
            "Platja des Cavallet",
            "Torre de ses Portes",
            "Pas marítim des Freus"
        ],
        "itinerari_passos": [
            {
                "pas": 1,
                "nom": "Sortida de ses Salines",
                "desc": "Inici a l'extrem oriental de la platja de ses Salines seguint el sender costaner."
            },
            {
                "pas": 2,
                "nom": "Camí des Freus",
                "desc": "Pas pel roquissar litoral amb vistes panoràmiques cap a l'illa de s'Espalmador."
            },
            {
                "pas": 3,
                "nom": "Torre de ses Portes",
                "desc": "Arribada a la talaia del segle XVI i retorn vorejant la platja des Cavallet."
            }
        ]
    },
    {
        "slug": "eivissa-torre-des-savinar",
        "nom": "Torre des Savinar i Es Vedrà",
        "municipi": "Sant Josep de sa Talaia",
        "zona": "Cala d'Hort / Sud-Oest",
        "illa": "Eivissa",
        "distancia_km": 4.2,
        "desnivell_positiu_m": 220,
        "dificultat": "Moderada",
        "durada_estimada": "1h 45min",
        "apte_unitats": [
            "Pioners/Rangers",
            "Rutes i guies"
        ],
        "punts_aigua": [
            "Cap punt al recorregut; imprescindible dur aigua des de Sant Josep"
        ],
        "consells_seguretat": "Penya-segat vertical de més de 200 metres sobre el mar. Risc extrem de caiguda al buit; prohibit totalment acostar-se a la vora del precipici o córrer pel camí. Terreny pedregós molt relliscant a la baixada. Evitar les hores centrals de sol i forta calor.",
        "descripcio": "Ascensió emblemàtica a la Torre des Savinar (o Torre del Pirata), atalaia del segle XVIII situada sobre un impressionant penya-segat davant els mítics illots d'Es Vedrà i Es Vedranell.",
        "lat": 38.8770,
        "lon": 1.2335,
        "punt_origen": "Mirador de Cala d'Hort / Camí des Savinar (accés des de Sant Josep)",
        "font": "Consell Insular d'Eivissa",
        "wikiloc_url": "https://www.wikiloc.com/rutas-senderismo/torre-des-savinar-mirador-des-vedra-15498201",
        "track_coordinates": [
            [38.8770, 1.2335],
            [38.8750, 1.2290],
            [38.8725, 1.2270],
            [38.8720, 1.2260]
        ],
        "punts_interes": [
            "Mirador de Cala d'Hort",
            "Camí des Savinar",
            "Torre des Savinar (segle XVIII)",
            "Vistes panoràmiques d'Es Vedrà i Es Vedranell"
        ],
        "itinerari_passos": [
            {
                "pas": 1,
                "nom": "Camí de terra des del mirador",
                "desc": "Sortida des de la pista de terra de Cala d'Hort en direcció al coll."
            },
            {
                "pas": 2,
                "nom": "Ascens a la Torre des Savinar",
                "desc": "Pujada per sender de pedra viva fins a la talaia sobre el penya-segat de 200 metres."
            },
            {
                "pas": 3,
                "nom": "Mirador d'Es Vedrà i retorn",
                "desc": "Contemplació de la reserva natural marina i descens amb precaució pel mateix sender."
            }
        ]
    },
    {
        "slug": "eivissa-els-amunts-sant-vicent",
        "nom": "PR-EI-101: Els Amunts (Sant Joan a Sant Vicent)",
        "municipi": "Sant Joan de Labritja",
        "zona": "Els Amunts / Nord",
        "illa": "Eivissa",
        "distancia_km": 12.5,
        "desnivell_positiu_m": 380,
        "dificultat": "Exigent",
        "durada_estimada": "4h 00min",
        "apte_unitats": [
            "Pioners/Rangers",
            "Rutes i guies"
        ],
        "punts_aigua": [
            "Sant Joan de Labritja (poble, inici)",
            "Cala de Sant Vicent (nucli final)"
        ],
        "consells_seguretat": "Recorregut llarg i exigent per l'espai protegit dels Amunts. Alt risc d'incendi forestal a l'estiu; prohibit estrictament encendre foc. Pendent pronunciat i terreny de pedra solta. Dur mínim 2.5 litres d'aigua per persona, calçat ferm de muntanya i protecció solar per a la calor intensa.",
        "descripcio": "Sendera de petit recorregut PR-EI-101 que creua la serra protegida dels Amunts, alternant boscos de pi blanc mediterrani, possessions rurals i el descens panoràmic a la cala de Sant Vicent.",
        "lat": 39.0782,
        "lon": 1.5140,
        "punt_origen": "Plaça de l'Església de Sant Joan de Labritja (parada bus L20A)",
        "font": "Consell Insular d'Eivissa",
        "wikiloc_url": "https://www.wikiloc.com/rutas-senderismo/pr-ei-101-els-amunts-sant-joan-cala-sant-vicent-22340912",
        "track_coordinates": [
            [39.0782, 1.5140],
            [39.0850, 1.5280],
            [39.0980, 1.5450],
            [39.1060, 1.5580],
            [39.1120, 1.5890]
        ],
        "punts_interes": [
            "Nucli tradicional de Sant Joan de Labritja",
            "Feixes i pinedes dels Amunts",
            "Puig d'en Roig",
            "Barranc de sa Jonquera",
            "Cala de Sant Vicent"
        ],
        "itinerari_passos": [
            {
                "pas": 1,
                "nom": "Sortida de Sant Joan",
                "desc": "Inici a l'església de Sant Joan seguint les marques grogues i blanques del PR."
            },
            {
                "pas": 2,
                "nom": "Travessa dels Amunts",
                "desc": "Pujada progressiva entre pinars i cases de camp amb feixes de pedra seca."
            },
            {
                "pas": 3,
                "nom": "Descens a Cala Sant Vicent",
                "desc": "Baixada pronunciada cap a la vall costanera i arribada a la platja."
            }
        ]
    },
    {
        "slug": "eivissa-far-des-moscarter",
        "nom": "Far des Moscarter i Portinatx",
        "municipi": "Sant Joan de Labritja",
        "zona": "Portinatx / Nord",
        "illa": "Eivissa",
        "distancia_km": 7.4,
        "desnivell_positiu_m": 180,
        "dificultat": "Moderada",
        "durada_estimada": "2h 30min",
        "apte_unitats": [
            "Llops/Daines",
            "Pioners/Rangers",
            "Rutes i guies"
        ],
        "punts_aigua": [
            "Portinatx (nucli urbà a l'inici i final)"
        ],
        "consells_seguretat": "Camí costaner vora penya-segats marítims alts i verticals. Mantenir distància de seguretat prudent respecte a la vora del penyal. Zona exposada a cops forts de vent de tramuntana i insolació intensa. Portar aigua abundant, gorra i calçat adient per terreny rocós.",
        "descripcio": "Ruta circular per la punta nord d'Eivissa fins al far des Moscarter (la torre de senyals marítims més alta de les Illes Balears amb 52m d'alçada) i la Torre de Portinatx.",
        "lat": 39.1110,
        "lon": 1.5175,
        "punt_origen": "Platja de Portinatx / Badia de Portinatx (parada bus L21)",
        "font": "Consell Insular d'Eivissa",
        "wikiloc_url": "https://www.wikiloc.com/rutas-senderismo/far-des-moscarter-torre-portinatx-eivissa-18450123",
        "track_coordinates": [
            [39.1110, 1.5175],
            [39.1180, 1.5240],
            [39.1245, 1.5320],
            [39.1190, 1.5150]
        ],
        "punts_interes": [
            "Badia de Portinatx",
            "Cala d'en Serra (mirador)",
            "Far des Moscarter (52 metres)",
            "Torre de Portinatx (segle XVIII)"
        ],
        "itinerari_passos": [
            {
                "pas": 1,
                "nom": "De Portinatx a Sa Punta",
                "desc": "Sortida des de la platja de Portinatx pel camí de costa en direcció nord."
            },
            {
                "pas": 2,
                "nom": "Far des Moscarter",
                "desc": "Arribada a l'espectacular far pintat amb franges blanques i negres sobre el penya-segat."
            },
            {
                "pas": 3,
                "nom": "Torre de Portinatx i retorn",
                "desc": "Retorn circular passant per la torre de defensa i tornada a la cala."
            }
        ]
    },
    {
        "slug": "eivissa-sant-mateu-cala-albarca",
        "nom": "Cala d'Albarca i Pont de Pedra",
        "municipi": "Sant Antoni de Portmany",
        "zona": "Pla de Corona / Nord-Oest",
        "illa": "Eivissa",
        "distancia_km": 6.8,
        "desnivell_positiu_m": 260,
        "dificultat": "Moderada",
        "durada_estimada": "2h 15min",
        "apte_unitats": [
            "Pioners/Rangers",
            "Rutes i guies"
        ],
        "punts_aigua": [
            "Sant Mateu d'Albarca (poble, inici); nul al tram de costa"
        ],
        "consells_seguretat": "Perill extrem de caiguda al buit: està terminantment prohibit creuar o caminar per damunt de l'arc natural de pedra (Pont de Pedra) suspès sobre el penya-segat. Desnivell fort i còdols relliscosos al descens cap a la cala; atenció a relliscades i evitar hores de màxima calor estival.",
        "descripcio": "Excursió pel cor rural de l'illa que descendeix per pinars i oliveres fins als monumentals penya-segats de Cala d'Albarca i el sorprenent pont natural de roca esculpit pel mar.",
        "lat": 39.0395,
        "lon": 1.3820,
        "punt_origen": "Església de Sant Mateu d'Albarca (Sant Antoni de Portmany, parada bus L30)",
        "font": "Consell Insular d'Eivissa",
        "wikiloc_url": "https://www.wikiloc.com/rutas-senderismo/sant-mateu-cala-dalbarca-pont-de-pedra-19842103",
        "track_coordinates": [
            [39.0395, 1.3820],
            [39.0460, 1.3850],
            [39.0520, 1.3880],
            [39.0560, 1.3910]
        ],
        "punts_interes": [
            "Església de Sant Mateu d'Albarca",
            "Pla vinícola d'Albarca",
            "Penya-segats verges de Cala d'Albarca",
            "Pont natural de pedra"
        ],
        "itinerari_passos": [
            {
                "pas": 1,
                "nom": "Camins rurals de Sant Mateu",
                "desc": "Sortida des de l'església creuant els camps de vinya i ametllers."
            },
            {
                "pas": 2,
                "nom": "Descens pel pinar a la costa",
                "desc": "Baixada amb pendent marcat cap a la balconada dels penya-segats."
            },
            {
                "pas": 3,
                "nom": "Pont de Pedra i cala",
                "desc": "Mirador de l'arc natural de pedra i retorn en ascens cap al poble."
            }
        ]
    },
    {
        "slug": "eivissa-torre-rovira-platges-comte",
        "nom": "Torre d'en Rovira i Platges de Comte",
        "municipi": "Sant Josep de sa Talaia",
        "zona": "Costa Ponent / Cala Comte",
        "illa": "Eivissa",
        "distancia_km": 5.5,
        "desnivell_positiu_m": 60,
        "dificultat": "Fàcil",
        "durada_estimada": "1h 45min",
        "apte_unitats": [
            "Castors/Fures",
            "Llops/Daines",
            "Pioners/Rangers",
            "Rutes i guies"
        ],
        "punts_aigua": [
            "Platges de Comte (serveis a l'inici) i Cala Bassa"
        ],
        "consells_seguretat": "Traçat costaner planer amb forta insolació i sense arbrat d'ombra. Portar aigua abundant, gorra i protecció solar. Precaució a les vores dels espadats costaners baixos quan hi hagi onatge o mar de fons. Ruta molt accessible i idònia per a infants.",
        "descripcio": "Ruta litoral planera que uneix les idíl·liques Platges de Comte amb la Torre d'en Rovira (segle XVIII), gaudint de panoràmiques directes a l'arxipèlag protegit de sa Conillera.",
        "lat": 38.9625,
        "lon": 1.2205,
        "punt_origen": "Aparcament de Platges de Comte (Cala Comte, parada bus L4)",
        "font": "Consell Insular d'Eivissa",
        "wikiloc_url": "https://www.wikiloc.com/rutas-senderismo/platges-de-comte-torre-den-rovira-cala-bassa-12948271",
        "track_coordinates": [
            [38.9625, 1.2205],
            [38.9690, 1.2230],
            [38.9740, 1.2290],
            [38.9680, 1.2410]
        ],
        "punts_interes": [
            "Platges de Comte (Cala Comte)",
            "Torre d'en Rovira (segle XVIII)",
            "Vistes a l'illot de sa Conillera",
            "Cala Roja",
            "Cala Bassa"
        ],
        "itinerari_passos": [
            {
                "pas": 1,
                "nom": "Inici a Platges de Comte",
                "desc": "Sortida de l'aparcament pel camí costaner en direcció nord."
            },
            {
                "pas": 2,
                "nom": "Torre d'en Rovira",
                "desc": "Visita exterior a la torre defensiva amb vista cap a sa Conillera."
            },
            {
                "pas": 3,
                "nom": "Connexió amb Cala Bassa i tornada",
                "desc": "Recorregut costaner fins a Cala Bassa i retorn planer."
            }
        ]
    },
    {
        "slug": "eivissa-torre-des-molar",
        "nom": "Torre des Molar i Port de Sant Miquel",
        "municipi": "Sant Joan de Labritja",
        "zona": "Port de Sant Miquel / Nord",
        "illa": "Eivissa",
        "distancia_km": 3.2,
        "desnivell_positiu_m": 120,
        "dificultat": "Fàcil",
        "durada_estimada": "1h 15min",
        "apte_unitats": [
            "Castors/Fures",
            "Llops/Daines",
            "Pioners/Rangers",
            "Rutes i guies"
        ],
        "punts_aigua": [
            "Port de Sant Miquel (platja, fonts públiques i botigues)"
        ],
        "consells_seguretat": "Camí curt amb pujada dreta sobre terreny rocós fins al cim de la talaia a 95 metres d'altitud. Compte amb el penya-segat obert al costat de la torre; mantenir la mainada allunyada del cantó de mar. Protecció solar i aigua imprescindible davant la manca d'ombra al capdamunt.",
        "descripcio": "Passejada costanera des de la platja del Port de Sant Miquel fins a la Torre des Molar, atalaia del segle XVIII que domina la boca del port i els illots de s'Illa Murada amb vistes impressionants de la costa nord.",
        "lat": 39.0805,
        "lon": 1.4420,
        "punt_origen": "Platja del Port de Sant Miquel (parada bus L25)",
        "font": "Consell Insular d'Eivissa",
        "wikiloc_url": "https://www.wikiloc.com/rutas-senderismo/port-de-sant-miquel-torre-des-molar-17382910",
        "track_coordinates": [
            [39.0805, 1.4420],
            [39.0840, 1.4390],
            [39.0875, 1.4320]
        ],
        "punts_interes": [
            "Badia del Port de Sant Miquel",
            "Cova de Can Marçà",
            "Torre des Molar (segle XVIII)",
            "Illot de s'Illa Murada"
        ],
        "itinerari_passos": [
            {
                "pas": 1,
                "nom": "Passeig des de la platja",
                "desc": "Sortida de la sorra del Port de Sant Miquel pujant pel camí de la cova."
            },
            {
                "pas": 2,
                "nom": "Pujada a la talaia",
                "desc": "Sender drecera per roca viva fins a la cota 95m."
            },
            {
                "pas": 3,
                "nom": "Mirador de la Torre des Molar",
                "desc": "Panoràmica de la badia i baixada pel mateix camí."
            }
        ]
    }
]

# ---------------------------------------------------------------------------
# 2. Formentera Green Routes (3 authentic routes)
# ---------------------------------------------------------------------------
RUTES_FORMENTERA = [
    {
        "slug": "formentera-ruta-verda-1-la-savina-ses-illetes",
        "nom": "Ruta Verda 1: La Savina a Ses Illetes",
        "municipi": "Formentera",
        "zona": "Parc Natural de ses Salines de Formentera",
        "illa": "Formentera",
        "distancia_km": 3.4,
        "desnivell_positiu_m": 10,
        "dificultat": "Fàcil",
        "durada_estimada": "1h 00min",
        "apte_unitats": [
            "Castors/Fures",
            "Llops/Daines",
            "Pioners/Rangers",
            "Rutes i guies"
        ],
        "punts_aigua": [
            "Port de la Savina (inici, fonts públiques i serveis)"
        ],
        "consells_seguretat": "Nul·la ombra natural i forta insolació. Calor elevada i reflex solar intens sobre la sorra i les salines; risc alt de deshidratació i cop de calor durant els mesos càlids. Dur barret, protecció solar factor 50 i mínim 2 litres d'aigua per persona. Respectar estrictament el pas per les passarel·les de fusta per no erosionar el sistema dunar protegit.",
        "descripcio": "Ruta verda de senderisme i cicloturisme que arrenca al port de la Savina, voreja l'Estany Pudent i els antics estanys saliners fins a la idíl·lica platja de ses Illetes, dins el Parc Natural de ses Salines d'Eivissa i Formentera.",
        "lat": 38.7335,
        "lon": 1.4170,
        "punt_origen": "Estació Marítima del Port de La Savina (parada bus L1/L2)",
        "font": "Consell de Formentera",
        "wikiloc_url": "https://www.wikiloc.com/rutas-senderismo/ruta-verda-1-la-savina-ses-illetes-formentera-14829104",
        "track_coordinates": [
            [38.7335, 1.4170],
            [38.7420, 1.4230],
            [38.7510, 1.4280],
            [38.7580, 1.4330]
        ],
        "punts_interes": [
            "Port de la Savina",
            "Estany Pudent i avifauna aquàtica",
            "Salines històriques de Formentera",
            "Platja de Cavall d'en Borràs",
            "Platja de ses Illetes"
        ],
        "itinerari_passos": [
            {
                "pas": 1,
                "nom": "Sortida de la Savina",
                "desc": "Inici al port vorejant l'Estany Pudent pel carril senyalitzat de terra."
            },
            {
                "pas": 2,
                "nom": "Camí de les Salines",
                "desc": "Recorregut entre els estanys saliners tradicionals i la costa de ponent."
            },
            {
                "pas": 3,
                "nom": "Passarel·les de ses Illetes",
                "desc": "Tram final per passarel·les de fusta sobre el sistema dunar fins a la platja."
            }
        ]
    },
    {
        "slug": "formentera-cami-sa-pujada-la-mola",
        "nom": "Camí de sa Pujada (La Mola)",
        "municipi": "Formentera",
        "zona": "Es Caló / La Mola",
        "illa": "Formentera",
        "distancia_km": 4.0,
        "desnivell_positiu_m": 195,
        "dificultat": "Moderada",
        "durada_estimada": "1h 30min",
        "apte_unitats": [
            "Llops/Daines",
            "Pioners/Rangers",
            "Rutes i guies"
        ],
        "punts_aigua": [
            "Es Caló de Sant Agustí (inici)",
            "El Pilar de la Mola (final)"
        ],
        "consells_seguretat": "Històric camí empedrat (Bé d'Interès Cultural) amb un desnivell empinat. Les lloses de pedra calcària polida són molt relliscoses amb humitat matinal o pluja; indispensable calçat de muntanya. Alts penya-segats sobre el mar; extremar la precaució i supervisió d'escoltes als miradors naturals per prevenir qualsevol perill de caiguda. Forta calor i sol directe a l'estiu; portar aigua abundant, gorra i crema de protecció solar.",
        "descripcio": "L'antiga via d'accés tradicional a l'altiplà de la Mola, també coneguda com a camí Romà, declarada Bé d'Interès Cultural. Ofereix les vistes panoràmiques més espectaculars de tot l'istme de Formentera i les aigües del nord.",
        "lat": 38.6780,
        "lon": 1.5170,
        "punt_origen": "Port pesquer d'Es Caló de Sant Agustí (parada bus L2)",
        "font": "Consell de Formentera",
        "wikiloc_url": "https://www.wikiloc.com/rutas-senderismo/ruta-verda-25-cami-de-sa-pujada-es-calo-la-mola-16382901",
        "track_coordinates": [
            [38.6780, 1.5170],
            [38.6720, 1.5240],
            [38.6690, 1.5350],
            [38.6680, 1.5450]
        ],
        "punts_interes": [
            "Port pesquer d'Es Caló de Sant Agustí",
            "Varadors tradicionals de fusta",
            "Camí empedrat de sa Pujada (BIC)",
            "Mirador natural de les Rotes",
            "Altiplà d'El Pilar de la Mola"
        ],
        "itinerari_passos": [
            {
                "pas": 1,
                "nom": "Inici a Es Caló",
                "desc": "Sortida des del port pesquer creuant la carretera Ma-2 cara a l'inici del camí empedrat."
            },
            {
                "pas": 2,
                "nom": "Ascensió pel Camí Romà",
                "desc": "Pujada progressiva per la calçada de pedra amb miradors cap als dos costats de l'illa."
            },
            {
                "pas": 3,
                "nom": "Arribada a La Mola",
                "desc": "Coronament de l'altiplà i arribada a la pista que condueix al poble del Pilar."
            }
        ]
    },
    {
        "slug": "formentera-far-cap-de-barbaria",
        "nom": "Far del Cap de Barbaria",
        "municipi": "Formentera",
        "zona": "Cap de Barbaria / Sud",
        "illa": "Formentera",
        "distancia_km": 4.4,
        "desnivell_positiu_m": 40,
        "dificultat": "Fàcil",
        "durada_estimada": "1h 15min",
        "apte_unitats": [
            "Castors/Fures",
            "Llops/Daines",
            "Pioners/Rangers",
            "Rutes i guies"
        ],
        "punts_aigua": [
            "Cap punt al recorregut; portar aigua des de Sant Francesc Xavier"
        ],
        "consells_seguretat": "Entorn semidesèrtic i rocós amb manca total d'ombra natural o arbrat. Forta calor i insolació extrema; dur mínim 2 litres d'aigua per persona, barret i protecció solar. Perill extrem de caiguda al buit a la Cova Foradada (avenc que s'obre verticalment sobre el penya-segat marítim a gran alçada) i al perímetre dels penya-segats del far; supervisió d'escoltes estricta i prohibit apropar-se a la vora del penyal.",
        "descripcio": "Trajecte tranquil pel paisatge àrid i solitari del sud de Formentera cap al far del Cap de Barbaria, la Torre de Garroveret i la cèlebre Cova Foradada foradada al penya-segat.",
        "lat": 38.6650,
        "lon": 1.3960,
        "punt_origen": "Pàrquing d'accés al Cap de Barbaria (barrera forestal)",
        "font": "Consell de Formentera",
        "wikiloc_url": "https://www.wikiloc.com/rutas-senderismo/ruta-verda-8-cap-de-barbaria-far-cova-foradada-15948302",
        "track_coordinates": [
            [38.6650, 1.3960],
            [38.6580, 1.3910],
            [38.6510, 1.3870],
            [38.6480, 1.3850]
        ],
        "punts_interes": [
            "Paisatge semidesèrtic del Cap de Barbaria",
            "Far de Barbaria",
            "Cova Foradada (avenc natural al penya-segat)",
            "Torre des Garroveret (segle XVIII)",
            "Penya-segats de la costa sud"
        ],
        "itinerari_passos": [
            {
                "pas": 1,
                "nom": "Pista des del pàrquing",
                "desc": "Sortida de la barrera per la pista asfaltada d'accés restringit a vianants i bicicletes."
            },
            {
                "pas": 2,
                "nom": "Arribada al Far",
                "desc": "Passeig fins a l'esplanada del far amb el mar obert a l'horitzó."
            },
            {
                "pas": 3,
                "nom": "Torre de Garroveret i Cova Foradada",
                "desc": "Exploració amb màxima prudència de la torre i els miradors abans de retornar."
            }
        ]
    }
]

def main():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    eivissa_path = DATA_DIR / "rutes_eivissa.json"
    formentera_path = DATA_DIR / "rutes_formentera.json"

    # Write Eivissa dataset
    with open(eivissa_path, "w", encoding="utf-8") as f:
        json.dump(RUTES_EIVISSA, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Generated {eivissa_path} ({len(RUTES_EIVISSA)} routes)")

    # Write Formentera dataset
    with open(formentera_path, "w", encoding="utf-8") as f:
        json.dump(RUTES_FORMENTERA, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Generated {formentera_path} ({len(RUTES_FORMENTERA)} routes)")

if __name__ == "__main__":
    main()
