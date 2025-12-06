#!/usr/bin/env python3
"""
Caption Generator for Kyana Watch Dataset
Generates descriptive .txt files for each image based on filename patterns.
"""

import os
from pathlib import Path
import re

def parse_filename(filename):
    """Extract components from filename to generate appropriate caption."""
    name = filename.replace('.png', '')
    parts = name.split('_')
    
    caption_parts = []
    
    # Component identification
    if 'FULL_ASSEMBLY' in name:
        caption_parts.append('kya-na health watch')
        if 'POWERBANK' in name:
            caption_parts.append('with powerbank attached')
        else:
            caption_parts.append('complete assembly')
    elif 'CORE_DEVICE' in name:
        caption_parts.append('kya-na watch core device')
    elif 'RING_STRAP' in name:
        caption_parts.append('kya-na watch ring with strap')
    elif 'POWERBANK' in name:
        caption_parts.append('kya-na powerbank accessory')
    elif 'CLASP' in name:
        caption_parts.append('kya-na watch clasp mechanism')
    elif 'COPPER_PINS' in name:
        caption_parts.append('kya-na watch copper connector pins')
    elif 'MAGNETIC' in name:
        caption_parts.append('kya-na watch magnetic connectors')
    elif 'BUTTON_SPEAKER' in name:
        caption_parts.append('kya-na watch button and speaker detail')
    elif 'DISPLAY' in name:
        caption_parts.append('kya-na watch LED display screen')
    elif 'ASSEMBLY' in name:
        caption_parts.append('kya-na watch assembly process')
    
    # Strap configuration
    if 'FLAT' in name:
        caption_parts.append('flat strap configuration')
    elif 'CIRCULAR' in name:
        caption_parts.append('circular wearable form')
    
    # Sensor states
    if 'SENSORS_ON' in name:
        caption_parts.append('biometric sensors active with LED glow')
    elif 'SENSORS_OFF' in name:
        caption_parts.append('sensors inactive')
    
    # Camera angles
    if '360' in name:
        caption_parts.append('rotating 360 degree view')
    elif 'FRONT' in name:
        caption_parts.append('front view')
    elif 'BACK' in name:
        caption_parts.append('back view')
    elif 'LEFT' in name:
        caption_parts.append('left side view showing speaker')
    elif 'RIGHT' in name:
        caption_parts.append('right side view showing button')
    elif 'TOP' in name:
        caption_parts.append('top view')
    elif 'BOTTOM' in name:
        caption_parts.append('bottom view showing sensors')
    elif 'LOW' in name:
        caption_parts.append('low angle view')
    elif 'HIGH' in name:
        caption_parts.append('high angle view')
    elif 'MID' in name:
        caption_parts.append('mid angle view')
    elif '2.5D' in name or '2_5D' in name:
        caption_parts.append('isometric 2.5D perspective')
    
    # Animation sequences
    if 'OPEN_ANIMATION' in name:
        caption_parts.append('opening animation sequence')
    elif 'CLOSE_ANIMATION' in name:
        caption_parts.append('closing animation sequence')
    elif 'CORE_TO_RING' in name:
        caption_parts.append('core device connecting to ring frame')
    elif 'POWERBANK_ATTACHMENT' in name:
        caption_parts.append('powerbank sliding into position')
    
    # Close-up details
    if 'CLOSEUP' in name or 'DETAIL' in name:
        caption_parts.append('close-up detail shot')
    
    # Material and design notes
    caption_parts.append('black metallic matte finish')
    caption_parts.append('33mm square watch form')
    
    # Add specific material details
    if 'SENSORS' in name or 'BOTTOM' in name or 'CORE_DEVICE' in name:
        caption_parts.append('chrome metal sensors on back')
    
    if 'STRAP' in name or 'FULL_ASSEMBLY' in name or 'RING_STRAP' in name:
        caption_parts.append('matte silicon strap with integrated sensors underneath')
    
    caption_parts.append('health smartwatch')
    
    return ', '.join(caption_parts)

def generate_captions(dataset_dir):
    """Generate caption txt files for all images in dataset."""
    dataset_path = Path(dataset_dir)
    
    if not dataset_path.exists():
        print(f"Error: Dataset directory not found: {dataset_dir}")
        return
    
    image_files = list(dataset_path.glob('*.png'))
    
    if not image_files:
        print(f"No PNG files found in {dataset_dir}")
        return
    
    print(f"Found {len(image_files)} images")
    print("Generating captions...")
    
    created_count = 0
    for img_path in image_files:
        txt_path = img_path.with_suffix('.txt')
        
        # Generate caption
        caption = parse_filename(img_path.name)
        
        # Write caption file
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(caption)
        
        created_count += 1
        
        if created_count % 50 == 0:
            print(f"  Progress: {created_count}/{len(image_files)}")
    
    print(f"\nComplete! Created {created_count} caption files")
    print(f"Location: {dataset_dir}")

if __name__ == '__main__':
    # Azure cloud path
    dataset_directory = '/data/kyana-images/dataset'
    
    # Fallback to local if running locally
    if not os.path.exists(dataset_directory):
        dataset_directory = './dataset'
    
    print("Kyana Watch Caption Generator")
    print(f"Dataset location: {dataset_directory}")
    print("-" * 50)
    
    generate_captions(dataset_directory)

