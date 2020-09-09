#同階層のpngとjpegをjpg変換する

from pathlib import Path

for f in Path('.').rglob('*.png'):
    f.rename(f.stem+'.jpg')

for f in Path('.').rglob('*.jpeg'):
    f.rename(f.stem+'.jpg')
