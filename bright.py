from PIL import Image, ImageEnhance

# 元画像の読み出し
img =Image.open("img.jpg")  

#コントラスト変更
brightnessEnhancer = ImageEnhance.Contrast(img)
img_brightness = brightnessEnhancer.enhance(1.5)

#保存
img_brightness.save("brightness.jpg")  