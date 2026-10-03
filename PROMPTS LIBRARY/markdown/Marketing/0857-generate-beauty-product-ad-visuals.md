---
id: "3b241426-eb50-80f3-abc5-c8c91d37899b"
title: "Generate Beauty Product Ad Visuals"
category: "Marketing"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Generate Beauty Product Ad Visuals

**Category:** Marketing

## Description

Create luxury fashion product photography with this AI prompt, featuring brand items, editorial styling, photorealistic models, and professional studio lighting composition.

## What This Prompt Does

● Generates a luxury fashion AI image featuring a female model wearing a red lace bra and blazer with branded products placed naturally in the bra cups.

● Creates photorealistic editorial-style product photography that matches exact brand reference images while maintaining proper physics and placement.

● Produces high-end commercial AI images with soft studio lighting, shallow depth of field, and brand-safe composition suitable for marketing campaigns.

## Prompt

```text
{
  "task": "luxury_editorial_fashion_product_photography_with_references",
  "references": {
    "products": [
      "USE_ATTACHED_[BRAND]_PRODUCT_REFERENCE_IMAGES_ONLY"
    ]
  },
  "output": {
    "type": "single_image",
    "aspect_ratio": "3:4",
    "resolution": "ultra_high_resolution",
    "quality": "high_end_editorial",
    "realism": "photorealistic",
    "nsfw_safety": "fully_clothed_no_nudity"
  },
  "subject": {
    "model": {
      "gender": "female",
      "age": "adult",
      "ethnicity": "ambiguous, non-celebrity",
      "facial_structure": {
        "jaw": "soft oval jawline",
        "cheekbones": "moderate, natural definition",
        "nose": "straight, slightly rounded tip",
        "lips": "natural fullness, understated volume",
        "eyes": "almond-shaped, neutral spacing"
      },
      "identity_guidance": "unique, non-famous face, does not resemble any known public figure",
      "hair": {
        "color": "[HAIR COLOR]",
        "style": "[HAIR STYLE]",
        "part": "subtle off-center part"
      },
      "expression": "[MODEL EXPRESSION]",
      "skin": "natural texture, realistic pores, no over-smoothing"
    },
    "wardrobe": {
      "bra": {
        "type": "lace bra",
        "color": "deep red",
        "coverage": "full coverage, opaque lace, no nipples visible",
        "structure": "supportive cups with realistic fabric tension"
      },
      "outer_layer": {
        "type": "tailored dark blazer",
        "fit": "structured shoulders, relaxed open front"
      }
    }
  },
  "products": [
    {
      "brand": "[BRAND]",
      "name": "[PRODUCT 1 NAME]",
      "reference_instruction": "match exact shape, size, color, and logo from reference image",
      "placement": {
        "position": "left bra cup",
        "physics": "resting naturally inside the cup with slight fabric compression",
        "visibility": "logo clearly visible"
      }
    },
    {
      "brand": "[BRAND]",
      "name": "[PRODUCT 2 NAME]",
      "reference_instruction": "use reference image for exact proportions",
      "placement": {
        "position": "center",
        "physics": "vertically supported by the bra cup, no floating",
        "visibility": "brand name readable"
      }
    },
    {
      "brand": "[BRAND]",
      "name": "[PRODUCT 3 NAME]",
      "reference_instruction": "replicate packaging precisely from reference",
      "placement": {
        "position": "right of center",
        "physics": "leaning gently against adjacent product, realistic contact shadows",
        "visibility": "cap and logo visible"
      }
    },
    {
      "brand": "[BRAND]",
      "name": "[PRODUCT 4 NAME]",
      "reference_instruction": "exact match to reference image",
      "placement": {
        "position": "right bra cup",
        "physics": "securely seated, no clipping, no distortion",
        "visibility": "clean, premium presentation"
      }
    }
  ],
  "composition": {
    "crop": "collarbone to mid-torso",
    "framing": "tight editorial crop, product-first composition",
    "balance": "clean symmetry with slight organic variation",
    "background": "soft neutral studio backdrop"
  },
  "lighting": {
    "style": "soft directional studio lighting",
    "key_light": "angled to sculpt collarbones and fabric texture",
    "fill_light": "subtle, preserving natural shadows",
    "product_highlights": "controlled reflections, no glare"
  },
  "color_grading": {
    "palette": "[COLOR PALETTE]",
    "contrast": "medium",
    "saturation": "refined, realistic"
  },
  "camera": {
    "lens": "85mm portrait lens",
    "aperture": "f/2.8",
    "depth_of_field": "shallow with sharp product focus",
    "perspective": "true-to-life proportions, no distortion"
  },
  "style_feel": [
    "modern [BRAND] campaign",
    "confident femininity",
    "editorial minimalism",
    "sensual but brand-safe",
    "non-celebrity model energy"
  ],
  "negative_prompts": [
    "celebrity resemblance",
    "public figure likeness",
    "extra products",
    "floating objects",
    "incorrect physics",
    "nudity",
    "nipples",
    "explicit sexual content",
    "over-smoothed skin",
    "logo distortion"
  ]
}
```
