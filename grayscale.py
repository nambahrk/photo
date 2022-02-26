from PIL import Image, ImageFilter

#pillowの画像開くライブラリ
img = Image.open("img.jpg")

# グレースケール変換
img_grayscale = img.convert('L')

#保存
img_grayscale.save("grayscale.jpg")
