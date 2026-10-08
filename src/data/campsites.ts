import type { Campsite, Island } from '../types';

import acampadaMallorcaRaw from '../../data/acampada_mallorca.json';
import acampadaMenorcaRaw from '../../data/acampada_menorca.json';
import acampadaPitiusesRaw from '../../data/acampada_pitiuses.json';

const mallorcaCampsites: Campsite[] = (acampadaMallorcaRaw as any[]).map((c) => ({
  ...c,
  illa: (c.illa || 'Mallorca') as Island,
}));

const menorcaCampsites: Campsite[] = (acampadaMenorcaRaw as any[]).map((c) => ({
  ...c,
  illa: (c.illa || 'Menorca') as Island,
}));

const pitiusesCampsites: Campsite[] = (acampadaPitiusesRaw as any[]).map((c) => ({
  ...c,
  illa: (c.illa || 'Eivissa') as Island,
}));

export const campsites: Campsite[] = [
  ...mallorcaCampsites,
  ...menorcaCampsites,
  ...pitiusesCampsites,
];

export function getAllCampsites(): Campsite[] {
  return campsites;
}

export function getCampsiteBySlug(slug: string): Campsite | undefined {
  if (!slug) return undefined;
  return campsites.find((c) => c.slug === slug);
}

export function getCampsitesByIsland(island?: Island | string): Campsite[] {
  if (!island || island.toLowerCase() === 'totes' || island.toLowerCase() === 'all') {
    return campsites;
  }
  const lower = island.toLowerCase().trim();
  return campsites.filter((c) => (c.illa || 'Mallorca').toLowerCase() === lower);
}

export default campsites;
