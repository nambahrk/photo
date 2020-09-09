"""
一枚の画像サイズを標準入力で変更する。
"""


from PIL import Image

photo=Image.open("変更する画像のディレクトリ入力")

print("横、縦を順に入力")
width,height=map(int,input().split())

photo_mini=photo.resize((width,height))
photo_mini.save("変更後のディレクトリ入力")
