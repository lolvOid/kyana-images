# Post-Render Training Setup Guide

## After You Complete Rendering

### Step 1: Organize Your Renders

Create this folder structure:
```
/kyana-images/
  /renders/
    /phase_1_essential/
      FULL_ASSEMBLY_FLAT_MID_360_1024x1024_0000.png
      FULL_ASSEMBLY_FLAT_MID_360_1024x1024_0001.png
      ...
    /phase_2_sensors/
      FULL_ASSEMBLY_FLAT_SENSORS_ON_LOW_360_1024x1024_0000.png
      ...
    /phase_3_details/
      COPPER_PINS_TOP_HIGH_360_1024x1024_0000.png
      ...
    /phase_4_animation/
      ASSEMBLY_ANIMATION_FLAT_1024x1024_0000.png
      ...
```

### Step 2: Generate Caption Files

For each .png file, create a matching .txt file with the same name:

**Example:**
```
FULL_ASSEMBLY_FLAT_MID_360_1024x1024_0000.png
FULL_ASSEMBLY_FLAT_MID_360_1024x1024_0000.txt
```

Use the `CAPTION_TEMPLATES.md` guide to write captions.

### Step 3: Verify Your Dataset

**Quality Check:**
```
☐ All PNG files have matching TXT caption files
☐ All images are 1024x1024 resolution
☐ Rotation sequences are smooth (no missing frames)
☐ Sensor states (on/off) are clearly visible
☐ No corrupted or black frames
☐ File names match the naming convention
```

**Count Your Images:**
```
Phase 1: ~252 images (7 renders × 36 frames)
Phase 2: ~144 images (4 renders × 36 frames)
Total Core: ~396 images minimum
```

---

## Training Configuration Files

### For AI-Toolkit (FLUX LoRA)

Create `config_ai_toolkit_kyana.yaml`:

```yaml
job: extension
config:
  name: kyana_smartwatch_lora_v1
  process:
    - type: sd_trainer
      training_folder: output
      device: cuda:0
      
  network:
    type: lora
    linear: 16
    linear_alpha: 16
    
  save:
    dtype: float16
    save_every: 100
    max_step_saves_to_keep: 3
    
  datasets:
    - folder_path: /path/to/kyana-images/renders
      caption_ext: txt
      caption_dropout_rate: 0.05
      shuffle_tokens: false
      cache_latents_to_disk: true
      resolution: [1024, 1024]
      
  train:
    batch_size: 1
    steps: 3000
    gradient_accumulation_steps: 1
    train_unet: true
    train_text_encoder: false
    gradient_checkpointing: true
    noise_scheduler: flowmatch
    optimizer: adamw8bit
    lr: 1e-4
    lr_scheduler: constant
    
    ema_config:
      use_ema: true
      ema_decay: 0.99
      
    dtype: bf16
    
  model:
    name_or_path: black-forest-labs/FLUX.1-dev
    is_flux: true
    quantize: true
    
  sample:
    sampler: flowmatch
    sample_every: 100
    width: 1024
    height: 1024
    prompts:
      - "Kyana health smartwatch rotating 360 degrees, black device with glossy screen, 33mm square design, white background"
      - "Kyana smartwatch closeup, copper magnetic connectors visible, 6 golden pins, ring frame detail"
      - "Kyana smartwatch with biometric sensors active, green LED lights glowing, bottom view, health monitoring"
      - "Kyana smartwatch with powerbank attached, modular battery system, green LED indicator, complete assembly"
      - "Kyana smartwatch core device only, LED display screen, speaker and button visible, side view"
    neg: "blurry, low quality, distorted, deformed, watermark, text, logo"
    seed: 42
    walk_seed: true
    guidance_scale: 4.0
    sample_steps: 20
```

### For Wan2.2 (Text-to-Video)

Training command structure:

```bash
# Text-to-Video Training
python train_t2v.py \
  --data_dir /path/to/kyana-images/renders/phase_1_essential \
  --output_dir ./output/kyana_t2v_v1 \
  --resolution 1024 \
  --frames 36 \
  --learning_rate 1e-4 \
  --batch_size 1 \
  --max_steps 3000 \
  --save_every 500 \
  --model_name wan2.2 \
  --caption_ext txt
```

### For Wan2.2 (Image-to-Video)

Training command structure:

```bash
# Image-to-Video Training (for animation sequences)
python train_i2v.py \
  --data_dir /path/to/kyana-images/renders \
  --output_dir ./output/kyana_i2v_v1 \
  --resolution 1024 \
  --frames 36 \
  --learning_rate 1e-4 \
  --batch_size 1 \
  --max_steps 2000 \
  --save_every 500 \
  --motion_type rotation \
  --caption_ext txt
```

---

## Training Strategy

### Stage 1: Core Product LoRA (FLUX)
**Goal:** Learn the product appearance, components, and style

**Dataset:** Phase 1 + Phase 2 (~400 images)
**Training:** AI-Toolkit with FLUX.1-dev
**Steps:** 3000 steps
**Time:** ~6-8 hours on RTX 4090

**Test prompts after training:**
```
"Kyana smartwatch 33mm square black device, rotating view, glossy display"
"Kyana smartwatch with powerbank module attached, green LED indicator"
"Kyana smartwatch bottom view, active biometric sensors glowing green"
```

### Stage 2: Detail Enhancement (FLUX)
**Goal:** Improve closeup details and specific components

**Dataset:** Phase 3 Details (~180 images)
**Training:** Fine-tune from Stage 1 LoRA
**Steps:** 1500 additional steps
**Time:** ~3-4 hours

**Test prompts:**
```
"Kyana smartwatch copper connectors closeup, 6 golden pins, top view"
"Kyana smartwatch button and speaker detail, side profile, closeup"
"Kyana smartwatch display screen closeup, glossy surface, reflections"
```

### Stage 3: Animation/Motion (Wan2.2 T2V)
**Goal:** Generate smooth rotation videos

**Dataset:** All Phase 1+2 sequences
**Training:** Text-to-Video on rotation sequences
**Steps:** 3000 steps
**Time:** ~12-16 hours (depends on hardware)

**Test prompts:**
```
"Kyana smartwatch rotating 360 degrees clockwise, black device, white background"
"Kyana smartwatch with powerbank, slow rotation, green LED visible"
```

### Stage 4: Advanced Motion (Wan2.2 I2V)
**Goal:** Assembly animations and complex movements

**Dataset:** Phase 4 Animation sequences
**Training:** Image-to-Video for assembly motions
**Steps:** 2000 steps
**Time:** ~8-10 hours

**Test prompts:**
```
"Core device descending and snapping into ring frame magnetically"
"Powerbank sliding onto strap and connecting to copper pins"
"Complete assembly rotating with all components visible"
```

---

## Recommended Training Order

### Week 1: Core Product
```
Day 1-2: Render Phase 1 Essential (~252 images)
Day 3:   Render Phase 2 Sensors (~144 images)
Day 4:   Generate all caption files
Day 5:   Train FLUX LoRA Stage 1 (3000 steps)
Day 6-7: Test and evaluate results
```

### Week 2: Details & Motion
```
Day 1:   Render Phase 3 Details (~180 images)
Day 2:   Generate captions, train Stage 2 (1500 steps)
Day 3-5: Train Wan2.2 T2V for rotations
Day 6-7: Test video generation, evaluate quality
```

### Week 3: Advanced (Optional)
```
Day 1-2: Render Phase 4 Animations
Day 3:   Generate animation captions
Day 4-6: Train Wan2.2 I2V for assembly sequences
Day 7:   Final testing and showcase creation
```

---

## Testing Your Trained Models

### FLUX LoRA Testing Prompts

**Basic Product:**
```
Kyana health smartwatch 33mm square design, black glossy display, front view
Kyana smartwatch complete assembly with flat strap, side angle view
Kyana smartwatch core device only, LED display visible, isometric view
```

**With Components:**
```
Kyana smartwatch with powerbank module on strap, green LED indicator active
Kyana smartwatch ring frame with 6 copper pins visible on top edge
Kyana smartwatch modular system, exploded view with separated components
```

**Sensor States:**
```
Kyana smartwatch bottom view, biometric sensors active, green LEDs glowing
Kyana smartwatch with all sensors illuminated, health monitoring mode
Kyana smartwatch sensors inactive, copper contacts visible
```

**Detail Shots:**
```
Kyana smartwatch copper connector pins extreme closeup, golden metallic finish
Kyana smartwatch button detail on right side, red accent visible
Kyana smartwatch clasp mechanism closeup, strap fastening system
```

**Context Scenes:**
```
Kyana smartwatch on modern desk, office environment, professional lighting
Kyana smartwatch on fitness mat with dumbbells, gym setting
Kyana smartwatch charging with powerbank, green LED glowing, nightstand
```

### T2V Testing Prompts

**Rotation Videos:**
```
Kyana smartwatch rotating 360 degrees clockwise, smooth turntable motion
Kyana smartwatch with powerbank, slow rotation showing all sides
Kyana smartwatch core device spinning on vertical axis, LED display visible
```

**Camera Motion:**
```
Kyana smartwatch, camera orbiting around device, 360 degree rotation
Kyana smartwatch, camera dolly forward zooming into display screen
Kyana smartwatch, camera panning from left to right, side profile view
```

### I2V Testing Prompts

**Assembly Motions:**
```
Core device descending and snapping magnetically into ring frame
Powerbank module sliding onto strap from side, LED activating
Ring frame and strap connecting, clasp mechanism fastening
```

**Component Highlights:**
```
Biometric sensors activating, green LEDs pulsing rhythmically
Copper connector pins catching light with metallic shimmer
Display screen powering on, interface appearing gradually
```

---

## Evaluation Criteria

### Image Quality (FLUX LoRA):
```
✓ Product proportions accurate (33mm square)
✓ Components correctly placed (button right, speaker left)
✓ Material accuracy (glossy display, matte strap)
✓ Color consistency (black with copper accents)
✓ Detail preservation (sensors, connectors visible)
```

### Video Quality (T2V/I2V):
```
✓ Smooth rotation without jitter
✓ Consistent lighting throughout
✓ No morphing or distortion
✓ Proper motion blur
✓ Temporal coherence (no flickering)
```

### Prompt Adherence:
```
✓ Follows component specifications
✓ Responds to angle/view directions
✓ Activates sensors when prompted
✓ Includes/excludes components as specified
✓ Maintains Kyana brand identity
```

---

## Optimization Tips

### If Images Look Wrong:
```
- Train longer (increase steps)
- Reduce learning rate (try 5e-5)
- Check caption quality and consistency
- Verify image resolution and quality
- Add more diverse angles
```

### If Videos Are Jittery:
```
- Use more frames (72 instead of 36)
- Ensure linear interpolation (no easing)
- Check for missing frames in sequence
- Reduce motion complexity
- Increase training steps
```

### If Details Are Lost:
```
- Add Phase 3 closeup training
- Include detail-focused captions
- Use higher resolution if possible
- Train detail LoRA separately
- Increase LoRA rank (32 instead of 16)
```

### If Colors Are Off:
```
- Verify consistent lighting in renders
- Check caption color descriptions
- Add color-specific training data
- Adjust white balance in renders
- Mention "black" explicitly in all captions
```

---

## Next Steps After Training

1. **Create Test Gallery**: Render 50-100 test prompts, evaluate results
2. **Version Control**: Save trained models with version numbers (v1, v2, etc.)
3. **Documentation**: Note what works well, what needs improvement
4. **Iteration**: Re-render problematic angles, retrain if needed
5. **Showcase**: Create demo video showing capabilities
6. **Color Variants**: Once satisfied, render white/silver/space grey versions

---

## Useful Tools

### Python Script for Batch Caption Generation
See `CAPTION_TEMPLATES.md` for the caption generator script.

### Image Quality Check Script
```python
from PIL import Image
import os

def check_images(folder_path):
    issues = []
    for file in os.listdir(folder_path):
        if file.endswith('.png'):
            img = Image.open(os.path.join(folder_path, file))
            if img.size != (1024, 1024):
                issues.append(f"{file}: Wrong size {img.size}")
            if not os.path.exists(file.replace('.png', '.txt')):
                issues.append(f"{file}: Missing caption file")
    
    if issues:
        print("Issues found:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("All images passed quality check!")

check_images('/path/to/renders')
```

### Training Progress Monitor
Most training frameworks provide tensorboard logs. Monitor:
- Loss curves (should decrease steadily)
- Sample outputs (quality should improve)
- Learning rate (should be stable)
- Memory usage (should be consistent)

---

## Support Resources

**AI-Toolkit Documentation:**
https://github.com/ostris/ai-toolkit

**FLUX.1 Model:**
https://huggingface.co/black-forest-labs/FLUX.1-dev

**Wan2.2 (if available):**
Check official repository for latest setup guides

**LoRA Training Guides:**
Search for "FLUX LoRA training tutorial" for latest best practices

---

Ready to start rendering and training! 🚀

