import cv2
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
from graph_helper import plot_graph 
    
def buildin_rgb_hsi(path):
    image=cv2.imread(path)
    plot_graph.display_histogram(image,'Histogram of RGB image')
    hsv_image=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    plot_graph.display_histogram(hsv_image,'Histogram of HSV image')
    Image.fromarray(hsv_image).show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    buildin_rgb_hsi('./images/colors.jpeg')        