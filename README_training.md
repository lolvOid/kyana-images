# Kyana Smartwatch LoRA Training Guide

## Product Overview
- **Product**: Kyana Health Smartwatch
- **Form Factor**: Square 33mm modular smartwatch
- **Key Features**: Modular magnetic ring system, biometric sensors, powerbank accessory
- **Colors**: Black (default), White, Silver, Space Grey

## Component Details

### Core Device
- Square 33mm case with glossy display
- **Left Side**: Speaker grille
- **Right Side**: Physical button
- **Bottom**: Circular biometric sensor array (6-8 LEDs - green and red)

### Ring Frame
- Square black frame surrounding core device
- **Inside Ring**: 4 copper magnetic connectors for core device attachment
- **Outside Top**: 6 copper pins for powerbank/charging connection
- **Sides**: Strap attachment slots

### Silicon Strap
- Matte black silicone material
- **Bottom Side**: 6 rectangular sensor windows with green LED indicators
- **Connection**: Slides into ring frame slots

### Powerbank Module
- Compact black cube with rounded edges
- Green LED status indicator
- USB-C charging port
- 6 copper pin connectors for strap attachment

## Training Files

### Text-to-Video Prompts
- `prompts_t2v_general.txt` - Short general prompts (25 prompts)
- `prompts_t2v_detailed.txt` - Detailed descriptive prompts (20 prompts)

### Image-to-Video Prompts
- `prompts_i2v_motion.txt` - Camera movements and animations (48 prompts)
- `prompts_i2v_scenes.txt` - Scene contexts and environments (30 prompts)
- `prompts_i2v_assembly_sequences.txt` - Component attachment and assembly (50 prompts)
- `prompts_i2v_wearing_demonstration.txt` - Wrist wearing and usage (50 prompts)
- `prompts_i2v_detailed_explainer.txt` - Technical explainer and infographic animations (75 prompts)
- `prompts_i2v_clasp_and_connections.txt` - Clasp mechanisms and connector details (50 prompts)
- `prompts_i2v_hands_interactions.txt` - Hand interactions and gestures (60 prompts)
- `prompts_i2v_product_lifestyle.txt` - Lifestyle and real-world usage scenarios (80 prompts)

### Technical Specifications
- `prompts_technical_specs.txt` - Detailed component specifications for tagging

### AI-Toolkit Configuration
- `config_ai_toolkit_lora.yaml` - Training configuration for FLUX LoRA

## Training Setup for Wan2.2

### Text-to-Video (T2V) Training
```bash
# Use general prompts for base training
python train_t2v.py \
  --prompts prompts_t2v_general.txt \
  --images_dir . \
  --output_dir ./output/kyana_t2v \
  --resolution 1024 \
  --learning_rate 1e-4 \
  --max_steps 3000
```

### Image-to-Video (I2V) Training

#### Basic Motion Training
```bash
python train_i2v.py \
  --prompts prompts_i2v_motion.txt \
  --images_dir . \
  --output_dir ./output/kyana_i2v_motion \
  --resolution 1024 \
  --learning_rate 1e-4 \
  --max_steps 2000
```

#### Assembly & Interaction Training
```bash
python train_i2v.py \
  --prompts prompts_i2v_assembly_sequences.txt \
  --images_dir . \
  --output_dir ./output/kyana_i2v_assembly \
  --resolution 1024 \
  --learning_rate 1e-4 \
  --max_steps 3000
```

#### Wearing & Hands Training
```bash
python train_i2v.py \
  --prompts prompts_i2v_hands_interactions.txt,prompts_i2v_wearing_demonstration.txt \
  --images_dir . \
  --output_dir ./output/kyana_i2v_hands \
  --resolution 1024 \
  --learning_rate 1e-4 \
  --max_steps 3000
```

#### Explainer & Lifestyle Training
```bash
python train_i2v.py \
  --prompts prompts_i2v_detailed_explainer.txt,prompts_i2v_product_lifestyle.txt \
  --images_dir . \
  --output_dir ./output/kyana_i2v_lifestyle \
  --resolution 1024 \
  --learning_rate 1e-4 \
  --max_steps 4000
```

## Prompt Structure

### Recommended Format
```
[Product Name] [Component Description], [Key Features], [Visual Details], [Context/Environment]
```

### Example
```
Kyana health smartwatch, square black device with glossy screen, 6 copper connectors visible at top edge, rotating 360 degrees on white background
```

## Key Training Considerations

1. **Component Focus**:
   - Core device with display (33mm square)
   - Ring frame (4 connectors inside, 6 pins outside top)
   - Biometric sensors (active/inactive states)
   - Powerbank module
   - Strap details

2. **States to Capture**:
   - Sensors OFF (copper appears gray/silver)
   - Sensors ON (green and red LEDs glowing)
   - Powerbank LED indicator (green)
   - Full assembly vs modular components

3. **Color Variants**:
   - Black (default) - current training set
   - White (future)
   - Silver (future)
   - Space Grey (future)

4. **Viewing Angles**:
   - Front (display)
   - Back (sensors)
   - Side (button/speaker)
   - Top (copper pins)
   - 3/4 views
   - Macro closeups

5. **Motion Types**:
   - 360° rotation
   - Tilt animations
   - Zoom in/out
   - Component assembly
   - LED activation sequences

## Dataset Preparation

1. Organize images by category:
   - Full assembly shots
   - Component closeups
   - Sensor detail views
   - Ring frame views
   - Powerbank shots

2. Create caption files (.txt) for each image matching the filename

3. Use consistent terminology:
   - "Kyana smartwatch" or "Kyana health smartwatch"
   - "33mm square case" for size reference
   - "4 copper magnetic connectors inside ring" for core attachment
   - "6 copper pins on top" for powerbank connection
   - "biometric sensors" with color descriptions
   - "ring frame" for the middle component
   - "core device" for the watch module
   - Color variants: "black" (default), "white", "silver", "space grey"

## Trigger Words
- `KYANA_WATCH` - main product
- `COPPER_CONNECTORS` - magnetic pins
- `BIOMETRIC_SENSORS` - LED sensor array
- `RING_FRAME` - modular ring
- `POWERBANK_MODULE` - battery accessory

## Quality Tips

1. Emphasize the modular magnetic system
2. Highlight copper connector details:
   - 4 magnetic pins inside ring (for core device)
   - 6 copper pins outside top (for powerbank)
3. Show biometric sensors in both states
4. Capture glossy display reflections
5. Include red accent detail on button
6. Show powerbank connection mechanism
7. Specify 33mm square case size
8. Note color variant in prompts (black default)

## Post-Training Testing

Test prompts should include:
- Different camera angles
- Component variations
- Lighting conditions
- Assembly states
- Active/inactive sensor states
