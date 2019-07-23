from django.shortcuts import render
import requests
from django.http import HttpResponse
from django.template import Context, loader
import numpy as np
from classifier import Classifier
from PIL import Image
from processed_image import Show_image
import base64
from io import BytesIO
import cv2

from .models import Question

clf = Classifier()
output = Show_image()

def history(request):
	print(request.user)
	data = Question.objects.filter(user=request.user)
	return render(request,'polls/history.html',{"data":data})

def home(request):

	flag = (request.method == "POST")
	if flag:
		# print(request.FILES)
		data = request.FILES.copy()
		file = data.get('query_img')
		img = Image.open(file)

		new_img = img.resize((256, 256))
		new_img = new_img.convert('RGB') 
		new_img = np.array(new_img) 
		pil_img = Image.fromarray(new_img.astype('uint8'), 'RGB')
		buff = BytesIO()
		pil_img.save(buff, format="JPEG")
		new_img = base64.b64encode(buff.getvalue()).decode("utf-8")
		new_img = "data:image/jpeg;base64," + new_img

		status,prob = clf.predict(img)
		probability = max(prob)
		output_image = output.show(img)
		output_image = "data:image/jpeg;base64," + output_image
		context = {"status":status, "output":output_image, "input":new_img, "flag":flag}

		ques = Question()
		ques.user = request.user
		ques.status = status
		ques.original_image = new_img
		ques.processed_image = output_image
		ques.save()

		return render(request, 'polls/home.html', context)

	return render(request,'polls/home.html',{"flag":flag})