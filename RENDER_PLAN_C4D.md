# Kyana Smartwatch - Cinema 4D Render Plan
# Resolution: 1024x1024
# Rotation: 360 degrees
# Recommended: 72 frames (5° per frame) or 36 frames (10° per frame)

## RENDER SETTINGS
- Resolution: 1024 x 1024
- FPS: 24
- Frames: 0-71 (72 frames) OR 0-35 (36 frames)
- Rotation: Y-axis 360°
- Background: White or Transparent

## CAMERA SETUP
All renders use rotating turntable with camera fixed:
- Camera Distance: Appropriate to fill frame
- Camera Height: Adjusted per view type
- Rotation: Object rotates on Y-axis, camera static

---

## PRIMARY RENDERS (Essential)

### 1. WATCH_CORE_ONLY_360
- Component: Core device only (no ring, no strap)
- Frames: 0-71
- View: Front/center angle
- Shows: LED display, speaker, button, all sides
- Output: WATCH_CORE_ONLY_360_1024x1024_####.png

### 2. WATCH_RING_STRAP_ONLY_360
- Component: Ring frame + strap (no core device)
- Frames: 0-71
- View: Front/center angle
- Shows: 4 internal magnetic connectors, 6 copper pins on top
- Output: WATCH_RING_STRAP_ONLY_360_1024x1024_####.png

### 3. WATCH_FULL_ASSEMBLY_360
- Component: Core + Ring + Strap (complete watch)
- Frames: 0-71
- View: Front/center angle (standard product view)
- Shows: Fully assembled watch, all angles
- Output: WATCH_FULL_ASSEMBLY_360_1024x1024_####.png

### 4. WATCH_WITH_POWERBANK_360
- Component: Core + Ring + Strap + Powerbank
- Frames: 0-71
- View: Front/center angle
- Shows: Complete system with battery module
- Output: WATCH_WITH_POWERBANK_360_1024x1024_####.png

### 5. POWERBANK_ONLY_360
- Component: Powerbank module standalone
- Frames: 0-71
- View: Center angle
- Shows: Battery cube, LED, USB-C port
- Output: POWERBANK_ONLY_360_1024x1024_####.png

---

## SECONDARY RENDERS (Additional Angles)

### 6. WATCH_FULL_ASSEMBLY_LOW_ANGLE_360
- Component: Core + Ring + Strap
- Frames: 0-71
- View: Low camera angle (looking up at watch)
- Shows: Bottom profile, thickness, strap curve
- Output: WATCH_FULL_ASSEMBLY_LOW_ANGLE_360_1024x1024_####.png

### 7. WATCH_FULL_ASSEMBLY_HIGH_ANGLE_360
- Component: Core + Ring + Strap
- Frames: 0-71
- View: High camera angle (looking down)
- Shows: Top view, 6 copper pins, display screen
- Output: WATCH_FULL_ASSEMBLY_HIGH_ANGLE_360_1024x1024_####.png

### 8. WATCH_FULL_ASSEMBLY_SIDE_CLOSEUP_360
- Component: Core + Ring + Strap
- Frames: 0-71
- View: Side angle closeup
- Shows: Button detail, speaker detail, thickness
- Output: WATCH_FULL_ASSEMBLY_SIDE_CLOSEUP_360_1024x1024_####.png

---

## SENSOR STATES (Static or Rotation)

### 9. WATCH_SENSORS_ACTIVE_360
- Component: Core + Ring + Strap
- Frames: 0-71
- View: Low angle showing bottom
- Sensors: GREEN and RED LEDs ON
- Shows: Active biometric sensors glowing
- Output: WATCH_SENSORS_ACTIVE_360_1024x1024_####.png

### 10. WATCH_SENSORS_OFF_360
- Component: Core + Ring + Strap
- Frames: 0-71
- View: Low angle showing bottom
- Sensors: All LEDs OFF
- Shows: Inactive sensors, copper color visible
- Output: WATCH_SENSORS_OFF_360_1024x1024_####.png

### 11. STRAP_SENSORS_ACTIVE_360
- Component: Strap only or with ring
- Frames: 0-71
- View: Bottom/underside view
- Sensors: 6 rectangular windows with GREEN LEDs ON
- Output: STRAP_SENSORS_ACTIVE_360_1024x1024_####.png

---

## DETAIL SHOTS (Close-up, can be 360° or specific angles)

### 12. COPPER_CONNECTORS_TOP_CLOSEUP
- Component: Ring frame top view
- Frames: 0-35 (36 frames, slower rotation)
- View: Extreme closeup of 6 copper pins
- Shows: Golden connector details, precision pins
- Output: COPPER_CONNECTORS_TOP_CLOSEUP_1024x1024_####.png

### 13. MAGNETIC_CONNECTORS_INSIDE_CLOSEUP
- Component: Ring frame internal view
- Frames: 0-35
- View: Looking inside ring at 4 magnetic pins
- Shows: Internal magnetic connection system
- Output: MAGNETIC_CONNECTORS_INSIDE_CLOSEUP_1024x1024_####.png

### 14. DISPLAY_SCREEN_CLOSEUP
- Component: Core device
- Frames: 0-35
- View: Front display screen closeup
- Shows: LED screen detail, glossy surface
- Output: DISPLAY_SCREEN_CLOSEUP_1024x1024_####.png

### 15. BUTTON_SPEAKER_CLOSEUP
- Component: Core device side
- Frames: 0-35
- View: Side profile extreme closeup
- Shows: Button on right, speaker grille on left
- Output: BUTTON_SPEAKER_CLOSEUP_1024x1024_####.png

---

## EXPLODED VIEWS (Optional, Advanced)

### 16. WATCH_EXPLODED_ASSEMBLY_360
- Component: All parts separated vertically
- Frames: 0-71
- View: Center angle
- Shows: Core floating above ring, ring above strap
- Output: WATCH_EXPLODED_ASSEMBLY_360_1024x1024_####.png

### 17. WATCH_ASSEMBLY_ANIMATION
- Component: Parts coming together
- Frames: 0-120 (5 seconds at 24fps)
- Animation: Exploded → Assembled over time
- Shows: Modular assembly process
- Output: WATCH_ASSEMBLY_ANIMATION_1024x1024_####.png

---

## LIFESTYLE/CONTEXT RENDERS (Optional)

### 18. WATCH_ON_WRIST_360
- Component: Watch on wrist model
- Frames: 0-71
- View: Natural wearing angle
- Shows: How it looks when worn
- Output: WATCH_ON_WRIST_360_1024x1024_####.png

### 19. WATCH_WITH_ACCESSORIES_360
- Component: Watch + charging cable + powerbank
- Frames: 0-71
- View: Product ecosystem
- Shows: Complete package layout
- Output: WATCH_WITH_ACCESSORIES_360_1024x1024_####.png

---

## COLOR VARIANTS (Future)

When ready for color variants, duplicate above with color suffix:
- `_BLACK_` (current/default)
- `_WHITE_`
- `_SILVER_`
- `_SPACE_GREY_`

Example: `WATCH_FULL_ASSEMBLY_WHITE_360_1024x1024_####.png`

---

## CINEMA 4D SETUP CHECKLIST

### Turntable Setup:
1. Place watch at world origin (0,0,0)
2. Create null object at origin as rotation parent
3. Parent watch to null object
4. Animate null object Y-rotation: 0° to 360° over 72 frames
5. Camera remains static, pointing at origin

### Keyframe Settings:
- Frame 0: Rotation Y = 0°
- Frame 72: Rotation Y = 360°
- Interpolation: Linear (no easing)

### Render Settings:
- Resolution: 1024 x 1024
- Format: PNG with Alpha
- Color Depth: 8-bit or 16-bit
- Anti-aliasing: Best quality
- Frame Range: 0 to 71 (or 0 to 35)
- Frame Step: 1

### Output Naming:
Cinema 4D Output: `$prj/$take/$take_####.$ext`
Results in: `WATCH_FULL_ASSEMBLY_360_0000.png`

---

## PRIORITY RENDERING ORDER

**Phase 1 - Essential (Must Have):**
1. WATCH_FULL_ASSEMBLY_360
2. WATCH_WITH_POWERBANK_360
3. WATCH_CORE_ONLY_360
4. WATCH_RING_STRAP_ONLY_360
5. POWERBANK_ONLY_360
6. WATCH_SENSORS_ACTIVE_360

**Phase 2 - Important (Recommended):**
7. WATCH_FULL_ASSEMBLY_LOW_ANGLE_360
8. WATCH_FULL_ASSEMBLY_SIDE_CLOSEUP_360
9. STRAP_SENSORS_ACTIVE_360
10. COPPER_CONNECTORS_TOP_CLOSEUP

**Phase 3 - Nice to Have:**
11. WATCH_FULL_ASSEMBLY_HIGH_ANGLE_360
12. MAGNETIC_CONNECTORS_INSIDE_CLOSEUP
13. DISPLAY_SCREEN_CLOSEUP
14. BUTTON_SPEAKER_CLOSEUP

**Phase 4 - Advanced:**
15. WATCH_EXPLODED_ASSEMBLY_360
16. WATCH_ASSEMBLY_ANIMATION
17. WATCH_ON_WRIST_360

---

## ESTIMATED RENDER TIME & FILE COUNT

If using 72 frames per rotation:
- Phase 1: 6 renders × 72 frames = 432 images
- Phase 2: 4 renders × 36-72 frames = ~200 images
- Phase 3: 4 renders × 36 frames = 144 images
- Phase 4: 3 renders × 72-120 frames = ~250 images

**Total: ~1000 images for complete dataset**

For faster training start, use 36 frames per rotation:
- Phase 1: 6 renders × 36 frames = 216 images
- Phase 2: 4 renders × 36 frames = 144 images
**Total: ~360 images for core dataset**

---

## RECOMMENDATION

**Start with 36 frames (10° increments) for Phase 1:**
- Faster rendering
- Still captures all angles
- Good for initial LoRA training
- Can upgrade to 72 frames later if needed

**Use 72 frames for final production:**
- Smoother video generation
- Better T2V/I2V results
- More training data
- Higher quality outputs

