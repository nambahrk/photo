"""
名前一括変更
"""

from pathlib import Path  #同階層のpngとjpegをjpg変換する
import os
import glob  #これで一括取得

#同階層のpngとjpegをjpg変換する
for f in Path('.').rglob('*.png'):
    f.rename(f.stem+'.jpg')

for f in Path('.').rglob('*.jpeg'):
    f.rename(f.stem+'.jpg')

#jpg取得
files = glob.glob("*.jpg")

#例　()'.data/images/*.jpg')


for i, old_name in enumerate(files):
    os.rename(old_name,'img' + str(i+1) + '.jpg')
