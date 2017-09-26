import cv2
import numpy as np

scale = 1
delta = 0
ddepth = cv2.CV_16S

img = cv2.imread('lena.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Gradient-X
grad_x = cv2.Sobel(gray,ddepth,1,0,ksize = 3, scale = scale, delta = delta,borderType = cv2.BORDER_DEFAULT)
#grad_x = cv2.Scharr(gray,ddepth,1,0)

# Gradient-Y
grad_y = cv2.Sobel(gray,ddepth,0,1,ksize = 3, scale = scale, delta = delta, borderType = cv2.BORDER_DEFAULT)
#grad_y = cv2.Scharr(gray,ddepth,0,1)

abs_grad_x = cv2.convertScaleAbs(grad_x)   # converting back to uint8
abs_grad_y = cv2.convertScaleAbs(grad_y)

dst = cv2.addWeighted(abs_grad_x,0.5,abs_grad_y,0.5,0)
#dst = cv2.add(abs_grad_x,abs_grad_y)

cv2.imshow('dst',dst)