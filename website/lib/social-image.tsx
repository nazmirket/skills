import {readFileSync} from "node:fs";
import {resolve} from "node:path";
import {ImageResponse} from "next/og";
import sharp from "sharp";
import {cardSize, discoverablePages} from "./discovery";

type Card = ReturnType<typeof discoverablePages>[number];
const font = (path: string) => readFileSync(resolve("node_modules/@fontsource", path));

function summaryLines(summary: string) {
  if (summary.length <= 36) return [summary];
  const middle = summary.length / 2;
  const spaces = [...summary.matchAll(/ /g)].map(match => match.index);
  const split = spaces.sort((a, b) => Math.abs(a - middle) - Math.abs(b - middle))[0];
  return split ? [summary.slice(0, split), summary.slice(split + 1)] : [summary];
}

export async function socialImage(page: Card) {
  const sprite = await sharp(resolve("public/mirket-sprite.png"))
    .resize(256, 256, {kernel: "nearest"})
    .png()
    .toBuffer();
  const titleSize = page.cardTitle === "Mirket" ? 80 : page.cardTitle.length > 12 ? 40 : 51;
  return new ImageResponse(
    <div style={{
      display: "flex", width: "100%", height: "100%", padding: "64px", background: "#100c10",
      color: "#fff2e9", fontFamily: "Plex", position: "relative",
    }}>
      <div style={{position: "absolute", top: 0, left: 0, right: 0, height: 8, background: "#b22222"}}/>
      <div style={{
        display: "flex", flexDirection: "column", width: "100%", background: "#191217",
        border: "2px solid #65343e", boxShadow: "8px 8px #34141d",
      }}>
        <div style={{
          display: "flex", alignItems: "center", justifyContent: "space-between",
          height: 72, padding: "0 28px", background: "#22171d", borderBottom: "2px solid #65343e",
          color: "#ff717d", fontSize: 21,
        }}>
          <div style={{display: "flex", alignItems: "center", gap: 14}}>
            <div style={{width: 12, height: 12, background: "#ff717d", boxShadow: "4px 4px #b22222"}}/>
            <span>MIRKET / {page.cardLabel}</span>
          </div>
          <span style={{color: "#c2aeb2"}}>SKILLS.MIRKET.DEV</span>
        </div>
        <div style={{display: "flex", alignItems: "center", flex: 1, padding: "24px 28px 28px", gap: 32}}>
          <div style={{
            display: "flex", flexDirection: "column", justifyContent: "center", flex: 1,
            gap: 30, minWidth: 0,
          }}>
            <div style={{fontFamily: "Pixel", fontSize: titleSize, lineHeight: 1.25}}>{page.cardTitle}</div>
            <div style={{display: "flex", flexDirection: "column", color: "#fff2e9", fontSize: 31, lineHeight: 1.3, borderLeft: "4px solid #b22222", paddingLeft: 16}}>
              {summaryLines(page.cardSummary).map(line => <span key={line}>{line}</span>)}
            </div>
          </div>
          <div style={{
            display: "flex", width: 288, height: 288, alignItems: "center", justifyContent: "center",
            flexShrink: 0, background: "#2a1820", border: "2px solid #65343e", boxShadow: "6px 6px #b22222",
          }}>
            {/* ImageResponse embeds the local source; a browser optimizer is not involved. */}
            {/* eslint-disable-next-line @next/next/no-img-element */}
            <img src={`data:image/png;base64,${sprite.toString("base64")}`} alt="" width={256} height={256}/>
          </div>
        </div>
      </div>
    </div>,
    {
      ...cardSize,
      fonts: [
        {name: "Pixel", data: font("press-start-2p/files/press-start-2p-latin-400-normal.woff")},
        {name: "Plex", data: font("ibm-plex-mono/files/ibm-plex-mono-latin-500-normal.woff")},
      ],
    },
  );
}
