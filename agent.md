# Instruccions per a l'Agent d'IA - Projecte Escoltes Mallorca

Aquest document descriu el comportament, el coneixement del domini i les instruccions per als assistents de programació d'IA (com Antigravity) que treballin en el Portal de Suport del Grup Escolta.

## Context del Projecte
- **Organització**: Equip de Suport del Grup Escolta a Mallorca (Illes Balears, Espanya).
- **Públic Objectiu**: Caps (responsables) escoltes, equip de suport, famílies i escoltes.
- **Idioma**: Els documents i els comentaris del codi es poden redactar en anglès, castellà o català (Català/Mallorquí), reflectint el caràcter multilingüe de Mallorca. Es prioritzarà el català per a la comunicació general i la documentació local del projecte.
- **Àrees de Focus Clau**: Seguretat en excursions i senderisme, planificació de rutes a la Serra de Tramuntana, logística de material, comunicació amb les famílies i organització administrativa.

## Directrius i Persona de l'Agent

1. **Priorització de la Seguretat**:
   - Sempre que se suggereixin rutes d'excursions o activitats, cal incloure advertències de seguretat, plantilles de llistes de comprovació i referències a contactes d'emergència (p. ex., servei d'emergències 112 a Espanya, IBANAT per a prevenció d'incendis forestals i avisos de l'AEMET).
2. **Context Local i Idioma**:
   - Cal tenir molt present la geografia específica de Mallorca (Serra de Tramuntana, Torrent de Pareis, Lluc, Puig Major, etc.).
   - Donar suport a cadenes de text multilingües si es creen elements d'interfície d'usuari (anglès, castellà, català).
3. **Codi Lleuger i Fàcil de Mantenir**:
   - Atès que l'equip de suport està format per voluntaris, cal dissenyar eines senzilles, robustes i fàcils de mantenir.
   - Evitar arquitectures de núvol excessivament complexes a menys que es demani explícitament. Es prefereixen pàgines estàtiques o eines web locals senzilles.

## Regles de la Pila Tecnològica
- **Frontend**: HTML/JS pur, CSS modern i net (amb dissenys adaptatius per a ús mòbil durant les excursions).
- **Icones i Gràfics**: Utilitzar icones SVG netes o recursos generats directament.
- **Emmagatzematge de Dades**: Fitxers JSON senzills, emmagatzematge local (localStorage) o bases de dades lleugeres per facilitar les còpies de seguretat i la importació/exportació.
