import cv2
from sys import argv
import numpy as np
import os
import glob

count = 0

def rust_detect(file):
	A = cv2.imread(file)
	img_hsv=cv2.cvtColor(A, cv2.COLOR_BGR2HSV)

	# Range for lower red
	lower_red = np.array([0,70,70])
	upper_red = np.array([20,200,150])
	mask0 = cv2.inRange(img_hsv, lower_red, upper_red)
	
	# range for upper red
	lower_red = np.array([170,70,70])
	upper_red = np.array([180,200,150])
	mask1 = cv2.inRange(img_hsv, lower_red, upper_red)
	
	# add both masks
	mask = mask0+mask1
	
	output_img = cv2.bitwise_and(A,A,mask=mask)
	
	print("\n\n\n Number of pixels depicting rust \n >> %d"%(np.sum(mask)/255))
	cv2.imshow('image1',output_img)
	cv2.imshow('image2',A)
	cv2.waitKey(0)
	cv2.imwrite('output_image%d.jpg'%count,output_img)
	cv2.imwrite('image%d.jpg'%count,A)
	cv2.destroyAllWindows()
	os.system("cls")
	
	
	
os.system("color 0a")
os.system("cls")

print(""" Welcome to the rust detection software!! 
 The software detects the rusted portion of metal
 and calculates nuber of rust piels for 
 comparitive analysis.\n\n""")
print("**********************************************")

images = glob.glob("Images/1AF-2204.jpg")

for path in images:
	count+=1
	rust_detect(path)

input("\n PRESS ENTER TO EXIT ")
