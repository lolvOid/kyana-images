#!/bin/bash
# Check status of all SDXL training jobs

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_DIR="$SCRIPT_DIR/output_sdxl"

echo "=========================================="
echo "SDXL Training Status"
echo "=========================================="
echo ""

if [ ! -d "$OUTPUT_DIR" ]; then
    echo "No training output directory found."
    exit 0
fi

for JOB_DIR in "$OUTPUT_DIR"/*/; do
    if [ ! -d "$JOB_DIR" ]; then
        continue
    fi
    
    JOB_NAME=$(basename "$JOB_DIR")
    PID_FILE="$JOB_DIR/training.pid"
    LOG_FILE="$JOB_DIR/training.log"
    
    echo "Job: $JOB_NAME"
    echo "  Directory: $JOB_DIR"
    
    if [ -f "$PID_FILE" ]; then
        PID=$(cat "$PID_FILE")
        if ps -p "$PID" > /dev/null 2>&1; then
            echo "  Status: RUNNING (PID: $PID)"
            # Get GPU usage if available
            if command -v nvidia-smi &> /dev/null; then
                GPU_MEM=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits | head -1)
                echo "  GPU Memory: ${GPU_MEM} MB"
            fi
        else
            echo "  Status: COMPLETED/STOPPED (PID: $PID no longer running)"
        fi
    else
        echo "  Status: UNKNOWN (no PID file)"
    fi
    
    if [ -f "$LOG_FILE" ]; then
        LOG_SIZE=$(du -h "$LOG_FILE" | cut -f1)
        LAST_LINE=$(tail -1 "$LOG_FILE" 2>/dev/null | cut -c1-80)
        echo "  Log: $LOG_FILE ($LOG_SIZE)"
        if [ -n "$LAST_LINE" ]; then
            echo "  Last log: $LAST_LINE"
        fi
    fi
    
    # Check for checkpoints
    CHECKPOINTS=$(find "$JOB_DIR" -name "checkpoint-*.safetensors" 2>/dev/null | wc -l)
    if [ "$CHECKPOINTS" -gt 0 ]; then
        echo "  Checkpoints: $CHECKPOINTS found"
        LATEST=$(find "$JOB_DIR" -name "checkpoint-*.safetensors" -printf '%T@ %p\n' 2>/dev/null | sort -n | tail -1 | cut -d' ' -f2- | xargs basename)
        echo "  Latest: $LATEST"
    fi
    
    echo ""
done

echo "=========================================="
echo "Active Training Processes:"
ps aux | grep "run.py.*train_sdxl" | grep -v grep || echo "  None"
echo "=========================================="


