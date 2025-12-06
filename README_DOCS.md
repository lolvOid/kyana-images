# 📚 Kyana Smartwatch Rendering & Training - Documentation Index

## All Your Reference Documents

Your complete guide to rendering and training the Kyana Smartwatch LoRA model.

---

## 🎯 START HERE

### **[WORKFLOW_CHECKLIST.md](WORKFLOW_CHECKLIST.md)**
**→ Your master checklist and progress tracker**
- Week-by-week plan
- Daily tasks breakdown
- Progress tracking checkboxes
- Success criteria
- Quick start guide

**Use this to:** Track your overall progress from rendering to training completion.

---

## 📋 RENDER PLANNING

### **[RENDER_PLAN_C4D.md](RENDER_PLAN_C4D.md)**
**→ Complete rendering specifications**
- All render phases (1-4)
- Camera angles and distances
- Component combinations
- Frame counts and naming
- Complete render list with specifications

**Use this for:** Understanding what to render and how to set up each shot.

---

### **[FLAT_VS_CIRCULAR_GUIDE.md](FLAT_VS_CIRCULAR_GUIDE.md)**
**→ Understanding the two strap configurations**
- FLAT vs CIRCULAR explained
- When to use each
- Camera distance differences
- Setup guide for both
- Visual comparisons

**Use this when:** Setting up straps in C4D - should they be straight or curved?

---

## ⚡ QUICK REFERENCES

### **[C4D_QUICK_REFERENCE.md](C4D_QUICK_REFERENCE.md)**
**→ Fast lookup for Cinema 4D settings**
- Quick setup checklist
- Camera distances by type
- Render settings copy-paste
- Lighting presets
- Material settings
- Troubleshooting
- Time estimates

**Use this while:** Actually working in Cinema 4D, keep it open for quick reference.

---

### **[DIMENSIONS_SCALE_GUIDE.md](DIMENSIONS_SCALE_GUIDE.md)**
**→ Exact physical dimensions and scale calculations**
- Product dimensions (33mm × 33mm × 8mm)
- Strap lengths (80mm + 130mm)
- Camera distance formulas
- Scale reference table
- C4D scene setup guide
- Framing validation

**Use this when:** Setting up your C4D scene with correct proportions and camera distances.

---

## ✍️ CAPTION WRITING

### **[CAPTION_TEMPLATES.md](CAPTION_TEMPLATES.md)**
**→ How to write captions for each image**
- Caption templates for all phases
- Angle calculation guide
- Python script for auto-generation
- Keyword reference
- Manual caption checklist

**Use this after:** Rendering is complete, to create .txt caption files for training.

---

## 🎓 TRAINING SETUP

### **[TRAINING_SETUP_GUIDE.md](TRAINING_SETUP_GUIDE.md)**
**→ Complete training workflow after rendering**
- Post-render organization
- Training configurations (AI-Toolkit, Wan2.2)
- Training stages (1-4)
- Testing prompts
- Evaluation criteria
- Optimization tips

**Use this when:** Ready to start training after all renders are complete.

---

## 📖 Reading Order by Phase

### **Phase 0: Planning (Before Starting)**
1. ✅ **WORKFLOW_CHECKLIST.md** - Understand the full workflow
2. ✅ **RENDER_PLAN_C4D.md** - Know what you're rendering
3. ✅ **FLAT_VS_CIRCULAR_GUIDE.md** - Understand strap configurations

### **Phase 1: Setting Up C4D**
1. ✅ **DIMENSIONS_SCALE_GUIDE.md** - Get exact measurements
2. ✅ **C4D_QUICK_REFERENCE.md** - Set up your scene
3. ✅ **RENDER_PLAN_C4D.md** - Reference specific render settings

### **Phase 2: During Rendering**
1. ✅ **C4D_QUICK_REFERENCE.md** - Quick settings lookup
2. ✅ **WORKFLOW_CHECKLIST.md** - Track your progress
3. ✅ **FLAT_VS_CIRCULAR_GUIDE.md** - Switch between configurations

### **Phase 3: After Rendering**
1. ✅ **CAPTION_TEMPLATES.md** - Write captions for images
2. ✅ **TRAINING_SETUP_GUIDE.md** - Prepare for training
3. ✅ **WORKFLOW_CHECKLIST.md** - Verify completion

### **Phase 4: Training**
1. ✅ **TRAINING_SETUP_GUIDE.md** - Follow training workflow
2. ✅ **WORKFLOW_CHECKLIST.md** - Track training progress

---

## 🔍 Quick Lookup Table

| I need to know... | Check this file |
|------------------|----------------|
| What to render next | WORKFLOW_CHECKLIST.md |
| Camera distance for full assembly | DIMENSIONS_SCALE_GUIDE.md |
| FLAT vs CIRCULAR distance | FLAT_VS_CIRCULAR_GUIDE.md |
| Render settings for C4D | C4D_QUICK_REFERENCE.md |
| Complete list of all renders | RENDER_PLAN_C4D.md |
| How to write captions | CAPTION_TEMPLATES.md |
| How to train after rendering | TRAINING_SETUP_GUIDE.md |
| Product dimensions | DIMENSIONS_SCALE_GUIDE.md |
| Lighting setup | C4D_QUICK_REFERENCE.md |
| Naming conventions | RENDER_PLAN_C4D.md |
| Testing prompts | TRAINING_SETUP_GUIDE.md |
| Troubleshooting C4D | C4D_QUICK_REFERENCE.md |
| Progress tracking | WORKFLOW_CHECKLIST.md |

---

## 📁 File Organization

```
/kyana-images/
  
  📚 DOCUMENTATION (You are here):
  ├── README_DOCS.md (this file)
  ├── WORKFLOW_CHECKLIST.md ⭐ START HERE
  ├── RENDER_PLAN_C4D.md
  ├── FLAT_VS_CIRCULAR_GUIDE.md
  ├── C4D_QUICK_REFERENCE.md
  ├── DIMENSIONS_SCALE_GUIDE.md
  ├── CAPTION_TEMPLATES.md
  └── TRAINING_SETUP_GUIDE.md
  
  🎬 RENDERS (Create these folders):
  └── /renders/
      ├── /phase_1_essential/
      ├── /phase_2_sensors/
      ├── /phase_3_details/
      └── /phase_4_animation/
  
  ⚙️ CONFIGS (Create these):
  └── /configs/
      ├── config_ai_toolkit_kyana.yaml
      └── config_wan22_kyana.yaml
  
  🎯 OUTPUT (Generated during training):
  └── /output/
      ├── /kyana_lora_v1/
      └── /kyana_t2v_v1/
```

---

## 💡 Tips for Using These Docs

### Print or Keep Open:
- **C4D_QUICK_REFERENCE.md** - Keep open while rendering
- **WORKFLOW_CHECKLIST.md** - Print and check off tasks

### Reference When Needed:
- **RENDER_PLAN_C4D.md** - Look up specific render specs
- **DIMENSIONS_SCALE_GUIDE.md** - When setting up scene
- **FLAT_VS_CIRCULAR_GUIDE.md** - When switching configurations

### Use After Completion:
- **CAPTION_TEMPLATES.md** - After rendering Phase 1-2
- **TRAINING_SETUP_GUIDE.md** - After all rendering done

---

## 🚀 Quick Start Path

**Day 1: Planning & Setup**
```
1. Read: WORKFLOW_CHECKLIST.md (understand the plan)
2. Read: RENDER_PLAN_C4D.md (know what to render)
3. Read: FLAT_VS_CIRCULAR_GUIDE.md (understand configurations)
4. Prepare: C4D scene with correct dimensions
```

**Day 2-4: Rendering**
```
1. Open: C4D_QUICK_REFERENCE.md (keep it handy)
2. Reference: DIMENSIONS_SCALE_GUIDE.md (for distances)
3. Follow: RENDER_PLAN_C4D.md Phase 1
4. Track: WORKFLOW_CHECKLIST.md
```

**Day 5: Captioning**
```
1. Use: CAPTION_TEMPLATES.md
2. Generate all .txt files
3. Verify with checklist
```

**Day 6+: Training**
```
1. Follow: TRAINING_SETUP_GUIDE.md
2. Configure and train
3. Test and iterate
```

---

## 🎯 Key Numbers to Remember

```
Device Size:        33mm × 33mm × 10mm
Strap Length:       80mm + 130mm = 210mm
Powerbank:          8mm thickness

Camera Distance:
- Full FLAT:        300-350mm
- Full CIRCULAR:    180-220mm
- Core Device:      80-100mm
- Closeups:         60-80mm

Frames per Render:  36 frames (10° per frame)
Total Images:       ~400 minimum (Phase 1+2)
Target Training:    3000 steps (FLUX LoRA)
```

---

## ✅ Documentation Checklist

Before you start rendering, make sure you've reviewed:

```
☐ Read WORKFLOW_CHECKLIST.md completely
☐ Understand RENDER_PLAN_C4D.md Phase 1
☐ Know difference between FLAT vs CIRCULAR
☐ Have C4D_QUICK_REFERENCE.md accessible
☐ Understand camera distances from DIMENSIONS_SCALE_GUIDE.md
☐ Know you'll need CAPTION_TEMPLATES.md later
☐ Aware of TRAINING_SETUP_GUIDE.md for after rendering
```

---

## 📞 Document Updates

All documentation has been updated with:
- ✅ Correct physical dimensions (33mm × 33mm × 8mm, 210mm straps)
- ✅ FLAT vs CIRCULAR configuration clarifications
- ✅ Accurate camera distances for both configs
- ✅ Complete phase-by-phase workflow
- ✅ Training preparation guides

**Last Updated:** December 2024

---

**Ready to start? Open [WORKFLOW_CHECKLIST.md](WORKFLOW_CHECKLIST.md) and begin Phase 1! 🎬**

