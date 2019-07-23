import cv2
import numpy as np           
import argparse, sys, os
import base64
from PIL import Image
from io import BytesIO

class Show_image():

	def show(self, img):
		img = img.resize((256, 256))
		img = img.convert('RGB') 

		img = np.array(img) 
		# Convert RGB to BGR 
		img = img[:, :, ::-1].copy() 


		imghls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
		imghls[np.where((imghls==[30,200,2]).all(axis=2))] = [0,200,0]
		huehls = imghls[:,:,0]
		huehls[np.where(huehls==[0])] = [35]
		ret, thresh = cv2.threshold(huehls,28,255,cv2.THRESH_BINARY_INV)
		thresh = thresh.astype('uint8')
		mask = cv2.bitwise_and(img,img,mask = thresh)

		_,contours,heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

		Infarea = 0
		for x in range(len(contours)):
			cv2.drawContours(img,contours[x],-1,(0,0,255))
			Infarea += cv2.contourArea(contours[x])

		img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
		pil_img = Image.fromarray(img.astype('uint8'), 'RGB')
		buff = BytesIO()
		pil_img.save(buff, format="JPEG")
		new_image_string = base64.b64encode(buff.getvalue()).decode("utf-8")

		return new_image_string