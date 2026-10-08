import type { TransportData, TransportLine, TrainLine, Island } from '../types';

import transportMallorcaRaw from '../../data/transport_mallorca.json';
import transportMenorcaRaw from '../../data/transport_menorca.json';
import transportPitiusesRaw from '../../data/transport_pitiuses.json';

const mallorcaBusLines: TransportLine[] = (
  (transportMallorcaRaw as any).linies_bus || []
).map((b: any) => ({
  ...b,
  illa: (b.illa || 'Mallorca') as Island,
}));

const menorcaBusLines: TransportLine[] = (
  (transportMenorcaRaw as any).linies_bus || []
).map((b: any) => ({
  ...b,
  illa: (b.illa || 'Menorca') as Island,
}));

const pitiusesBusLines: TransportLine[] = (
  (transportPitiusesRaw as any).linies_bus || []
).map((b: any) => {
  const isFormentera =
    (b.codi && b.codi.toUpperCase().startsWith('FOR')) ||
    (Array.isArray(b.municipis_coberts) && b.municipis_coberts.includes('Formentera'));
  return {
    ...b,
    illa: (b.illa || (isFormentera ? 'Formentera' : 'Eivissa')) as Island,
  };
});

const mallorcaTrainLines: TrainLine[] = (
  (transportMallorcaRaw as any).linies_tren || []
).map((t: any) => ({
  ...t,
  illa: (t.illa || 'Mallorca') as Island,
}));

export const allBusLines: TransportLine[] = [
  ...mallorcaBusLines,
  ...menorcaBusLines,
  ...pitiusesBusLines,
];

export const transport: TransportData = {
  linies_bus: allBusLines,
  linies_tren: mallorcaTrainLines,
};

export function getAllBusLines(): TransportLine[] {
  return transport.linies_bus;
}

export function getBusLinesByIsland(island?: Island | string): TransportLine[] {
  if (!island || island.toLowerCase() === 'totes' || island.toLowerCase() === 'all') {
    return transport.linies_bus;
  }
  const lower = island.toLowerCase().trim();
  return transport.linies_bus.filter(
    (b) => (b.illa || 'Mallorca').toLowerCase() === lower
  );
}

export function getAllTrainLines(): TrainLine[] {
  return transport.linies_tren || [];
}

export function getAllTransport(): TransportData {
  return transport;
}

export default transport;
