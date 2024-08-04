import cv2
import numpy as np
from matplotlib import pyplot as plt

def log_transform(img):
    c=255/np.log(1+np.max(img)) 
    log_image=c*(np.log(img + 1)) 
    log_image=np.array(log_image, dtype=np.uint8)
    return log_image

def plot_log_transform(img):
    adjusted_image=log_transform(img)
    original_pixels=img.flatten()
    adjusted_pixels=adjusted_image.flatten()
    plt.figure(figsize=(8,6))
    plt.scatter(original_pixels,adjusted_pixels,alpha=0.1,s=1)
    plt.plot([0,255],[0,255],color='red',linestyle='--')
    plt.title(f'Log Transformation')
    plt.xlabel('Original Pixel Value')
    plt.ylabel('Adjusted Pixel Value')
    plt.xlim([0,255])
    plt.ylim([0,255])
    plt.grid(True)
    plt.show()

if __name__=='__main__':
    img=cv2.imread('./images/log-transform.png')
    log_img=log_transform(img)
    stack=np.hstack((img,log_img))
    cv2.imshow('Orginal vs Log transformed',stack)
    cv2.waitKey(0)
    cv2.destroyAllWindows
    plot_log_transform(img)
    