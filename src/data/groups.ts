import type { ScoutGroup, Island } from '../types';

import agrupamentsMallorcaRaw from '../../data/agrupaments_mallorca.json';
import agrupamentsMenorcaRaw from '../../data/agrupaments_menorca.json';
import agrupamentsPitiusesRaw from '../../data/agrupaments_pitiuses.json';

const mallorcaGroups: ScoutGroup[] = (agrupamentsMallorcaRaw as any[]).map((g) => ({
  ...g,
  illa: (g.illa || 'Mallorca') as Island,
}));

const menorcaGroups: ScoutGroup[] = (agrupamentsMenorcaRaw as any[]).map((g) => ({
  ...g,
  illa: (g.illa || 'Menorca') as Island,
}));

const pitiusesGroups: ScoutGroup[] = (agrupamentsPitiusesRaw as any[]).map((g) => ({
  ...g,
  illa: (g.illa || 'Eivissa') as Island,
}));

export const groups: ScoutGroup[] = [
  ...mallorcaGroups,
  ...menorcaGroups,
  ...pitiusesGroups,
];

export function getAllGroups(): ScoutGroup[] {
  return groups;
}

export function getGroupBySlug(slug: string): ScoutGroup | undefined {
  if (!slug) return undefined;
  return groups.find((g) => g.slug === slug);
}

export function getGroupsByIsland(island?: Island | string): ScoutGroup[] {
  if (!island || island.toLowerCase() === 'totes' || island.toLowerCase() === 'all') {
    return groups;
  }
  const lower = island.toLowerCase().trim();
  return groups.filter((g) => (g.illa || 'Mallorca').toLowerCase() === lower);
}

export default groups;
