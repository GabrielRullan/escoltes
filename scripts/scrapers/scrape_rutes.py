import os
import json

def get_mallorca_routes_data():
    rutes = [
        {
            "slug": "gr221-etapa-1-port-andratx-trapa",
            "nom": "GR-221 Etapa 1: Port d'Andratx - Sant Elm - La Trapa",
            "distancia_km": 11.5,
            "desnivell_positiu_m": 480,
            "dificultat": "Moderada",
            "durada_estimada": "3h 45min",
            "punts_aigua": ["Sant Elm (poble)", "Font de la Trapa (sense garantia potabilitat)"],
            "passos_finca_privada": ["Finca de la Trapa (Grup Balear d'Ornitologia - GOB)"],
            "punts_interes": ["Monestir de la Trapa", "Cala en Basset", "Vistes a sa Dragonera"],
            "consells_seguretat": "Tram sense ombra a l'estiu. Aigua obligatòria mínim 2L per escolta.",
            "apte_unitats": ["Pioners/Rangers", "Rovers/Rutes"],
            "lat": 39.5785, "lon": 2.3550,
            "descripcio": "Primera etapa del GR-221 que connecta Port d'Andratx i Sant Elm amb el Monestir de la Trapa."
        },
        {
            "slug": "gr221-etapa-4-deia-port-soller",
            "nom": "GR-221 Etapa 4: Deià - Port de Sóller (Camí de Castelló)",
            "distancia_km": 10.2,
            "desnivell_positiu_m": 310,
            "dificultat": "Fàcil - Moderada",
            "durada_estimada": "3h 15min",
            "punts_aigua": ["Deià (poble)", "Can Boi", "Refugi de Muleta / Port de Sóller"],
            "passos_finca_privada": ["Camí de Castelló (passos de pedra en sec habilitats)"],
            "punts_interes": ["Tafona de Can Boi", "Capella de Castelló", "Far de Muleta"],
            "consells_seguretat": "Ideal per a branques joves (Castors, Llops). Camí molt ben senyalitzat.",
            "apte_unitats": ["Llops/Daines", "Pioners/Rangers", "Rovers/Rutes"],
            "lat": 39.7491, "lon": 2.6483,
            "descripcio": "Etapa costanera assequible i d'alt valor patrimonial entre Deià i el Port de Sóller, passant pel Refugi de Muleta i Can Boi."
        },
        {
            "slug": "gr221-etapa-5-soller-tossals-verds",
            "nom": "GR-221 Etapa 5: Sóller - Refugi de Tossals Verds (per Biniaraix)",
            "distancia_km": 14.8,
            "desnivell_positiu_m": 890,
            "dificultat": "Exigent",
            "durada_estimada": "5h 30min",
            "punts_aigua": ["Biniaraix (font)", "Font de l'Ofre (no sempre flueix)", "Refugi de Tossals Verds"],
            "passos_finca_privada": ["Finca de l'Ofre (respectar estrictament el camí marcat)"],
            "punts_interes": ["Barranc de Biniaraix", "Coll de l'Ofre", "Embassament de Cúber"],
            "consells_seguretat": "Fort desnivell inicial pel monument del Barranc de Biniaraix. En pluja, el torrent va molt carregat.",
            "apte_unitats": ["Pioners/Rangers", "Rovers/Rutes"],
            "lat": 39.7663, "lon": 2.7153,
            "descripcio": "Espectacular etapa de muntanya que remunta el Barranc de Biniaraix, passa per Cúber i culmina al Refugi de Tossals Verds."
        },
        {
            "slug": "gr221-etapa-6-tossals-verds-son-amer",
            "nom": "GR-221 Etapa 6: Refugi de Tossals Verds - Refugi de Son Amer (Lluc)",
            "distancia_km": 15.3,
            "desnivell_positiu_m": 830,
            "dificultat": "Exigent",
            "durada_estimada": "5h 45min",
            "punts_aigua": ["Refugi de Tossals Verds", "Font des Prat", "Monestir de Lluc"],
            "passos_finca_privada": ["Coll des Coloms / Prat de Cúber"],
            "punts_interes": ["Coll de les Cases de la Neu", "Puig de Massanella (desviació)", "Lluc"],
            "consells_seguretat": "Coll alt exposat a vent i boira a l'hivern. Equipament tècnic i calçat de muntanya obligatori.",
            "apte_unitats": ["Pioners/Rangers", "Rovers/Rutes"],
            "lat": 39.7583, "lon": 2.8222,
            "descripcio": "L'etapa reina del GR-221 que travessa el cor de la serra de Tramuntana des de Tossals Verds fins al santuari de Lluc."
        },
        {
            "slug": "volta-puig-de-maria-pollenca",
            "nom": "Volta al Puig de Maria (Pollença)",
            "distancia_km": 4.5,
            "desnivell_positiu_m": 240,
            "dificultat": "Fàcil",
            "durada_estimada": "1h 45min",
            "punts_aigua": ["Pollença poble", "Santuari del Puig de Maria"],
            "passos_finca_privada": ["Camí públic pavimentat i empedrat"],
            "punts_interes": ["Santuari del segle XIV", "Vistes a la badia de Pollença i Alcúdia"],
            "consells_seguretat": "Excel·lent opció per a iniciació de Castors i Llops.",
            "apte_unitats": ["Castors/Fures", "Llops/Daines", "Pioners/Rangers"],
            "lat": 39.8735, "lon": 3.0180,
            "descripcio": "Ruta fàcil d'iniciació per a les branques més joves cap al cim del Puig de Maria de Pollença."
        },
        {
            "slug": "castell-d-alaro",
            "nom": "Excursió al Castell d'Alaró (des d'Orient o Es Verger)",
            "distancia_km": 8.0,
            "desnivell_positiu_m": 450,
            "dificultat": "Moderada",
            "durada_estimada": "3h 00min",
            "punts_aigua": ["Orient / Es Verger", "Hostal del Castell d'Alaró"],
            "passos_finca_privada": ["Camí del Castell"],
            "punts_interes": ["Castell d'Alaró", "Hospederia", "Vistes panoràmiques del Pla i la Serra"],
            "consells_seguretat": "Compte amb les pedres resbaladisses en dies de pluja.",
            "apte_unitats": ["Llops/Daines", "Pioners/Rangers", "Rovers/Rutes"],
            "lat": 39.7025, "lon": 2.7915,
            "descripcio": "Excursió clàssica de l'escoltisme mallorquí cap a la fortalesa rocosa del Castell d'Alaró."
        },
        {
            "slug": "torrent-de-pareis",
            "nom": "Torrent de Pareis (Només estiu / temps sec)",
            "distancia_km": 7.2,
            "desnivell_positiu_m": 50,
            "dificultat": "Molt Exigent / Tècnica",
            "durada_estimada": "5h 00min",
            "punts_aigua": ["Escorca (inici) - CAP AIGUA EN TOT EL RECORREGUT"],
            "passos_finca_privada": ["Entre d'Escorca"],
            "punts_interes": ["Entreforc", "Cova des Romagueral", "Sa Calobra"],
            "consells_seguretat": "PROHIBIT amb qualsevol risc de pluja (risc de riada mortal). Destresa, cordes de seguretat i 3L d'aigua obligatoris. Només Rovers/Caps.",
            "apte_unitats": ["Rovers/Rutes"],
            "lat": 39.8260, "lon": 2.8460,
            "descripcio": "La travessa de cañón més famosa de la Mediterrània. Extrema precaució i preparació tècnica."
        }
    ]
    return rutes

def main():
    os.makedirs("data", exist_ok=True)
    data = get_mallorca_routes_data()
    output_path = os.path.join("data", "rutes_mallorca.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"S'han desat {len(data)} rutes amb coordenades a {output_path}")

if __name__ == "__main__":
    main()
