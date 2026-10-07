---
id: "3b241426-eb50-8056-aa87-de183f4d13df"
title: "Generate Museum Exhibit Product Grids"
category: "Marketing"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Generate Museum Exhibit Product Grids

**Category:** Marketing

## Description

Create museum-quality product exhibits with this AI prompt, featuring hero shots, technical cutaways, lifestyle photography, and professional infographic labels.

## What This Prompt Does

● Generates a three-panel AI image layout displaying a product in museum exhibition style with hero shot, technical cutaway, and lifestyle use.
● Creates photorealistic product photography with infographic callouts, material close-ups, and specification labels across a 16:9 grid.
● Produces premium museum-quality AI images featuring clean typography, studio lighting, and detailed component breakdowns for any product type.

## Prompt

```text
{
  "prompt_name": "Museum Exhibit Label - 3x1 Grid ([PRODUCT TYPE])",
  "version": "1.1",
  "canvas": {
    "aspect_ratio": "16:9",
    "resolution": "2048x1152",
    "grid": {
      "type": "3x1",
      "panel_count": 3,
      "panel_spacing": "2.5%",
      "outer_margin": "4%"
    }
  },
  "global_style": {
    "aesthetic": "premium museum exhibition photography + clean infographic",
    "background": "minimal gallery gray gradient, subtle wall texture, soft vignette",
    "lighting": "museum spotlight + soft studio fill, realistic shadows",
    "color_grade": "neutral-warm whites, accurate blacks, natural highlights",
    "branding_rules": "no real brand names, no logos, no recognizable trademarks; create a generic premium [PRODUCT TYPE] design"
  },
  "typography": {
    "font_style": "clean modern sans-serif",
    "hierarchy": "title bold, labels medium, details regular",
    "color": "white or near-white with subtle cool accent",
    "legibility_rules": "crisp readable text, no distorted letters, keep text minimal"
  },
  "product": {
    "category": "[PRODUCT TYPE]",
    "design": {
      "description": "[PRODUCT DESIGN: form factor, color, silhouette, and distinguishing shape language]",
      "materials": "[PRODUCT DESIGN: primary shell material, secondary surface treatments, accent materials, and tactile elements]",
      "finish_details": "micro-scratches only if realistic, clean reflections, no fingerprints"
    }
  },
  "panels": [
    {
      "panel_index": 1,
      "title": {
        "text": "EXHIBIT A — HERO PRODUCT",
        "placement": "top left of panel",
        "size": "small"
      },
      "scene": {
        "shot_type": "studio hero product photo",
        "camera": {
          "angle": "3/4 view",
          "focal_length_mm": 70,
          "depth_of_field": "medium"
        },
        "composition": {
          "subject_placement": "centered",
          "props": "minimal pedestal or matte plinth, museum-like"
        },
        "content": [
          "[PRODUCT TYPE] displayed in its primary presentation state (open, unfolded, or resting)",
          "one component optionally placed in front for scale and detail",
          "soft contact shadow, premium reflections"
        ]
      },
      "museum_plaque": {
        "enabled": true,
        "placement": "bottom of panel on pedestal front or floating label",
        "material": "brushed aluminum or matte acrylic",
        "text_content": {
          "title": "[EXHIBIT IDENTITY: product name and model designation]",
          "subtitle": "[EXHIBIT IDENTITY: object classification label]",
          "details": [
            "[EXHIBIT IDENTITY: date]",
            "[EXHIBIT IDENTITY: materials list]",
            "[EXHIBIT IDENTITY: weight or key dimension]",
            "[EXHIBIT IDENTITY: accession number]"
          ]
        }
      }
    },
    {
      "panel_index": 2,
      "title": {
        "text": "EXHIBIT B — MATERIALS & INTERIOR",
        "placement": "top left of panel",
        "size": "small"
      },
      "layout": {
        "type": "split-with-insets",
        "description": "main image with two small inset close-ups + a compact spec block"
      },
      "scene": {
        "shot_type": "technical museum display",
        "camera": {
          "angle": "slight top-down",
          "focal_length_mm": 85,
          "depth_of_field": "shallow on close-ups"
        },
        "content": [
          "main: [PRODUCT TYPE] shown in clean cross-section cutaway revealing internal components realistically, not toy-like",
          "inset_1: macro close-up of primary outer surface texture and seam detail",
          "inset_2: macro close-up of secondary material or interface detail"
        ]
      },
      "infographic": {
        "enabled": true,
        "callouts": {
          "style": "thin clean lines with round endpoints",
          "count": 4,
          "labels": [
            {
              "name": "[CALLOUT 1: core functional component name]",
              "subtitle": "[CALLOUT 1: one-line descriptor]",
              "anchor": "[CALLOUT 1: component location]"
            },
            {
              "name": "[CALLOUT 2: power or energy component name]",
              "subtitle": "[CALLOUT 2: one-line descriptor]",
              "anchor": "[CALLOUT 2: component location]"
            },
            {
              "name": "[CALLOUT 3: input/output component name]",
              "subtitle": "[CALLOUT 3: one-line descriptor]",
              "anchor": "[CALLOUT 3: component location]"
            },
            {
              "name": "[CALLOUT 4: comfort or ergonomic feature name]",
              "subtitle": "[CALLOUT 4: one-line descriptor]",
              "anchor": "[CALLOUT 4: component location]"
            }
          ]
        },
        "spec_block": {
          "placement": "lower right of panel",
          "style": "museum label card",
          "text": [
            "[SPEC 1: surface finish detail]",
            "[SPEC 2: mechanical or construction detail]",
            "[SPEC 3: fit or form factor detail]",
            "[SPEC 4: charging, connectivity, or interface detail]"
          ]
        }
      }
    },
    {
      "panel_index": 3,
      "title": {
        "text": "EXHIBIT C — IN USE",
        "placement": "top left of panel",
        "size": "small"
      },
      "scene": {
        "shot_type": "lifestyle portrait",
        "camera": {
          "angle": "3/4 face close portrait",
          "focal_length_mm": 85,
          "depth_of_field": "shallow — product + face sharp"
        },
        "subject": {
          "description": "[LIFESTYLE SUBJECT: appearance, expression, outfit style]",
          "pose": "[LIFESTYLE SUBJECT: interaction gesture with the product]",
          "environment": "clean modern museum-like interior or minimal studio lifestyle backdrop",
          "privacy": "no celebrity, no recognizable person"
        },
        "focus_rules": [
          "product must be clearly visible in use on/with the subject",
          "realistic skin texture, natural hair detail, authentic lighting"
        ]
      },
      "caption_label": {
        "enabled": true,
        "placement": "bottom of panel",
        "style": "small museum caption strip",
        "text": "[CAPTION: one-line museum-voice description of the product in everyday use]"
      }
    }
  ],
  "quality_rules": {
    "realism": "photorealistic materials, believable reflections and shadows",
    "consistency": "same product design across all three panels",
    "avoid": [
      "illegible or garbled text",
      "warped product geometry",
      "real brand logos or trademarked product names",
      "celebrity likeness",
      "overcrowded labels"
    ],
    "output": "crisp, premium, ad-grade"
  }
}
```
