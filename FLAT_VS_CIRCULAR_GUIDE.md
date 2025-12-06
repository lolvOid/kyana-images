# Kyana Smartwatch - FLAT vs CIRCULAR Configuration Guide

## Two Main Rendering Configurations

You'll be rendering the watch in **TWO different strap configurations**:

---

## 📐 CONFIGURATION 1: FLAT/STRAIGHTENED (Product Photography)

### Description:
Straps are laid out straight, extended horizontally from the device like a typical product photo.

### Visual Layout:
```
    Strap 2 (130mm)         Device (33mm)         Strap 1 (80mm)
├─────────────────────────┼─────────┼────────────────────┤
                          │  ████   │
                          │  CORE   │
                          │  ████   │
                          └─────────┘
                         Ring + Straps

Total length: ~210mm when fully extended
```

### Camera Distance:
- **300-350mm** from center
- Captures full 210mm length plus margins

### Use Cases:
- ✅ Product photography (e-commerce, catalog)
- ✅ Technical specifications display
- ✅ Component showcase
- ✅ Detail views of sensors, connectors
- ✅ Professional marketing materials

### Best Angles:
- MID: Standard product view
- LOW: Show bottom sensors clearly
- HIGH: Display top copper connectors
- EYE-LEVEL: Side profile, button/speaker details

### Render Names:
```
FULL_ASSEMBLY_FLAT_MID_360
FULL_WITH_POWERBANK_FLAT_MID_360
RING_STRAP_FLAT_MID_360
STRAP_FLAT_SENSORS_ON_LOW_360
```

---

## 🔄 CONFIGURATION 2: CIRCULAR/CURVED (Lifestyle/Wearable)

### Description:
Straps are curved to form a circular bracelet shape, simulating how it looks when worn on a wrist.

### Visual Layout:
```
         ┌─────────────┐
      ╱                 ╲
    ╱       ████          ╲
   │       CORE            │  ← Strap curves to form
   │       ████            │     circular bracelet
   │    Ring + Straps      │
    ╲                     ╱
      ╲                 ╱
         └─────────────┘

Diameter: ~60-70mm (wrist-sized circle)
Circumference: 210mm (same total length)
```

### Camera Distance:
- **180-220mm** from center
- More compact, circular form fits in frame

### Use Cases:
- ✅ Lifestyle photography
- ✅ Wrist-worn appearance
- ✅ Realistic product context
- ✅ User experience visualization
- ✅ Social media content
- ✅ Marketing campaigns showing "how it looks worn"

### Best Angles:
- MID: Slightly elevated to show curve
- 3/4 VIEW: Angled to emphasize circular form
- Rotate to show all sides of bracelet

### Render Names:
```
FULL_ASSEMBLY_CIRCULAR_MID_360
FULL_WITH_POWERBANK_CIRCULAR_MID_360
RING_STRAP_CIRCULAR_MID_360
FULL_ASSEMBLY_CIRCULAR_SENSORS_ON_LOW_360
```

---

## 🎯 Key Differences Summary

| Aspect | FLAT Configuration | CIRCULAR Configuration |
|--------|-------------------|----------------------|
| **Strap Position** | Straightened, extended | Curved to form circle |
| **Total Length** | ~210mm linear | ~60-70mm diameter |
| **Camera Distance** | 300-350mm | 180-220mm |
| **Frame Composition** | Horizontal, wide | Compact, round |
| **Purpose** | Product showcase | Lifestyle/context |
| **Viewing Style** | Technical, clean | Natural, wearable |
| **Best For** | E-commerce, specs | Marketing, social media |

---

## 📋 When to Use Each Configuration

### Use FLAT for:
1. **Technical documentation**
   - Showing all components clearly
   - Displaying dimensions and scale
   - Highlighting specific features

2. **E-commerce product pages**
   - Clean, professional product shots
   - Multiple angles of device
   - Detail views of sensors, connectors

3. **Training data (LoRA)**
   - Clear component identification
   - Consistent framing
   - Technical accuracy

4. **Assembly demonstrations**
   - Showing how parts connect
   - Component separation
   - Modular system explanation

### Use CIRCULAR for:
1. **Marketing campaigns**
   - Lifestyle imagery
   - User experience focus
   - Emotional connection

2. **Social media content**
   - Instagram/Facebook posts
   - Promotional materials
   - Influencer content

3. **App/website heroes**
   - Landing page imagery
   - Hero banners
   - Lifestyle sections

4. **Context shots**
   - "In use" scenarios
   - Wrist-worn appearance
   - Realistic product visualization

---

## 🎬 Rendering Priority

### Phase 1 Priority (Start Here):
**FLAT Configuration First:**
```
1. FULL_ASSEMBLY_FLAT_MID_360          ← Start with this
2. FULL_WITH_POWERBANK_FLAT_MID_360
3. CORE_DEVICE_ONLY_MID_360
4. RING_STRAP_FLAT_MID_360
5. POWERBANK_ONLY_MID_360
```
**Why FLAT first?**
- Easier to set up in C4D
- Better for training data (clear component views)
- Essential for technical documentation

### Phase 1B (Add Circular):
**CIRCULAR Configuration:**
```
6. FULL_ASSEMBLY_CIRCULAR_MID_360
7. FULL_WITH_POWERBANK_CIRCULAR_MID_360
```
**Why add CIRCULAR?**
- More natural, realistic appearance
- Better for marketing materials
- Shows wearable context

---

## 🔧 C4D Setup Differences

### FLAT Configuration Setup:
```
Strap 1 & 2:
- Position: Extended horizontally from ring
- Rotation: 0° (straight)
- Layout: Linear along X-axis
- Strap 1: +X direction (80mm)
- Strap 2: -X direction (130mm)

Camera:
- Spline radius: 325mm (midpoint of 300-350mm)
- Height: +30-50mm (mid-angle)
- FOV: 36°
```

### CIRCULAR Configuration Setup:
```
Strap 1 & 2:
- Position: Curved around device center
- Rotation: Follow circular spline or bend deformer
- Layout: Form closed loop/bracelet
- Diameter: 60-70mm
- Circumference: 210mm (same total length)

Camera:
- Spline radius: 200mm (midpoint of 180-220mm)
- Height: +30-50mm (mid-angle)
- FOV: 36°
- Slight tilt to emphasize curve
```

---

## 💡 Pro Tips

### For FLAT Renders:
```
✓ Keep straps perfectly horizontal for consistency
✓ Use grid snap to ensure straight alignment
✓ Center device at world origin (0,0,0)
✓ Equal spacing on both sides for balance
✓ Great for showing strap length and clasp detail
```

### For CIRCULAR Renders:
```
✓ Use spline wrap or bend deformer for smooth curve
✓ Ensure circle is centered at device
✓ Maintain 210mm total circumference
✓ Adjust camera angle slightly (not pure top-down)
✓ Show natural bracelet form
✓ Great for demonstrating wearability
```

---

## 📊 Training Data Recommendation

### For LoRA Training:
**Ratio: 70% FLAT / 30% CIRCULAR**

**Why this ratio?**
- FLAT provides clearer component learning
- FLAT shows technical details better
- CIRCULAR adds context and variation
- Mix ensures versatility in generation

**Example Split:**
```
Phase 1: 7 FLAT renders + 2 CIRCULAR renders
Phase 2: 4 FLAT renders + 1 CIRCULAR render
Total: 11 FLAT + 3 CIRCULAR = ~75% / 25% ratio
```

---

## ✅ Quick Decision Guide

**Ask yourself: What's the primary use?**

```
Need technical specs?          → FLAT
Need e-commerce photos?        → FLAT
Need assembly instructions?    → FLAT
Need sensor detail views?      → FLAT
Need connector closeups?       → FLAT

Need marketing imagery?        → CIRCULAR
Need lifestyle photos?         → CIRCULAR
Need "worn" appearance?        → CIRCULAR
Need social media content?     → CIRCULAR
Need emotional appeal?         → CIRCULAR

Need complete dataset?         → BOTH (70% FLAT, 30% CIRCULAR)
```

---

## 🎯 Final Recommendation

**Start with FLAT configuration** to build your core dataset:
- Easier to set up
- Better training data clarity
- Essential for product specs

**Add CIRCULAR later** for variety and context:
- Enhances visual appeal
- Shows realistic use case
- Improves marketing potential

**Both configurations use the same core workflow**, just different strap positions and camera distances! 🚀

