import numpy
import cv2
from skimage.measure import compare_ssim
from skimage.io import imread
import imutils
import sys

	a=0
	b=0
	#def bf():
	#global a
	lowerBound=numpy.array([55,60,0])
	upperBound=numpy.array([90,200,255])
	cam= cv2.imread('./static/images/before.JPg')
	img=cv2.resize(cam,(340,220))
	imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	mask=cv2.inRange(imgHSV,lowerBound,upperBound)
	imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	mask=cv2.inRange(imgHSV,lowerBound,upperBound)
	ratio_white = cv2.countNonZero(mask)/(img.size/3)
	a=numpy.round(ratio_white*100, 2)
	print('Mangrove percentage(Before):', numpy.round(ratio_white*100, 2))
    #cv2.imshow("mask",mask)
	#cv2.imshow("cam1",img)
	cv2.imwrite("./static/images/before1.jpg",mask)
	#cv2.waitKey(80)
	#return a
	#def af():
	#global b
	lowerBound=numpy.array([55,60,0])
	upperBound=numpy.array([90,200,255])
	cam= cv2.imread('./static/images/after.JPg')
	img=cv2.resize(cam,(340,220))
	imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	mask=cv2.inRange(imgHSV,lowerBound,upperBound)
	ratio_white = cv2.countNonZero(mask)/(img.size/3)
	b=numpy.round(ratio_white*100, 2)
	print('Mangrove percentage(After):', numpy.round(ratio_white*100, 2))
	#cv2.imshow("mask",mask)
	#cv2.imshow("cam1",img)
	cv2.imwrite("./static/images/after1.jpg",mask)
	#cv2.waitKey(10)
	#return b
	#yield cv2.imencode('.jpg',mask)[1].tobytes(
	#def diff(a,b):
	c=a-b
	#return str(c)
	#print(a-b)
	print('Mangrove percentage difference:',c)
	#a=af()
	#b=bf()
	#diff(a,b)
	g = cv2.imread("./static/images/after1.jpg")
	h = cv2.imread("./static/images/before1.jpg")
	# convert the images to grayscale
	grayA = cv2.cvtColor(g, cv2.COLOR_BGR2GRAY)
	grayB = cv2.cvtColor(h, cv2.COLOR_BGR2GRAY)
	# compute the Structural Similarity Index (SSIM) between the two
	# images, ensuring that the difference image is returned
	(score, diff) = compare_ssim(grayA, grayB, full=True)
	diff = (diff * 255).astype("uint8") #DIFFERENCE IMAGE 
	#print("Change Percent: {}".format(score))
	# threshold the difference image, followed by finding contours to
	# obtain the regions of the two input images that differ
	#thresh image --> overlay on after image 
	thresh = cv2.threshold(diff, 0, 255,
	    cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
	cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	    cv2.CHAIN_APPROX_NONE) #chain approx none saves all points, not just vertices 
	#cnts = cnts[0] if imutils.is_cv2() else cnts[1]
	contours,hierarchy= cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) 
	#DO NOT DRAW BOUNDING BOXES.... DO INTENSITY
	#more change = more darker
	#contours round mangrove.... if loss, put intensity 
	# loop over the contours
	for i in contours:
	    # compute the bounding box of the contour and then draw the
	    # bounding box on both input images to represent where the two
	    # images differ
	    area = cv2.contourArea(i)
	    #if area > 1000:
	     #       cv2.drawContours(a,c,-1,(255,0,0),3)
	    if area > 300 and area < 5000:
	            cv2.drawContours(g,i,-1, (0,255,0),3)
	    if area > 200 and area < 300:
	            cv2.drawContours(g,i,-1,(255,0,0),3)
	     
	        
	# show the output images

	#cv2.imshow("After", a)
	#cv2.imshow("Before", b)
	cv2.imwrite("./static/images/change.jpg",g)

	#cv2.waitKey(0)
