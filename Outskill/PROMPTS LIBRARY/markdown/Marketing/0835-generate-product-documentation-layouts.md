---
id: "3b241426-eb50-8074-8c4b-c6fa87701bea"
title: "Generate Product Documentation Layouts"
category: "Marketing"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Generate Product Documentation Layouts

**Category:** Marketing

## Description

Generate professional product documentation layouts with this AI prompt, featuring multi-angle views, technical annotations, and high-end industrial design presentation styling.

## What This Prompt Does

● Creates a professional product documentation layout with multiple views of an uploaded item arranged in a technical presentation style
● Generates detailed annotations with thin lines pointing to visible components, each labeled with precise descriptions based only on what can be seen
● Produces an ultra-high resolution AI image that mimics industrial design documentation with studio lighting and neutral colors

## Prompt

```text
{
  "reference": {
    "type": "image",
    "usage": "Use the uploaded image as the sole source of truth. Do not assume product category in advance."
  },
  "scene": {
    "description": "[DESIGN AESTHETIC] product presentation layout inspired by high-end industrial design and product documentation.",
    "background": "[BACKGROUND SURFACE]"
  },
  "layout": {
    "top_left": {
      "content": "Brand name",
      "style": "Modern sans-serif typography, subtle, elegant"
    },
    "left_column": {
      "content": "Multiple auxiliary product views",
      "views": [
        "Primary front or main view",
        "Secondary side view",
        "Alternate angle or rear view",
        "Detail or top view if applicable"
      ],
      "arrangement": "Vertically stacked, evenly spaced, aligned"
    },
    "right_section": {
      "content": "Main hero product render",
      "style": "Large, dominant, photorealistic",
      "lighting": "Soft studio lighting",
      "materials": "Visually accurate to the uploaded product"
    }
  },
  "annotations": {
    "analysis_phase": [
      "Visually analyze the product to identify distinct physical components",
      "Determine visible materials, surfaces, interfaces, and structures",
      "Ignore assumed internal mechanisms or hidden features"
    ],
    "binding_rules": [
      "Each annotation line must point to one clearly visible component",
      "Each label must describe exactly what that component is and does, based only on visual evidence",
      "No label may rely on the product category for meaning",
      "One line equals one component equals one explanation"
    ],
    "line_style": {
      "type": "Hairline-thin vector lines",
      "color": "[LINE COLOR]",
      "termination": "Exact contact point on the referenced component"
    },
    "labels": {
      "content_rules": [
        "Use neutral, descriptive nouns joint",
        "Mention material only if visually identifiable",
        "Mention function only if structurally implied",
        "Avoid category-specific terminology unless clearly visible"
      ],
      "placement_rules": [
        "Place text outside the product silhouette",
        "Maintain consistent spacing",
        "Avoid overlaps",
        "Align labels for technical clarity"
      ],
      "tone": "Factual, precise, non-marketing",
      "typography": "Minimal technical sans-serif"
    }
  },
  "visual_style": {
    "aesthetic": "[DESIGN AESTHETIC]",
    "mood": "Calm, precise, professional",
    "color_palette": "Neutral and restrained"
  },
  "rendering": {
    "quality": "Ultra-high resolution",
    "shadows": "Soft and realistic",
    "accuracy": "Exact proportions and geometry fidelity"
  },
  "rules": {
    "do_not": [
      "Assume product category",
      "Hallucinate features",
      "Use generic marketing language",
      "Mismatch labels and components",
      "Decorate annotation lines"
    ],
    "focus_on": [
      "Visual truth",
      "Semantic correctness",
      "Component-level understanding",
      "Professional design documentation"
    ]
  }
}
```
