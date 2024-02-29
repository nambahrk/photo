from pathlib import Path  
from PIL import Image
import os
import glob 
import re

#change extension
for f in Path('.').rglob('*.(png|jpeg)'):
    f.rename(f.stem + '.jpg')

# rename files
files = sorted(glob.glob("*.jpg"), key=lambda x: [int(c) if c.isdigit() else c for c in re.split(r'(\D+|\d+)', x)])
for i, old_name in enumerate(files, start=1):
    os.rename(old_name, f'img{i}.jpg')

# change size 
photos = glob.glob("*.jpg")
for i in photos:
    photo = Image.open(i)
    photo_mini = photo.resize((800, 600))  

    title, ext = os.path.splitext(i)
    new_name = f'{title}.jpg'  
    photo_mini.save(new_name) 
    
