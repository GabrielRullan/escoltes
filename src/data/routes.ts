import type { Route, Island } from '../types';

import rutesMallorcaRaw from '../../data/rutes_mallorca.json';
import rutesMenorcaRaw from '../../data/rutes_menorca.json';
import rutesEivissaRaw from '../../data/rutes_eivissa.json';
import rutesFormenteraRaw from '../../data/rutes_formentera.json';

const mallorcaRoutes: Route[] = (rutesMallorcaRaw as any[]).map((r) => ({
  ...r,
  illa: (r.illa || 'Mallorca') as Island,
}));

const menorcaRoutes: Route[] = (rutesMenorcaRaw as any[]).map((r) => ({
  ...r,
  illa: (r.illa || 'Menorca') as Island,
}));

const eivissaRoutes: Route[] = (rutesEivissaRaw as any[]).map((r) => ({
  ...r,
  illa: (r.illa || 'Eivissa') as Island,
}));

const formenteraRoutes: Route[] = (rutesFormenteraRaw as any[]).map((r) => ({
  ...r,
  illa: (r.illa || 'Formentera') as Island,
}));

export const routes: Route[] = [
  ...mallorcaRoutes,
  ...menorcaRoutes,
  ...eivissaRoutes,
  ...formenteraRoutes,
];

export function getAllRoutes(): Route[] {
  return routes;
}

export function getRouteBySlug(slug: string): Route | undefined {
  if (!slug) return undefined;
  return routes.find((r) => r.slug === slug);
}

export function getRoutesByIsland(island?: Island | string): Route[] {
  if (!island || island.toLowerCase() === 'totes' || island.toLowerCase() === 'all') {
    return routes;
  }
  const lower = island.toLowerCase().trim();
  return routes.filter((r) => (r.illa || 'Mallorca').toLowerCase() === lower);
}

export default routes;
