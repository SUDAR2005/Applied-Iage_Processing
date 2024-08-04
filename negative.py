import cv2
gray=cv2.imread('./images/colors.jpeg',0)
gray_neg=cv2.bitwise_not(gray)
cv2.imshow('Normal Image',gray)
cv2.imshow('Negative Image',gray_neg)
cv2.waitKey(0)
cv2.destroyAllWindows()
