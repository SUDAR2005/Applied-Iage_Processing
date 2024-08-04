import cv2
import numpy as np
from PIL import Image
from graph_helper import plot_graph

def hist_equalizer(color):
    h,bin_b=np.histogram(color.flatten(),256,[0,256])
    cdf=np.cumsum(h)
    cdf_m=np.ma.masked_equal(cdf,0)
    cdf_m=(cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    cdf_final=np.ma.filled(cdf_m,0).astype('uint8')
    return cdf_final[color]

def myhistogram_equalization(img):
    blue,green,red=cv2.split(img)
    equ_b=hist_equalizer(blue)
    equ_g=hist_equalizer(green)
    equ_r=hist_equalizer(red)
    equ=cv2.merge((equ_b,equ_g,equ_r))
    return equ

def histogram_equalization(img):
    blue,green,red=cv2.split(img)
    equ_b=cv2.equalizeHist(blue)
    equ_g=cv2.equalizeHist(green)
    equ_r=cv2.equalizeHist(red)
    equ=cv2.merge((equ_b,equ_g,equ_r))
    return equ

if __name__=='__main__':
    orginal=cv2.imread('./images/colors.jpeg')
    plot_graph.display_histogram(orginal,'Histogram before Equalization')
    #final=histogram_equalization(orginal)
    final=myhistogram_equalization(orginal)
    plot_graph.display_histogram(final,'Histogram after Equalization')
    ''' cv2.namedWindow("Before and After", cv2.WINDOW_NORMAL) 
    cv2.resizeWindow("Before and After", 700, 700) '''
    stacked = np.hstack((orginal,final))
    cv2.imshow('Before and After',stacked)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    