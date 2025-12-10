#!/usr/bin/env python3
"""Convert JSONL metadata to individual .txt caption files for diffusion-pipe."""

import json
import os
from pathlib import Path

# Paths
dataset_dir = Path("/data/kyana-images/dataset_videos")
metadata_file = dataset_dir / "metadata.jsonl"
videos_dir = dataset_dir / "videos"

# Read JSONL and create .txt files
with open(metadata_file, 'r') as f:
    for line in f:
        entry = json.loads(line.strip())
        video_filename = entry["file"].replace("videos/", "")
        prompt = entry["prompt"]
        
        # Create .txt file with same name as video
        txt_filename = video_filename.rsplit('.', 1)[0] + '.txt'
        txt_path = videos_dir / txt_filename
        
        # Write prompt to txt file
        with open(txt_path, 'w') as txt_file:
            txt_file.write(prompt)
        
        print(f"Created: {txt_filename}")

print(f"\nConversion complete! Created {sum(1 for _ in open(metadata_file))} caption files.")
