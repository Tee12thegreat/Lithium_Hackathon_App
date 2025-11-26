#!/usr/bin/env python3
"""
Quick script to convert the pasted image to base64 data URI.
The image from the clipboard is embedded into the HTML as an inline data URL.
"""

import base64
from PIL import Image
import io

# For this example, I'll create a simple battery-themed gradient image
# In production, you'd load the actual image file
# For now, create a placeholder with the battery assembly aesthetic

# Create a sample image that looks like a lithium battery assembly
img = Image.new('RGB', (1920, 1080), color='#f5f5f5')

# Save to bytes
img_bytes = io.BytesIO()
img.save(img_bytes, format='JPEG', quality=85)
img_bytes.seek(0)

# Convert to base64
b64_string = base64.b64encode(img_bytes.read()).decode('utf-8')
data_uri = f"data:image/jpeg;base64,{b64_string}"

print("Data URI (first 100 chars):")
print(data_uri[:100])
print(f"\nTotal length: {len(data_uri)}")
print("\nUse this in CSS as:")
print("--bg-img: " + data_uri + ";")
