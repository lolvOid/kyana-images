# Cinema 4D Quick Reference - Kyana Smartwatch Renders

## PRODUCT DIMENSIONS (Physical Specs)

```
Core Device:         30mm × 30mm × 10mm (1.0cm thick)
Outer Ring Frame:    33mm × 33mm × 7mm (0.7cm thick)
Powerbank:           8mm (0.8cm thick)
Strap 1 (short):     80mm (8cm) when straightened
Strap 2 (long):      130mm (13cm) when straightened
Total strap flat:    210mm (21cm)
Full device assembled: 33mm outer (ring), 30mm core inside
```

---

## Quick Setup Checklist

### 1. Scene Setup (Do Once)
```
☐ Create circular spline at origin (0,0,0)
☐ Set spline radius to match distance needed
☐ Create camera
☐ Add camera to spline (Align to Spline tag)
☐ Set device at world origin
☐ Test 0-35 frame animation
```

### 2. Camera Spline Radius by Render Type
```
Full Assembly (with straps):  300-350mm radius
Core Device Only (30mm):      70-90mm radius  
Ring Frame Only (33mm):       80-100mm radius
Powerbank Only (8mm):         70-90mm radius
Closeups:                     50-70mm radius
```

### 3. Camera Heights (Y-Position)
```
MID-ANGLE:     +30mm to +50mm (most renders)
EYE-LEVEL:     0mm (side details)
LOW ANGLE:     -40mm (sensors)
HIGH ANGLE:    +100mm (top view)
```

## Render Settings Copy-Paste

### Output Settings
```
Resolution: 1024 x 1024
Format: PNG
Alpha Channel: Yes
Color Depth: 8-bit
Frame Range: 0-35
Frame Step: 1
```

### Quality Settings
```
Anti-Aliasing: Best (16x)
Filter: Mitchell
Global Illumination: On
Ambient Occlusion: On (if needed)
```

## Naming Convention

### Format:
```
[COMPONENT]_[VARIANT]_[ANGLE]_360_1024x1024_####
```

### Examples:
```
FULL_ASSEMBLY_FLAT_MID_360_1024x1024_0000.png
POWERBANK_ONLY_MID_360_1024x1024_0000.png
CORE_DEVICE_SENSORS_ON_LOW_360_1024x1024_0000.png
```

## Animation Keyframes

### 360° Rotation (36 frames)
```
Frame 0:  Camera Position = 0% on spline
Frame 35: Camera Position = 100% on spline
Interpolation: Linear
```

### Assembly Animation (120 frames)
```
Frame 0-30:    Strap on surface
Frame 31-50:   Ring descends
Frame 51-80:   Core device descends and snaps
Frame 81-100:  Powerbank slides in
Frame 101-120: Gentle final rotation
```

## Component Visibility Layers

### Create These Layers:
```
LAYER 1: OUTER_RING
LAYER 2: CORE_DEVICE
LAYER 3: STRAP_FLAT
LAYER 4: STRAP_CIRCULAR
LAYER 5: POWERBANK
LAYER 6: SENSORS_LIGHTS
```

### Quick Toggle for Renders:
```
Full Assembly Flat:     1 + 2 + 3
Full Assembly Circular: 1 + 2 + 4
Ring Only:              1
Core Only:              2
With Powerbank:         1 + 2 + 3 + 5
Sensors Active:         Enable LAYER 6
```

## Lighting Setup

### Standard Product Lighting:
```
KEY LIGHT:  Front-right, 60° angle, 100% intensity
FILL LIGHT: Front-left, 40° angle, 40% intensity  
RIM LIGHT:  Back-top, 70° angle, 60% intensity
GROUND:     Below, soft diffused, 20% intensity
```

### Sensor Active Lighting:
```
Add emissive materials to sensor LEDs
Green LEDs: RGB (0, 255, 100), Luminance 150%
Red LEDs:   RGB (255, 50, 50), Luminance 150%
```

## Material Quick Settings

### Core Device Display:
```
Surface: Glossy Black
Reflection: 80%
Specular: High
Clearcoat: On
```

### Ring Frame:
```
Surface: Matte Black
Reflection: 20%
Metal Pins: Copper material
```

### Strap:
```
Surface: Silicone shader
Reflection: 10%
Subsurface: Subtle
Color: Black RGB (20, 20, 20)
```

### Powerbank:
```
Surface: Matte Black plastic
LED: Green emissive material
USB-C Port: Dark grey metal
```

## Batch Render Order

### Day 1 - Phase 1 (Essential):
```
1. FULL_ASSEMBLY_FLAT_MID_360
2. FULL_WITH_POWERBANK_FLAT_MID_360
3. CORE_DEVICE_ONLY_MID_360
4. POWERBANK_ONLY_MID_360
5. RING_STRAP_FLAT_MID_360
```

### Day 2 - Phase 2 (Sensors):
```
6. FULL_ASSEMBLY_FLAT_SENSORS_ON_LOW_360
7. FULL_ASSEMBLY_FLAT_SENSORS_OFF_LOW_360
8. CORE_DEVICE_SENSORS_ON_LOW_360
9. STRAP_FLAT_SENSORS_ON_LOW_360
```

### Day 3 - Phase 1B (Circular):
```
10. FULL_ASSEMBLY_CIRCULAR_MID_360
11. FULL_WITH_POWERBANK_CIRCULAR_MID_360
12. FULL_ASSEMBLY_CIRCULAR_SENSORS_ON_LOW_360
```

## Troubleshooting

### Camera moves but view is wrong:
```
✓ Check "Align to Spline" tag is enabled
✓ Verify spline is circular and centered at origin
✓ Camera should point toward origin (0,0,0)
```

### Device not centered in frame:
```
✓ Adjust camera distance (spline radius)
✓ Check camera's "Look at" target is at origin
✓ Verify device is exactly at world origin
```

### Rotation not smooth:
```
✓ Set interpolation to LINEAR (no easing)
✓ Check keyframes at Frame 0 and Frame 35 only
✓ Verify camera moves from 0% to 100% on spline
```

### Alpha channel not working:
```
✓ Enable "Alpha Channel" in render settings
✓ Set background to transparent (not white)
✓ Save as PNG (not JPG)
```

## Performance Tips

### For Faster Test Renders:
```
- Use 18 frames (20° per frame) for preview
- Reduce resolution to 512x512 for tests
- Turn off Global Illumination for tests
- Use "Quick" anti-aliasing preset
```

### For Final Quality:
```
- Use full 36 frames (10° per frame)
- Full 1024x1024 resolution
- Enable all lighting features
- "Best" anti-aliasing preset
- Render overnight/in background
```

## File Organization

### Create These Folders:
```
/RENDERS/
  /PHASE_1_ESSENTIAL/
  /PHASE_2_SENSORS/
  /PHASE_3_DETAILS/
  /PHASE_4_ANIMATION/
  /TEST_RENDERS/
```

### Backup Strategy:
```
After each phase completion:
- Copy renders to external drive
- ZIP completed phase folders
- Keep C4D project file versions
```

## Time Estimates

### Per 36-frame sequence:
```
Simple component: 10-20 minutes
Full assembly:    20-40 minutes
Closeup detail:   15-30 minutes
```

### Total Phase 1: ~3-4 hours
### Total Phase 2: ~2-3 hours
### Total Phase 3: ~3-4 hours

