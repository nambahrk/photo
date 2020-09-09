#同階層のjpgとjpegをpng変換する

from pathlib import Path

for f in Path('.').rglob('*.jpg'):
    f.rename(f.stem+'.png')

for f in Path('.').rglob('*.jpeg'):
    f.rename(f.stem+'.png')
