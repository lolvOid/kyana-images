#!/usr/bin/env python3
"""
Organize SDXL dataset into categories and inject unique tokens into captions.

This script:
1. Scans the dataset directory for .png and .txt file pairs
2. Organizes them into category-specific folders
3. Automatically injects unique tokens into captions
"""

import os
import shutil
from pathlib import Path
from collections import defaultdict

# Configuration
SOURCE_DIR = Path("/data/kyana-images/dataset")
OUTPUT_BASE = Path("/data/kyana-images/datasets")

# Category definitions: (category_name, [prefixes], token)
# Note: AI-Toolkit expects images and captions in the same folder
CATEGORIES = [
    ("device_core", ["FULL_DEVICE", "CORE_DEVICE"], "<devX>"),
    ("strap", ["STRAP", "RING_STRAP"], "<strapX>"),
    ("clasp", ["CLASP"], "<claspX>"),
    ("powerbank", ["POWERBANK", "FULL_WITH_POWERBANK"], "<powerX>"),
    ("internal_details", ["MAGNETIC", "COPPER_PINS"], "<internalX>"),
]

def get_file_category(filename):
    """Determine which category a file belongs to based on filename prefix."""
    filename_upper = filename.upper()
    for category_name, prefixes, _ in CATEGORIES:
        for prefix in prefixes:
            if filename_upper.startswith(prefix):
                return category_name, CATEGORIES[[c[0] for c in CATEGORIES].index(category_name)][2]
    return None, None

def inject_token(caption_file, token):
    """Inject token at the beginning of caption if not already present."""
    try:
        with open(caption_file, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        
        if not content:
            return False
        
        if content.startswith(token):
            return False
        
        new_content = f"{token} {content}"
        
        with open(caption_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
    except Exception as e:
        print(f"Error processing caption {caption_file}: {e}")
        return False

def organize_dataset():
    """Main function to organize the dataset."""
    stats = defaultdict(lambda: {"images": 0, "captions": 0, "updated": 0})
    unmatched_files = []
    
    if not SOURCE_DIR.exists():
        print(f"Error: Source directory {SOURCE_DIR} does not exist!")
        return
    
    OUTPUT_BASE.mkdir(parents=True, exist_ok=True)
    
    print(f"Scanning {SOURCE_DIR} for image-caption pairs...")
    
    image_files = sorted(SOURCE_DIR.glob("*.png"))
    total_files = len(image_files)
    
    print(f"Found {total_files} image files")
    
    for img_file in image_files:
        img_name = img_file.stem
        caption_file = SOURCE_DIR / f"{img_name}.txt"
        
        if not caption_file.exists():
            print(f"Warning: No caption file for {img_file.name}")
            unmatched_files.append(img_file.name)
            continue
        
        category, token = get_file_category(img_file.name)
        
        if not category:
            print(f"Warning: No category match for {img_file.name}")
            unmatched_files.append(img_file.name)
            continue
        
        category_dir = OUTPUT_BASE / category
        category_dir.mkdir(parents=True, exist_ok=True)
        
        dest_img = category_dir / img_file.name
        dest_caption = category_dir / caption_file.name
        
        shutil.copy2(img_file, dest_img)
        shutil.copy2(caption_file, dest_caption)
        
        stats[category]["images"] += 1
        stats[category]["captions"] += 1
        
        if inject_token(dest_caption, token):
            stats[category]["updated"] += 1
    
    print("\n" + "="*60)
    print("Organization Summary")
    print("="*60)
    
    total_images = 0
    total_captions = 0
    total_updated = 0
    
    for category, data in sorted(stats.items()):
        print(f"\n{category}:")
        print(f"  Images: {data['images']}")
        print(f"  Captions: {data['captions']}")
        print(f"  Tokens injected: {data['updated']}")
        total_images += data['images']
        total_captions += data['captions']
        total_updated += data['updated']
    
    print(f"\nTotal:")
    print(f"  Images organized: {total_images}")
    print(f"  Captions organized: {total_captions}")
    print(f"  Captions updated: {total_updated}")
    
    if unmatched_files:
        print(f"\nWarning: {len(unmatched_files)} files could not be categorized")
        if len(unmatched_files) <= 20:
            for f in unmatched_files:
                print(f"  - {f}")
        else:
            print(f"  (showing first 20 of {len(unmatched_files)})")
            for f in unmatched_files[:20]:
                print(f"  - {f}")
    
    print(f"\nOrganized datasets saved to: {OUTPUT_BASE}")
    print("\nDone!")

if __name__ == "__main__":
    organize_dataset()

