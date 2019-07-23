import numpy as np
import cv2
from keras.preprocessing.image import img_to_array  
from keras.models import Sequential,load_model      
import argparse, sys, os
import tensorflow as tf

class Classifier():

	def __init__(self):
		self.model = load_model('E_demo.h5')
		self.model._make_predict_function()
		self.graph = tf.get_default_graph()

	def predict(self, img):
		img = img.resize((256, 256))
		img = img.convert('RGB')
		x = img_to_array(img)
		x = x[:, :, ::-1].copy()
		x = np.array(x, dtype=np.float16) / 255.0
		x = np.expand_dims(x, axis=0)
		with self.graph.as_default():
			output = self.model.predict(x)

		k=0
		for i in output[0]:
			if i==max(output[0]):
				output[0][k]=1	
			else:
				output[0][k]=0
			k=k+1

		output=list(output[0])
		# print(type(output))

		if output == [0,1,0,0]:
			status="Early blight"

		elif output == [0,0,0,1]:
			status="Late blight"

		elif output == [1,0,0,0]:
			status="Bacterial spot"

		elif output == [0,0,1,0]:
			status = "Healthy"

		return status
