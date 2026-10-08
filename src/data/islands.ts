import type { IslandInfo, Island } from '../types';

export const ARCHIPELAGO_CENTER: [number, number] = [39.50, 3.00];
export const ARCHIPELAGO_ZOOM: number = 8;

export const ISLANDS: IslandInfo[] = [
  {
    id: 'Mallorca',
    nom: 'Mallorca',
    name: 'Mallorca',
    center: [39.6953, 2.95],
    zoom: 9,
    bounds: [
      [39.25, 2.30],
      [39.95, 3.50],
    ],
  },
  {
    id: 'Menorca',
    nom: 'Menorca',
    name: 'Menorca',
    center: [39.95, 4.10],
    zoom: 10,
    bounds: [
      [39.75, 3.75],
      [40.10, 4.35],
    ],
  },
  {
    id: 'Eivissa',
    nom: 'Eivissa',
    name: 'Eivissa',
    center: [38.98, 1.40],
    zoom: 10,
    bounds: [
      [38.80, 1.15],
      [39.15, 1.65],
    ],
  },
  {
    id: 'Formentera',
    nom: 'Formentera',
    name: 'Formentera',
    center: [38.70, 1.45],
    zoom: 11,
    bounds: [
      [38.60, 1.35],
      [38.80, 1.60],
    ],
  },
];

export function getIslands(): IslandInfo[] {
  return ISLANDS;
}

export function getIslandById(id: string): IslandInfo | undefined {
  if (!id) return undefined;
  const lower = id.toLowerCase().trim();
  return ISLANDS.find(
    (island) =>
      island.id.toLowerCase() === lower ||
      island.nom.toLowerCase() === lower ||
      island.name.toLowerCase() === lower
  );
}

export default ISLANDS;
