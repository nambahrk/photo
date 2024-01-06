from pathlib import Path  
import os
import glob  
import re

for f in Path('.').rglob('*.png'):
    f.rename(f.stem+'.jpg')

for f in Path('.').rglob('*.jpeg'):
    f.rename(f.stem+'.jpg')

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

files = sorted(glob.glob("*.jpg"), key=natural_keys)

for i, old_name in enumerate(files):
    os.rename(old_name,'img' + str(i+1) + '.jpg')
