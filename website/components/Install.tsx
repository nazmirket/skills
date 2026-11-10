"use client";

import { useState } from "react";
import Link from "next/link";

const plugin = "mirket@mirket";
const repository = "https://github.com/nazmirket/skills.git";

const hosts = {
  Codex: [
    `codex plugin marketplace add ${repository}`,
    `codex plugin add ${plugin}`,
  ],
  "Claude Code": [
    "claude plugin marketplace add nazmirket/skills",
    `claude plugin install ${plugin}`,
  ],
};

const methods = ["Agent prompt", "Manual commands"] as const;
type Host = keyof typeof hosts;
type Method = typeof methods[number];

function InstallSnippet({host, method, prompt}: {host: Host; method: Method; prompt: string}) {
  const [status, setStatus] = useState<"idle" | "copied" | "error">("idle");
  const isPrompt = method === "Agent prompt";
  const value = isPrompt ? prompt : hosts[host].join("\n");

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

export default function Install({prompts}: {prompts: Record<Host, string>}) {
  const [host, setHost] = useState<Host>("Codex");
  const [method, setMethod] = useState<Method>("Agent prompt");

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
            {(Object.keys(hosts) as Host[]).map(name => <label key={name}>
              <input type="radio" name="mirket-install-host" checked={host === name} onChange={() => setHost(name)}/>
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
      <InstallSnippet key={`${host}/${method}`} host={host} method={method} prompt={prompts[host]}/>
      <p className="install-note">Start a fresh session after installation. Review hooks if your host asks you to trust them.</p>
      <p className="install-note">Memory is optional. <Link href="/docs/#optional-local-hindsight">Local Hindsight setup →</Link></p>
    </div>
  </section>;
}
