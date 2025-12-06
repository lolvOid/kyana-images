# Kyana Smartwatch - Physical Dimensions & Scale Reference

## Exact Product Dimensions

### Core Device (Watch Face Module)
```
┌─────────────────┐
│                 │
│   30mm × 30mm   │  ← Square face (fits inside ring)
│                 │
│   Thickness:    │
│      10mm       │
└─────────────────┘

LED Display (top surface)
Speaker: Left side
Button: Right side
Sensors: Bottom (8 LEDs in circular array)
```

### Ring Frame (Outer Housing)
```
┌─────────────────┐
│  ╔═══════════╗  │  ← Ring frame: 33mm × 33mm × 7mm
│  ║  CORE 30  ║  │     Holds 30mm core inside
│  ║   × 30    ║  │
│  ╚═══════════╝  │
└─────────────────┘

Inside: 4 magnetic connectors (holds 30mm core device)
Top Outside: 6 copper pins (for powerbank charging)
Sides: Strap attachment points
Overall: 33mm × 33mm × 7mm thick
```

### Powerbank Module
```
┌───────┐
│   8mm │  ← Compact cube
│  thick│
│       │
│ Green │  ← LED indicator
│  LED  │
│       │
│ USB-C │  ← Charging port
└───────┘

Attaches to strap via 6 copper pin connectors
Adds 8mm to total system
```

### Straps (When Laid Flat/Straightened)
```
Strap 1 (Short Side):
├─────────────────────┤  80mm (8cm)
[Clasp End]    [Connection to Ring]

Strap 2 (Long Side):
├─────────────────────────────────────┤  130mm (13cm)
[Connection to Ring]        [Clasp End]

Total Strap Length When Flat: 210mm (21cm)

Strap Features:
- 6 rectangular sensor windows on bottom
- Matte black silicone material
- Clasp mechanism for fastening
```

---

## Full Assembly Dimensions

### Flat Configuration (Straps Straightened)
```
        Strap 2 (130mm)           Strap 1 (80mm)
├─────────────────────────────┬─────┬──────────────────┤
                              │33mm │ ← Ring (33mm × 7mm)
                              │30mm │ ← Core (30mm × 10mm inside)
                        [Ring Frame]
                         [Core Device]
                              
Total Length: ~210mm + ring frame width
Center Device: Core 30mm × 30mm × 10mm inside Ring 33mm × 33mm × 7mm
Overall visible: 33mm × 33mm (ring exterior)
```

### With Powerbank
```
        Strap 2 (130mm)           Strap 1 (80mm)
├─────────────────────────────┬─────┬──────────────────┤
                    ┌──┐      │33mm │
                    │PB│      │     │        ← Powerbank (8mm)
                    └──┘[Ring Frame]
                         [Core Device]

Powerbank adds 8mm thickness to strap section
Total system includes all modular components
```

### Circular Configuration (Straps Curved)
```
         ┌───────────┐
      ╱               ╲
    ╱    [Core 33mm]   ╲
   │    [Ring Frame]    │  ← Strap forms circle
   │                    │     approximating wrist
    ╲                  ╱
      ╲               ╱
         └───────────┘

Strap curves to form wearable bracelet
Total circumference: ~210mm (adjustable via clasp)
```

---

## Scale Reference for Camera Setup

### Rule of Thumb for Camera Distance

**For objects to fill 70-80% of 1024×1024 frame:**

```
Camera Distance ≈ 2.5 to 3.0 × Object's Longest Dimension
```

### Applied to Kyana Components:

#### 1. Core Device Only (30mm)
```
Object Size: 30mm
Camera Distance: 70-90mm (≈2.5-3× size)
Result: Device fills 80-90% of frame
```

#### 2. Full Assembly with Straps (210mm length, 33mm width)
```
Object Size: ~210mm (strap length), 33mm width (ring exterior)
Camera Distance: 300-350mm (≈1.5-1.7× size for elongated object)
Result: Full watch fits with margins
Note: Straps are thin, so can be closer than 3× rule
```

#### 3. Powerbank Only (small cube, ~8mm)
```
Object Size: 8mm thickness
Camera Distance: 80-100mm (closer due to small size)
Result: Component visible with detail
```

#### 4. Detail Closeups (connector pins, sensors)
```
Object Size: 3-5mm features
Camera Distance: 50-70mm (macro range)
Result: Extreme closeup of small details
```

---

## Cinema 4D Scene Setup Guide

### Step 1: Set World Scale
```
In C4D Preferences:
- Units: Millimeters (mm)
- Grid: 10mm spacing
- Snap: 1mm precision
```

### Step 2: Position Components at Origin
```
Core Device: Place at (0, 0, 0)
- Size: 30mm × 30mm × 10mm
- Center pivot at device center

Ring Frame: Surrounds Core (when assembled)
- Size: 33mm × 33mm × 7mm
- Fits around 30mm core device
- 4 internal magnetic connectors hold core
- 6 copper pins on top exterior

Straps: Attach to ring frame sides
- When laid flat (for product shots):
  - Strap 1: Extends 80mm in one direction
  - Strap 2: Extends 130mm in opposite direction
- When curved (for wearable shots):
  - Form circular shape
  - Total circumference: 210mm
```

### Step 3: Camera Spline Setup
```
For Full Assembly Renders:
1. Create Circle Spline at (0, 0, 0)
2. Radius: 325mm (midpoint of 300-350mm)
3. Camera position on spline: 0-100%
4. Camera height: +30mm (mid-angle)
5. Camera "Look At" target: (0, 0, 0)

For Core Device Only:
1. Radius: 80mm (midpoint of 70-90mm)
2. Camera height: +10mm (proportional to smaller object)
3. All else same

For Closeups:
1. Radius: 60mm (midpoint of 50-70mm)
2. Camera height: +5mm to +10mm
3. May need tighter field of view (FOV: 25-30°)
```

### Step 4: Test Your Setup
```
1. Render frame 0 (front view)
2. Check framing:
   - Object fills 70-80% of frame? ✓
   - Too tight? Increase radius
   - Too loose? Decrease radius
3. Render frame 18 (side view at 180°)
4. Verify consistent framing throughout rotation
```

---

## Camera Distance Quick Reference Table

| Component Setup | Object Size | Camera Radius | Camera Height | FOV |
|----------------|-------------|---------------|---------------|-----|
| **Full Assembly Flat** | 210mm length, 33mm width | 300-350mm | +30-50mm | 36° |
| **Full Assembly Circular** | ~210mm circum | 300-350mm | +30-50mm | 36° |
| **Full + Powerbank** | 210mm + PB | 320-370mm | +30-50mm | 36° |
| **Core Device Only** | 30mm × 30mm × 10mm | 70-90mm | +10-15mm | 36° |
| **Ring Frame Only** | 33mm × 33mm × 7mm | 80-100mm | +10-15mm | 36° |
| **Powerbank Only** | 8mm thick | 70-90mm | +10-15mm | 36° |
| **Ring + Strap (no core)** | 210mm length, 33mm width | 300-350mm | +30-50mm | 36° |
| **Copper Pins Closeup** | 5mm features | 60-80mm | +50-80mm (high angle) | 30° |
| **Button/Speaker Detail** | 3mm features | 50-70mm | 0mm (eye-level) | 25° |
| **Display Screen Closeup** | 30mm screen | 50-70mm | +10mm | 30° |
| **Sensor Array Detail** | 10mm array | 60-80mm | -30-50mm (low angle) | 30° |

---

## Framing Tips

### Horizontal Orientation (Straps Extended Left-Right)
```
Best for: Full assembly shots showing complete strap length
Camera: Orbits around horizontal device
Result: Watch appears in typical product photography pose
```

### Vertical Orientation (Straps Extended Up-Down)
```
Best for: Showing watch "standing" or worn position
Camera: Orbits around vertical device
Result: Watch appears as if on wrist, portrait style
```

### Wearable Position (Straps Curved)
```
Best for: Lifestyle/context shots, realistic wearing
Camera: Orbits at slight angle to show curvature
Result: Natural wrist-worn appearance
```

---

## Common C4D Setup Issues & Solutions

### Issue: Device appears tiny in frame
```
Problem: Camera too far away
Solution: Reduce spline radius by 50%
Example: 350mm → 175mm
```

### Issue: Device appears huge, cropped
```
Problem: Camera too close
Solution: Increase spline radius by 50%
Example: 100mm → 150mm
```

### Issue: Straps cut off at edges
```
Problem: Radius calculated for device only, not full length
Solution: Use strap length (210mm) for calculation
Correct Distance: 300-350mm for full assembly
```

### Issue: Rotation looks jerky
```
Problem: Too few frames or easing applied
Solution: Use 36 frames minimum, LINEAR interpolation
Check: Frame 0 = 0%, Frame 35 = 100% on spline
```

### Issue: Details not visible in closeup
```
Problem: Camera too far or FOV too wide
Solution: 
- Reduce radius to 60-80mm
- Change FOV to 25-30° (narrower)
- Add depth of field for focus
```

---

## Validation Checklist

Before starting batch renders:

```
☐ World units set to millimeters
☐ Core device is 30mm × 30mm × 10mm in scene
☐ Ring frame is 33mm × 33mm × 7mm in scene
☐ Ring fits around 30mm core (3mm gap on each side)
☐ Strap total length is 210mm when flat
☐ Powerbank is 8mm thickness
☐ Camera spline radius matches object size
☐ Camera height appropriate for angle type
☐ Test render shows 70-80% frame fill
☐ Rotation is smooth (linear interpolation)
☐ All 36 frames animate correctly
☐ Lighting is consistent throughout rotation
```

---

## Export Settings Reminder

```
Resolution: 1024 × 1024
Format: PNG with Alpha
Frames: 0-35 (36 total)
Naming: [Component]_[Angle]_360_1024x1024_####.png
```

---

Perfect for printing or keeping open while setting up C4D! 📐

