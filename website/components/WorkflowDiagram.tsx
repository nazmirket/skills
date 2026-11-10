"use client";

import { Player, type PlayerRef } from "@remotion/player";
import { useCurrentFrame } from "remotion";
import { useEffect, useRef, useState } from "react";
import PixelIcon, { type PixelGlyph } from "./PixelIcon";

import workflows from "../data/workflows.json";

type Variant = keyof typeof workflows;
type CompositionProps = { variant: Variant; compact: boolean };

function Workflow({variant, compact}: CompositionProps) {
  const frame = useCurrentFrame();
  const active = Math.floor(frame / 45);
  return <ol className={`workflow-stages${compact ? " workflow-stages--compact" : ""}`}>
    {workflows[variant].stages.map(([label, detail, glyph], index) => <li key={label} className={`workflow-stage${index === active ? " is-current" : ""}`}>
      <div className="stage-marker"><PixelIcon glyph={glyph as PixelGlyph}/><span aria-hidden="true">0{index + 1}</span></div>
      <strong>{label}</strong>
      <span className="stage-detail">{detail}</span>
    </li>)}
  </ol>;
}

export default function WorkflowDiagram({variant = "loop"}: {variant?: Variant}) {
  const {title, figure} = workflows[variant];
  const [width, setWidth] = useState(320);
  const compact = width < 510;
  const [reducedMotion, setReducedMotion] = useState(true);
  const [playing, setPlaying] = useState(false);
  const player = useRef<PlayerRef>(null);
  const media = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const motion = window.matchMedia("(prefers-reduced-motion: reduce)");
    const updateMotion = () => {
      setReducedMotion(motion.matches);
      setPlaying(!motion.matches);
    };
    updateMotion();
    motion.addEventListener("change", updateMotion);
    return () => {
      motion.removeEventListener("change", updateMotion);
    };
  }, []);

  useEffect(() => {
    const element = media.current;
    if (!element) return;
    const observer = new ResizeObserver(([entry]) => setWidth(Math.max(1, Math.round(entry.contentRect.width))));
    observer.observe(element);
    return () => observer.disconnect();
  }, []);

  function toggle() {
    if (playing) player.current?.pause();
    else player.current?.play();
    setPlaying(!playing);
  }

  return <figure className="diagram-frame">
    <figcaption className="panel-bar diagram-title"><span><b>{figure}</b> / {title}</span><button className="motion-toggle" type="button" onClick={toggle} aria-label={`${playing ? "Pause" : "Play"} animation: ${title}`}>{playing ? "Ⅱ PAUSE" : "▶ PLAY"}</button></figcaption>
    <div className="diagram-media" ref={media}>
      <Player ref={player} key={String(reducedMotion)} component={Workflow} inputProps={{variant, compact}} durationInFrames={180} compositionWidth={width} compositionHeight={compact ? 202 : 116} fps={30} autoPlay={!reducedMotion} initiallyMuted numberOfSharedAudioTags={0} spaceKeyToPlayOrPause={false} loop style={{width:"100%", display:"block"}} />
    </div>
  </figure>;
}
