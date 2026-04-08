# Prompt Templates

## Canonical style blend prompt

```text
{subject}, in the {style_title} aesthetic ({era}), {summary}.
Visual cues: {visual_cues}.
Materials + architecture: {materials}; {architecture}.
Palette emphasis: {color_palette}.
Render style: highly detailed concept art, cinematic composition.
Avoid: {negative_tokens}.
```

## Multi-style interpolation prompt

```text
A fusion of {style_a_title} and {style_b_title}: {subject}.
Take 60% visual language from {style_a_prompt_tokens} and 40% from {style_b_prompt_tokens}.
Preserve historical materials and believable industrial design.
```
