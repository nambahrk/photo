"""
一括で変更する場合（任意の大きさを入力）
"""

from PIL import Image
import os
import glob  #これで一括取得

photos = glob.glob(ディレクトリ入力)

#例　()'.data/images/*.png')

print("横、縦の長さを入力")

width,height=map(int,input().split())


for i in images:
    photo = Image.open(i)
    #タプル形式で入力
    photo_mini=photo.resize(width,height)

    #title取得
    title,ext=os.path.splitext(i)

    #「元のタイトル+mini+拡張子」で保存
    photo_mini.save(title + 'mini'+ ext)
