#!/bin/bash
# Start all SDXL LoRA trainings sequentially in non-interruptible mode
# Each training will start after the previous one completes

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Activate conda environment
source /data/miniconda3/etc/profile.d/conda.sh
conda activate ai-toolkit

# Training configs in order
CONFIGS=(
    "train_sdxl_device_core_lora.yaml"
    "train_sdxl_strap_lora.yaml"
    "train_sdxl_clasp_lora.yaml"
    "train_sdxl_powerbank_lora.yaml"
    "train_sdxl_ring_frame_lora.yaml"
)

echo "=========================================="
echo "Starting Sequential SDXL LoRA Training"
echo "=========================================="
echo ""

for CONFIG in "${CONFIGS[@]}"; do
    CONFIG_PATH="$SCRIPT_DIR/$CONFIG"
    
    if [ ! -f "$CONFIG_PATH" ]; then
        echo "Warning: Config file not found: $CONFIG_PATH, skipping..."
        continue
    fi
    
    # Extract job name from config
    JOB_NAME=$(grep -E "^  name:" "$CONFIG_PATH" | head -1 | awk '{print $2}' || echo "unknown")
    OUTPUT_DIR="$SCRIPT_DIR/output_sdxl/$JOB_NAME"
    LOG_FILE="$OUTPUT_DIR/training.log"
    
    # Create output directory
    mkdir -p "$OUTPUT_DIR"
    
    echo "=========================================="
    echo "Starting: $CONFIG"
    echo "Job name: $JOB_NAME"
    echo "Output: $OUTPUT_DIR"
    echo "=========================================="
    
    # Start training with nohup
    cd /data/ai-toolkit
    nohup python run.py "$CONFIG_PATH" >> "$LOG_FILE" 2>&1 &
    TRAIN_PID=$!
    
    echo "Training started with PID: $TRAIN_PID"
    echo "Monitoring training progress..."
    echo ""
    
    # Save PID
    echo "$TRAIN_PID" > "$OUTPUT_DIR/training.pid"
    
    # Wait for training to complete
    echo "Waiting for training to complete..."
    while kill -0 "$TRAIN_PID" 2>/dev/null; do
        sleep 60
        # Show progress every minute
        if [ -f "$LOG_FILE" ]; then
            echo "$(date): Training in progress... (check $LOG_FILE for details)"
        fi
    done
    
    # Check exit status
    wait "$TRAIN_PID"
    EXIT_CODE=$?
    
    if [ $EXIT_CODE -eq 0 ]; then
        echo "✓ Training completed successfully: $CONFIG"
    else
        echo "✗ Training failed with exit code $EXIT_CODE: $CONFIG"
        echo "Check log: $LOG_FILE"
        read -p "Continue with next training? (y/n) " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "Stopping training sequence."
            exit 1
        fi
    fi
    
    echo ""
    echo "Waiting 30 seconds before starting next training..."
    sleep 30
    echo ""
done

echo "=========================================="
echo "All trainings completed!"
echo "=========================================="


