# Kya-na Health Watch - Image & Video Generation Guide

## After Training is Complete

Once your LoRA is trained, use it to generate explainer content for marketing, documentation, and videos.

---

## 1. Image Generation Prompts

### A. Product Hero Shots

```
kya-na health watch, complete assembly, circular wearable form, front view, 
black metallic matte finish, 33mm square watch, matte silicon strap, 
professional product photography, clean white background
```

```
kya-na health watch, 3/4 angle view, circular form worn on wrist, 
black metallic finish, LED display active showing time, 
matte silicon strap, studio lighting
```

### B. Feature Highlights

**Sensors Active:**
```
kya-na watch core device, bottom view, chrome metal biometric sensors glowing green, 
LED indicators active, close-up detail, black metallic finish, 
technical product shot
```

**Display Screen:**
```
kya-na health watch, top view, LED display screen showing health metrics, 
glossy black screen surface, 33mm square watch face, 
user interface visible
```

**Copper Charging Pins:**
```
kya-na watch copper connector pins, top view of ring frame, 
6 golden copper contacts visible, high angle close-up, 
precision engineering detail
```

### C. Components & Assembly

**Separated Components:**
```
kya-na watch components, exploded view, core device, ring frame, 
matte silicon strap, powerbank accessory, all parts floating with spacing, 
technical diagram style, white background
```

**Powerbank Attachment:**
```
kya-na health watch with powerbank attached, side view, 
8mm powerbank module on back, magnetic connection visible, 
black metallic finish, product detail shot
```

### D. Strap Configurations

**Flat/Extended:**
```
kya-na watch, flat strap configuration, fully extended showing clasp mechanism, 
silicon strap with sensor windows visible underneath, 
210mm total length, product photography
```

**Circular/Wearable:**
```
kya-na watch, circular wearable form, strap curved into bracelet shape, 
clasp closed, ready to wear, matte silicon strap, 
lifestyle product shot
```

---

## 2. Video Generation Prompts (T2V)

### A. 360° Product Spin

```
kya-na health watch rotating 360 degrees, complete assembly, 
circular wearable form, smooth continuous rotation on turntable, 
black metallic matte finish, studio lighting, 
camera orbits around watch showing all angles
```

### B. Feature Demonstrations

**Sensor Activation:**
```
kya-na watch sensors activating, chrome metal sensors on back glowing green, 
LED lights pulsing, biometric monitoring active, 
close-up view, technical demonstration
```

**Display Interface:**
```
kya-na health watch display screen, user interface animating through menus, 
health metrics updating, time display, heart rate shown, 
LED screen close-up, modern UI design
```

### C. Assembly Sequences

**Core Installing into Ring:**
```
kya-na watch assembly animation, core device descending and snapping 
magnetically into ring frame, smooth mechanical motion, 
isometric 2.5D angle, technical explainer video
```

**Powerbank Attachment:**
```
kya-na powerbank sliding into position on watch back, 
magnetic connection engaging, copper pins aligning, 
side view animation, product demonstration
```

**Clasp Opening/Closing:**
```
kya-na watch clasp mechanism, circular strap opening, 
pin releasing from buckle hole, strap separating, 
smooth mechanical animation, detail shot
```

### D. Lifestyle & Context

**Wearing the Watch:**
```
kya-na health watch being worn on wrist, circular form, 
strap wrapping around arm, clasp fastening, 
first-person perspective, lifestyle video
```

**Daily Use Scenario:**
```
kya-na watch in use, checking health metrics on display, 
finger tapping screen, sensors monitoring biometrics, 
real-world usage demonstration
```

---

## 3. Image-to-Video (I2V) Workflow

### Start with a Reference Image

1. **Generate a static product image** using the prompts above
2. **Use that image as I2V input** with motion prompts:

**Example I2V Prompts:**

```
Input: [kya-na watch front view image]
Motion: "camera slowly orbits 90 degrees to the right, 
smooth cinematic movement, product reveal"
```

```
Input: [kya-na watch with sensors off]
Motion: "biometric sensors activate one by one, 
green LED glow appearing on chrome sensors, 
technical demonstration"
```

```
Input: [kya-na watch flat strap]
Motion: "strap gradually curves into circular wearable form, 
clasp moving toward connection, smooth transformation"
```

---

## 4. Explainer Video Sequence

### Full Product Story (30-60 seconds)

**Shot 1 (0-5s):** Hero shot, watch rotating 360°
```
kya-na health watch, complete assembly, circular wearable form, 
rotating slowly on black background, dramatic lighting, 
product reveal
```

**Shot 2 (5-10s):** Display closeup with UI
```
kya-na watch LED display screen, health metrics animating, 
heart rate, steps, sleep data shown, modern interface, 
close-up detail
```

**Shot 3 (10-15s):** Sensor activation
```
kya-na watch bottom view, chrome biometric sensors activating, 
green LED glow, health monitoring active, technical shot
```

**Shot 4 (15-20s):** Assembly animation
```
kya-na watch assembly sequence, components coming together, 
core snapping into ring, powerbank attaching, 
isometric 2.5D animation
```

**Shot 5 (20-25s):** Strap configurations
```
kya-na watch transforming from flat to circular form, 
clasp mechanism engaging, smooth transition, 
product demonstration
```

**Shot 6 (25-30s):** Final lifestyle shot
```
kya-na health watch worn on wrist, circular form, 
display showing time, daily wear scenario, 
lifestyle product shot
```

---

## 5. Technical Specifications Overlay Graphics

Generate clean product shots, then add text overlays in post:

**Dimensions Shot:**
```
kya-na watch technical diagram view, flat strap configuration, 
orthographic projection, clean lines, measurement-ready, 
white background
```

Add in post:
- 33mm × 33mm watch face
- 10mm core height
- 210mm total strap length
- 8mm powerbank thickness

---

## 6. Marketing Variations

### Different Contexts

**Tech/Modern:**
```
kya-na health watch, futuristic setting, holographic UI elements floating above display, 
sci-fi aesthetic, advanced technology visualization
```

**Fitness/Active:**
```
kya-na watch on athletic wrist, post-workout scene, 
sensors showing elevated heart rate, fitness tracking active, 
sports lifestyle
```

**Medical/Professional:**
```
kya-na health watch, clinical setting, medical monitoring display, 
precise biometric data shown, healthcare professional context
```

---

## 7. Batch Generation Tips

### For Consistency:

1. **Always include "kya-na health watch" or "kya-na watch"** in prompts
2. **Specify materials:** "black metallic matte finish, matte silicon strap, chrome sensors"
3. **Use exact dimensions:** "33mm square watch"
4. **Lock in configurations:** "circular wearable form" vs "flat strap configuration"

### Avoid Hallucinations:

- Don't add colors not in training (stay with black)
- Don't change strap material (silicon only)
- Don't invent features (stick to sensors, display, powerbank, clasp)
- Use consistent sensor description (chrome metal, green/red LEDs)

---

## 8. Negative Prompts (What to Avoid)

```
blurry, low quality, distorted, deformed, watermark, text, logo, 
unrealistic materials, wrong colors, glossy plastic, leather strap, 
round watch face, different design, brand confusion
```

---

## 9. Recommended Settings

**For Images:**
- Resolution: 1024×1024 or 1024×1536 (portrait product shots)
- Steps: 20-30
- CFG Scale: 4-7
- Sampler: FlowMatch or DPM++

**For Videos:**
- Resolution: 1024×576 or 768×768
- Frames: 24-48 (1-2 seconds at 24fps)
- Motion strength: Medium (avoid over-animation)
- Consistency: Use reference images when possible

---

## 10. Output Organization

```
outputs/
├── hero_shots/          # Main product images
├── features/            # Sensor, display, connector closeups
├── assembly/            # Component and assembly sequences
├── lifestyle/           # Worn/context shots
├── technical/           # Diagrams and specifications
└── videos/
    ├── 360_spins/
    ├── feature_demos/
    └── explainer_sequences/
```

---

## Quick Reference: Most Useful Prompts

**General Hero Shot:**
```
kya-na health watch, complete assembly, circular wearable form, 
black metallic matte finish, matte silicon strap, professional product photography
```

**Technical Detail:**
```
kya-na watch [component], close-up detail, black metallic finish, 
chrome metal sensors, technical product shot, clean background
```

**Animation:**
```
kya-na watch [action/motion], smooth animation, 
isometric 2.5D perspective, product demonstration
```

Replace [component] with: core device, ring frame, strap, powerbank, sensors, display
Replace [action/motion] with: rotating, assembling, activating, transforming, etc.

