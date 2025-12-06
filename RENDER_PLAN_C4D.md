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

**For Full Assembly Views:**
- Distance from center: 150-200mm (device fills 70-80% of frame)
- Allows space for strap curves, full watch visible

**For Component Only (Core Device, Powerbank):**
- Distance from center: 100-120mm (component fills 80-90% of frame)
- Tighter framing for smaller parts

**For Detail/Closeup:**
- Distance from center: 80-100mm (detail fills frame)
- Extreme closeup of connectors, sensors, button

---

## COMPONENTS TO RENDER

### **ASSEMBLY COMBINATIONS:**

1. **OUTER_RING_ONLY**
   - Just the ring frame (hollow square)
   - Shows: 4 internal magnetic connectors, 6 copper pins on top

2. **CORE_DEVICE_ONLY**
   - Just the core module
   - Shows: LED display, speaker, button, all sides

3. **POWERBANK_ONLY**
   - Just the battery module
   - Shows: Green LED, USB-C port, all angles

4. **STRAP_FLAT_ONLY**
   - Flat strap version alone
   - Shows: Clasp mechanism, 6 sensor windows

5. **STRAP_CIRCULAR_ONLY**
   - Circular strap version alone
   - Shows: Curved shape, sensors

6. **RING_STRAP_FLAT** (No Core)
   - Ring + Flat strap
   - Shows: Empty center, connector system

7. **RING_STRAP_CIRCULAR** (No Core)
   - Ring + Circular strap
   - Shows: Empty center, modular system

8. **FULL_ASSEMBLY_FLAT**
   - Core + Ring + Flat Strap
   - Shows: Complete watch, flat strap variant

9. **FULL_ASSEMBLY_CIRCULAR**
   - Core + Ring + Circular Strap
   - Shows: Complete watch, circular strap variant

10. **FULL_WITH_POWERBANK_FLAT**
    - Core + Ring + Flat Strap + Powerbank
    - Shows: Extended battery system

11. **FULL_WITH_POWERBANK_CIRCULAR**
    - Core + Ring + Circular Strap + Powerbank
    - Shows: Complete system with battery

---

## COMPLETE RENDER LIST

### **PHASE 1 - ESSENTIAL PRODUCT SHOTS (Priority)**

#### 1A. FULL_ASSEMBLY_FLAT_MID_360
- Components: Core + Ring + Flat Strap
- Camera: Mid-angle (your current setup)
- Frames: 0-35 (36 frames)
- Distance: 150-200mm
- Output: `FULL_ASSEMBLY_FLAT_MID_360_1024x1024_####.png`

#### 1B. FULL_ASSEMBLY_CIRCULAR_MID_360
- Components: Core + Ring + Circular Strap
- Camera: Mid-angle
- Frames: 0-35
- Distance: 150-200mm
- Output: `FULL_ASSEMBLY_CIRCULAR_MID_360_1024x1024_####.png`

#### 2A. FULL_WITH_POWERBANK_FLAT_MID_360
- Components: Core + Ring + Flat Strap + Powerbank
- Camera: Mid-angle
- Frames: 0-35
- Distance: 150-200mm
- Output: `FULL_WITH_POWERBANK_FLAT_MID_360_1024x1024_####.png`

#### 2B. FULL_WITH_POWERBANK_CIRCULAR_MID_360
- Components: Core + Ring + Circular Strap + Powerbank
- Camera: Mid-angle
- Frames: 0-35
- Distance: 150-200mm
- Output: `FULL_WITH_POWERBANK_CIRCULAR_MID_360_1024x1024_####.png`

#### 3. CORE_DEVICE_ONLY_MID_360
- Components: Core Device only
- Camera: Mid-angle
- Frames: 0-35
- Distance: 100-120mm (closer, fills frame)
- Output: `CORE_DEVICE_ONLY_MID_360_1024x1024_####.png`

#### 4. POWERBANK_ONLY_MID_360
- Components: Powerbank only
- Camera: Mid-angle
- Frames: 0-35
- Distance: 100-120mm
- Output: `POWERBANK_ONLY_MID_360_1024x1024_####.png`

#### 5. RING_STRAP_FLAT_MID_360
- Components: Ring + Flat Strap (no core)
- Camera: Mid-angle
- Frames: 0-35
- Distance: 150-200mm
- Output: `RING_STRAP_FLAT_MID_360_1024x1024_####.png`

---

### **PHASE 2 - SENSOR STATES (Essential for Training)**

#### 6A. FULL_ASSEMBLY_FLAT_SENSORS_ON_LOW_360
- Components: Core + Ring + Flat Strap
- Camera: LOW angle (looking up from below)
- Frames: 0-35
- Distance: 150-200mm
- Sensors: CORE sensors (green/red) ON, STRAP sensors (green) ON
- Output: `FULL_ASSEMBLY_FLAT_SENSORS_ON_LOW_360_1024x1024_####.png`

#### 6B. FULL_ASSEMBLY_CIRCULAR_SENSORS_ON_LOW_360
- Components: Core + Ring + Circular Strap
- Camera: LOW angle
- Frames: 0-35
- Distance: 150-200mm
- Sensors: All ON
- Output: `FULL_ASSEMBLY_CIRCULAR_SENSORS_ON_LOW_360_1024x1024_####.png`

#### 7. FULL_ASSEMBLY_FLAT_SENSORS_OFF_LOW_360
- Components: Core + Ring + Flat Strap
- Camera: LOW angle
- Frames: 0-35
- Distance: 150-200mm
- Sensors: All OFF
- Output: `FULL_ASSEMBLY_FLAT_SENSORS_OFF_LOW_360_1024x1024_####.png`

#### 8. CORE_DEVICE_SENSORS_ON_LOW_360
- Components: Core Device only
- Camera: LOW angle (show bottom sensors)
- Frames: 0-35
- Distance: 100-120mm
- Sensors: Bottom biometric sensors ON (green/red LEDs)
- Output: `CORE_DEVICE_SENSORS_ON_LOW_360_1024x1024_####.png`

#### 9. STRAP_FLAT_SENSORS_ON_LOW_360
- Components: Flat Strap only (or with ring)
- Camera: LOW angle (show strap bottom)
- Frames: 0-35
- Distance: 150mm
- Sensors: 6 rectangular sensor windows with green LEDs ON
- Output: `STRAP_FLAT_SENSORS_ON_LOW_360_1024x1024_####.png`

---

### **PHASE 3 - DETAIL SHOTS (Closeup & Specific Angles)**

#### 10. COPPER_PINS_TOP_HIGH_360
- Components: Ring frame only or with strap
- Camera: HIGH angle (looking down from above)
- Frames: 0-35
- Distance: 120mm (closeup)
- Focus: 6 copper pins on top of ring clearly visible
- Output: `COPPER_PINS_TOP_HIGH_360_1024x1024_####.png`

#### 11. MAGNETIC_CONNECTORS_INSIDE_HIGH_360
- Components: Ring frame only (empty)
- Camera: HIGH angle + tilted to look inside
- Frames: 0-35
- Distance: 120mm
- Focus: 4 internal magnetic connectors visible
- Output: `MAGNETIC_CONNECTORS_INSIDE_HIGH_360_1024x1024_####.png`

#### 12. BUTTON_SPEAKER_DETAIL_FLAT_360
- Components: Core Device only
- Camera: EYE-LEVEL / FLAT angle (same height as device)
- Frames: 0-35
- Distance: 80-100mm (extreme closeup)
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
- Components: Core Device only
- Camera: MID angle slightly high
- Frames: 0-35
- Distance: 80mm (very close)
- Focus: LED display screen, glossy surface detail
- Output: `DISPLAY_SCREEN_CLOSEUP_MID_360_1024x1024_####.png`

---

### **PHASE 4 - ASSEMBLY ANIMATION (For I2V Training)**

#### 15. ASSEMBLY_ANIMATION_FLAT
- Animation sequence (not just rotation)
- Frames: 0-120 (5 seconds at 24fps)
- Camera: MID angle, STATIC (not moving)
- Distance: 150-200mm
- Animation:
  - Frame 0-30: Strap flat on surface
  - Frame 31-50: Ring descends and connects to strap
  - Frame 51-80: Core device descends and snaps into ring (magnetic)
  - Frame 81-100: Powerbank slides in from side
  - Frame 101-120: Final assembled watch with gentle rotation
- Output: `ASSEMBLY_ANIMATION_FLAT_1024x1024_####.png`

#### 16. DISASSEMBLY_ANIMATION_FLAT
- Reverse of assembly
- Frames: 0-120
- Camera: MID angle, STATIC
- Animation: Complete watch → separates into components
- Output: `DISASSEMBLY_ANIMATION_FLAT_1024x1024_####.png`

#### 17. EXPLODED_VIEW_360
- All components separated vertically with gaps
- Camera: MID angle, ORBITING on spline
- Frames: 0-35
- Distance: 200mm (wider to fit all parts)
- Spacing: 50mm between each component vertically
- Stack from top: Core → Ring → Strap → Powerbank
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
- **Full assembly**: 150-200mm
- **Components**: 100-120mm
- **Closeups**: 80-100mm

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
