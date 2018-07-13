#import libraries
import cv2
import numpy as np
import os

#import classifier for face and eye detection
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Import Classifier for Face and Eye Detection
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
r = cv2.CascadeClassifier ('haarcascade_profileface.xml')
def face_detector (img, size=0.5):
	try:
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	except Exception as e:
		return 0,img

	
	faces = face_classifier.detectMultiScale(gray,1.3,5)
	if faces is ():
		faces = r.detectMultiScale(gray,1.3,5)
		if faces is ():
			return 0,img
	# Given coordinates to detect face and eyes location from ROI
	print len (faces)
	roi_color=[]

	for (x, y, w, h) in faces:
		c=15
		x = x - c 
		w = w + c 
		y = y - c 
		h = h + c
		roi_gray = gray[y: y+h, x: x+w]
		roi_color.append( img[y: y+h, x: x+w])
	leng= roi_color.__len__()
	print leng
	return leng,roi_color
		# Webcam setup for Face Detection



n=0
for path in os.listdir("inputs"):
	print path
	cap = cv2.imread("inputs/"+path)
	#cap = cv2.resize(cap, (400, 300)) 
	
	leng ,frames = face_detector (cap)
	for i in range (0,leng):
		cv2.imwrite("outputs/test%d.jpg" % n ,frames[i])
		n+=1
