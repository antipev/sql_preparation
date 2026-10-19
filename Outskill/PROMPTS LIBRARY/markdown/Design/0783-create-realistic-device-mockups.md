---
id: "3b241426-eb50-802f-bf8a-f9dd3eff9b21"
title: "Create Realistic Device Mockups"
category: "Design"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Create Realistic Device Mockups

**Category:** Design

## Description

Generate detailed device showcases with this AI prompt, featuring multiple perspectives, screen content integration, material breakdowns, and realistic product visualization.

## What This Prompt Does

● Creates a realistic AI image showcasing a device from multiple angles with integrated screen content.
● Displays three different perspectives of the device on the left while breaking down materials on the right.
● Generates a split-layout product visualization with detailed material swatches and technical annotations.

## Prompt

```text
{
  "objective": "Create a detailed visual showcase of the [DEVICE], integrating a [SCREEN CONTENT] into the device's display area",
  "image_specifications": {
    "style": "Realistic product showcase",
    "layout": "Split layout: Perspectives on the left, Material breakdown on the right",
    "aspect_ratio": "3:2",
    "background": "Minimal white or neutral background"
  },
  "left_side": {
    "section_title": "[DEVICE] Perspectives",
    "views": [
      {
        "view": "Top-down",
        "description": "Top view of the [DEVICE] showing the full interface and screen; [SCREEN CONTENT] is displayed inside the screen area"
      },
      {
        "view": "Front view",
        "description": "Frontal view with screen area showing the [SCREEN CONTENT] in the device's native display style"
      },
      {
        "view": "Side view",
        "description": "Profile showing ports, controls, and side thickness; no screen content required"
      }
    ],
    "screen_integration": {
      "source": "[SCREEN CONTENT] (era-appropriate version for the [DEVICE])",
      "placement": "Insert image within the device's screen area maintaining correct aspect ratio and perspective"
    },
    "visual_style": "Consistent lighting and rendering to match realistic hardware and authentic screen display"
  },
  "right_side": {
    "section_title": "Material & Surface Breakdown",
    "content": [
      {
        "material": "Casing",
        "material_type": "[MATERIAL PALETTE: primary body material and color]",
        "swatch_image": "Close-up of casing grain and texture",
        "label_style": "Thin annotation line pointing to body shell"
      },
      {
        "material": "Buttons/Controls",
        "material_type": "[MATERIAL PALETTE: control surface material and color]",
        "swatch_image": "Button/control texture and color samples",
        "label_style": "Color-coded with control callouts"
      },
      {
        "material": "Screen cover",
        "material_type": "[MATERIAL PALETTE: screen cover material and finish]",
        "swatch_image": "Screen cover material sample with appropriate tint",
        "label_style": "Pointer to screen area"
      }
    ]
  },
  "visual_elements": {
    "separation": "Vertical divider between left and right sections",
    "consistency": "Matching shadows, fonts, and labeling across views",
    "gameplay_overlay": "Display style matching original [DEVICE] screen characteristics"
  },
  "output_format": {
    "type": "Image",
    "high_resolution": true,
    "use_case": ["Retro tech showcase", "Product design portfolio", "Hardware history infographic"]
  }
}
```
