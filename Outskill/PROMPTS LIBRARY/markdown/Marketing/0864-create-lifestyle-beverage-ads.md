---
id: "3b241426-eb50-805e-94f1-dddac5901157"
title: "Create Lifestyle Beverage Ads"
category: "Marketing"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Create Lifestyle Beverage Ads

**Category:** Marketing

## Description

Create stunning beverage advertisements with this AI prompt, featuring hero shots, macro details, lifestyle scenes, splash photography, and modern branding elements.

## What This Prompt Does

● Generates a 3×2 grid AI image showcasing a beverage product across six distinct panels with professional photography styles.

● Creates varied shots including hero bottle display, macro droplet details, lifestyle scenes, dynamic splash effects, and minimalist compositions.

● Produces a modern beverage advertisement AI image with fresh lighting, clean backgrounds, and customizable branding elements.

## Prompt

```text
{
  "Objective": "Create a visually striking 3×2 advertisement for [PRODUCT NAME] [BEVERAGE TYPE], presenting an everyday hydration product with a stylish, high-quality background and modern lifestyle aesthetic.",
  "Canvas": {
    "Aspect_Ratio": "4:5",
    "Grid_Structure": "3×2 equal panels",
    "Orientation": "Portrait",
    "Use_Case": [
      "Beverage marketing campaigns",
      "Fitness and lifestyle promotions",
      "Social media ads",
      "Retail display visuals"
    ]
  },
  "Product_Description": {
    "Category": "[BEVERAGE TYPE]",
    "Bottle_Type": "Clear recyclable plastic bottle",
    "Features": [
      "Crisp transparent label",
      "Condensation droplets for freshness effect",
      "Eco-friendly packaging",
      "Daily hydration essential"
    ]
  },
  "Background_Design": {
    "Environment": "Minimal modern setting with light concrete textures",
    "Surface": "Matte stone or light gray slab",
    "Accent_Elements": [
      "Soft blue gradient backdrop",
      "Subtle water splash elements",
      "Natural daylight beams"
    ],
    "Lighting": "Bright diffused daylight with crisp highlights",
    "Mood": ["Fresh", "Pure", "Clean"]
  },
  "Panels": [
    {
      "Panel_Number": 1,
      "Title": "Hero Bottle Shot",
      "Description": "Bottle centered upright with visible condensation droplets.",
      "Visual_Details": {
        "Camera_Angle": "Front-facing symmetrical composition",
        "Mood": ["Pure", "Refreshing"]
      }
    },
    {
      "Panel_Number": 2,
      "Title": "Cold Detail Close-Up",
      "Description": "Macro shot of water droplets on bottle surface.",
      "Visual_Details": {
        "Depth_of_Field": "Ultra-shallow with crisp droplet texture",
        "Mood": ["Cold", "Hydrating"]
      }
    },
    {
      "Panel_Number": 3,
      "Title": "Active Lifestyle Moment",
      "Description": "Adult holding bottle outdoors after light workout.",
      "Visual_Details": {
        "Lighting": "Bright natural daylight",
        "Mood": ["Energetic", "Healthy"]
      }
    },
    {
      "Panel_Number": 4,
      "Title": "Water Splash Scene",
      "Description": "Bottle surrounded by dynamic frozen water splash.",
      "Visual_Details": {
        "Lighting": "High-speed capture lighting",
        "Mood": ["Dynamic", "Crisp"]
      }
    },
    {
      "Panel_Number": 5,
      "Title": "Minimal Counter Display",
      "Description": "Bottle placed in clean kitchen environment.",
      "Visual_Details": {
        "Mood": ["Modern", "Daily essential"]
      }
    },
    {
      "Panel_Number": 6,
      "Title": "Signature Clean Finish",
      "Description": "Bottle silhouetted against soft blue gradient background.",
      "Visual_Details": {
        "Lighting": "Soft rim light",
        "Mood": ["Iconic", "Simple"]
      }
    }
  ],
  "Branding": {
    "Product_Name": "[PRODUCT NAME]",
    "Brand_Personality": "Clean, reliable, modern",
    "Color_Palette": [COLOR PALETTE],
    "Typography": "Clean modern sans-serif"
  },
  "Visual_Style": {
    "Style_Keywords": [
      "Modern beverage photography",
      "High realism",
      "Fresh daylight aesthetic",
      "Minimal composition",
      "Clean branding"
    ]
  },
  "Camera_And_Lighting": {
    "Photography_Type": "Professional product and lifestyle photography",
    "Shot_Types": [
      "Studio hero shot",
      "Macro droplet detail",
      "Lifestyle outdoor scene",
      "High-speed splash capture"
    ],
    "Lighting_Style": "Bright diffused daylight with controlled highlights",
    "Exposure": "Crisp and balanced",
    "Shadows": "Soft and clean"
  },
  "Mood_Keywords": [
    "Fresh",
    "Hydrating",
    "Clean",
    "Modern",
    "Healthy",
    "Crisp"
  ],
  "Negative_Prompt": [
    "Cloudy water",
    "Dirty bottle",
    "Crushed packaging",
    "Harsh flash lighting",
    "Overexposed highlights",
    "Cartoon style",
    "Low-resolution textures",
    "Watermarks",
    "Text overlays"
  ]
}
```

---

## VARIABLES GUIDE

| Variable | Description | Example Values | Dependency Notes |
|----------|-------------|----------------|------------------|
| **[PRODUCT NAME]** | Brand name used throughout the ad | `PUREDROP`, `GLACIALUX`, `HYDRAFLOW` | Appears in Objective and Branding block. Pure text swap, zero cascading risk. |
| **[BEVERAGE TYPE]** | The specific packaged beverage being advertised | `Bottled Drinking Water`, `Sparkling Water`, `Cold-Pressed Juice` | **Extreme coupling — rivals FRESHMORN bread as the deepest cascade in the series.** Changing the beverage type cascades into container design, liquid color, condensation behavior, splash physics, macro detail subject, lifestyle context, accent elements, AND background gradient. Transparent liquids compound the problem because the liquid's color is visible through the container. See full cascade guide, transparency coupling analysis, and liquid physics library below. |
| **[COLOR PALETTE]** | Array of 3 brand colors defining visual identity | `["Crystal Blue", "Pure White", "Light Gray"]`, `["Lime Green", "Frosted White", "Leaf Green"]`, `["Golden Amber", "Cream White", "Warm Brown"]` | Must be provided as a JSON array of 3 color strings. **Triple-layer coupling unique to transparent beverage photography.** Palette drives (1) background gradient tone visible through bottle, (2) liquid color consistency, and (3) accent element coloring. The primary accent color must match or complement the liquid's actual color, or the image reads as artificially colored. See palette-to-liquid mapping below. |

### Cascade Guide for [BEVERAGE TYPE]

**Layer 1: Product Description Cascade**

| Field Path | Original Value | What to Update | Coupling Severity |
|---|---|---|---|
| `Product_Description.Bottle_Type` | "Clear recyclable plastic bottle" | Match to actual container (glass bottle, aluminum can, carton, jar) | **Critical** — changes transparency behavior, reflection properties, and macro detail subject |
| `Product_Description.Features` | Water-specific array (transparent label, condensation, eco-packaging, daily essential) | Replace with beverage-relevant qualities | High |

**Layer 2: Scene Bible Cascade**

| Field Path | Original Value | What to Update | Coupling Severity |
|---|---|---|---|
| `Background_Design.Accent_Elements[0]` | "Soft blue gradient backdrop" | Update gradient color to match new liquid's color identity | **Critical** |
| `Background_Design.Accent_Elements[1]` | "Subtle water splash elements" | Replace with beverage-appropriate liquid dynamics (juice pour, foam, bubbles, condensation stream) | **Critical** |
| `Background_Design.Mood` | ["Fresh", "Pure", "Clean"] | Update if beverage shifts from purity to indulgence/energy/luxury positioning | Medium |

**Layer 3: Panel Array Cascade**

| Panel | Original Content | What to Update | Coupling Severity |
|---|---|---|---|
| **Panel 1: Hero Shot** | "Bottle centered upright with visible condensation droplets" | Update container noun; condensation only applies to cold beverages | High |
| **Panel 2: Macro Detail** | "Macro shot of water droplets on bottle surface" | Replace with beverage's signature surface detail (bubbles for sparkling, fruit pulp texture for juice, foam for kombucha) | **Critical** |
| **Panel 3: Lifestyle** | "Adult holding bottle outdoors after light workout" | Update activity context (workout → morning routine for juice, social setting for sparkling, yoga for wellness drink) | High |
| **Panel 4: Splash Scene** | "Bottle surrounded by dynamic frozen water splash" | Replace liquid dynamics with beverage-appropriate version (juice burst, carbonation explosion, tea pour) | **Critical** |
| **Panel 5: Counter Display** | "Bottle placed in clean kitchen environment" | Update if container form changes or kitchen context shifts | Low |
| **Panel 6: Silhouette Finish** | "Bottle silhouetted against soft blue gradient background" | Update gradient color to match new brand palette | Medium |

**Layer 4: Technical Updates**

| Field Path | Original Value | When to Update |
|---|---|---|
| `Camera_And_Lighting.Shot_Types[3]` | "High-speed splash capture" | Replace "splash" if beverage dynamics differ (pour, fizz, foam) |
| `Negative_Prompt[0]` | "Cloudy water" | Replace with beverage-specific quality failure ("flat carbonation," "separated juice," "murky tea") |
| `Negative_Prompt[1]` | "Dirty bottle" | Keep universally |
| `Negative_Prompt[2]` | "Crushed packaging" | Keep universally |

### Transparency Coupling Analysis (Unique to This Template)

This is the only prompt in the fourteen-prompt series where the product is transparent, creating an optical dependency between product and background that no previous prompt had to manage.

**How transparency changes everything:**

In opaque-product prompts (all previous entries), background and product are visually separate systems. You can change the background without affecting how the product looks, and vice versa. In this prompt, the clear bottle acts as a lens — the background gradient, surface tone, and accent elements are literally visible *through* the product.
```
OPAQUE PRODUCT (all previous prompts):
  [Background] ← visually behind → [Product]
  Independent systems. Change one without affecting the other.

TRANSPARENT PRODUCT (this prompt):
  [Background] ← visible through → [Product/Liquid] ← refracts → [Background]
  Fused optical system. Background color IS part of the product's visual identity.
```
