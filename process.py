from PIL import Image, ImageFilter, ImageEnhance #Pillow
import cv2 #OpenCV
import sys
import numpy as np
from pathlib import Path


def blur(img):
    img_blur = img.filter(ImageFilter.GaussianBlur(8))
    img_blur.save("blur.jpg")

def bright(img):
    brightnessEnhancer = ImageEnhance.Brightness(img)
    img_brightness = brightnessEnhancer.enhance(1.5)
    img_brightness.save("brightness.jpg")

def compress(img):
    img_p = img.convert('P')
    img_p.save("compression.png")

def grayscale(img):
    img_grayscale = img.convert('L')
    img_grayscale.save("grayscale.jpg")

def monochrome(img):
    img_grayscale = img.convert('L')
    img_monochrome = img_grayscale.convert('1')
    img_monochrome.save("monochrome.jpg")       

def rotate(img):
    img_rotate = img.rotate(90, expand=True)
    img_rotate.save("rotate.jpg")    

def anime(img):
    k=20
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply blur and edge detection
    edge = cv2.blur(gray, (3, 3))
    edge = cv2.Canny(edge, 50, 150, apertureSize=3)
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

    # Adjust image intensity
    img = np.array(img / k, dtype=np.uint8)
    img = np.array(img * k, dtype=np.uint8)

    # Subtract edge from the original image
    anime = cv2.subtract(img, edge)

    cv2.imwrite("./anime.jpg", anime)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python process.py input_image operation")
        print("Valid operations: blur, bright, compress, grayscale, monochrome, rotate, anime")
    else:
        input_image_path = sys.argv[1]
        operation = sys.argv[2]

        img = Image.open(input_image_path)
        img2 = cv2.imread(input_image_path)

        if operation == "blur":
            blur(img)
        elif operation == "bright":
            bright(img)
        elif operation == "compress":
            compress(img)
        elif operation == "grayscale":
            grayscale(img)
        elif operation == "monochrome":
            monochrome(img)    
        elif operation == "rotate":
            rotate(img)               
        elif operation == "anime":
            anime(img2)    
        else:
            print("Invalid operation. Valid operations: blur, bright, compress, grayscale, monochrome, rotate, anime")

