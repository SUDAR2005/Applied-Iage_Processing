import cv2
import numpy as np
import matplotlib.pyplot as plt
from graph_helper import plot_graph 

def myEqualizeHist(img):
    hist,bins=np.histogram(img.flatten(),256,[0,256])
    cdf=np.cumsum(hist)
    cdf_m=np.ma.masked_equal(cdf,0)
    cdf_m=(cdf_m-cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    cdf_final=np.ma.filled(cdf_m,0).astype('uint8')
    img=cdf_final[img]
    return img
    
def main(path,function):
    img=cv2.imread(path,0)
    plot_graph.display_histogram(img,'Image before Equalization')
    equalized_img=function(img)
    plot_graph.display_histogram(equalized_img,'Image after Equalization')
    comp_stack=np.hstack((img,equalized_img))
    cv2.imshow('Image before and after histigram equilization',comp_stack)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
    
if __name__=='__main__':
    print('Predefined Histogram Equalizer')
    main('./images/moon-crater.jpeg',cv2.equalizeHist)
    print('My Histogram Equalizer')
    main('./images/moon-crater.jpeg',myEqualizeHist)
    
     