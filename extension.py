from pathlib import Path

def tojpg():
    for f in Path('.').rglob('*.png'):
        f.rename(f.stem+'.jpg')
    for f in Path('.').rglob('*.jpeg'):
        f.rename(f.stem+'.jpg')

def topng():
    for f in Path('.').rglob('*.jpg'):
        f.rename(f.stem+'.png')
    for f in Path('.').rglob('*.jpeg'):
        f.rename(f.stem+'.png')
