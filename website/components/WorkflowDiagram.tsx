"use client";

import { Player } from "@remotion/player";
import { useCurrentFrame } from "remotion";
import { useEffect, useRef, useState } from "react";
import PixelIcon, { type PixelGlyph } from "./PixelIcon";

import workflows from "../data/workflows.json";

type Variant = keyof typeof workflows;
type CompositionProps = { variant: Variant; compact: boolean };

function StageList({variant, active, layout}: {variant: Variant; active: number; layout: string}) {
  return <ol className={`workflow-stages ${layout}`}>
    {workflows[variant].stages.map(([label, detail, glyph], index) => <li key={label} className={`workflow-stage${index === active ? " is-current" : ""}`}>
      <div className="stage-marker"><PixelIcon glyph={glyph as PixelGlyph}/><span aria-hidden="true">0{index + 1}</span></div>
      <strong>{label}</strong>
      <span className="stage-detail">{detail}</span>
    </li>)}
  </ol>;
}

function Workflow({variant, compact}: CompositionProps) {
  const frame = useCurrentFrame();
  return <StageList variant={variant} active={Math.floor(frame / 45)} layout={compact ? "workflow-stages--compact" : ""}/>;
}

export default function WorkflowDiagram({variant = "loop"}: {variant?: Variant}) {
  const {title, figure} = workflows[variant];
  const [width, setWidth] = useState(0);
  const compact = width < 510;
  const [reducedMotion, setReducedMotion] = useState(true);
  const media = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const query = window.matchMedia("(prefers-reduced-motion: reduce)");
    const update = () => setReducedMotion(query.matches);
    update();
    query.addEventListener("change", update);
    return () => query.removeEventListener("change", update);
  }, []);

  useEffect(() => {
    const element = media.current;
    if (!element) return;
    const observer = new ResizeObserver(([entry]) => setWidth(Math.round(entry.contentRect.width)));
    observer.observe(element);
    return () => observer.disconnect();
  }, []);

  return <figure className="diagram-frame">
    <figcaption className="panel-bar diagram-title"><span><b>{figure}</b> / {title}</span></figcaption>
    <div className="diagram-media" ref={media}>
      {reducedMotion || !width
        ? <StageList variant={variant} active={0} layout="workflow-stages--static"/>
        : <Player component={Workflow} inputProps={{variant, compact}} durationInFrames={180} compositionWidth={width} compositionHeight={compact ? 202 : 116} fps={30} autoPlay initiallyMuted numberOfSharedAudioTags={0} controls={false} clickToPlay={false} allowFullscreen={false} spaceKeyToPlayOrPause={false} loop style={{width:"100%", display:"block"}}/>}
    </div>
  </figure>;
}
