#!/bin/bash
# Kyana Watch LoRA Training - Azure Cloud Setup Script

set -e  # Exit on error

echo "========================================="
echo "Kya-na Health Watch LoRA Training Setup"
echo "========================================="
echo ""

# Check if we're in the right directory
if [ ! -d "/data/kyana-images" ]; then
    echo "Creating /data/kyana-images directory..."
    mkdir -p /data/kyana-images
    mkdir -p /data/kyana-images/dataset
    mkdir -p /data/kyana-images/output
fi

cd /data/kyana-images

# Activate conda environment
echo "Activating ai-toolkit environment..."
source ~/miniconda3/etc/profile.d/conda.sh || source ~/anaconda3/etc/profile.d/conda.sh
conda activate ai-toolkit

# Check Python
echo "Python version:"
python --version
echo ""

# Check GPU
echo "GPU Information:"
nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader
echo ""

# Check dataset
echo "Checking dataset..."
image_count=$(ls dataset/*.png 2>/dev/null | wc -l)
echo "Found $image_count images in dataset/"

if [ "$image_count" -eq 0 ]; then
    echo "WARNING: No images found in dataset/"
    echo "Please upload your dataset first!"
    exit 1
fi

# Generate captions
echo ""
echo "========================================="
echo "Step 1: Generating Captions"
echo "========================================="
python generate_captions.py

caption_count=$(ls dataset/*.txt 2>/dev/null | wc -l)
echo "Created $caption_count caption files"

# Verify config
echo ""
echo "========================================="
echo "Step 2: Verifying Config"
echo "========================================="
if [ ! -f "train_config.yaml" ]; then
    echo "ERROR: train_config.yaml not found!"
    exit 1
fi
echo "Config file found: train_config.yaml"

# Show training parameters
echo ""
echo "Training Parameters:"
echo "  - Base Model: FLUX.1-dev"
echo "  - Batch Size: 4"
echo "  - Steps: 3000"
echo "  - Learning Rate: 0.0001"
echo "  - Resolution: 1024x1024"
echo "  - Output: /data/kyana-images/output/"
echo ""

# Ask for confirmation
read -p "Start training? (y/n): " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Training cancelled."
    exit 0
fi

# Start training
echo ""
echo "========================================="
echo "Step 3: Starting Training"
echo "========================================="
echo "Training started at: $(date)"
echo "This will take several hours depending on your GPU..."
echo ""

# Run training with ai-toolkit
python -m ai_toolkit.train --config train_config.yaml 2>&1 | tee training.log

echo ""
echo "========================================="
echo "Training Complete!"
echo "========================================="
echo "Finished at: $(date)"
echo ""
echo "Model saved to: /data/kyana-images/output/"
echo "Training log: /data/kyana-images/training.log"
echo ""
echo "Download your model:"
echo "  rsync -avz user@azure-vm:/data/kyana-images/output/ ./trained_models/"

