from PIL import Image, ImageFilter

#pillowの画像開くライブラリ
img = Image.open("img.jpg")

#ぼかす
img_blur = img.filter(ImageFilter.GaussianBlur(8))

#保存
img_blur.save("blur.jpg")
