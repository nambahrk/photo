import cv2
import numpy as np
from PIL import Image

from pathlib import Path
import os
import glob  #これで一括取得

#同階層のjpgとjpegをppg変換する
for f in Path('.').rglob('*.jpg'):
    f.rename(f.stem+'.png')

for f in Path('.').rglob('*.jpeg'):
    f.rename(f.stem+'.png')

#透過
photos = glob.glob("*.png")

for i in photos:
    img = cv2.imread(i, -1)                       # -1はAlphaを含んだ形式(0:グレー, 1:カラー)
    color_lower = np.array([255, 0, 0, 255])                 # 抽出する色の下限(BGR形式)
    color_upper = np.array([255, 0, 0, 255])                 # 抽出する色の上限(BGR形式)
    img_mask = cv2.inRange(img, color_lower, color_upper)    # 範囲からマスク画像を作成
    img_bool = cv2.bitwise_not(img, img, mask=img_mask)      # 元画像とマスク画像の演算(背景を白くする)
    cv2.imwrite(i, img_bool)
