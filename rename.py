"""
名前一括変更
"""

import os
import glob  #これで一括取得

files = glob.glob("*.jpg")

#例　()'.data/images/*.jpg')


for i, old_name in enumerate(files):
    os.rename(old_name,'img' + str(i+1) + '.jpg')
