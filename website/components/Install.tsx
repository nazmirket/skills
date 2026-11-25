"use client";

import { useState } from "react";
import Link from "next/link";

const methods = ["Agent prompt", "Manual commands"] as const;
type Host = {name: string; prompt: string; commands: string};
type Method = typeof methods[number];

function InstallSnippet({host, method, value}: {host: string; method: Method; value: string}) {
  const [status, setStatus] = useState<"idle" | "copied" | "error">("idle");
  const isPrompt = method === "Agent prompt";

  async function copy() {
    try {
      await navigator.clipboard.writeText(value);
      setStatus("copied");
    } catch {
      setStatus("error");
    }
  }

  return <div className="install-snippet">
    <p className="install-hint">{isPrompt ? "Paste into your agent to get started." : "Run these commands in your terminal."}</p>
    <pre className="terminal-code" tabIndex={0} aria-label={isPrompt ? `${host} setup prompt` : `${host} installation commands`}>{value}</pre>
    <div className="install-snippet-footer">
      <button className="copy-button" type="button" onClick={copy}>{status === "copied" ? "Copied ✓" : isPrompt ? "Copy prompt" : "Copy commands"}</button>
      <p className="install-feedback" role="status">{status === "copied" ? "Copied to clipboard." : status === "error" ? "Select the text above to copy it." : ""}</p>
    </div>
  </div>;
}

export default function Install({hosts}: {hosts: Host[]}) {
  const [hostIndex, setHostIndex] = useState(0);
  const [method, setMethod] = useState<Method>("Agent prompt");
  const host = hosts[hostIndex];

  return <section id="install" className="install-window" aria-labelledby="install-title">
    <div className="panel-bar install-bar">
      <h2 id="install-title"><span className="status-dot" aria-hidden="true"/> Install Mirket</h2>
      <span>SETUP</span>
    </div>
    <div className="install-content">
      <div className="install-options">
        <fieldset className="install-choice">
          <legend>Host</legend>
          <div className="install-options-group">
            {hosts.map(({name}, index) => <label key={name}>
              <input type="radio" name="mirket-install-host" checked={hostIndex === index} onChange={() => setHostIndex(index)}/>
              <span>{name}</span>
            </label>)}
          </div>
        </fieldset>
        <fieldset className="install-choice">
          <legend>Method</legend>
          <div className="install-options-group">
            {methods.map(name => <label key={name}>
              <input type="radio" name="mirket-install-method" checked={method === name} onChange={() => setMethod(name)}/>
              <span>{name}</span>
            </label>)}
          </div>
        </fieldset>
      </div>
      <InstallSnippet key={`${host.name}/${method}`} host={host.name} method={method} value={method === "Agent prompt" ? host.prompt : host.commands}/>
      <p className="install-note">Start a fresh session after installation. Review hooks if your host asks you to trust them.</p>
      <p className="install-note"><Link className="text-link" href="/docs/other-agents/">Install skills in other agents <span aria-hidden="true">→</span></Link></p>
    </div>
  </section>;
}
