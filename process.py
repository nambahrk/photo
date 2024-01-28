from PIL import Image, ImageFilter, ImageEnhance
import sys
import os

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



if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_image operation")
        print("Valid operations: blur, bright, compress, grayscale, monochrome, rotate")
    else:
        input_image_path = sys.argv[1]
        operation = sys.argv[2]

        img = Image.open(input_image_path)

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
        else:
            print("Invalid operation. Valid operations: blur, bright, compress, grayscale, monochrome, rotate")
