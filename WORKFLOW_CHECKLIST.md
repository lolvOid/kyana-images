# Kyana Smartwatch - Complete Workflow Checklist

## 📋 Overview

This is your master checklist for rendering and training the Kyana Smartwatch LoRA model.

---

## ✅ Phase 1: Pre-Production Setup

### Cinema 4D Scene Preparation
```
☐ Open C4D project with all components
☐ Create circular spline at world origin (0,0,0)
☐ Set up camera on spline with "Align to Spline" tag
☐ Test camera animation (0-35 frames = 360°)
☐ Set up component layers for easy toggling
☐ Configure lighting (key, fill, rim)
☐ Set up materials (glossy display, matte strap, copper pins)
☐ Create sensor emissive materials (green/red LEDs)
```

### Render Settings Configuration
```
☐ Resolution: 1024 x 1024
☐ Format: PNG with Alpha
☐ Frame Range: 0-35 (36 frames)
☐ Anti-aliasing: Best quality
☐ Output path: Set naming convention
☐ Test render 1 frame to verify setup
```

---

## ✅ Phase 2: Rendering (Week 1-2)

### Day 1-2: Essential Product Renders (Phase 1)
```
☐ FULL_ASSEMBLY_FLAT_MID_360 (36 frames)
   - Camera: Mid-angle (+30-50mm height)
   - Distance: 150-200mm
   - Components: Core + Ring + Flat Strap

☐ FULL_WITH_POWERBANK_FLAT_MID_360 (36 frames)
   - Add powerbank to strap
   - Ensure green LED is visible

☐ CORE_DEVICE_ONLY_MID_360 (36 frames)
   - Hide all except core device
   - Distance: 100-120mm (closer)

☐ POWERBANK_ONLY_MID_360 (36 frames)
   - Only powerbank visible
   - Show USB-C port and LED

☐ RING_STRAP_FLAT_MID_360 (36 frames)
   - Ring + Strap, no core device
   - Show empty center with connectors

☐ FULL_ASSEMBLY_CIRCULAR_MID_360 (36 frames)
   - Switch to circular strap variant

☐ FULL_WITH_POWERBANK_CIRCULAR_MID_360 (36 frames)
   - Circular strap + powerbank
```

**Expected Output:** ~252 images

### Day 3: Sensor State Renders (Phase 2)
```
☐ FULL_ASSEMBLY_FLAT_SENSORS_ON_LOW_360 (36 frames)
   - Camera: LOW angle (-40mm height)
   - Sensors: Green/Red LEDs ON
   - Clear view of bottom sensor array

☐ FULL_ASSEMBLY_FLAT_SENSORS_OFF_LOW_360 (36 frames)
   - Same setup, all LEDs OFF

☐ CORE_DEVICE_SENSORS_ON_LOW_360 (36 frames)
   - Core only, low angle
   - Bottom sensors active

☐ STRAP_FLAT_SENSORS_ON_LOW_360 (36 frames)
   - Strap sensors (6 windows) active

☐ FULL_ASSEMBLY_CIRCULAR_SENSORS_ON_LOW_360 (36 frames)
   - Circular strap with active sensors
```

**Expected Output:** ~180 images

### Day 4 (Optional): Detail Renders (Phase 3)
```
☐ COPPER_PINS_TOP_HIGH_360 (36 frames)
   - Camera: HIGH angle (+100mm)
   - Distance: 120mm closeup
   - Focus: 6 copper pins on top

☐ BUTTON_SPEAKER_DETAIL_FLAT_360 (36 frames)
   - Camera: EYE-LEVEL (0mm height)
   - Distance: 80-100mm extreme closeup
   - Focus: Button right, speaker left

☐ DISPLAY_SCREEN_CLOSEUP_MID_360 (36 frames)
   - Very close to display
   - Show glossy screen detail

☐ CLASP_MECHANISM_DETAIL_FLAT_360 (36 frames)
   - Strap clasp closeup

☐ MAGNETIC_CONNECTORS_INSIDE_HIGH_360 (36 frames)
   - Inside ring view
   - 4 internal magnetic pins
```

**Expected Output:** ~180 images

### Day 5 (Advanced): Animation Renders (Phase 4)
```
☐ ASSEMBLY_ANIMATION_FLAT (120 frames)
   - Camera: STATIC (not rotating)
   - Animate components assembling
   - Frame 0-30: Strap on surface
   - Frame 31-50: Ring descends
   - Frame 51-80: Core snaps in
   - Frame 81-100: Powerbank slides on
   - Frame 101-120: Gentle rotation

☐ EXPLODED_VIEW_360 (36 frames)
   - All components separated vertically
   - Camera orbits around
   - 50mm spacing between parts

☐ DISASSEMBLY_ANIMATION_FLAT (120 frames)
   - Reverse of assembly
```

**Expected Output:** ~276 images

---

## ✅ Phase 3: Post-Production (Week 2)

### Day 6: Organization & Verification
```
☐ Create folder structure:
   /renders/phase_1_essential/
   /renders/phase_2_sensors/
   /renders/phase_3_details/
   /renders/phase_4_animation/

☐ Move rendered PNGs to appropriate folders

☐ Verify all renders:
   - Check resolution (1024x1024)
   - Check for black/corrupted frames
   - Verify smooth rotation sequences
   - Count total images per phase

☐ Backup all renders to external drive
```

### Day 7: Caption Generation
```
☐ Read CAPTION_TEMPLATES.md

☐ For each PNG file, create matching .txt file

☐ Use caption templates with correct angles:
   - Frame 0 = 0°
   - Frame 18 = 180°
   - Frame 35 = 350°

☐ Verify every PNG has matching TXT:
   FULL_ASSEMBLY_FLAT_MID_360_1024x1024_0000.png
   FULL_ASSEMBLY_FLAT_MID_360_1024x1024_0000.txt

☐ Quality check captions:
   - Include "Kyana smartwatch"
   - Include "33mm"
   - Include angle in degrees
   - Include visible components
   - Consistent terminology

☐ Total caption files should match PNG count
```

---

## ✅ Phase 4: Training Setup (Week 3)

### Day 8: Prepare Training Environment
```
☐ Install AI-Toolkit or Wan2.2 framework

☐ Download FLUX.1-dev base model

☐ Verify GPU requirements:
   - VRAM: 24GB+ recommended
   - CUDA enabled
   - Drivers up to date

☐ Create training folders:
   /output/kyana_lora_v1/
   /logs/

☐ Copy config files from TRAINING_SETUP_GUIDE.md
```

### Day 9-10: Train Core Product LoRA (FLUX)
```
☐ Dataset: Phase 1 + Phase 2 (~400 images)

☐ Configure training:
   - Steps: 3000
   - Learning rate: 1e-4
   - Batch size: 1
   - LoRA rank: 16

☐ Start training (6-8 hours)

☐ Monitor progress via tensorboard

☐ Save checkpoints every 100 steps
```

### Day 11: Test & Evaluate
```
☐ Generate test images with prompts:
   "Kyana smartwatch 33mm rotating view"
   "Kyana smartwatch with powerbank, green LED"
   "Kyana smartwatch bottom view, sensors active"

☐ Evaluate quality:
   - Proportions accurate?
   - Components correct?
   - Details clear?
   - Colors consistent?

☐ If good: Proceed to next stage
☐ If poor: Adjust settings, retrain
```

### Day 12-14: Train T2V (Optional)
```
☐ Use Phase 1+2 rotation sequences

☐ Train Text-to-Video model:
   - Steps: 3000
   - Frames: 36
   - Motion: rotation

☐ Test video generation:
   "Kyana smartwatch rotating 360 degrees"

☐ Evaluate motion smoothness
```

---

## ✅ Phase 5: Optimization & Iteration

### If Results Need Improvement:
```
☐ Identify issues:
   - Proportions wrong?
   - Missing details?
   - Wrong colors?
   - Poor video motion?

☐ Re-render problematic angles:
   - Adjust camera distance
   - Improve lighting
   - Check material settings

☐ Add more training data:
   - More angles
   - More closeups
   - Better sensor visibility

☐ Adjust training parameters:
   - Increase steps
   - Lower learning rate
   - Change LoRA rank

☐ Retrain with improvements
```

---

## 📊 Progress Tracking

### Rendering Progress
```
Phase 1 Essential:   [ ] 0/252 images (7 renders × 36 frames)
Phase 2 Sensors:     [ ] 0/180 images (5 renders × 36 frames)
Phase 3 Details:     [ ] 0/180 images (5 renders × 36 frames)
Phase 4 Animation:   [ ] 0/276 images (3 renders × 36-120 frames)

Total Target: ~888 images
Current: ___ images complete
```

### Caption Progress
```
Phase 1 Captions:    [ ] 0/252 .txt files
Phase 2 Captions:    [ ] 0/180 .txt files
Phase 3 Captions:    [ ] 0/180 .txt files
Phase 4 Captions:    [ ] 0/276 .txt files

Total: ___/888 caption files complete
```

### Training Progress
```
FLUX LoRA Core:      [ ] Not Started [ ] Training [ ] Complete
FLUX LoRA Details:   [ ] Not Started [ ] Training [ ] Complete
Wan2.2 T2V:          [ ] Not Started [ ] Training [ ] Complete
Wan2.2 I2V:          [ ] Not Started [ ] Training [ ] Complete
```

---

## 📁 File Organization

### Your Project Should Look Like This:
```
/kyana-images/
  ├── RENDER_PLAN_C4D.md
  ├── C4D_QUICK_REFERENCE.md
  ├── CAPTION_TEMPLATES.md
  ├── TRAINING_SETUP_GUIDE.md
  ├── WORKFLOW_CHECKLIST.md (this file)
  │
  ├── /renders/
  │   ├── /phase_1_essential/
  │   │   ├── FULL_ASSEMBLY_FLAT_MID_360_1024x1024_0000.png
  │   │   ├── FULL_ASSEMBLY_FLAT_MID_360_1024x1024_0000.txt
  │   │   └── ... (252 image + txt pairs)
  │   ├── /phase_2_sensors/
  │   │   └── ... (180 image + txt pairs)
  │   ├── /phase_3_details/
  │   │   └── ... (180 image + txt pairs)
  │   └── /phase_4_animation/
  │       └── ... (276 image + txt pairs)
  │
  ├── /configs/
  │   ├── config_ai_toolkit_kyana.yaml
  │   └── config_wan22_kyana.yaml
  │
  ├── /output/
  │   ├── /kyana_lora_v1/
  │   └── /kyana_t2v_v1/
  │
  └── /tests/
      ├── test_prompts.txt
      └── /test_outputs/
```

---

## 🎯 Success Criteria

### Minimum Viable Dataset (Start Training):
```
✅ Phase 1 Complete: 252 images with captions
✅ Phase 2 Complete: 180 images with captions
✅ All images 1024x1024 PNG
✅ All captions include key info (name, size, angle, components)
✅ Quality checked: no corrupted frames

Total: ~400 images minimum to start training
```

### Complete Dataset (Best Results):
```
✅ All 4 Phases Complete: ~888 images with captions
✅ Multiple camera angles per component
✅ Sensor states (on/off) covered
✅ Detail closeups included
✅ Animation sequences rendered

Total: 888 images for comprehensive training
```

### Trained Model Quality:
```
✅ Can generate Kyana smartwatch from text
✅ Correct proportions (33mm square)
✅ Accurate component placement
✅ Can toggle sensors on/off
✅ Can add/remove powerbank
✅ Multiple viewing angles work
✅ Details are clear (connectors, button, etc.)
✅ (Optional) Can generate rotation videos
```

---

## 🚀 Quick Start (If Starting Fresh Today)

### Priority for This Week:
1. **Today**: Set up C4D, test render 1 sequence (36 frames)
2. **Tomorrow**: Render Phase 1 Essential (252 images)
3. **Day 3**: Render Phase 2 Sensors (180 images)
4. **Day 4**: Generate all 432 caption files
5. **Day 5**: Train FLUX LoRA (3000 steps)
6. **Weekend**: Test and evaluate results

### Minimum for Basic Training:
- Phase 1 Essential: **MUST HAVE**
- Phase 2 Sensors: **MUST HAVE**
- Phase 3 Details: *Optional, adds quality*
- Phase 4 Animation: *Optional, for video*

**Start with ~400 images (Phase 1+2) to get working results fast!**

---

## 💡 Pro Tips

1. **Test Early**: Render 1 full sequence first, verify before batch rendering
2. **Backup Often**: Copy renders to external drive after each phase
3. **Caption As You Go**: Don't wait until all rendering is done
4. **Start Training Sooner**: Don't need all phases to begin testing
5. **Iterate**: Train → Test → Improve → Retrain
6. **Save Versions**: Keep v1, v2, v3 models as you improve
7. **Document Issues**: Note what needs improvement for next iteration

---

## 📞 Need Help?

### Check These First:
- `RENDER_PLAN_C4D.md` - Full rendering specifications
- `C4D_QUICK_REFERENCE.md` - Quick C4D setup guide
- `CAPTION_TEMPLATES.md` - Caption writing examples
- `TRAINING_SETUP_GUIDE.md` - Training configuration details

### Common Issues:
- **Camera not rotating correctly**: Check spline alignment, "Align to Spline" tag
- **Device off-center**: Verify device is at (0,0,0), adjust camera distance
- **Missing alpha**: Enable PNG alpha in render settings
- **Captions too long**: Keep under 75 words, focus on essentials

---

**Ready to start? Begin with Phase 1, Day 1! 🎬**

Good luck with your Kyana Smartwatch LoRA training!

