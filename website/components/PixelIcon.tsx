const shapes = {
  target: "M3 0h2v2h2v1h1v2H7v1H5v2H3V6H1V5H0V3h1V2h2zm0 3v2h2V3z",
  plan: "M1 0h6v8H1zM2 1v6h4V1zm1 1h2v1H3zm0 2h2v1H3z",
  design: "M3 0h2v1h1v1h1v1h1v2H7v1H6v1H5v1H3V7H2V6H1V5H0V3h1V2h1V1h1zm0 3v2h2V3z",
  bug: "M2 0h1v1h2V0h1v2h1v1h1v1H7v1h1v1H7v1H6v1H2V7H1V6H0V5h1V4H0V3h1V2h1zm1 3v1h2V3z",
  inspect: "M1 0h4v1h1v4H5v1h1v1h1v1H5V7H4V6H1V5H0V1h1zm0 2v2h1v1h2V4h1V2H4V1H2v1z",
  check: "M6 1h2v2H7v1H6v1H5v1H4v1H2V6H1V5H0V3h2v1h1v1h1V4h1V3h1z",
  signal: "M3 0h2v2h1v1h2v2H6v1H5v2H3V6H2V5H0V3h2V2h1z",
  clean: "M5 0h2v2H6v2H5v1h2v2H6v1H1V7H0V5h1V4h3V2h1z",
  prompt: "M0 1h2v1h1v1h1v2H3v1H2v1H0V5h1V4h1V3H1V2H0zm5 5h3v1H5z",
} as const;

export type PixelGlyph = keyof typeof shapes;

export default function PixelIcon({glyph}: {glyph: PixelGlyph}) {
  return <svg viewBox="0 0 8 8" aria-hidden="true" shapeRendering="crispEdges"><path d={shapes[glyph]} fill="currentColor" fillRule="evenodd"/></svg>;
}
