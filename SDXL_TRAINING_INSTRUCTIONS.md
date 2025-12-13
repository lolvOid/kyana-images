# SDXL Multi-LoRA Training Instructions

This guide provides step-by-step instructions for organizing your dataset and training 5 separate SDXL LoRAs for the kya-na health watch product.

## Prerequisites

- AI-Toolkit installed and configured
- CUDA-capable GPU with sufficient VRAM (recommended: 16GB+ for full precision SDXL)
- Dataset located at `/data/kyana-images/dataset` with paired `.png` and `.txt` files
- Python 3.8+ with standard libraries (os, shutil, pathlib)

## Step 1: Organize the Dataset

Run the organization script to categorize your dataset and inject unique tokens:

```bash
cd /data/kyana-images
python3 organize_sdxl_datasets.py
```

### What the Script Does

1. Scans `/data/kyana-images/dataset` for all `.png` files
2. Finds matching `.txt` caption files
3. Categorizes files based on filename prefixes:
   - `FULL_DEVICE*` or `CORE_DEVICE*` → `device_core`
   - `STRAP*` or `RING_STRAP*` → `strap`
   - `CLASP*` → `clasp`
   - `POWERBANK*` or `FULL_WITH_POWERBANK*` → `powerbank`
   - `MAGNETIC*` or `COPPER_PINS*` → `internal_details`
4. Creates organized folder structure at `/data/kyana-images/datasets/`
5. Copies files to appropriate `images/` and `captions/` subfolders
6. Automatically injects tokens at the start of captions:
   - `<devX>` for device_core
   - `<strapX>` for strap
   - `<claspX>` for clasp
   - `<powerX>` for powerbank
   - `<internalX>` for internal_details

### Verify Organization

After running the script, verify the organization:

```bash
# Check folder structure
ls -la /data/kyana-images/datasets/

# Count files in each category
for dir in device_core strap clasp powerbank internal_details; do
    echo "$dir:"
    echo "  Images: $(ls /data/kyana-images/datasets/$dir/images/*.png 2>/dev/null | wc -l)"
    echo "  Captions: $(ls /data/kyana-images/datasets/$dir/captions/*.txt 2>/dev/null | wc -l)"
done

# Sample a caption to verify token injection
head -1 /data/kyana-images/datasets/device_core/captions/*.txt | head -5
```

Expected output should show tokens at the start of captions.

## Step 2: Review Training Configs

All 5 training configs are ready:
- `train_sdxl_device_core_lora.yaml`
- `train_sdxl_strap_lora.yaml`
- `train_sdxl_clasp_lora.yaml`
- `train_sdxl_powerbank_lora.yaml`
- `train_sdxl_internal_details_lora.yaml`

### Config Settings Summary

- **Base Model**: `stabilityai/stable-diffusion-xl-base-1.0`
- **Resolution**: 1024x1024
- **Batch Size**: 1
- **Gradient Accumulation**: 4 (effective batch size: 4)
- **Optimizer**: AdamW (full precision)
- **Learning Rates**: 
  - UNet: 1e-4
  - Text Encoder: 5e-5
- **LoRA Rank**: 32
- **LoRA Alpha**: 32
- **Training Steps**: 3500
- **Save Every**: 500 steps
- **Mixed Precision**: fp16
- **Text Encoder Training**: Enabled

## Step 3: Train Each LoRA

Train the LoRAs sequentially or in parallel (if you have multiple GPUs). Each training job will take approximately 4-8 hours depending on your GPU and dataset size.

### Training Command

For each LoRA, run:

```bash
# Device Core LoRA
ai-toolkit train train_sdxl_device_core_lora.yaml

# Strap LoRA
ai-toolkit train train_sdxl_strap_lora.yaml

# Clasp LoRA
ai-toolkit train train_sdxl_clasp_lora.yaml

# Powerbank LoRA
ai-toolkit train train_sdxl_powerbank_lora.yaml

# Internal Details LoRA
ai-toolkit train train_sdxl_internal_details_lora.yaml
```

### Training Output

Trained LoRAs will be saved to:
```
/data/kyana-images/output_sdxl/
  device_core_lora/
    checkpoint-500.safetensors
    checkpoint-1000.safetensors
    ...
    checkpoint-3500.safetensors
  strap_lora/
    ...
  clasp_lora/
    ...
  powerbank_lora/
    ...
  internal_details_lora/
    ...
```

### Monitor Training

Check training progress:
```bash
# View latest training logs
tail -f /data/kyana-images/output_sdxl/*/training.log

# Check GPU usage
watch -n 1 nvidia-smi

# View sample images (generated every 500 steps)
ls -la /data/kyana-images/output_sdxl/*/samples/
```

## Step 4: Using Multiple LoRAs Together

After training, you can combine multiple LoRAs during inference. In your inference pipeline:

1. Load the base SDXL model
2. Load and apply multiple LoRAs simultaneously
3. Use the appropriate tokens in your prompts

### Example Combined Prompt

```
<devX> <strapX> <claspX> kya-na health watch complete wearable unit, core device mounted in ring frame with textured strap, clasp in closed position, six small flexible sensors underneath each strap, biometric sensors active, black metallic matte finish, professional product photography, white background
```

### Token Usage Guidelines

- Use `<devX>` when generating core device or full device images
- Use `<strapX>` when generating strap or ring frame images
- Use `<claspX>` when generating clasp mechanism images
- Use `<powerX>` when generating powerbank images
- Use `<internalX>` when generating internal detail images
- Combine multiple tokens when generating composite images

## Resource Requirements

### VRAM Usage (Full Precision SDXL)

- **Training**: ~16-20GB VRAM per training job
- **Inference**: ~8-12GB VRAM (depending on resolution and batch size)

### Training Time Estimates

- **Per LoRA**: 4-8 hours (depending on GPU and dataset size)
- **Total for 5 LoRAs**: 20-40 hours (sequential) or 4-8 hours (parallel with 5 GPUs)

### Disk Space

- **Dataset organization**: ~2x original dataset size (files are copied, not moved)
- **Training outputs**: ~500MB-1GB per LoRA checkpoint
- **Total training outputs**: ~3.5-7GB (7 checkpoints × 5 LoRAs)

## Troubleshooting

### Out of Memory (OOM) Errors

If you encounter CUDA OOM errors:

1. **Reduce batch size**: Change `batch_size: 1` to `batch_size: 1` with `gradient_accumulation: 8` (already optimized)
2. **Enable gradient checkpointing**: Already enabled in configs
3. **Use quantization**: Switch to quantized SDXL models (requires config modification)
4. **Reduce resolution**: Change `resolution: [1024, 1024]` to `resolution: [768, 768]` (not recommended for product quality)

### Slow Training

- Ensure `cache_text_embeddings: true` is enabled (already set)
- Check GPU utilization: `nvidia-smi`
- Verify data loading isn't bottleneck: Check if GPU utilization is consistently high

### Missing Files After Organization

- Original files in `/data/kyana-images/dataset` are preserved (script copies, doesn't move)
- Check script output for unmatched files
- Manually categorize unmatched files if needed

### Token Not Working in Inference

- Ensure token is at the start of the prompt
- Verify LoRA was trained with the token
- Check that LoRA is properly loaded in your inference pipeline
- Ensure token matches exactly (case-sensitive): `<devX>`, not `<DEVX>` or `<devx>`

### Poor Generation Quality

- Verify captions have tokens injected correctly
- Check sample images during training for quality progression
- Consider increasing training steps (currently 3500)
- Verify dataset quality and caption accuracy
- Ensure negative prompts are appropriate

## Next Steps

After training completes:

1. **Evaluate sample images** from each LoRA checkpoint
2. **Select best checkpoints** (typically later steps, but not always)
3. **Test individual LoRAs** in isolation
4. **Test combined LoRAs** for composite images
5. **Fine-tune prompts** based on generation results
6. **Consider additional training** if specific aspects need improvement

## Support

For AI-Toolkit specific issues, refer to:
- AI-Toolkit documentation
- AI-Toolkit GitHub repository
- Community forums

For dataset or caption issues, review:
- `sdxl_caption_examples.md` for caption format guidelines
- Original dataset captions for consistency

