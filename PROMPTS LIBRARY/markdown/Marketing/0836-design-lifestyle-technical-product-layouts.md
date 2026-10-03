---
id: "3b241426-eb50-80fa-998d-d6ed7c8aca65"
title: "Design Lifestyle Technical Product Layouts"
category: "Marketing"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Design Lifestyle Technical Product Layouts

**Category:** Marketing

## Description

Generate premium product catalog layouts with this AI prompt, featuring lifestyle photography, technical drawings, material swatches, and architectural specifications.

## What This Prompt Does

● Generates a vertical AI image combining lifestyle product photography with technical specification panels in a 3:4 layout.
● Creates editorial-style product presentation featuring natural lighting and architectural line drawings showing multiple product views.
● Produces a design catalog aesthetic with material swatches, minimal typography, and premium warm color grading while preserving the original product's exact form.

## Prompt

```text
{
  "reference_images": {
    "product_image": "UPLOADED_IMAGE",
    "usage_rule": "Use the uploaded image as the exact visual reference for the product's form, proportions, materials, and overall identity. Do not redesign or reinterpret the product."
  },
  "layout": {
    "canvas": {
      "orientation": "vertical",
      "aspect_ratio": "3:4",
      "background": "[CANVAS SURFACE]"
    },
    "structure": {
      "top_section": "lifestyle_hero",
      "bottom_section": "technical_specification"
    }
  },
  "top_section": {
    "type": "lifestyle_product_image",
    "composition": {
      "placement": "top_center",
      "scale": "dominant",
      "margin": "generous whitespace around product"
    },
    "environment": {
      "setting": "[INTERIOR ENVIRONMENT]",
      "lighting": {
        "type": "natural sunlight",
        "direction": "angled side light",
        "quality": "soft but high-contrast shadows"
      },
      "floor": "subtle ground surface consistent with [INTERIOR ENVIRONMENT]",
      "background": "wall texture consistent with [INTERIOR ENVIRONMENT]"
    },
    "rendering": {
      "style": "editorial lifestyle photography",
      "detail": "high realism",
      "color_grading": "warm, muted, premium"
    }
  },
  "bottom_section": {
    "type": "technical_specification_panel",
    "layout": {
      "grid": "modular",
      "alignment": "clean, architectural"
    },
    "technical_drawings": {
      "placement": "bottom_left_and_center",
      "style": "architectural line drawings",
      "views": [
        "front view",
        "side view",
        "three-quarter cutaway or profile view"
      ],
      "projection": "orthographic",
      "line_style": {
        "color": "[DRAWING LINE COLOR]",
        "weight": "fine technical lines"
      },
      "annotations": {
        "type": "measurement and construction callouts",
        "language": "neutral technical labels",
        "density": "minimal, editorial"
      }
    },
    "materials_panel": {
      "placement": "bottom_right",
      "content": {
        "type": "material_swatches",
        "count": "3-4 depending on product",
        "format": "square or rectangular samples"
      },
      "textures": {
        "source": "derived from the product materials",
        "examples": [
          "fabric",
          "leather",
          "metal",
          "wood",
          "plastic"
        ]
      },
      "labels": {
        "style": "small editorial captions",
        "tone": "technical but refined"
      }
    }
  },
  "typography": {
    "style": "minimal editorial",
    "usage": "subtle captions, no large headlines",
    "color": "soft black or dark brown"
  },
  "overall_style": {
    "mood": "design catalog / product design journal",
    "aesthetic": "architectural, premium, calm",
    "avoid": [
      "clutter",
      "bold colors",
      "heavy branding",
      "overly decorative graphics"
    ]
  },
  "constraints": {
    "do_not": [
      "change product design",
      "invent new materials",
      "add logos unless present in reference",
      "use perspective distortion in drawings"
    ]
  }
}
```
