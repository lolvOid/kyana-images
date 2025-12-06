# Azure Cloud LoRA Training Setup - Kya-na Health Watch

## Environment Details
- **Platform:** Azure Cloud GPU
- **Conda Environment:** `ai-toolkit`
- **Data Location:** `/data/`
- **Training Method:** Wan2.2 T2V/I2V LoRA
- **Dataset:** 756 product images (1024x1024 PNG)

---

## Step 1: Upload Dataset to Azure

### On Local Machine (Mac):

```bash
# Sync dataset to Azure
rsync -avz --progress /Users/freddie/Projects/lolvOid/kyana-images/dataset/ \
  user@azure-vm-ip:/data/kyana-images/

# Or use Azure CLI
az storage blob upload-batch \
  --destination kyana-training \
  --source /Users/freddie/Projects/lolvOid/kyana-images/dataset/ \
  --account-name yourstorageaccount
```

---

## Step 2: Setup on Azure VM

### SSH into Azure:
```bash
ssh user@azure-vm-ip
```

### Activate Environment:
```bash
conda activate ai-toolkit
cd /data/kyana-images
```

### Install Dependencies:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install transformers accelerate diffusers safetensors omegaconf pyyaml pillow tqdm
pip install git+https://github.com/huggingface/diffusers.git
```

---

## Step 3: Generate Captions

Run the caption generation script (see `generate_captions.py`):

```bash
python generate_captions.py
```

This will create `.txt` files for all 756 images based on their filenames.

---

## Step 4: Configure Training

Edit `train_config.yaml` with your settings:
- Adjust batch size based on GPU memory
- Set output directory
- Configure learning rate and epochs

---

## Step 5: Start Training

### Using AI-Toolkit:
```bash
python -m ai_toolkit.train --config train_config.yaml
```

### Monitor Training:
```bash
# View logs
tail -f training.log

# Check GPU usage
nvidia-smi -l 1
```

---

## Step 6: Export and Download Model

After training completes:

```bash
# Model will be saved to /data/kyana-images/output/lora_model.safetensors

# Download to local machine
rsync -avz --progress user@azure-vm-ip:/data/kyana-images/output/ \
  /Users/freddie/Projects/lolvOid/kyana-images/trained_models/
```

---

## Training Parameters Recommendations

**For T2V (Text-to-Video):**
- Batch size: 2-4 (depending on GPU memory)
- Learning rate: 1e-5 to 5e-5
- Epochs: 10-20
- Resolution: 1024x1024
- Mixed precision: fp16

**For I2V (Image-to-Video):**
- Similar settings but focus on motion/animation frames
- Use clasp and assembly animation sequences

---

## Estimated Training Time

**With 756 images:**
- 1x A100 (40GB): ~4-6 hours
- 1x V100 (32GB): ~6-8 hours  
- 1x RTX 4090: ~8-10 hours

Actual time varies based on batch size and epochs.

---

## Troubleshooting

**Out of Memory:**
- Reduce batch size in config
- Use gradient checkpointing
- Enable mixed precision (fp16)

**Slow Training:**
- Check data loader workers setting
- Verify GPU utilization with `nvidia-smi`
- Consider distributed training if multiple GPUs available

**Poor Results:**
- Increase training epochs
- Adjust learning rate
- Check caption quality
- Ensure dataset variety (you have good coverage!)

