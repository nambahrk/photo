from PIL import Image

# 元画像の読み出し
img =Image.open("img.jpg")  

# グレースケール変換
img_grayscale = img.convert('L')

# モノクローム変換
img_monochrome = img_grayscale.convert('1')

#保存
img_monochrome.save("monochrome.jpg")    