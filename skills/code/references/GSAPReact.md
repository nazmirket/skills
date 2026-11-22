# GSAP in React

Use this example when a React project already uses GSAP, ScrollTrigger and `@gsap/react`. It exercises a bug that a first playback can hide. A component may work alone, then move its sibling or leave a scroll trigger or tween alive when the user leaves the page.

Render `RemountDemo` in a local client-side test route or story. Each track registers its own scroll trigger. A button starts a tween later, outside the hook's initial setup. The container ref scopes the selector to one track, and `contextSafe` associates that later tween with the same cleanup. React manages the button listener. For manually registered listeners, timers or observers, also remove or cancel the registration on teardown.

```jsx
import { useRef, useState } from "react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useGSAP } from "@gsap/react";

gsap.registerPlugin(ScrollTrigger, useGSAP);

function Track({ name }) {
  const root = useRef(null);
  const { contextSafe } = useGSAP(() => {
    ScrollTrigger.create({
      id: `demo-track-${name}`,
      trigger: root.current,
      toggleClass: "in-view",
    });
  }, { scope: root, dependencies: [name], revertOnUpdate: true });

  const move = contextSafe(() => {
    gsap.to(".marker", { x: 24, duration: 1, overwrite: "auto" });
  });

  return (
    <section ref={root} aria-label={name}>
      <button type="button" onClick={move}>Move {name}</button>
      <div className="marker" aria-hidden="true">●</div>
    </section>
  );
}

export function RemountDemo() {
  const [showLeft, setShowLeft] = useState(true);
  const [ids, setIds] = useState([]);

  function inspectTriggers() {
    const registered = ScrollTrigger.getAll().map(trigger => trigger.vars.id);
    setIds(registered.filter(id => id?.startsWith("demo-track-")).sort());
  }

  return (
    <>
      <button type="button" onClick={() => setShowLeft(shown => !shown)}>
        {showLeft ? "Remove left" : "Restore left"}
      </button>
      {showLeft && <Track name="left" />}
      <Track name="right" />
      <button type="button" onClick={inspectTriggers}>Inspect triggers</button>
      <output>{ids.join(", ")}</output>
    </>
  );
}
```

1. Inspect triggers with both tracks mounted. Expect one left and one right. Move left and check that only its marker moves.
2. Remove left during its tween and inspect again. Only the right trigger should remain. For an automated check, keep a reference to the departing marker and assert that `gsap.getTweensOf(oldMarker)` is empty immediately after unmount. Waiting for the tween to finish would hide a leak.
3. Restore left and inspect again. Expect one trigger per track, a fresh left marker at its initial position, and a working right button. Repeat with React development Strict Mode enabled to exercise its extra setup and cleanup cycle.
