import cv2
import numpy as np

img = cv2.imread("photo.jpg")

img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


cv2.imshow("window",img)
cv2.waitKey(0)