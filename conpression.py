from PIL import Image


#pngに限る
input_file = "./img.png"

img = Image.open(input_file)
img_p = img.convert('P')

#画像保存
img_p.save("compression.png")