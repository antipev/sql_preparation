---
id: "3b241426-eb50-80b0-a1b2-ca84923b58e2"
title: "Create Healthcare Advertisement Panels"
category: "Marketing"
source: notion
source_url: https://app.notion.com/p/3b241426eb50803b866ddc703f9ecbff
---

# Create Healthcare Advertisement Panels

**Category:** Marketing

## Description

Design professional healthcare advertisements with this AI prompt, featuring consultation, treatment, and result panels for clinic marketing and patient trust.

## What This Prompt Does

● Generates a professional three-panel AI image advertisement showing a complete healthcare patient journey from consultation to treatment to results.

● Creates realistic clinic scenes with customizable healthcare specialty, featuring medical professionals, modern equipment, and confident patient outcomes.

● Produces trust-focused AI images optimized for clinic websites and health marketing campaigns with clean clinical lighting and professional medical atmosphere.

## Prompt

```text
{
  "Objective": "Create a professional 1×3 horizontal advertisement for [CLINIC NAME] [HEALTHCARE SPECIALTY], emphasizing trust, hygiene, modern equipment, and healthy confident results.",
  "Canvas": {
    "Aspect_Ratio": "3:2",
    "Grid_Structure": "1×3 horizontal panels",
    "Orientation": "Landscape",
    "Use_Case": [
      "Clinic website banners",
      "Health awareness campaigns",
      "Social media health ads",
      "Local service marketing"
    ]
  },
  "Service_Description": {
    "Category": "[HEALTHCARE SPECIALTY] Services",
    "Core_Services": [
      "General dental checkups",
      "Professional teeth cleaning",
      "Cosmetic dentistry",
      "Whitening treatments"
    ],
    "Clinic_Features": [
      "Modern sterilized equipment",
      "Digital dental imaging",
      "Comfort-focused patient care",
      "Certified dental professionals"
    ]
  },
  "Background_Design": {
    "Environment": "Bright modern dental clinic interior",
    "Color_Theme": ["Soft White", "Light Blue", "Mint Green"],
    "Lighting": "Clean diffused clinical lighting",
    "Mood": ["Safe", "Professional", "Healthy"]
  },
  "Panels": [
    {
      "Panel_Number": 1,
      "Title": "Friendly Consultation",
      "Description": "Dentist smiling and speaking with patient in modern clinic room.",
      "Visual_Details": {
        "Camera_Angle": "Mid-shot, natural interaction",
        "Mood": ["Trust", "Comfort"]
      }
    },
    {
      "Panel_Number": 2,
      "Title": "Professional Treatment",
      "Description": "Close-up of dentist performing careful dental procedure with gloves and mask.",
      "Visual_Details": {
        "Focus": "Sterile tools and modern equipment",
        "Lighting": "Bright, clear clinical light",
        "Mood": ["Precision", "Hygiene"]
      }
    },
    {
      "Panel_Number": 3,
      "Title": "Healthy Smile Result",
      "Description": "Confident adult smiling naturally with bright teeth.",
      "Visual_Details": {
        "Lighting": "Soft natural light",
        "Mood": ["Confidence", "Health", "Satisfaction"]
      }
    }
  ],
  "Branding": {
    "Clinic_Name": "[CLINIC NAME]",
    "Tagline": "Your Healthiest Smile Starts Here",
    "Brand_Personality": "Caring, professional, modern",
    "Color_Palette": [COLOR PALETTE],
    "Typography": "Clean medical sans-serif"
  },
  "Visual_Style": {
    "Style_Keywords": [
      "Healthcare advertising",
      "Modern clinic photography",
      "High realism",
      "Clean minimal composition",
      "Medical professionalism"
    ]
  },
  "Camera_And_Lighting": {
    "Photography_Type": "Professional healthcare photography",
    "Shot_Types": [
      "Consultation mid-shot",
      "Procedure close-up",
      "Smile portrait"
    ],
    "Lighting_Style": "Bright diffused clinical lighting",
    "Exposure": "Clean and balanced",
    "Shadows": "Minimal and soft"
  },
  "Mood_Keywords": [
    "Healthy",
    "Trustworthy",
    "Professional",
    "Clean",
    "Comfortable",
    "Confident"
  ],
  "Negative_Prompt": [
    "Dirty instruments",
    "Dark lighting",
    "Scary atmosphere",
    "Unrealistic white teeth glow",
    "Cluttered background",
    "Cartoon style",
    "Low-resolution detail",
    "Watermarks",
    "Text overlays"
  ]
}
```

---

## VARIABLES GUIDE

| Variable | Description | Example Values | Dependency Notes |
|----------|-------------|----------------|------------------|
| **[CLINIC NAME]** | Healthcare provider brand name | `SMILECRAFT`, `VIVIDCARE`, `NEXTHEALTH` | Appears in Objective and Branding block. Also requires updating `Branding.Tagline` to match new specialty. Pure name swap otherwise. |
| **[HEALTHCARE SPECIALTY]** | The specific medical or wellness service being advertised | `Dental Clinic`, `Dermatology Center`, `Physiotherapy Studio` | **Extreme coupling — the deepest in the healthcare context.** Changes the professional role in every panel, the equipment visible, the facility environment, the procedure depicted, the patient outcome visualization, AND the trust-signaling visual cues. See full cascade guide, patient journey mapping, and trust-signal architecture below. |
| **[COLOR PALETTE]** | Array of 3 brand colors defining visual identity | `["Dental Blue", "White", "Soft Mint"]`, `["Warm Coral", "Cream White", "Blush Pink"]`, `["Sage Green", "White", "Light Tan"]` | Must be provided as a JSON array of 3 color strings. **Healthcare trust constraint.** Medical advertising has a narrower palette tolerance than any previous prompt category. Colors must simultaneously feel clinical (clean, hygienic) and approachable (warm, not sterile). See healthcare palette science below. |

### Cascade Guide for [HEALTHCARE SPECIALTY]

This cascade operates differently from product-based prompts. Changing a product swaps what the camera points at. Changing a healthcare specialty swaps the entire professional context: who's in the room, what they're doing, what equipment is visible, what the patient experiences, and what "success" looks like.

**Layer 1: Service Description Cascade**

| Field Path | Original Value | What to Update | Coupling Severity |
|---|---|---|---|
| `Service_Description.Core_Services` | Dental-specific array (checkups, cleaning, cosmetic, whitening) | Replace entirely with specialty-relevant services | **Critical** |
| `Service_Description.Clinic_Features` | Dental-specific features (sterilized equipment, dental imaging, patient care, certified professionals) | Replace equipment and imaging references; "comfort-focused patient care" and "certified professionals" transfer universally | High |

**Layer 2: Scene Bible Cascade**

| Field Path | Original Value | What to Update | Coupling Severity |
|---|---|---|---|
| `Background_Design.Environment` | "Bright modern dental clinic interior" | Replace specialty reference; keep "bright modern" — universal healthcare positive signal | Medium |
| `Background_Design.Color_Theme` | ["Soft White", "Light Blue", "Mint Green"] | May transfer for most medical specialties. Dermatology and wellness may shift warmer. See dual-color architecture note below. | Medium |

**Layer 3: Panel Array Cascade — The Patient Journey**

Every panel rewrites because each represents a stage of a specialty-specific patient experience:

| Panel | Original Content | What to Update | Coupling Severity |
|---|---|---|---|
| **Panel 1: Consultation** | "Dentist smiling and speaking with patient in modern clinic room" | Replace professional role title. Update interaction context (dermatologist examining skin, physio assessing movement, optometrist reviewing chart). | **Critical** |
| **Panel 2: Treatment** | "Close-up of dentist performing careful dental procedure with gloves and mask" | Replace procedure type, visible equipment, and protective gear appropriate to specialty. | **Critical** |
| **Panel 2: Focus** | "Sterile tools and modern equipment" | Replace with specialty-specific equipment (dermatoscope, therapy bands, eye examination tools) | **Critical** |
| **Panel 3: Result** | "Confident adult smiling naturally with bright teeth" | Replace outcome visualization. This is the hardest panel to swap because "healthy smile" is universally readable, but other specialties have less visually obvious results. See outcome visualization challenge below. | **Critical** |

**Layer 4: Technical and Branding Updates**

| Field Path | Original Value | When to Update |
|---|---|---|
| `Branding.Tagline` | "Your Healthiest Smile Starts Here" | **Always.** Tagline is dental-specific. Must be rewritten for every specialty. |
| `Camera_And_Lighting.Shot_Types` | ["Consultation mid-shot", "Procedure close-up", "Smile portrait"] | Update "Smile portrait" to specialty-appropriate result shot ("clear skin portrait," "movement demonstration," "vision test") |
| `Camera_And_Lighting.Photography_Type` | "Professional healthcare photography" | Transfers universally |
| `Visual_Style.Style_Keywords[1]` | "Modern clinic photography" | Transfers universally |
| `Negative_Prompt[3]` | "Unrealistic white teeth glow" | Replace with specialty-specific quality failure ("airbrushed skin" for derm, "exaggerated flexibility" for physio) |
| `Negative_Prompt[0]` | "Dirty instruments" | Transfers universally for clinical specialties; replace with equivalent for wellness/non-clinical services |

### Patient Journey Architecture: The 3-Panel Trust Funnel

This prompt's 3-panel structure encodes a specific psychological narrative designed to convert healthcare skeptics into patients. Each panel addresses a different trust barrier:
```
Panel 1: CONSULTATION         Panel 2: TREATMENT           Panel 3: RESULT
"Will they listen to me?"  →  "Are they competent?"     →  "Will I get results?"
├─ Trust barrier: Fear      ├─ Trust barrier: Competence  ├─ Trust barrier: Outcome
├─ Visual cue: Smile,       ├─ Visual cue: Equipment,     ├─ Visual cue: Patient
│  eye contact, warmth       │  sterility, precision        │  confidence, health
└─ Mood: Trust, Comfort      └─ Mood: Precision, Hygiene   └─ Mood: Confidence, Health
```

This funnel structure transfers to any healthcare specialty because the trust barriers are universal. What changes is the specific visual encoding of each barrier.

### Specialty Swap Mapping Table

| Healthcare Specialty | Panel 1: Consultation | Panel 2: Treatment | Panel 3: Result | Tagline Suggestion |
|---|---|---|---|---|
| **Dental Clinic** (original) | Dentist conversing with patient in exam room | Close-up of dental procedure with sterile tools | Confident smile with bright teeth | "Your Healthiest Smile Starts Here" |
| **Dermatology Center** | Dermatologist examining patient's skin with dermatoscope | Close-up of skin treatment (laser, microneedling, or topical application) | Clear, glowing skin portrait in natural light | "Your Healthiest Skin Starts Here" |
| **Physiotherapy Studio** | Physio discussing recovery plan with patient beside equipment | Close-up of guided movement therapy or joint treatment | Patient demonstrating confident, pain-free movement | "Move Freely, Live Fully" |
| **Optometry Clinic** | Optometrist speaking with patient at slit lamp | Close-up of eye examination or lens fitting | Person wearing new glasses with confident expression | "See the World More Clearly" |
| **Chiropractic Center** | Chiropractor reviewing spine imaging with patient | Close-up of spinal adjustment with proper positioning | Patient standing tall with relaxed, comfortable posture | "Align Your Health, Elevate Your Life" |
| **Veterinary Clinic** | Vet greeting pet owner and animal warmly | Close-up of careful examination of animal | Happy pet with relieved, smiling owner | "Where Healthy Pets Come First" |

### The Outcome Visualization Challenge (Panel 3)

Panel 3 is the hardest panel to swap because dental advertising has an inherent visual advantage: a smile is universally readable as a positive health outcome in a single photograph. Most other healthcare specialties don't have an equally instant visual result.

| Specialty | Outcome Visibility | Panel 3 Difficulty | Visual Strategy |
|---|---|---|---|
| **Dental** (original) | **Instant** — smile reads in milliseconds | Low | Direct result portrait (smile) |
| **Dermatology** | **High** — clear skin is visible and aspirational | Low | Direct result portrait (glowing skin) |
| **Optometry** | **Medium** — glasses are visible but "better vision" is invisible | Medium | Show confidence wearing new frames; can't show "sharper vision" directly |
| **Physiotherapy** | **Low** — "less pain" and "better mobility" are invisible states | High | Show movement/activity that implies recovered function (walking freely, stretching comfortably) |
| **Chiropractic** | **Very Low** — "aligned spine" is invisible | High | Show posture improvement and relaxed body language as proxy for internal alignment |
| **Mental Health** | **Invisible** — emotional wellbeing has no direct visual marker | Very High | Show calm, present, connected expression. Risk of cliché (person staring at sunset). Consider replacing Panel 3 entirely with a supportive environment shot instead. |

**Invisible outcome workaround:** For specialties where the result is invisible (physio, chiropractic, mental health), shift Panel 3 from "result portrait" to "life-after-treatment moment" — show the patient doing something they couldn't do before, rather than displaying the medical outcome directly.

### Healthcare Palette Science

Medical advertising operates within a narrower color tolerance than any other prompt category in the series. Colors carry specific psychological signals in healthcare contexts:

| Color Family | Healthcare Signal | Safe For | Dangerous For |
|---|---|---|---|
| **Light Blue** | Clinical trust, sterility, calm | All medical specialties — universal healthcare positive | Overuse → cold, institutional feeling |
| **Mint/Soft Green** | Healing, freshness, hygiene | Dental, dermatology, general practice | Dark green → surgical/operating room association |
| **White** | Cleanliness, precision, sterility | All specialties (must be primary or secondary, never absent) | Alone → sterile and unwelcoming |
| **Warm Coral/Blush** | Approachability, warmth, caring | Wellness-adjacent specialties (dermatology, aesthetic, pediatric) | Surgery, emergency, clinical labs (too soft for serious medical) |
| **Sage/Earth tones** | Natural, holistic, calm | Physiotherapy, chiropractic, naturopathic, wellness | Acute medical services (too casual for clinical trust) |
| **Deep Navy** | Authority, expertise, premium | Specialist clinics, surgical centers | Pediatric, family practice (too formal/intimidating) |

**Healthcare palette rules:**
1. White must always be one of the three colors — its absence signals lack of cleanliness
2. At least one color must be cool-toned (blue, mint, teal) — warm-only palettes feel non-medical
3. Saturated or neon colors are incompatible with healthcare trust — they read as commercial/retail rather than clinical
4. Black is absent from every viable healthcare palette — it signals mourning, fear, or severity

### Dual-Color Architecture (Unique to This Template)

This is the only prompt in the series with two independent color systems:
```
Background_Design.Color_Theme    →  Controls clinical environment appearance
["Soft White", "Light Blue", "Mint Green"]    (universal medical cleanliness signals)
                    │
                    │  (operate independently)
                    │
Branding.Color_Palette           →  Controls brand identity overlay
["Dental Blue", "White", "Soft Mint"]         (brand differentiation within medical space)
```
