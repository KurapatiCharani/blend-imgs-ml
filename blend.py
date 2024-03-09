import cv2
import numpy as np

img1 = cv2.imread("E:\\blend\\thunder.jpg")
img1 = cv2.resize(img1,(500,600))

img2 = cv2.imread("E:\\blend\\ocean.jpg")
img2 = cv2.resize(img2,(500,600))

result = cv2.addWeighted(img1,0.4,img2,0.3,0)
cv2.imshow("animated clouds",result)

cv2.waitKey(0)
cv2.destroyAllWindows()
