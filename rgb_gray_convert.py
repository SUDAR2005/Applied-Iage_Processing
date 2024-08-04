import cv2
import numpy as np
import PIL.Image as im

def convert_to_grayscale(image_path):
    img=cv2.imread(image_path)
    B,G,R=cv2.split(img)
    gray=0.299*R + 0.587*G + 0.114*B
    return img,im.fromarray(gray)

if __name__ == "__main__":
    img,grayscale_image=convert_to_grayscale('./images/black-hole.jpeg')
    grayscale_image.show()