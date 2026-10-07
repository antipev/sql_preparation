---
id: "3b241426-eb50-8039-8cfb-e5d4f43473ff"
title: "Create Lifestyle Tech Advertisement Layouts"
category: "Marketing"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Create Lifestyle Tech Advertisement Layouts

**Category:** Marketing

## Description

Create natural lifestyle tech advertisements with this AI prompt, featuring hero images, product details, interaction shots, and authentic daylight photography.

## What This Prompt Does

● Generates a natural lifestyle AI image advertisement with a 3:4 portrait layout featuring a tech product in authentic home settings.

● Creates one large hero image showing a person using the product in soft daylight, plus four smaller grid panels displaying product details and lifestyle moments.

● Produces realistic AI images that avoid commercial studio lighting and gaming clichés, focusing instead on cozy and relaxed everyday product usage.

## Prompt

```text
{
  "Objective": "Create a natural lifestyle advertisement for the [PRODUCT NAME] [TECH PRODUCT]. The layout uses a 3:4 composition with a large hero image on top and a 2×2 grid below. The style should feel authentic and relaxed, using natural daylight rather than commercial studio lighting.",
  
  "Canvas": {
    "Aspect_Ratio": "3:4",
    "Orientation": "Portrait",
    "Layout_Structure": {
      "Top_Half": "Large hero image",
      "Bottom_Half": "2×2 equal grid"
    },
    "Use_Case": [
      "Gaming lifestyle post",
      "Social media campaign",
      "Tech lifestyle advertisement"
    ]
  },
  "Typography": {
    "Brand_Name": {
      "Text": "[PRODUCT NAME]",
      "Placement": "Top center",
      "Style": "Minimal modern sans-serif",
      "Color": "Neutral black or soft gray"
    },
    "Tagline": {
      "Text": "Play Naturally.",
      "Placement": "Below brand name",
      "Style": "Thin clean sans-serif"
    }
  },
  "Top_Hero_Section": {
    "Subject": "Person relaxing on a couch holding the game controller",
    "Environment": "Cozy living room with large window",
    "Lighting": "Soft natural daylight coming from the side window",
    "Mood": ["Relaxed", "Casual", "Authentic"],
    "Focus": "Gamepad in hands with natural grip",
    "Camera_Angle": "Over-the-shoulder or slightly elevated angle",
    "Background": "Soft blurred living room interior"
  },
  "Bottom_Grid_Panels": [
    {
      "Panel_Number": 1,
      "Title": "Controller Texture Detail",
      "Description": "Macro close-up of joystick and buttons.",
      "Focus": "Material texture and design"
    },
    {
      "Panel_Number": 2,
      "Title": "Hand Interaction",
      "Description": "Natural shot of hands pressing buttons during gameplay.",
      "Focus": "Real usage and comfort"
    },
    {
      "Panel_Number": 3,
      "Title": "Living Room Scene",
      "Description": "Controller resting on a wooden coffee table beside a console.",
      "Focus": "Natural lifestyle setting"
    },
    {
      "Panel_Number": 4,
      "Title": "Relaxed Gaming Moment",
      "Description": "Player sitting comfortably with sunlight entering the room.",
      "Focus": "Casual gaming environment"
    }
  ],
  "Visual_Style": {
    "Style_Keywords": [
      "Natural lifestyle photography",
      "Authentic gaming moment",
      "Soft daylight",
      "Minimal composition",
      "High realism"
    ]
  },
  "Camera_And_Lighting": {
    "Photography_Type": "Lifestyle tech photography",
    "Lighting_Style": "Natural window daylight",
    "Exposure": "Soft and balanced",
    "Shadows": "Gentle natural shadows"
  },
  "Mood_Keywords": [
    "Relaxed",
    "Authentic",
    "Cozy",
    "Natural",
    "Modern"
  ],
  "Negative_Prompt": [
    "RGB gamer lighting",
    "Overly commercial studio lighting",
    "Neon gaming setup",
    "Excessive branding",
    "Cartoon style",
    "Low-resolution textures",
    "Watermarks",
    "Text artifacts"
  ]
}
```

---

## VARIABLES GUIDE

| Variable | Description | Example Values | Dependency Notes |
|----------|-------------|----------------|------------------|
| **[PRODUCT NAME]** | Tech product brand name | `NEXPLAY`, `CALMCAST`, `HOMELINK` | Appears in Objective and Typography.Brand_Name.Text. Also requires updating Typography.Tagline.Text to match the product's brand voice. "Play Naturally" is gaming-specific — other tech products need different taglines. Low cascade otherwise. |
| **[TECH PRODUCT]** | The specific consumer tech product being advertised in a lifestyle context | `Wireless Game Controller`, `Wireless Headphones`, `Smart Speaker` | **Extreme coupling — cascades through every section of the template because the product defines every human interaction.** The hero section's subject action changes (holding controller → wearing headphones → speaking to speaker). All four grid panels change (macro detail subject, hand interaction type, resting-on-table companion object, usage posture). The anti-convention negative prompts change (RGB gamer lighting is gaming-specific). See full cascade guide, product-interaction architecture, and anti-convention mapping below. |
| **[COLOR PALETTE]** | Array of 3 implied environment tones (this template has no explicit palette — adding one creates optional environmental color control) | `["Warm Wood", "Soft White", "Natural Green"]`, `["Cool Grey", "Warm Cream", "Soft Charcoal"]`, `["Warm Beige", "Muted Olive", "Soft Linen"]` | **Optional variable.** The original prompt has no Color_Palette — environment tones are implied through natural daylight + wooden coffee table + cozy living room. Adding an explicit palette via a new `Fashion_Aesthetic.Color_Palette` or `Environment_Palette` field would give color control without changing the organic feel. Palette must feel domestic and natural — saturated or commercial colors break the "authentic" positioning. |

### Cascade Guide for [TECH PRODUCT]

This cascade is unique in the series because there's no Product_Description block to update. Instead, the product's identity is entirely encoded in HOW it appears across scenes. Changing the product means changing every scene description.

**Layer 1: Hero Section Cascade**

| Field Path | Original Value | What to Update | Coupling Severity |
|---|---|---|---|
| `Top_Hero_Section.Subject` | "Person relaxing on a couch holding the game controller" | Replace interaction verb and body position. Different products create different postures. See product-posture mapping below. | **Critical** |
| `Top_Hero_Section.Focus` | "Gamepad in hands with natural grip" | Replace with product-specific visual focus — what part of the product is most visible in use? | **Critical** |
| `Top_Hero_Section.Camera_Angle` | "Over-the-shoulder or slightly elevated angle" | Update if product's visibility changes with angle. Controllers are best seen from slightly above (looking down at hands). Headphones are best seen from the side (profile showing ear cup). Speakers are best seen at eye-level. | High |
| `Top_Hero_Section.Environment` | "Cozy living room with large window" | Usually transfers for most consumer tech. Update if product has a different natural habitat (studio monitors → desk setup, outdoor speaker → patio/garden). | Medium |

**Layer 2: Grid Panel Cascade**

| Panel | Original Content | What to Update | Coupling Severity |
|---|---|---|---|
| **Panel 1: Texture Detail** | "Macro close-up of joystick and buttons" | Replace with product's signature tactile/visual detail. Every tech product has different macro subjects. See texture-detail mapping below. | **Critical** |
| **Panel 2: Hand Interaction** | "Natural shot of hands pressing buttons during gameplay" | Replace with product's specific use-gesture. Hands pressing buttons → fingers adjusting dial → hand tapping touchscreen → voice gesture near speaker. | **Critical** |
| **Panel 3: Resting Scene** | "Controller resting on a wooden coffee table beside a console" | Replace product and companion device. The "resting" shot shows the product at rest in its natural domestic habitat. | **Critical** |
| **Panel 3: Companion Object** | "beside a console" | Update to product's natural pairing (headphones → beside phone/laptop, speaker → beside books/plant, tablet → beside coffee cup) | **Critical** |
| **Panel 4: Usage Moment** | "Player sitting comfortably with sunlight entering the room" | Replace activity descriptor. "Player sitting" → "listener relaxing" / "reader lounging" / "person working quietly." | High |

**Layer 3: Anti-Convention and Technical Updates**

| Field Path | Original Value | When to Update |
|---|---|---|
| `Negative_Prompt[0]` | "RGB gamer lighting" | **Replace with product category's conventional visual cliché.** Every tech product has a marketing convention this template rejects. See anti-convention mapping below. |
| `Negative_Prompt[2]` | "Neon gaming setup" | Same — replace with category convention |
| `Canvas.Use_Case[0]` | "Gaming lifestyle post" | Replace with product-appropriate platform descriptor |
| `Visual_Style.Style_Keywords[1]` | "Authentic gaming moment" | Replace "gaming" with product-appropriate activity |
| `Typography.Tagline.Text` | "Play Naturally." | Replace with product-appropriate tagline. "Play" is gaming-specific. |

### Product-Interaction Architecture: The Five-Frame Interaction Map

This template's defining feature is that the product is shown through INTERACTION, not isolation. Each frame captures a different relationship between human and product:
```
HERO:       Person + Product + Environment (product in active use)
Panel 1:    Product alone (macro detail — the only frame without human)
Panel 2:    Hands + Product (tactile interaction close-up)
Panel 3:    Product + Environment (product at rest in domestic context)
Panel 4:    Person + Environment (product implied, atmosphere dominant)
```
