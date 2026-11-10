import {discoverablePages} from "../../../lib/discovery";
import {socialImage} from "../../../lib/social-image";

export const dynamic = "force-static";
export const dynamicParams = false;

export function generateStaticParams() {
  return discoverablePages().map(({image}) => ({image}));
}

export async function GET(_request: Request, {params}: {params: Promise<{image: string}>}) {
  const {image} = await params;
  const page = discoverablePages().find(item => item.image === image);
  return page ? socialImage(page) : new Response(null, {status: 404});
}
