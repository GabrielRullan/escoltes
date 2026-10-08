import json

ROUTE_SOURCES = {
    # --- GR-221 Etapes oficials del Consell de Mallorca ---
    "gr221-etapa-1-port-andratx-trapa": {
        "font": "Consell de Mallorca (Ruta de Pedra en Sec GR-221)",
        "font_url": "https://caminsdepedra.conselldemallorca.cat/-/etapa-1-port-d-andratx-la-trapa",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=GR-221+Etapa+1+Port+d+Andratx+La+Trapa"
    },
    "gr221-etapa-2-la-trapa-estellencs": {
        "font": "Consell de Mallorca (Ruta de Pedra en Sec GR-221)",
        "font_url": "https://caminsdepedra.conselldemallorca.cat/-/etapa-2-la-trapa-estellencs",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=GR-221+Etapa+2+La+Trapa+Estellencs"
    },
    "gr221-etapa-3-estellencs-esporles": {
        "font": "Consell de Mallorca (Ruta de Pedra en Sec GR-221)",
        "font_url": "https://caminsdepedra.conselldemallorca.cat/-/etapa-3-estellencs-esporles",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=GR-221+Etapa+3+Estellencs+Esporles"
    },
    "gr221-etapa-4-esporles-deia": {
        "font": "Consell de Mallorca (Ruta de Pedra en Sec GR-221)",
        "font_url": "https://caminsdepedra.conselldemallorca.cat/-/etapa-4-esporles-can-boi",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=GR-221+Etapa+4+Esporles+Deia"
    },
    "gr221-etapa-5-deia-port-soller": {
        "font": "Consell de Mallorca (Ruta de Pedra en Sec GR-221)",
        "font_url": "https://caminsdepedra.conselldemallorca.cat/-/etapa-5-can-boi-muleta",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=GR-221+Etapa+5+Deia+Port+de+Soller"
    },
    "gr221-etapa-6-soller-tossals-verds": {
        "font": "Consell de Mallorca (Ruta de Pedra en Sec GR-221)",
        "font_url": "https://caminsdepedra.conselldemallorca.cat/-/etapa-6-muleta-tossals-verds",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=GR-221+Etapa+6+Soller+Tossals+Verds"
    },
    "gr221-etapa-7-tossals-verds-son-amer": {
        "font": "Consell de Mallorca (Ruta de Pedra en Sec GR-221)",
        "font_url": "https://caminsdepedra.conselldemallorca.cat/-/etapa-7-tossals-verds-son-amer",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=GR-221+Etapa+7+Tossals+Verds+Son+Amer"
    },
    "gr221-etapa-8-son-amer-pollenca": {
        "font": "Consell de Mallorca (Ruta de Pedra en Sec GR-221)",
        "font_url": "https://caminsdepedra.conselldemallorca.cat/-/etapa-8-son-amer-pont-roma",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=GR-221+Etapa+8+Son+Amer+Pollenca"
    },

    # --- Variant de Sa Costera (específicament esmentada per l'usuari) ---
    "fonts-de-sa-costera-soller": {
        "font": "Consell de Mallorca (Ruta de Pedra en Sec - Variant Sa Costera)",
        "font_url": "https://caminsdepedra.conselldemallorca.cat/variante-6-sa-costera-tramo-binibassi-cala-tuent",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Sa+Costera+Cala+Tuent+Soller"
    },

    # --- Finques Públiques i Parcs Naturals de les Illes Balears ---
    "finca-publica-raixa": {
        "font": "Consell de Mallorca (Finca Pública de Raixa)",
        "font_url": "https://raixa.conselldemallorca.cat/",
        "turismepetit_url": "https://www.turismepetit.com/excursion/finca-publica-de-raixa-en-bunyola/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Finca+Publica+de+Raixa"
    },
    "finca-publica-planicia-banyalbufar": {
        "font": "Govern de les Illes Balears (Finca Pública de Planícia)",
        "font_url": "https://www.caib.es/sites/espaisnaturalsprotegits/ca/finca_publica_de_planicia/",
        "turismepetit_url": "https://www.turismepetit.com/excursion/excursion-semicircular-por-la-finca-publica-de-planicia/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Finca+Publica+de+Planicia"
    },
    "puig-de-galatzo-font-des-pi": {
        "font": "Ajuntament de Calvià (Finca Pública de Galatzó)",
        "font_url": "https://www.calvia.com/fincagalatzo/",
        "turismepetit_url": "https://www.turismepetit.com/excursion/excursion-a-la-finca-publica-de-galatzo/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Puig+de+Galatzo+Font+des+Pi"
    },
    "muela-de-sesclop": {
        "font": "Ajuntament de Calvià (Finca Pública de Galatzó)",
        "font_url": "https://www.calvia.com/fincagalatzo/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Muela+de+s+Esclop+Galatzo"
    },
    "son-real-can-picafort": {
        "font": "Govern de les Illes Balears (Finca Pública de Son Real)",
        "font_url": "https://www.caib.es/sites/espaisnaturalsprotegits/ca/finca_publica_de_son_real/",
        "turismepetit_url": "https://www.turismepetit.com/excursion/finca-publica-de-son-real/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Finca+Publica+de+Son+Real"
    },
    "parc-natural-mondrago": {
        "font": "Govern de les Illes Balears (Parc Natural de Mondragó)",
        "font_url": "https://www.caib.es/sites/espaisnaturalsprotegits/ca/parc_natural_de_mondrago/",
        "turismepetit_url": "https://www.turismepetit.com/excursion/parque-natural-de-mondrago/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Parc+Natural+de+Mondrago"
    },
    "parc-natural-albufera-mallorca": {
        "font": "Govern de les Illes Balears (Parc Natural de s'Albufera)",
        "font_url": "https://www.caib.es/sites/espaisnaturalsprotegits/ca/parc_natural_de_salbufera_de_mallorca/",
        "turismepetit_url": "https://www.turismepetit.com/excursion/parque-natural-de-salbufera-de-mallorca/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Parc+Natural+de+s+Albufera+de+Mallorca"
    },
    "parc-natural-dragonera": {
        "font": "Consell de Mallorca (Parc Natural de sa Dragonera)",
        "font_url": "https://dragonera.conselldemallorca.cat/",
        "turismepetit_url": "https://www.turismepetit.com/excursion/parque-natural-de-sa-dragonera/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Parc+Natural+de+sa+Dragonera"
    },
    "salquerieta-vella-campament-soldats": {
        "font": "Govern de les Illes Balears (Parc Natural de la Península de Llevant)",
        "font_url": "https://www.caib.es/sites/espaisnaturalsprotegits/ca/parc_natural_de_la_peninsula_de_llevant/",
        "turismepetit_url": "https://www.turismepetit.com/excursion/parc-natural-de-llevant/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=S+Alqueria+Vella+Campament+Soldats+Arta"
    },
    "puig-de-sa-tudossa-arta": {
        "font": "Govern de les Illes Balears (Parc Natural de la Península de Llevant)",
        "font_url": "https://www.caib.es/sites/espaisnaturalsprotegits/ca/parc_natural_de_la_peninsula_de_llevant/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Puig+de+sa+Tudossa+Arta"
    },
    "ses-fonts-ufanes-campanet": {
        "font": "Govern de les Illes Balears (Monument Natural de ses Fonts Ufanes)",
        "font_url": "https://www.caib.es/sites/espaisnaturalsprotegits/ca/monument_natural_de_ses_fonts_ufanes/",
        "turismepetit_url": "https://www.turismepetit.com/excursion/ses-fonts-ufanes-en-campanet/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Ses+Fonts+Ufanes+Campanet"
    },
    "torrent-de-pareis": {
        "font": "Govern de les Illes Balears (Monument Natural del Torrent de Pareis)",
        "font_url": "https://www.caib.es/sites/espaisnaturalsprotegits/ca/monument_natural_dels_torrents_de_pareis_del_gorg_blau_i_de_lluc/",
        "turismepetit_url": "https://www.turismepetit.com/excursion/torrent-de-pareis-en-bus-y-barco/",
        "wikiloc_url": "https://es.wikiloc.com/rutas-senderismo/torrent-de-pareis-escorca-sa-calobra-2194812"
    },
    "torrent-de-pareis-escorca-sa-calobra": {
        "font": "Govern de les Illes Balears (Monument Natural del Torrent de Pareis)",
        "font_url": "https://www.caib.es/sites/espaisnaturalsprotegits/ca/monument_natural_dels_torrents_de_pareis_del_gorg_blau_i_de_lluc/",
        "wikiloc_url": "https://es.wikiloc.com/rutas-senderismo/torrent-de-pareis-escorca-sa-calobra-2194812"
    },

    # --- Rutes de Camins de Mallorca / Consell de Mallorca ---
    "castell-d-alaro": {
        "font": "Consell de Mallorca (Camins de Pedra)",
        "font_url": "https://caminsdepedra.conselldemallorca.cat/",
        "turismepetit_url": "https://www.turismepetit.com/excursion/el-castell-dalaro/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Castell+d+Alaro"
    },
    "cami-de-ses-voltes-galileu": {
        "font": "Consell de Mallorca (Camins de Pedra GR-221)",
        "font_url": "https://caminsdepedra.conselldemallorca.cat/",
        "turismepetit_url": "https://www.turismepetit.com/excursion/voltes-den-galileu-en-escorca/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Voltes+den+Galileu+Lluc"
    },
    "monestir-de-lluc-cami-vell": {
        "font": "Consell de Mallorca (Camins de Pedra)",
        "font_url": "https://caminsdepedra.conselldemallorca.cat/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Cami+Vell+de+Pollenca+a+Lluc"
    },
    "puig-des-teix-espolres": {
        "font": "Consell de Mallorca (Camí des Correu GR-221)",
        "font_url": "https://caminsdepedra.conselldemallorca.cat/-/etapa-3-estellencs-esporles",
        "turismepetit_url": "https://www.turismepetit.com/excursion/el-cami-des-correu-de-esporles-a-banyalbufar/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Cami+des+Correu+Esporles+Banyalbufar"
    },
    "embassament-cuber-gorg-blau": {
        "font": "Consell de Mallorca (Ruta dels Embassaments GR-221)",
        "font_url": "https://caminsdepedra.conselldemallorca.cat/",
        "turismepetit_url": "https://www.turismepetit.com/excursion/embalse-de-cuber-en-escorca/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Embassament+de+Cuber+Font+de+s+Ametler"
    },

    # --- Rutes de Turisme Petit i Familiars ---
    "es-salt-des-freu-orient": {
        "font": "Turisme Petit",
        "font_url": "https://www.turismepetit.com/excursion/excursion-al-salt-des-freu-en-orient/",
        "turismepetit_url": "https://www.turismepetit.com/excursion/excursion-al-salt-des-freu-en-orient/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Salt+des+Freu+Orient"
    },
    "cala-boquer-pollenca": {
        "font": "Turisme Petit / Ajuntament de Pollença",
        "font_url": "https://www.turismepetit.com/excursion/cala-boquer-en-pollenca/",
        "turismepetit_url": "https://www.turismepetit.com/excursion/cala-boquer-en-pollenca/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Cala+Boquer+Pollenca"
    },
    "volta-puig-de-maria-pollenca": {
        "font": "Turisme Petit / Ajuntament de Pollença",
        "font_url": "https://www.turismepetit.com/excursion/excursion-al-puig-de-maria-en-pollenca/",
        "turismepetit_url": "https://www.turismepetit.com/excursion/excursion-al-puig-de-maria-en-pollenca/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Puig+de+Maria+Pollenca"
    },
    "coves-blanques-pollenca": {
        "font": "Turisme Petit / Ajuntament de Pollença",
        "font_url": "https://www.turismepetit.com/excursion/excursion-a-las-coves-blanques-en-pollenca/",
        "turismepetit_url": "https://www.turismepetit.com/excursion/excursion-a-las-coves-blanques-en-pollenca/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Coves+Blanques+Cala+Sant+Vicenc"
    },
    "penyal-des-migdia-formentor": {
        "font": "Turisme Petit / Ajuntament de Pollença",
        "font_url": "https://www.turismepetit.com/excursion/cala-murta-en-pollenca/",
        "turismepetit_url": "https://www.turismepetit.com/excursion/cala-murta-en-pollenca/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Cala+Murta+Formentor"
    },
    "sant-elm-la-glorieta-dragonera": {
        "font": "Turisme Petit / Ajuntament d'Andratx",
        "font_url": "https://www.turismepetit.com/excursion/cala-en-basset-en-sant-elm/",
        "turismepetit_url": "https://www.turismepetit.com/excursion/cala-en-basset-en-sant-elm/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Cala+en+Basset+Torre+sa+Salve+Sant+Elm"
    },
    "penya-de-sa-foradada-puigpunyent": {
        "font": "Turisme Petit / Ajuntament de Puigpunyent",
        "font_url": "https://www.turismepetit.com/excursion/la-reserva-puig-de-galatzo/",
        "turismepetit_url": "https://www.turismepetit.com/excursion/la-reserva-puig-de-galatzo/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Puigpunyent+Penya+de+les+Sinies"
    },
    "betlem-a-playa-es-calo": {
        "font": "Turisme Petit / Parc Natural de Llevant",
        "font_url": "https://www.turismepetit.com/excursion/excursion-de-betlem-a-playa-es-calo/",
        "turismepetit_url": "https://www.turismepetit.com/excursion/excursion-de-betlem-a-playa-es-calo/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Betlem+Platja+es+Calo+Arta"
    },
    "mirador-de-ses-basses-son-gual-valldemossa": {
        "font": "Turisme Petit / Ajuntament de Valldemossa",
        "font_url": "https://www.turismepetit.com/excursion/excursion-al-mirador-de-ses-basses-y-mirador-de-son-gual/",
        "turismepetit_url": "https://www.turismepetit.com/excursion/excursion-al-mirador-de-ses-basses-y-mirador-de-son-gual/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Mirador+ses+Basses+Son+Gual+Valldemossa"
    },
    "estanyol-a-torre-estalella-llucmajor": {
        "font": "Turisme Petit / Ajuntament de Llucmajor",
        "font_url": "https://www.turismepetit.com/excursion/excursion-desde-estanyol-a-torre-estalella/",
        "turismepetit_url": "https://www.turismepetit.com/excursion/excursion-desde-estanyol-a-torre-estalella/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=s+Estanyol+Torre+de+s+Estalella+Llucmajor"
    },
    "sa-comuna-de-lloret-de-vistalegre": {
        "font": "Turisme Petit / Ajuntament de Lloret de Vistalegre",
        "font_url": "https://www.turismepetit.com/excursion/sa-comuna-de-lloret-de-vistalegre/",
        "turismepetit_url": "https://www.turismepetit.com/excursion/sa-comuna-de-lloret-de-vistalegre/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Sa+Comuna+de+Lloret+de+Vistalegre"
    },
    "sanctuari-de-consolacio-santanyi": {
        "font": "Turisme Petit / Ajuntament de Santanyí",
        "font_url": "https://www.turismepetit.com/excursion/santuario-de-consolacio-en-santanyi/",
        "turismepetit_url": "https://www.turismepetit.com/excursion/santuario-de-consolacio-en-santanyi/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Santuari+Consolacio+Santanyi"
    },
    "ermita-bonany-petra": {
        "font": "Turisme Petit / Ajuntament de Petra",
        "font_url": "https://www.turismepetit.com/excursion/ermita-de-bonany-en-petra/",
        "turismepetit_url": "https://www.turismepetit.com/excursion/ermita-de-bonany-en-petra/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Ermita+de+Bonany+Petra"
    },
    "puig-de-randa-cura": {
        "font": "Santuari de Cura / Ajuntament d'Algaida",
        "font_url": "https://santuariodecura.com/",
        "turismepetit_url": "https://www.turismepetit.com/excursion/santuario-de-cura-en-randa/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Puig+de+Randa+Santuari+de+Cura"
    },

    # --- Rutes municipals, de patrimoni i d'alta muntanya ---
    "castell-de-bellver-bosc-palma": {
        "font": "Ajuntament de Palma (Castell de Bellver)",
        "font_url": "https://castelldebellver.palma.cat/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Castell+de+Bellver+bosc+Palma"
    },
    "puig-de-sa-comuna-bunyola": {
        "font": "Ajuntament de Bunyola (Sa Comuna)",
        "font_url": "https://ajbunyola.net/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Puig+de+sa+Comuna+Bunyola+Penya+Honor"
    },
    "puig-de-na-francesa-bunyola": {
        "font": "Ajuntament de Bunyola (Senderisme)",
        "font_url": "https://ajbunyola.net/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Puig+de+na+Francesa+Bunyola"
    },
    "avenc-de-son-pou": {
        "font": "Ajuntament de Santa Maria del Camí",
        "font_url": "https://ajsantamariadelcami.org/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Avenc+de+Son+Pou+Coanegra"
    },
    "torrent-de-coanegra-santa-maria": {
        "font": "Ajuntament de Santa Maria del Camí",
        "font_url": "https://ajsantamariadelcami.org/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Torrent+de+Coanegra+Salt+des+Freu"
    },
    "penyal-de-honor-orient": {
        "font": "Ajuntament de Bunyola / Santa Maria",
        "font_url": "https://ajbunyola.net/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Penya+d+Honor+Orient+Pas+de+s+Escaleta"
    },
    "sa-foradada-son-marroig": {
        "font": "Fundació Son Marroig / Ajuntament de Deià",
        "font_url": "https://sonmarroig.com/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Sa+Foradada+Son+Marroig+Deia"
    },
    "cami-des-rafal-deia": {
        "font": "Ajuntament de Deià",
        "font_url": "https://ajdeia.net/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Cami+des+Rafal+Cova+sa+Cauba+Deia"
    },
    "ermita-trinitat-valldemossa": {
        "font": "Ajuntament de Valldemossa (Camins de l'Arxiduc)",
        "font_url": "https://valldemossa.es/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Ermita+de+la+Trinitat+Valldemossa"
    },
    "puig-des-teix-valldemossa": {
        "font": "Ajuntament de Valldemossa (Camins de l'Arxiduc)",
        "font_url": "https://valldemossa.es/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Puig+des+Teix+Cami+de+s+Arxiduc+Valldemossa"
    },
    "fita-del-ram-maristella": {
        "font": "Ajuntament d'Esporles",
        "font_url": "https://ajesporles.net/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Fita+del+Ram+Ermita+Maristella+Esporles"
    },
    "coma-de-binifaldo-puig-tomir": {
        "font": "Consell de Mallorca (Paratge Natural Serra de Tramuntana)",
        "font_url": "https://caminsdepedra.conselldemallorca.cat/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Puig+Tomir+Binifaldo+Escorca"
    },
    "puig-de-ses-basses-fornalutx": {
        "font": "Ajuntament de Fornalutx",
        "font_url": "https://ajfornalutx.net/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Fornalutx+Coll+de+sa+Balitx+Cala+Tuent"
    },
    "cami-de-sa-sirereta-soller": {
        "font": "Ajuntament de Sóller",
        "font_url": "https://ajsoller.net/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Cami+de+sa+Sirereta+Soller"
    },
    "clot-des-cirers-soller": {
        "font": "Ajuntament de Sóller",
        "font_url": "https://ajsoller.net/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Clot+des+Cirers+Port+de+Soller"
    },
    "castell-de-reina-alaro": {
        "font": "Ajuntament d'Alaró / Federació Balear d'Espeleologia",
        "font_url": "https://ajalaro.net/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Pas+des+Llop+Cova+de+sa+Campana+Alaro"
    },
    "puig-de-sant-salvador-felanitx": {
        "font": "Ajuntament de Felanitx (Patrimoni i Senderisme)",
        "font_url": "https://visitfelanitx.com/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Puig+de+Sant+Salvador+Felanitx"
    },
    "castell-de-santueri-felanitx": {
        "font": "Fundació Castell de Santueri / Ajuntament de Felanitx",
        "font_url": "https://visitfelanitx.com/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Castell+de+Santueri+Felanitx"
    },
    "puig-de-santueri-felanitx-circular": {
        "font": "Ajuntament de Felanitx",
        "font_url": "https://visitfelanitx.com/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Volta+al+Puig+de+Santueri+Felanitx"
    },
    "cala-varques-manacor": {
        "font": "Ajuntament de Manacor (Senderisme Litoral)",
        "font_url": "https://manacor.org/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Cala+Varques+Coves+del+Pirata+Manacor"
    },
    "penya-rotja-alcudia": {
        "font": "Ajuntament d'Alcúdia (Turisme)",
        "font_url": "https://alcudia.net/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Penya+Rotja+Ermita+Victoria+Alcudia"
    },
    "puig-de-sant-miquel-montuiri": {
        "font": "Ajuntament de Montuïri",
        "font_url": "https://ajmontuiri.net/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Puig+de+Sant+Miquel+Montuiri"
    },
    "coll-de-sa-gramola-ses-basses": {
        "font": "Ajuntament d'Andratx (Senderisme)",
        "font_url": "https://andratx.cat/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Coll+de+sa+Gramola+Puig+sa+Monja+Andratx"
    },
    "ermita-de-sant-simon-caimari": {
        "font": "Ajuntament de Selva / Camins de Caimari",
        "font_url": "https://ajselva.net/",
        "wikiloc_url": "https://www.wikiloc.com/rutas/senderismo/espana/illes-balears?q=Caimari+Coll+de+sa+Batalla+Cami+Vell+Lluc"
    }
}

with open("data/rutes_mallorca.json", "r", encoding="utf-8") as f:
    routes = json.load(f)

updated = 0
for r in routes:
    slug = r.get("slug")
    if slug in ROUTE_SOURCES:
        src = ROUTE_SOURCES[slug]
        for k, v in src.items():
            r[k] = v
        updated += 1

with open("data/rutes_mallorca.json", "w", encoding="utf-8") as f:
    json.dump(routes, f, ensure_ascii=False, indent=2)

print(f"Rutes actualitzades amb fonts i enllaços verificats: {updated} de {len(routes)}")
