import Image from "next/image";

export default function Mascot() {
  return <span className="mascot" aria-hidden="true">
    <Image className="mascot-sprite" src="/mirket-sprite.png" alt="" width={64} height={64} loading="eager"/>
    <svg className="mascot-overlay" viewBox="0 0 64 64" shapeRendering="crispEdges">
        {/* These pixels cover only the near eye in the 64×64 sprite. */}
        <g className="mascot-wink">
          <path fill="#331912" d="M26 15h5v5h-9v-3h2v-1h2z"/>
          <path fill="#b88c65" d="M23 17h2v1h3v-1h2v1h-2v1h-3v-1h-2z"/>
          <path fill="#150805" d="M23 18h2v1h3v-1h2v1h-2v1h-3v-1h-2z"/>
        </g>
        <path className="mascot-spark" fill="currentColor" d="M12 7h1v2h2v1h-2v2h-1v-2h-2V9h2z"/>
    </svg>
  </span>;
}
