from matplotlib import pyplot as plt
import numpy as np

class plot_graph:
    def display_histogram(img,title):
        hist,bins=np.histogram(img.flatten(),256,[0,256])
        plt.hist(img.flatten(),256,[0,256],color='blue')
        plt.title(title)
        plt.xlim([0,256])
        plt.show()    
    