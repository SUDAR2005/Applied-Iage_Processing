import cv2
import numpy as np

def contrast_stretch(img):
    min_val=np.min(img)
    max_val=np.max(img)
    stretched_img=(img-min_val)*(255.0/(max_val-min_val))
    stretched_img=np.uint8(stretched_img)
    return stretched_img

def contrast_stretch_color(img):
    channels=cv2.split(img)
    stretched_channels=[]
    for channel in channels:
        min_val=np.min(channel)
        max_val=np.max(channel)
        stretched_channel=(channel-min_val)*(255.0/(max_val-min_val))
        stretched_channel=np.uint8(stretched_channel)
        stretched_channels.append(stretched_channel)
    stretched_img=cv2.merge(stretched_channels)
    return stretched_img
def main(path,key=0):
    img=cv2.imread(path,key)
    stretched_img=contrast_stretch(img)
    stack=np.hstack((img,stretched_img))
    cv2.imshow('Original vs Contrast Stretched',stack)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__=='__main__':
    main('images\low-contrast.jpeg',0)
    main('images\low-contrast.jpeg',3)