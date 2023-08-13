"""
一括で変更する場合（直接サイズを入力、同階層全て）
"""

from PIL import Image
import os
import glob  #これで一括取得

photos = glob.glob("*.jpg")

#例　()'.data/images/*.png')

for i in photos:
    photo = Image.open(i)
    photo_mini=photo.resize((800,600))   #ここで大きさを決める(横、縦)

    #title取得
    title,ext=os.path.splitext(i)

    #「元のタイトル+拡張子」で保存
    photo_mini.save(title + ext)
