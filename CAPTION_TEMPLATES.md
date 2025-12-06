# Caption Templates for Kyana Smartwatch LoRA Training

## Auto-Caption Format

After rendering, create .txt files matching each .png filename with these caption templates:

---

## PHASE 1 - Full Assembly

### FULL_ASSEMBLY_FLAT_MID_360_1024x1024_####.txt
```
Kyana health smartwatch 33mm square design, complete assembly with core device, black ring frame, and flat black silicone strap, [ANGLE]° rotation view, glossy LED display screen, modular watch system, product photography
```

**Angle calculation**: `ANGLE = frame_number × 10`
- Frame 0 = 0°
- Frame 18 = 180°
- Frame 35 = 350°

### FULL_ASSEMBLY_CIRCULAR_MID_360_1024x1024_####.txt
```
Kyana smartwatch 33mm with circular strap design, complete assembly with core device, black ring frame, and curved black strap, [ANGLE]° rotation, glossy display, modular system
```

### FULL_WITH_POWERBANK_FLAT_MID_360_1024x1024_####.txt
```
Kyana smartwatch 33mm square with powerbank module attached, complete system with core device, ring, flat strap, and black battery accessory, [ANGLE]° view, green LED indicator active, modular charging system
```

### FULL_WITH_POWERBANK_CIRCULAR_MID_360_1024x1024_####.txt
```
Kyana smartwatch with powerbank and circular strap, full assembly with battery module on strap, [ANGLE]° rotation, green LED indicator visible, extended battery system
```

### CORE_DEVICE_ONLY_MID_360_1024x1024_####.txt
```
Kyana smartwatch core device standalone, 33mm square black case with glossy LED display screen, speaker grille on left side, physical button on right side, [ANGLE]° view, detachable core module
```

### POWERBANK_ONLY_MID_360_1024x1024_####.txt
```
Kyana smartwatch powerbank module, compact black cube battery accessory with rounded edges, green LED status indicator, USB-C charging port, [ANGLE]° rotation, modular power system
```

### RING_STRAP_FLAT_MID_360_1024x1024_####.txt
```
Kyana smartwatch ring frame with flat black strap, no core device, hollow square center, 4 copper magnetic connectors inside ring, 6 copper pins on top, [ANGLE]° view, modular attachment system
```

---

## PHASE 2 - Sensor States

### FULL_ASSEMBLY_FLAT_SENSORS_ON_LOW_360_1024x1024_####.txt
```
Kyana smartwatch 33mm from low angle, complete assembly with active biometric sensors, green and red LED lights glowing on bottom sensor array, strap sensors illuminated green, [ANGLE]° rotation, health monitoring active
```

### FULL_ASSEMBLY_CIRCULAR_SENSORS_ON_LOW_360_1024x1024_####.txt
```
Kyana smartwatch circular design low angle view, active biometric sensors visible, green LED photodiodes and red LEDs glowing, circular sensor array on device bottom, [ANGLE]° view, monitoring mode active
```

### FULL_ASSEMBLY_FLAT_SENSORS_OFF_LOW_360_1024x1024_####.txt
```
Kyana smartwatch from low angle, complete assembly with inactive sensors, all LEDs off, copper sensor contacts visible in silver/grey, [ANGLE]° rotation, standby mode
```

### CORE_DEVICE_SENSORS_ON_LOW_360_1024x1024_####.txt
```
Kyana core device bottom view with active sensors, circular biometric sensor array with green and red LED lights illuminated, 33mm device, [ANGLE]° rotation, optical heart rate monitoring active
```

### STRAP_FLAT_SENSORS_ON_LOW_360_1024x1024_####.txt
```
Kyana smartwatch flat strap bottom view, 6 rectangular sensor windows with active green LED indicators, black silicone material, sensor array illuminated, [ANGLE]° view, health tracking sensors
```

---

## PHASE 3 - Detail Shots

### COPPER_PINS_TOP_HIGH_360_1024x1024_####.txt
```
Kyana smartwatch ring frame top view closeup, 6 golden copper charging pins visible on top edge, spring-loaded magnetic connectors, precision engineering detail, [ANGLE]° rotation, powerbank connection interface
```

### MAGNETIC_CONNECTORS_INSIDE_HIGH_360_1024x1024_####.txt
```
Kyana smartwatch ring frame interior closeup, 4 copper magnetic connectors inside hollow square frame, golden pins for core device attachment, [ANGLE]° view, modular magnetic system detail
```

### BUTTON_SPEAKER_DETAIL_FLAT_360_1024x1024_####.txt
```
Kyana smartwatch core device side profile extreme closeup, physical button on right side with red accent, speaker grille slots on left side, glossy black finish, [ANGLE]° rotation, side detail view
```

### CLASP_MECHANISM_DETAIL_FLAT_360_1024x1024_####.txt
```
Kyana smartwatch strap clasp mechanism closeup, black silicone strap with metal pin fastening system, adjustment holes visible, secure closure detail, [ANGLE]° view, strap connection system
```

### DISPLAY_SCREEN_CLOSEUP_MID_360_1024x1024_####.txt
```
Kyana smartwatch display screen extreme closeup, 33mm square glossy LED screen with curved edges, reflective black surface, rounded corners, premium finish detail, [ANGLE]° rotation
```

---

## PHASE 4 - Animations

### ASSEMBLY_ANIMATION_FLAT_1024x1024_####.txt

**Frames 0-30:**
```
Kyana smartwatch flat black silicone strap laid on surface, beginning of assembly sequence, modular watch system components
```

**Frames 31-50:**
```
Kyana smartwatch ring frame descending toward strap, black square ring with copper connectors, assembly process in progress
```

**Frames 51-80:**
```
Kyana smartwatch core device 33mm descending into ring frame, magnetic connection engaging, LED display visible, assembly sequence
```

**Frames 81-100:**
```
Kyana smartwatch powerbank module sliding onto strap from side, battery accessory connecting to copper pins, green LED activating, final assembly stage
```

**Frames 101-120:**
```
Kyana smartwatch complete assembly rotating gently, full system with core, ring, strap and powerbank, [ANGLE]° rotation, finished product view
```

### DISASSEMBLY_ANIMATION_FLAT_1024x1024_####.txt
```
Kyana smartwatch disassembly sequence, complete watch separating into modular components, frame [####] of teardown animation, product demonstration
```

### EXPLODED_VIEW_360_1024x1024_####.txt
```
Kyana smartwatch exploded view, all components separated vertically, core device floating above ring frame, ring above strap, powerbank below, [ANGLE]° orbital rotation, modular system visualization
```

---

## Caption Variables Quick Reference

### Angles (for 36-frame renders):
```
Frame 00 = 0°     Frame 13 = 130°   Frame 26 = 260°
Frame 01 = 10°    Frame 14 = 140°   Frame 27 = 270°
Frame 02 = 20°    Frame 15 = 150°   Frame 28 = 280°
Frame 03 = 30°    Frame 16 = 160°   Frame 29 = 290°
Frame 04 = 40°    Frame 17 = 170°   Frame 30 = 300°
Frame 05 = 50°    Frame 18 = 180°   Frame 31 = 310°
Frame 06 = 60°    Frame 19 = 190°   Frame 32 = 320°
Frame 07 = 70°    Frame 20 = 200°   Frame 33 = 330°
Frame 08 = 80°    Frame 21 = 210°   Frame 34 = 340°
Frame 09 = 90°    Frame 22 = 220°   Frame 35 = 350°
Frame 10 = 100°   Frame 23 = 230°
Frame 11 = 110°   Frame 24 = 240°
Frame 12 = 120°   Frame 25 = 250°
```

### Essential Keywords (always include):
- "Kyana smartwatch" or "Kyana health smartwatch"
- "33mm" (device size)
- "black" (color)
- Component specifics (core, ring, strap, powerbank)
- Angle in degrees
- Key features visible in that frame

### Optional Descriptors (add when relevant):
- "modular system"
- "glossy LED display"
- "copper connectors/pins"
- "biometric sensors"
- "green LED" or "red LED"
- "silicone strap"
- "magnetic attachment"
- "product photography"
- "health monitoring"

---

## Python Script to Auto-Generate Captions

Save this as `generate_captions.py`:

```python
import os
from pathlib import Path

def generate_angle_caption(base_caption, frame_num, total_frames=36):
    angle = int(frame_num * (360 / total_frames))
    return base_caption.replace('[ANGLE]', str(angle))

# Define base captions
captions_template = {
    'FULL_ASSEMBLY_FLAT_MID_360': 
        "Kyana health smartwatch 33mm square design, complete assembly with core device, black ring frame, and flat black silicone strap, [ANGLE]° rotation view, glossy LED display screen, modular watch system",
    
    'CORE_DEVICE_ONLY_MID_360':
        "Kyana smartwatch core device standalone, 33mm square black case with glossy LED display screen, speaker grille on left side, physical button on right side, [ANGLE]° view, detachable core module",
    
    # Add more templates here...
}

# Auto-generate caption files
def create_caption_files(render_name, frames=36):
    base = captions_template.get(render_name)
    if not base:
        print(f"No template for {render_name}")
        return
    
    for frame in range(frames):
        filename = f"{render_name}_1024x1024_{frame:04d}.txt"
        caption = generate_angle_caption(base, frame, frames)
        
        with open(filename, 'w') as f:
            f.write(caption)
        
        print(f"Created: {filename}")

# Usage:
# create_caption_files('FULL_ASSEMBLY_FLAT_MID_360', 36)
```

---

## Manual Caption Checklist

When writing captions manually:

✅ Product name: "Kyana smartwatch" or "Kyana health smartwatch"
✅ Size: "33mm"
✅ Components visible: core/ring/strap/powerbank
✅ Angle: rotation degree
✅ Key features: display, sensors, LEDs, connectors
✅ Material: black, silicone, glossy, copper
✅ State: sensors on/off, LED indicators
✅ Style: modular system, product photography

❌ Avoid:
- Overly long captions (keep under 75 words)
- Vague descriptions
- Inconsistent terminology
- Missing angle information
- Generic phrases without specifics

