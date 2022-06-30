import cv2
import numpy as np

fpath = "E:\\tzuwen\\tree_segmentation2\\Unet_tree_2\\2022-03-10_1031.png"

green = np.uint8([[[0,0,255]]])
hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print(hsv_green)

img = cv2.imread(fpath)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([0,43,46])
upper_red = np.array([10,255,255])
lower_blue = np.array([78,43,46])
upper_blue = np.array([99,255,255])
lower_indigo = np.array([100,43,46])
upper_indigo = np.array([124,255,255])
lower_purple = np.array([125,43,46])
upper_purple = np.array([155,255,255])

red_mask = cv2.inRange(hsv,lower_red,upper_red)
blue_mask = cv2.inRange(hsv,lower_blue,upper_blue)
indigo_mask = cv2.inRange(hsv,lower_indigo,upper_indigo)
purple_mask = cv2.inRange(hsv,lower_purple,upper_purple)


red = cv2.bitwise_and(img,img,mask=red_mask)
blue = cv2.bitwise_and(img,img,mask=blue_mask)
indigo = cv2.bitwise_and(img,img,mask=indigo_mask)
purple = cv2.bitwise_and(img,img,mask=purple_mask)

res =  red+blue+indigo+purple
cv2.imshow("oringnal",img)
cv2.imshow("HSV",hsv)
# cv2.imshow("mask", red_mask)
cv2.imshow("result",res)
cv2.waitKey(0)
#cv2.destoryAllWindows()