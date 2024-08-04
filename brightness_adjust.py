import numpy as np
import cv2
from matplotlib import pyplot as plt
import numpy as np
from graph_helper import plot_graph 

def adjust_gamma(image,gamma=1.0):
    img_normalized = img/255.0
    corrected_img = np.power(img_normalized, gamma)
    corrected_img = np.uint8(corrected_img * 255)
    return corrected_img

def plot_gamma_transformation(image,gamma=1.0):
    adjusted_image=adjust_gamma(image,gamma)
    original_pixels=image.flatten()
    adjusted_pixels=adjusted_image.flatten()
    plt.figure(figsize=(8,6))
    plt.scatter(original_pixels,adjusted_pixels,alpha=0.1,s=1)
    plt.plot([0,255],[0,255],color='red',linestyle='--')
    plt.title(f'Gamma Correction (Gamma={gamma})')
    plt.xlabel('Original Pixel Value')
    plt.ylabel('Adjusted Pixel Value')
    plt.xlim([0,255])
    plt.ylim([0,255])
    plt.grid(True)
    plt.show()

if __name__=='__main__':
    path=input("Enter the path of image: ")
    gamma=float(input("Enter the gamma falue \n>1 - Darken\n<1 - lighten\n1-same image\n"))
    img=cv2.imread(path)
    plot_graph.display_histogram(img,'Histogram before Adjusting brightness')
    gamma_corrected=adjust_gamma(img,gamma)
    plot_graph.display_histogram(gamma_corrected,f'Histogram after Adjusting brightness gamma={gamma}')
    stacked=np.hstack((img,gamma_corrected))
    cv2.imshow('Orginal and Gamma corrected image',stacked)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    plot_gamma_transformation(img,gamma)