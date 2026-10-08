/**
 * Type definitions for Escoltes de les Illes Balears portal.
 * Balearic archipelago expansion (Mallorca, Menorca, Eivissa, Formentera).
 */

export type Island = 'Mallorca' | 'Menorca' | 'Eivissa' | 'Formentera';

export interface Route {
  slug: string;
  nom: string;
  municipi: string;
  zona?: string;
  illa: Island;
  distancia_km: number;
  desnivell_positiu_m: number;
  dificultat: string;
  durada_estimada: string;
  apte_unitats: string[];
  punts_aigua?: string[];
  passos_finca_privada?: string[];
  punts_interes?: string[];
  consells_seguretat?: string;
  descripcio: string;
  lat: number;
  lon: number;
  track_coordinates?: [number, number][];
  itinerari_passos?: string[];
  font?: string;
  font_url?: string;
  wikiloc_url?: string;
  punt_origen?: string;
  punts_a_tenir_en_compte?: string[];
  turismepetit_url?: string;
}

export interface Campsite {
  slug: string;
  nom: string;
  categoria: string;
  municipi: string;
  illa: Island;
  titularitat: string;
  contacte: string;
  web: string;
  observacions: string;
  capacitat: number;
  serveis: string[];
  permis_antelacio: string;
  restriccio_foc: string;
  acces_emergencia: string;
  lat: number;
  lon: number;
  descripcio: string;
  punt_origen: string;
}

export interface ScoutGroup {
  slug: string;
  nom: string;
  associacio: string;
  municipi: string;
  illa: Island;
  zona?: string;
  ubicacio_detall: string;
  email: string;
  web: string;
  lat: number;
  lon: number;
  descripcio: string;
}

export interface TransportLine {
  codi: string;
  nom: string;
  corredor?: string;
  municipis_coberts: string[];
  parades_clau: string[];
  link_horaris: string;
  illa?: Island;
}

export interface TrainLine {
  codi: string;
  nom: string;
  operator: string;
  municipis_coberts: string[];
  estacions_clau: string[];
  rutes_connectades?: string[];
  agrupaments_connectats?: string[];
  link_horaris: string;
  illa?: Island;
}

export interface TransportData {
  linies_bus: TransportLine[];
  linies_tren?: TrainLine[];
}

export interface IslandInfo {
  id: Island;
  nom: string;
  name: string;
  center: [number, number];
  zoom: number;
  bounds: [[number, number], [number, number]];
}

export interface Experience {
  id?: string;
  ruta_slug: string;
  nom: string;
  email?: string;
  branca: string;
  agrupament: string;
  valoracio: number;
  comentari: string;
  data?: string;
  autoritzat?: boolean;
  authorized?: boolean;
}

export interface AemetMunicipi {
  municipi: string;
  slug: string;
  codi_aemet: string;
}
