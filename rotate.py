from PIL import Image
import os
import glob  #これで一括取得

photos = glob.glob("*.jpg")

#例　()'.data/images/*.png')

for i in photos:
    photo = Image.open(i)
    photo_rotate = photo.rotate(90, expand=True)

    #title取得
    title,ext=os.path.splitext(i)

    #「元のタイトル+拡張子」で保存
    photo_rotate.save(title + ext)
