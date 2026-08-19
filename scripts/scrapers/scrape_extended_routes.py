import os
import json

def get_extended_routes_dataset():
    routes = [
        # --- GR-221 ETAPES ---
        {
            "slug": "gr221-etapa-1-port-andratx-trapa",
            "nom": "GR-221 Etapa 1: Port d'Andratx a La Trapa",
            "municipi": "Andratx",
            "zona": "Tramuntana Sud",
            "distancia_km": 11.8,
            "desnivell_positiu_m": 480,
            "dificultat": "Moderada",
            "durada_estimada": "4h 30min",
            "apte_unitats": ["Pioners/Rangers", "Rovers/Rutes"],
            "punts_aigua": ["Port d'Andratx (abans de sortir)", "Sant Elm"],
            "passos_finca_privada": ["Pas de sa Gramola (camí públic)", "Coll des Pal (obert)"],
            "punts_interes": ["Coll des Pal", "Cala en Basset", "Monestir de la Trapa", "Vistes a sa Dragonera"],
            "consells_seguretat": "Tram sense ombra a la primera meitat. Evitar hores centrals de sol a l'estiu.",
            "descripcio": "Primer tram de la Ruta de Pedra en Sec GR-221 que voreja els penya-segats del sud-oest de Mallorca des del Port d'Andratx fins a l'antic monestir trapenc de la Trapa.",
            "lat": 39.5440, "lon": 2.3800,
            "track_coordinates": [
                [39.5440, 2.3800],
                [39.5610, 2.3690],
                [39.5780, 2.3610],
                [39.5980, 2.3580]
            ],
            "itinerari_passos": [
                {"pas": 1, "nom": "Inici al Port d'Andratx", "desc": "Sortida des de la zona del port cap al camí del Coll des Pal."},
                {"pas": 2, "nom": "Ascens al Coll des Pal", "desc": "Punyada de pujada per sender de pedra amb vistes a la badia d'Andratx."},
                {"pas": 3, "nom": "Cala en Basset i Mirador", "desc": "Desviament cap al mirador de sa Dragonera i de la torre de Cala en Basset."},
                {"pas": 4, "nom": "Arribada a la Trapa", "desc": "Descens cap a les cases i marjades del monestir de la Trapa."}
            ]
        },
        {
            "slug": "gr221-etapa-2-la-trapa-estellencs",
            "nom": "GR-221 Etapa 2: La Trapa a Estellencs",
            "municipi": "Andratx / Estellencs",
            "zona": "Tramuntana Sud",
            "distancia_km": 14.5,
            "desnivell_positiu_m": 620,
            "dificultat": "Exigent",
            "durada_estimada": "5h 45min",
            "apte_unitats": ["Pioners/Rangers", "Rovers/Rutes"],
            "punts_aigua": ["Font de ses Fontanelles", "Vila d'Estellencs"],
            "passos_finca_privada": ["Pas de s'Escapçat", "Ses Fontanelles (passos habilitats)"],
            "punts_interes": ["Coll de sa Gramola", "Puig de s'Esclop", "Vall d'Estellencs"],
            "consells_seguretat": "Atenció a la baixada del Pas de s'Escapçat amb terregada descomposada.",
            "descripcio": "Etapa de transició de la Tramuntana sud que travessa el Coll de sa Gramola i les faldilles del puig de s'Esclop fins al poble d'Estellencs.",
            "lat": 39.5980, "lon": 2.3580,
            "track_coordinates": [
                [39.5980, 2.3580],
                [39.6080, 2.3910],
                [39.6210, 2.4280],
                [39.6380, 2.4550]
            ],
            "itinerari_passos": [
                {"pas": 1, "nom": "Sortida de la Trapa", "desc": "Ascensió pel pas de s'Escapçat fins a recuperar el camí alt."},
                {"pas": 2, "nom": "Coll de sa Gramola", "desc": "Creuament de la carretera Ma-10 a la zona del coll de sa Gramola."},
                {"pas": 3, "nom": "Ses Fontanelles", "desc": "Pas pel refugi privat de ses Fontanelles i ascens cap a la Coma d'en Vidal."},
                {"pas": 4, "nom": "Arribada a Estellencs", "desc": "Baixada entre marjades d'oliveres fins al poble d'Estellencs."}
            ]
        },
        {
            "slug": "gr221-etapa-3-estellencs-esporles",
            "nom": "GR-221 Etapa 3: Estellencs a Esporles",
            "municipi": "Estellencs / Esporles",
            "zona": "Tramuntana Sud",
            "distancia_km": 15.2,
            "desnivell_positiu_m": 540,
            "dificultat": "Moderada",
            "durada_estimada": "5h 15min",
            "apte_unitats": ["Llops/Daines", "Pioners/Rangers", "Rovers/Rutes"],
            "punts_aigua": ["Font de sa Coma (Banyalbufar)", "Banyalbufar vila", "Esporles vila"],
            "passos_finca_privada": ["Camí des Correu (públic senyalitzat)"],
            "punts_interes": ["Marjades de Banyalbufar", "Camí des Correu", "Plana de sa Fita del Ram"],
            "consells_seguretat": "Tram molt ben senyalitzat. Cuidar els peus a la terregada de pedres del Camí des Correu.",
            "descripcio": "Una de les etapes més històriques que recorre l'antic Camí des Correu entre Banyalbufar i Esporles travessant boscos d'alzinar.",
            "lat": 39.6380, "lon": 2.4550,
            "track_coordinates": [
                [39.6380, 2.4550],
                [39.6520, 2.4810],
                [39.6680, 2.5120],
                [39.6689, 2.5769]
            ],
            "itinerari_passos": [
                {"pas": 1, "nom": "Estellencs a Banyalbufar", "desc": "Tram pel vell camí de la marjades de Banyalbufar."},
                {"pas": 2, "nom": "Banyalbufar Vila", "desc": "Punt de recàrrega d'aigua i menjar al poble."},
                {"pas": 3, "nom": "Camí des Correu", "desc": "Pujada tradicional empedrada per l'alzinar d'Esporles."},
                {"pas": 4, "nom": "Arribada a Esporles", "desc": "Descens suau fins al passeig d'Esporles."}
            ]
        },
        {
            "slug": "gr221-etapa-4-esporles-deia",
            "nom": "GR-221 Etapa 4: Esporles a Deià",
            "municipi": "Esporles / Valldemossa / Deià",
            "zona": "Tramuntana Central",
            "distancia_km": 19.6,
            "desnivell_positiu_m": 890,
            "dificultat": "Exigent",
            "durada_estimada": "6h 45min",
            "apte_unitats": ["Pioners/Rangers", "Rovers/Rutes"],
            "punts_aigua": ["Esporles vila", "Valldemossa vila", "Deià vila (Refugi Can Boi)"],
            "passos_finca_privada": ["Camí de sa Coma des Cairats", "Pla des Pouet"],
            "punts_interes": ["Muntanya de sa Comuna", "Valldemossa", "Camí de s'Arxiduc", "Son Marroig"],
            "consells_seguretat": "Etapa llarga amb desnivell acusat. Cal estar atents a la boira a la cresta de s'Arxiduc.",
            "descripcio": "Espectacular travessa que connecta Esporles amb Valldemossa i ascendeix pel Camí de s'Arxiduc abans de baixar al poble de Deià.",
            "lat": 39.6689, "lon": 2.5769,
            "track_coordinates": [
                [39.6689, 2.5769],
                [39.7119, 2.6225],
                [39.7280, 2.6350],
                [39.7491, 2.6483]
            ],
            "itinerari_passos": [
                {"pas": 1, "nom": "Esporles a Valldemossa", "desc": "Pujada per sa Comuna d'Esporles i baixada cap a Valldemossa."},
                {"pas": 2, "nom": "Valldemossa a sa Coma des Cairats", "desc": "Ascensió cap al Pla des Pouet i la serra de s'Arxiduc."},
                {"pas": 3, "nom": "Camí de s'Arxiduc", "desc": "Cresta panoràmica sobre la mar de Deià i sa Foradada."},
                {"pas": 4, "nom": "Descens a Deià i Refugi Can Boi", "desc": "Baixada de pedra empedrada fins al centre de Deià."}
            ]
        },
        {
            "slug": "gr221-etapa-5-deia-port-soller",
            "nom": "GR-221 Etapa 5: Deià al Port de Sóller",
            "municipi": "Deià / Sóller",
            "zona": "Tramuntana Central",
            "distancia_km": 10.2,
            "desnivell_positiu_m": 310,
            "dificultat": "Fàcil - Moderada",
            "durada_estimada": "3h 30min",
            "apte_unitats": ["Castors/Fures", "Llops/Daines", "Pioners/Rangers", "Rovers/Rutes"],
            "punts_aigua": ["Deià (Can Boi)", "Son Mico (cafè/aigua)", "Port de Sóller (Refugi Muleta)"],
            "passos_finca_privada": ["Camí des Pintors", "Son Mico (obert)"],
            "punts_interes": ["Cala Deià", "Llucalcari", "Finca de Son Mico", "Cap Gros i Far de Muleta"],
            "consells_seguretat": "Ideal per a totes les unitats escoltes. Ruta amena entre oliveres i mar.",
            "descripcio": "Una de les etapes més amables del GR-221 que discorre per la costa nord entre hortes d'oliveres centenàries i vistes al mar mediterrani.",
            "lat": 39.7491, "lon": 2.6483,
            "track_coordinates": [
                [39.7491, 2.6483],
                [39.7610, 2.6620],
                [39.7820, 2.6780],
                [39.7942, 2.6869]
            ],
            "itinerari_passos": [
                {"pas": 1, "nom": "Sortida de Deià (Can Boi)", "desc": "Camí baix cap a les hortes de Deià i Llucalcari."},
                {"pas": 2, "nom": "Pintors i Son Mico", "desc": "Travessa de la finca tradicional de Son Mico."},
                {"pas": 3, "nom": "Camí de Muleta", "desc": "Sendera flanquejada de fites fins a la pineda del Cap Gros."},
                {"pas": 4, "nom": "Refugi de Muleta", "desc": "Arribada al far i refugi de Muleta sobre la badia del Port de Sóller."}
            ]
        },
        {
            "slug": "gr221-etapa-6-soller-tossals-verds",
            "nom": "GR-221 Etapa 6: Sóller a Tossals Verds",
            "municipi": "Sóller / Escorca",
            "zona": "Tramuntana Central",
            "distancia_km": 15.0,
            "desnivell_positiu_m": 820,
            "dificultat": "Exigent",
            "durada_estimada": "5h 30min",
            "apte_unitats": ["Pioners/Rangers", "Rovers/Rutes"],
            "punts_aigua": ["Biniaraix", "Font de sa Mula", "Refugi Tossals Verds"],
            "passos_finca_privada": ["Barranc de Biniaraix (públic d'interès cultural)", "Coll des Cornadors"],
            "punts_interes": ["Barranc de Biniaraix", "Coll de l'Ofre", "Embassament de Cúber", "Pas des Llis"],
            "consells_seguretat": "Pujada contínua i empedrada al Barranc. Portar aigua suficient per a l'ascensió.",
            "descripcio": "Espectacular pujada pel monument d'enginyeria de pedra en sec del Barranc de Biniaraix fins al coll de l'Ofre i l'embassament de Cúber.",
            "lat": 39.7661, "lon": 2.7156,
            "track_coordinates": [
                [39.7661, 2.7156],
                [39.7580, 2.7480],
                [39.7821, 2.7915],
                [39.7583, 2.8222]
            ],
            "itinerari_passos": [
                {"pas": 1, "nom": "Sóller a Biniaraix", "desc": "Passeig des de la plaça de Sóller fins al llogaret de Biniaraix."},
                {"pas": 2, "nom": "Barranc de Biniaraix", "desc": "Ascensió pel famós camí empedrat del barranc entre bancals de taronjers i oliveres."},
                {"pas": 3, "nom": "Coll de l'Ofre i Cúber", "desc": "Superació del coll de l'Ofre amb vistes a la vall de Sóller i l'embassament de Cúber."},
                {"pas": 4, "nom": "Coll des Coloms a Tossals Verds", "desc": "Baixada pel Pas des Llis o Coll des Coloms fins al refugi de Tossals Verds."}
            ]
        },
        {
            "slug": "gr221-etapa-7-tossals-verds-son-amer",
            "nom": "GR-221 Etapa 7: Tossals Verds a Son Amer (Lluc)",
            "municipi": "Escorca",
            "zona": "Tramuntana Nord",
            "distancia_km": 14.8,
            "desnivell_positiu_m": 830,
            "dificultat": "Exigent",
            "durada_estimada": "5h 45min",
            "apte_unitats": ["Pioners/Rangers", "Rovers/Rutes"],
            "punts_aigua": ["Refugi Tossals Verds", "Font des Prat", "Font de sa Coma de sa Vinya", "Son Amer / Lluc"],
            "passos_finca_privada": ["Coll des Prat", "Coll de sa Batalla"],
            "punts_interes": ["Coll des Prat", "Puig de Massanella", "Ses Voltes d'en Galileu", "Monestir de Lluc"],
            "consells_seguretat": "Punt més alt del GR-221 (Coll des Prat, 1.205m). Atenció a les nevades a l'hivern i vent fort.",
            "descripcio": "El sostre del GR-221. Travessa les altures de la serra entre el Puig de Massanella i les Voltes d'en Galileu fins al Santuari de Lluc.",
            "lat": 39.7583, "lon": 2.8222,
            "track_coordinates": [
                [39.7583, 2.8222],
                [39.7910, 2.8450],
                [39.8080, 2.8690],
                [39.8215, 2.8872]
            ],
            "itinerari_passos": [
                {"pas": 1, "nom": "Sortida de Tossals Verds", "desc": "Camí cap a la Font des Prat per la frondosa vall d'Escorca."},
                {"pas": 2, "nom": "Ascens al Coll des Prat", "desc": "Pujada sostinguda fins al punt més alt del GR-221 a 1.205 metres d'altitud."},
                {"pas": 3, "nom": "Ses Voltes d'en Galileu", "desc": "Baixada espectacular pel zigzag empedrat de les cases de neu d'en Galileu."},
                {"pas": 4, "nom": "Arribada a Son Amer (Lluc)", "desc": "Entrada a la vall de Lluc i refugi de Son Amer."}
            ]
        },
        {
            "slug": "gr221-etapa-8-son-amer-pollenca",
            "nom": "GR-221 Etapa 8: Son Amer a Pollença",
            "municipi": "Escorca / Pollença",
            "zona": "Tramuntana Nord",
            "distancia_km": 16.7,
            "desnivell_positiu_m": 240,
            "dificultat": "Fàcil - Moderada",
            "durada_estimada": "4h 45min",
            "apte_unitats": ["Castors/Fures", "Llops/Daines", "Pioners/Rangers", "Rovers/Rutes"],
            "punts_aigua": ["Son Amer", "Binifaldó", "Font de la Sinieta", "Pollença vila"],
            "passos_finca_privada": ["Camí Vell de Lluc a Pollença (públic)"],
            "punts_interes": ["Binifaldó", "Puig Tomir", "Vall de March", "Pont Romà de Pollença"],
            "consells_seguretat": "Etapa còmoda i principalment en descens. Molt indicada per a unitats menudes.",
            "descripcio": "Última etapa del GR-221 que descendeix des de l'alzinar de Binifaldó per la frondosa vall de March fins al Pont Romà de Pollença.",
            "lat": 39.8215, "lon": 2.8872,
            "track_coordinates": [
                [39.8215, 2.8872],
                [39.8311, 2.8988],
                [39.8520, 2.9480],
                [39.8780, 3.0150]
            ],
            "itinerari_passos": [
                {"pas": 1, "nom": "Sortida de Son Amer", "desc": "Passeig ombrívol fins a les cases de Binifaldó."},
                {"pas": 2, "nom": "Coll de sa Batalla a Vall de March", "desc": "Descens suau pel Camí Vell de Pollença."},
                {"pas": 3, "nom": "Vall de March", "desc": "Planura de conreu paral·lela al torrent de Sant Jordi."},
                {"pas": 4, "nom": "Pont Romà i Pollença", "desc": "Entrada triomfal a Pollença pel Pont Romà."}
            ]
        },

        # --- EXCURSIONS DE FAMÍLIA I TURISME PETIT ---
        {
            "slug": "es-salt-des-freu-orient",
            "nom": "Es Salt des Freu (Orient / Bunyola)",
            "municipi": "Bunyola",
            "zona": "Tramuntana Central",
            "distancia_km": 4.5,
            "desnivell_positiu_m": 120,
            "dificultat": "Molt Fàcil",
            "durada_estimada": "1h 45min",
            "apte_unitats": ["Castors/Fures", "Llops/Daines", "Pioners/Rangers", "Rovers/Rutes"],
            "punts_aigua": ["Font de Cals Reis (Orient)"],
            "passos_finca_privada": ["Camí des Freu (públic)"],
            "punts_interes": ["Salt d'aigua des Freu", "Bosc de la Comuna de Bunyola", "Vila d'Orient"],
            "consells_seguretat": "Atenció a les pedres resbaladisses devora el torrent en època de pluges.",
            "descripcio": "Una de les excursions de família i escoltes més populars de Mallorca. Un passeig plàcid per l'alzinar que condueix a les espectaculars cascades del Salt des Freu.",
            "lat": 39.7210, "lon": 2.7680,
            "track_coordinates": [
                [39.7210, 2.7680],
                [39.7250, 2.7720],
                [39.7290, 2.7780]
            ],
            "itinerari_passos": [
                {"pas": 1, "nom": "Inici a la carretera d'Orient", "desc": "Aparcament al km 8.5 de la Ma-2100."},
                {"pas": 2, "nom": "Pineda i Alzinar des Freu", "desc": "Sender ample en descens suau."},
                {"pas": 3, "nom": "Cascada des Salt des Freu", "desc": "Arribada a les pozes i salts d'aigua."}
            ]
        },
        {
            "slug": "ses-fonts-ufanes-campanet",
            "nom": "Ses Fonts Ufanes (Campanet)",
            "municipi": "Campanet",
            "zona": "Raiguer",
            "distancia_km": 3.8,
            "desnivell_positiu_m": 60,
            "dificultat": "Molt Fàcil",
            "durada_estimada": "1h 15min",
            "apte_unitats": ["Castors/Fures", "Llops/Daines", "Pioners/Rangers", "Rovers/Rutes"],
            "punts_aigua": ["Centre de Visitors de Gabellí Petit"],
            "passos_finca_privada": ["Finca Pública de Gabellí Petit (Govern)"],
            "punts_interes": ["Fenomen hidrogeològic de les Fonts Ufanes", "Ermita de Sant Miquel", "Alzinar de Gabellí"],
            "consells_seguretat": "Ideal després d'episodis de pluja intensa per veure brotar l'aigua del terra.",
            "descripcio": "Ruta circular plana per la finca pública de Gabellí Petit per admirar l'únic fenomen hidrogeològic de les Fonts Ufanes quan l'aigua brota de l'alzinar.",
            "lat": 39.7890, "lon": 2.9640,
            "track_coordinates": [
                [39.7890, 2.9640],
                [39.7920, 2.9680],
                [39.7950, 2.9710]
            ],
            "itinerari_passos": [
                {"pas": 1, "nom": "Ermita de Sant Miquel", "desc": "Inici a la fita d'entrada de la finca Gabellí Petit."},
                {"pas": 2, "nom": "Camí de l'Alzinar", "desc": "Passejada adapada per a totes les edats."},
                {"pas": 3, "nom": "Brollador de les Ufanes", "desc": "Punt on l'aigua s'anega entre els arbres en dies de pluja."}
            ]
        },
        {
            "slug": "parc-natural-mondrago",
            "nom": "Parc Natural de Mondragó (Santanyí)",
            "municipi": "Santanyí",
            "zona": "Migjorn",
            "distancia_km": 5.2,
            "desnivell_positiu_m": 40,
            "dificultat": "Molt Fàcil",
            "durada_estimada": "2h 00min",
            "apte_unitats": ["Castors/Fures", "Llops/Daines", "Pioners/Rangers", "Rovers/Rutes"],
            "punts_aigua": ["Centre d'Informació del Parc Natural (sa Font de n'Alis)"],
            "passos_finca_privada": ["Parc Natural Protegit (públic)"],
            "punts_interes": ["Cala Mondragó", "s'Amarador", "Estany de sa Font de n'Alis", "Mirador des Cap des Moro"],
            "consells_seguretat": "Portar protecció solar i aigua a l'estiu.",
            "descripcio": "Ruta litoral per un dels parcs naturals més frondosos i ben conservats del sud de Mallorca, combinant estanys d'aigua dolça, pinedes i platges verges.",
            "lat": 39.3520, "lon": 3.1890,
            "track_coordinates": [
                [39.3520, 3.1890],
                [39.3560, 3.1920],
                [39.3590, 3.1960]
            ],
            "itinerari_passos": [
                {"pas": 1, "nom": "Centre d'Interpretació", "desc": "Inici al pàrquing de sa Font de n'Alis."},
                {"pas": 2, "nom": "Estany i Platja de s'Amarador", "desc": "Sendera de fusta que voreja la marjal."},
                {"pas": 3, "nom": "Mirador des Cap des Moro", "desc": "Vistes a les penyes litorals del sud."}
            ]
        }
    ]
    return routes

def main():
    os.makedirs("data", exist_ok=True)
    routes = get_extended_routes_dataset()
    output_path = os.path.join("data", "rutes_mallorca.json")
    
    # Read existing routes to keep all 59 routes and update enriched waypoint routes
    if os.path.exists(output_path):
        with open(output_path, "r", encoding="utf-8") as f:
            existing = json.load(f)
            # Create dict by slug
            routes_dict = {r["slug"]: r for r in existing}
            for enriched in routes:
                routes_dict[enriched["slug"]] = enriched
            full_routes = list(routes_dict.values())
    else:
        full_routes = routes
        
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(full_routes, f, ensure_ascii=False, indent=2)
    print(f"S'han desat AMB ÈXIT {len(full_routes)} rutes amb itinerari pas a pas i tracks a {output_path}")

if __name__ == "__main__":
    main()
