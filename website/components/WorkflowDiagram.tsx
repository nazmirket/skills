import Link from "next/link";
import PixelIcon from "./PixelIcon";
import workflows from "../data/workflows.json";

const {routing, example} = workflows;

function DiagramCaption({figure, label, title}: {figure: string; label: string; title: string}) {
  return <figcaption className="diagram-caption">
    <span className="diagram-label">{figure} / {label}</span>
    <h3>{title}</h3>
  </figcaption>;
}

function RoutingDiagram() {
  return <figure className="diagram-frame">
    <DiagramCaption {...routing}/>
    <div className="routing-flow">
      <div className="route-node route-node--primary">
        <strong>{routing.start.label}</strong>
        <p>{routing.start.detail}</p>
      </div>
      <div className="route-options">
        <p className="diagram-label route-cue">{routing.branchCue}</p>
        <div className="route-branches">
          {routing.branches.map(({label, detail}) => <div className="route-node" key={label}>
            <strong>{label}</strong>
            <p>{detail}</p>
          </div>)}
        </div>
      </div>
      <div className="route-node route-node--result">
        <strong>{routing.finish.label}</strong>
        <p>{routing.finish.detail}</p>
      </div>
    </div>
  </figure>;
}

function ExampleDiagram() {
  return <figure className="diagram-frame">
    <DiagramCaption {...example}/>
    <div className="example-trace">
      <div className="trace-prompt">
        <span className="diagram-label">YOU ASK</span>
        <p>{example.prompt}</p>
      </div>
      <ol className="trace-steps">
        {example.steps.map(({skill, label, role, detail}) => <li key={skill}>
          <Link className="trace-skill" href={`/docs/skills/${skill}/`}>
            <span className="trace-glyph"><PixelIcon glyph={skill}/></span>
            {label}
          </Link>
          <span className="diagram-label">{role}</span>
          <p>{detail}</p>
        </li>)}
      </ol>
      <div className="trace-result">
        <span className="diagram-label">WHAT YOU GET BACK</span>
        <p>{example.report}</p>
      </div>
    </div>
  </figure>;
}

export default function WorkflowDiagrams() {
  return <div className="diagram-grid">
    <RoutingDiagram/>
    <ExampleDiagram/>
  </div>;
}
