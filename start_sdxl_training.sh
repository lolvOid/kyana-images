#!/bin/bash
# Start SDXL LoRA training in non-interruptible mode
# Usage: ./start_sdxl_training.sh [config_file]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Activate conda environment
source /data/miniconda3/etc/profile.d/conda.sh
conda activate ai-toolkit

# Default config if not provided
CONFIG_FILE="${1:-train_sdxl_device_core_lora.yaml}"
CONFIG_PATH="$SCRIPT_DIR/$CONFIG_FILE"

if [ ! -f "$CONFIG_PATH" ]; then
    echo "Error: Config file not found: $CONFIG_PATH"
    exit 1
fi

# Extract job name from config
JOB_NAME=$(grep -E "^  name:" "$CONFIG_PATH" | head -1 | awk '{print $2}' || echo "unknown")
OUTPUT_DIR="$SCRIPT_DIR/output_sdxl/$JOB_NAME"
LOG_FILE="$OUTPUT_DIR/training.log"

# Create output directory
mkdir -p "$OUTPUT_DIR"

echo "Starting training for: $CONFIG_FILE"
echo "Job name: $JOB_NAME"
echo "Output directory: $OUTPUT_DIR"
echo "Log file: $LOG_FILE"
echo ""

# Start training with nohup (non-interruptible)
cd /data/ai-toolkit
nohup python run.py "$CONFIG_PATH" >> "$LOG_FILE" 2>&1 &
TRAIN_PID=$!

# Wait a moment for process to start
sleep 2

# Get the actual Python process PID (child of nohup)
ACTUAL_PID=$(ps aux | grep "python run.py.*$(basename "$CONFIG_PATH")" | grep -v grep | awk '{print $2}' | head -1)

if [ -n "$ACTUAL_PID" ]; then
    echo "$ACTUAL_PID" > "$OUTPUT_DIR/training.pid"
    echo "Training started with PID: $ACTUAL_PID"
else
    echo "$TRAIN_PID" > "$OUTPUT_DIR/training.pid"
    echo "Training started with PID: $TRAIN_PID"
fi

echo "To monitor progress: tail -f $LOG_FILE"
echo "To check GPU usage: nvidia-smi"
echo "To stop training: kill \$(cat $OUTPUT_DIR/training.pid)"
echo ""
echo "Process will continue even if terminal is closed."
echo "PID saved to: $OUTPUT_DIR/training.pid"

