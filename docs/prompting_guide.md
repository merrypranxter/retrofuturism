# Prompt Construction and Usage Notes

## Prompt scaffold (single style)

```text
{subject} in {style_title} ({era}).
Visual cues: {visual_cues}.
Shape language: {shape_language}.
Pattern + symbol system: {pattern_systems}; {symbol_systems}.
Materials and surfaces: {materials}.
Composition: {composition_rules}.
Lighting: {lighting_atmosphere}.
Include: {common_subjects}.
Avoid: {negative_tokens}.
```

## Prompt scaffold (hybrid style)

```text
{subject}. Hybrid style: 70% {style_A} + 30% {style_B}.
Base structure, materials, and composition from {style_A}.
Accent motifs and typography from {style_B} only.
Keep historical plausibility and avoid visual contradictions.
```

## Reliability checklist before rendering

- Are all motif families from the same era cluster?
- Are materials plausible for that style period?
- Do symbols match the social context (state, consumer, ritual, industrial)?
- Is composition template aligned with style intent?
- Are negative tokens filtering out adjacent-style leakage?

## Common failure modes

- "Sci-fi soup": too many style families in one scene.
- "Anachronistic UI": modern flat touch UI inside analog settings.
- "Texture flattening": overusing one grunge/noise layer across all styles.
- "Unrooted symbolism": adding symbols with no cultural or narrative function.
