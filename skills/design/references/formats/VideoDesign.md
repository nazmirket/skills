# Video design

Use when the deliverable is an edited video: an explainer, demo recording, lesson, trailer, or social cut. Use [Motion Design](MotionDesign.md) when playback behavior, an animated asset, or a timed interaction is itself the result.

## Establish the edit

Identify the audience, intended takeaway, channel and viewing conditions. Agree on duration or target range, aspect ratios and crops, required audio or captions, and the editable or finished outputs. Record provenance and permitted use for footage, music, voices and other assets. Distinguish a real demonstration from an illustrative recreation.

Outline the beats around the audience's question or task. Choose one timeline for shots, voice, captions, titles and sound. When narration carries the explanation, time the scene to the spoken cue and leave room to read or see the action. For a product recording, use representative safe data and show the action and its effect; avoid using an edited cut as proof of runtime speed. Use [Video](../concepts/Video.md) for framing, pacing and sequencing choices.

## Review what will ship

Watch the actual export at normal speed and at the intended size. Verify key crops, titles, first and final frame, audio intelligibility, and the ending or loop if specified. For each required aspect ratio, check captions and key action against the real crop. Try muted viewing where expected and confirm the captions are accurate, timed, readable, and preserve important speech and sounds.

Open the export in the intended player or delivery environment. Return the named exports and, when requested, the editable timeline, captions or transcript, poster, and required media or fonts. State which variants, playback conditions and accessibility features were checked, and what could not be verified.

## Inspect the export at a timestamp

Use the final encoded file. Compare its decoded dimensions, duration and streams with the brief. Listen at a known speech or sound cue on the intended track. A listed audio stream can still contain silence. If FFmpeg is available, this command returns the container duration and the streams a player can select.

```sh
ffprobe -v error -show_entries format=duration:stream=index,codec_type,width,height,avg_frame_rate -of json final.mp4
```

For a long cut, skim a contact sheet to locate suspect sections. A missed transition may last a single frame. Step through consecutive full frames around its edit point. For example, this inspects a cut two seconds into a clip whose timeline starts at zero. Use a fresh scratch directory for the images and substitute the export's path.

```sh
ffmpeg -hide_banner -n -i final.mp4 -map 0:v:0 -vf "select='between(t,1.92,2.09)',showinfo" -fps_mode passthrough cut-%03d.png
```

Match the ordered PNGs to the filter's logged `pts_time` values. Choose a window that includes frames on both sides at the actual frame rate. A flash between shots should have an identifiable timestamp. For a suspected freeze, compare its start and end with the intended hold in the edit. For a loop, play across the seam several times and inspect the last and first full frames.

Record the export, time, expected beat and observation, such as “2.00 s, a white frame appears between the two product shots.” After a repair, inspect that interval in the new export and replay it at normal speed with the intended sound and captions.
