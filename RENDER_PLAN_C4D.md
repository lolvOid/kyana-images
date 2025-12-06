# Kyana Smartwatch - Cinema 4D Render Plan
# Camera Setup: Orbiting on Circular Spline (0-360°)
# Device: Stationary at center

## RENDER SETTINGS
- Resolution: 1024 x 1024
- FPS: 24
- Frames: 0-71 (72 frames) OR 0-35 (36 frames)
- Camera: Moves on circular spline 360°, aligned to spline
- Device: Static at world origin

---

## CAMERA ANGLES NEEDED

### **1. MID-ANGLE (Your Current Setup) - MOST IMPORTANT**
- Camera position: Slightly above device level (current setup)
- Best for: Product showcase, showing top and sides together
- Use for: 90% of renders
- Distance: Medium (full device fills 70-80% of frame)

### **2. EYE-LEVEL / FLAT ANGLE - ESSENTIAL**
- Camera at exact same height as device center
- Best for: Side details (button, speaker), profile views
- Use for: Detail shots, side views
- Distance: Same as mid-angle

### **3. LOW ANGLE - IMPORTANT FOR SENSORS**
- Camera below device, looking up
- Best for: Bottom sensors, showing biometric array clearly
- Use for: Sensor-active states, technical details
- Distance: Same as mid-angle

### **4. HIGH ANGLE - OPTIONAL**
- Camera above device, looking down
- Best for: Top view, showing 6 copper pins on ring
- Use for: Connector details, top-down views
- Distance: Same as mid-angle

---

## CAMERA DISTANCE RECOMMENDATIONS

**For Full Assembly FLAT (straps straightened - 210mm length):**
- Distance from center: 300-350mm 
- Frame captures: Full watch with extended straps horizontally
- Use for: Product photography, technical specs, component showcase
- Best angles: MID, LOW (for sensors), HIGH (for top connectors)

**For Full Assembly CIRCULAR (straps curved - ~60-70mm diameter):**
- Distance from center: 180-220mm
- Frame captures: Watch in wearable circular form, more compact
- Use for: Lifestyle shots, wrist-worn appearance, realistic context
- Best angles: MID (slightly angled to show curve), 3/4 view

**For Core Device Only (30mm × 30mm):**
- Distance from center: 70-90mm (≈2.5× device width)
- Frame captures: Device fills 80-90% of frame
- Tighter framing for device alone
- Formula: ~2.5-3× device width for good framing

**For Powerbank Only (8mm thick cube):**
- Distance from center: 80-100mm (similar to core device)
- Small component, needs closer camera
- Show LED indicator and USB-C port clearly

**For Detail/Closeup:**
- Distance from center: 60-80mm
- Extreme closeup of connectors, sensors, button
- For macro shots of copper pins, LED sensors
- May need narrower FOV (25-30°)

---

## PRODUCT DIMENSIONS (Actual Physical Specs)

### **Core Device (Watch Module):**
- Width: 30mm
- Height: 30mm  
- Thickness: 10mm (1.0cm)
- Note: Sits inside the ring frame

### **Outer Ring Frame:**
- Width: 33mm
- Height: 33mm
- Thickness: 7mm (0.7cm)
- Note: Surrounds and holds the 30mm core device

### **Powerbank:**
- Thickness: 8mm (0.8cm)
- Note: Attaches to strap, adds to overall system length

### **Straps:**

**When FLAT/STRAIGHTENED (for product shots):**
- Strap 1 (Short side): 80mm (8cm)
- Strap 2 (Long side): 130mm (13cm)
- Total strap length flat: 210mm (21cm)
- Configuration: Straps extended horizontally from device
- Use for: Product photography, component showcase

**When CIRCULAR/CURVED (for wearing simulation):**
- Forms wearable circle/bracelet shape
- Approximate diameter: 60-70mm (fits wrist)
- Total circumference: 210mm (same as flat length)
- Configuration: Straps curved to form closed loop
- Use for: Lifestyle shots, wrist-worn appearance

### **Full Assembly Dimensions:**
- Core device: 30mm × 30mm × 10mm
- Outer ring: 33mm × 33mm × 7mm
- Full device (core + ring): 33mm × 33mm overall, max thickness 10mm (core)
- **FLAT config**: ~210mm length when laid straight
- **CIRCULAR config**: ~60-70mm diameter circle
- With powerbank: +8mm thickness on strap section (powerbank only)

---

## COMPONENTS TO RENDER

### **ASSEMBLY COMBINATIONS:**

1. **OUTER_RING_ONLY**
   - Just the ring frame (hollow square, 33mm × 33mm × 7mm)
   - Shows: 4 internal magnetic connectors, 6 copper pins on top

2. **CORE_DEVICE_ONLY**
   - Just the core module (30mm × 30mm × 10mm)
   - Shows: LED display, speaker, button, all sides

3. **POWERBANK_ONLY**
   - Just the battery module (8mm thick)
   - Shows: Green LED, USB-C port, all angles

4. **STRAP_FLAT_ONLY**
   - Flat strap version alone (80mm + 130mm = 210mm total)
   - Configuration: Straightened/extended horizontally
   - Shows: Clasp mechanism, 6 sensor windows

5. **STRAP_CIRCULAR_ONLY**
   - Circular strap version alone
   - Configuration: Curved to form bracelet shape (~60-70mm diameter)
   - Shows: Curved shape, sensors, realistic wearable form

6. **RING_STRAP_FLAT** (No Core)
   - Ring + Flat strap (straps straightened)
   - Shows: Empty center, connector system, 210mm strap length

7. **RING_STRAP_CIRCULAR** (No Core)
   - Ring + Circular strap (straps curved)
   - Shows: Empty center, modular system, wearable form

8. **FULL_ASSEMBLY_FLAT**
   - Core + Ring + Flat Strap (straightened)
   - Shows: Complete watch, flat strap variant, full 210mm length

9. **FULL_ASSEMBLY_CIRCULAR**
   - Core + Ring + Circular Strap (curved)
   - Shows: Complete watch, circular strap variant, wearable form

10. **FULL_WITH_POWERBANK_FLAT**
    - Core + Ring + Flat Strap + Powerbank (straightened)
    - Shows: Extended battery system, full length display

11. **FULL_WITH_POWERBANK_CIRCULAR**
    - Core + Ring + Circular Strap + Powerbank (curved)
    - Shows: Complete system with battery, wearable configuration

---

## COMPLETE RENDER LIST

### **PHASE 1 - ESSENTIAL PRODUCT SHOTS (Priority)**

#### 1A. FULL_ASSEMBLY_FLAT_MID_360
- Components: Core + Ring + Flat Strap (straps straightened, 210mm length)
- Camera: Mid-angle (your current setup)
- Frames: 0-35 (36 frames)
- Distance: 300-350mm (to fit full strap length horizontally)
- Configuration: Product photography style, straps extended
- Output: `FULL_ASSEMBLY_FLAT_MID_360_1024x1024_####.png`

#### 1B. FULL_ASSEMBLY_CIRCULAR_MID_360
- Components: Core + Ring + Circular Strap (curved to ~60-70mm diameter)
- Camera: Mid-angle
- Frames: 0-35
- Distance: 180-220mm (more compact, circular form)
- Configuration: Wearable style, straps form bracelet
- Output: `FULL_ASSEMBLY_CIRCULAR_MID_360_1024x1024_####.png`

#### 2A. FULL_WITH_POWERBANK_FLAT_MID_360
- Components: Core + Ring + Flat Strap + Powerbank (straightened)
- Camera: Mid-angle
- Frames: 0-35
- Distance: 300-350mm (full length with powerbank on strap)
- Configuration: Extended straps, powerbank visible on strap
- Output: `FULL_WITH_POWERBANK_FLAT_MID_360_1024x1024_####.png`

#### 2B. FULL_WITH_POWERBANK_CIRCULAR_MID_360
- Components: Core + Ring + Circular Strap + Powerbank (curved)
- Camera: Mid-angle
- Frames: 0-35
- Distance: 180-220mm (circular form with powerbank)
- Configuration: Wearable style with battery module
- Output: `FULL_WITH_POWERBANK_CIRCULAR_MID_360_1024x1024_####.png`

#### 3. CORE_DEVICE_ONLY_MID_360
- Components: Core Device only (30mm × 30mm × 10mm)
- Camera: Mid-angle
- Frames: 0-35
- Distance: 70-90mm (closer, device fills frame)
- Output: `CORE_DEVICE_ONLY_MID_360_1024x1024_####.png`

#### 4. POWERBANK_ONLY_MID_360
- Components: Powerbank only (8mm thick)
- Camera: Mid-angle
- Frames: 0-35
- Distance: 80-100mm
- Output: `POWERBANK_ONLY_MID_360_1024x1024_####.png`

#### 5. RING_STRAP_FLAT_MID_360
- Components: Ring + Flat Strap (no core)
- Camera: Mid-angle
- Frames: 0-35
- Distance: 300-350mm (full strap length)
- Output: `RING_STRAP_FLAT_MID_360_1024x1024_####.png`

---

### **PHASE 2 - SENSOR STATES (Essential for Training)**

#### 6A. FULL_ASSEMBLY_FLAT_SENSORS_ON_LOW_360
- Components: Core + Ring + Flat Strap
- Camera: LOW angle (looking up from below)
- Frames: 0-35
- Distance: 300-350mm
- Sensors: CORE sensors (green/red) ON, STRAP sensors (green) ON
- Output: `FULL_ASSEMBLY_FLAT_SENSORS_ON_LOW_360_1024x1024_####.png`

#### 6B. FULL_ASSEMBLY_CIRCULAR_SENSORS_ON_LOW_360
- Components: Core + Ring + Circular Strap
- Camera: LOW angle
- Frames: 0-35
- Distance: 300-350mm
- Sensors: All ON
- Output: `FULL_ASSEMBLY_CIRCULAR_SENSORS_ON_LOW_360_1024x1024_####.png`

#### 7. FULL_ASSEMBLY_FLAT_SENSORS_OFF_LOW_360
- Components: Core + Ring + Flat Strap
- Camera: LOW angle
- Frames: 0-35
- Distance: 300-350mm
- Sensors: All OFF
- Output: `FULL_ASSEMBLY_FLAT_SENSORS_OFF_LOW_360_1024x1024_####.png`

#### 8. CORE_DEVICE_SENSORS_ON_LOW_360
- Components: Core Device only (30mm × 30mm × 10mm)
- Camera: LOW angle (show bottom sensors)
- Frames: 0-35
- Distance: 70-90mm (close to 30mm device)
- Sensors: Bottom biometric sensors ON (green/red LEDs)
- Output: `CORE_DEVICE_SENSORS_ON_LOW_360_1024x1024_####.png`

#### 9. STRAP_FLAT_SENSORS_ON_LOW_360
- Components: Flat Strap only (or with ring)
- Camera: LOW angle (show strap bottom)
- Frames: 0-35
- Distance: 200-250mm (strap length 210mm)
- Sensors: 6 rectangular sensor windows with green LEDs ON
- Output: `STRAP_FLAT_SENSORS_ON_LOW_360_1024x1024_####.png`

---

### **PHASE 3 - DETAIL SHOTS (Closeup & Specific Angles)**

#### 10. COPPER_PINS_TOP_HIGH_360
- Components: Ring frame only or with strap
- Camera: HIGH angle (looking down from above)
- Frames: 0-35
- Distance: 100mm (closeup)
- Focus: 6 copper pins on top of ring clearly visible
- Output: `COPPER_PINS_TOP_HIGH_360_1024x1024_####.png`

#### 11. MAGNETIC_CONNECTORS_INSIDE_HIGH_360
- Components: Ring frame only (empty)
- Camera: HIGH angle + tilted to look inside
- Frames: 0-35
- Distance: 100mm
- Focus: 4 internal magnetic connectors visible
- Output: `MAGNETIC_CONNECTORS_INSIDE_HIGH_360_1024x1024_####.png`

#### 12. BUTTON_SPEAKER_DETAIL_FLAT_360
- Components: Core Device only (30mm × 30mm × 10mm)
- Camera: EYE-LEVEL / FLAT angle (same height as device)
- Frames: 0-35
- Distance: 50-70mm (extreme closeup)
- Focus: Button (right side) and Speaker (left side) detail
- Output: `BUTTON_SPEAKER_DETAIL_FLAT_360_1024x1024_####.png`

#### 13. CLASP_MECHANISM_DETAIL_FLAT_360
- Components: Flat Strap only
- Camera: EYE-LEVEL
- Frames: 0-35
- Distance: 100mm
- Focus: Clasp mechanism and connection detail
- Output: `CLASP_MECHANISM_DETAIL_FLAT_360_1024x1024_####.png`

#### 14. DISPLAY_SCREEN_CLOSEUP_MID_360
- Components: Core Device only (30mm × 30mm × 10mm)
- Camera: MID angle slightly high
- Frames: 0-35
- Distance: 50mm (very close)
- Focus: LED display screen, glossy surface detail
- Output: `DISPLAY_SCREEN_CLOSEUP_MID_360_1024x1024_####.png`

---

### **PHASE 4 - ASSEMBLY ANIMATION (For I2V Training)**

#### 15. ASSEMBLY_ANIMATION_FLAT
- Animation sequence (not just rotation)
- Frames: 0-120 (5 seconds at 24fps)
- Camera: MID angle, STATIC (not moving)
- Distance: 350mm (wide to fit all components)
- Animation:
  - Frame 0-30: Strap flat on surface (210mm length visible)
  - Frame 31-50: Ring (33mm × 7mm) descends and connects to strap
  - Frame 51-80: Core device (30mm × 10mm) descends and snaps into ring (magnetic)
  - Frame 81-100: Powerbank (8mm thick) slides in from side
  - Frame 101-120: Final assembled watch with gentle rotation
- Output: `ASSEMBLY_ANIMATION_FLAT_1024x1024_####.png`

#### 16. DISASSEMBLY_ANIMATION_FLAT
- Reverse of assembly
- Frames: 0-120
- Camera: MID angle, STATIC
- Distance: 350mm
- Animation: Complete watch → separates into components
- Output: `DISASSEMBLY_ANIMATION_FLAT_1024x1024_####.png`

#### 17. EXPLODED_VIEW_360
- All components separated vertically with gaps
- Camera: MID angle, ORBITING on spline
- Frames: 0-35
- Distance: 350mm (wider to fit all parts)
- Spacing: 50mm between each component vertically
- Stack from top: Core (30mm × 10mm) → Ring (33mm × 7mm) → Strap (210mm) → Powerbank (8mm)
- Output: `EXPLODED_VIEW_360_1024x1024_####.png`

---

## SUMMARY BY CAMERA ANGLE

### **MID-ANGLE (Your Current Setup) - Use for:**
- All full assembly renders (Phase 1)
- Product showcase views
- Component solo shots
- Most versatile angle

### **LOW ANGLE - Use for:**
- Sensor active/inactive states (Phase 2)
- Bottom biometric sensor details
- Strap sensor array views
- Technical demonstration

### **HIGH ANGLE - Use for:**
- Top copper pins closeup (Phase 3)
- Internal magnetic connectors
- Top-down connector views

### **EYE-LEVEL / FLAT ANGLE - Use for:**
- Button & speaker side details (Phase 3)
- Clasp mechanism
- Side profile technical shots

---

## RENDER PRIORITY ORDER

**Start Here (Must Have):**
1. FULL_ASSEMBLY_FLAT_MID_360
2. FULL_WITH_POWERBANK_FLAT_MID_360
3. FULL_ASSEMBLY_FLAT_SENSORS_ON_LOW_360
4. CORE_DEVICE_ONLY_MID_360
5. RING_STRAP_FLAT_MID_360

**Next Priority (Important):**
6. FULL_ASSEMBLY_CIRCULAR_MID_360
7. POWERBANK_ONLY_MID_360
8. STRAP_FLAT_SENSORS_ON_LOW_360
9. CORE_DEVICE_SENSORS_ON_LOW_360
10. COPPER_PINS_TOP_HIGH_360

**Additional (Nice to Have):**
11. BUTTON_SPEAKER_DETAIL_FLAT_360
12. CLASP_MECHANISM_DETAIL_FLAT_360
13. FULL_WITH_POWERBANK_CIRCULAR_MID_360
14. MAGNETIC_CONNECTORS_INSIDE_HIGH_360

**Advanced (For Animation Training):**
15. ASSEMBLY_ANIMATION_FLAT
16. EXPLODED_VIEW_360
17. DISASSEMBLY_ANIMATION_FLAT

---

## CINEMA 4D SETUP CHECKLIST

### Camera on Spline Setup:
1. Create circular spline at world origin
2. Camera rides on spline with "Align to Spline" enabled
3. Animate camera position along spline: 0% to 100% over 36 frames
4. Device stays static at center (0,0,0)

### Frame Settings:
- Frame 0: Camera at 0% spline position (0°)
- Frame 36: Camera at 100% spline position (360°)
- Interpolation: Linear

### Camera Height Adjustments:
- **MID**: Camera Y = +20mm to +50mm above device center
- **FLAT/EYE-LEVEL**: Camera Y = 0mm (same as device center)
- **LOW**: Camera Y = -30mm to -50mm below device center
- **HIGH**: Camera Y = +80mm to +120mm above device center

### Distance from Center (Spline Radius):
- **Full assembly with straps**: 300-350mm
- **Core device only** (30mm): 70-90mm (≈2.5-3× device size)
- **Ring frame only** (33mm): 80-100mm
- **Powerbank only** (8mm thick): 70-90mm
- **Closeup details**: 50-70mm

### Render Output Settings:
- Format: PNG with Alpha
- Resolution: 1024 x 1024
- Color Depth: 8-bit
- Anti-aliasing: Best
- Frame Range: 0 to 35
- Output: `$prj/$take/$take_####.png`

---

## ESTIMATED RENDER COUNT

**Phase 1** (Essential Product): 7 renders × 36 frames = **252 images**
**Phase 2** (Sensor States): 4 renders × 36 frames = **144 images**
**Phase 3** (Details): 5 renders × 36 frames = **180 images**
**Phase 4** (Animation): 3 renders × 36-120 frames = **210 images**

**Total Core Dataset: ~400 images** (Phase 1 + 2)
**Total Complete: ~786 images** (All phases)

---

## RECOMMENDATION

**Start with 36 frames (10° per frame):**
✅ Faster rendering
✅ Good coverage for training
✅ Can upgrade to 72 frames later

**Focus on Phase 1 + Phase 2 first:**
✅ Essential for product LoRA
✅ Covers all angles and sensor states
✅ ~400 images = solid training dataset

**Your current mid-angle setup is perfect for 90% of renders!**
Just adjust camera height for LOW, HIGH, and FLAT angles as needed.
