import numpy as np
from graph_helper import plot_graph
import cv2
import numpy as np

def low_contrast(path):
    image=cv2.imread(path,0)
    plot_graph.display_histogram(image,'Histogram before applying Threshold')
    _,thresholded_image=cv2.threshold(image,200,255,cv2.THRESH_BINARY)
    plot_graph.display_histogram(image,'Histogram after applying Threshold')
    stack=np.hstack((image,thresholded_image))
    cv2.imshow('Comparision',stack)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def high_contrast(path):
    image=cv2.imread(path,0)
    plot_graph.display_histogram(image,'Histogram before CLAHE')
    clahe=cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
    hc_image=clahe.apply(image)
    plot_graph.display_histogram(hc_image,'Histogram after CLAHE')
    stack=np.hstack((image,hc_image))
    cv2.imshow('Comparision',stack)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  

if __name__=='__main__':
    path=input('Enter the path: ')
    low_contrast(path)
    high_contrast(path)
    