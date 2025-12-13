#!/usr/bin/env python3
"""
Rename files to use ring_frame terminology instead of COPPER_PINS, MAGNETIC, etc.

This script renames:
- COPPER_PINS_* → RING_FRAME_PINS_*
- MAGNETIC_* → RING_FRAME_MAGNETIC_*
- CORE_TO_RING_ATTACHMENT_* → RING_FRAME_ATTACHMENT_*
"""

import os
from pathlib import Path
import re

# Directories to process
DIRECTORIES = [
    Path("/data/kyana-images/dataset"),
    Path("/data/kyana-images/datasets/ring_frame"),
    Path("/data/kyana-images/dataset_videos/videos"),
]

# Renaming patterns: (old_pattern, new_pattern, description)
RENAME_PATTERNS = [
    (r"COPPER_PINS_", "RING_FRAME_PINS_", "Copper pins to ring frame pins"),
    (r"MAGNETIC_", "RING_FRAME_MAGNETIC_", "Magnetic to ring frame magnetic"),
    (r"CORE_TO_RING_ATTACHMENT_", "RING_FRAME_ATTACHMENT_", "Core to ring attachment to ring frame attachment"),
]

def rename_files_in_directory(directory):
    """Rename files in a directory according to patterns."""
    if not directory.exists():
        print(f"Directory {directory} does not exist, skipping...")
        return 0
    
    renamed_count = 0
    files_to_rename = []
    
    # Find all files that match patterns
    for file_path in directory.rglob("*"):
        if not file_path.is_file():
            continue
        
        filename = file_path.name
        new_filename = filename
        
        # Apply all rename patterns
        for old_pattern, new_pattern, _ in RENAME_PATTERNS:
            if re.search(old_pattern, filename):
                new_filename = re.sub(old_pattern, new_pattern, new_filename)
        
        if new_filename != filename:
            files_to_rename.append((file_path, new_filename))
    
    # Rename files
    for file_path, new_filename in files_to_rename:
        new_path = file_path.parent / new_filename
        try:
            file_path.rename(new_path)
            print(f"Renamed: {file_path.name} → {new_filename}")
            renamed_count += 1
        except Exception as e:
            print(f"Error renaming {file_path}: {e}")
    
    return renamed_count

def main():
    """Main function."""
    print("Renaming files to use ring_frame terminology...")
    print("=" * 60)
    
    total_renamed = 0
    
    for directory in DIRECTORIES:
        print(f"\nProcessing {directory}...")
        count = rename_files_in_directory(directory)
        total_renamed += count
        print(f"  Renamed {count} files")
    
    print("\n" + "=" * 60)
    print(f"Total files renamed: {total_renamed}")
    print("Done!")

if __name__ == "__main__":
    main()

