from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	status = models.CharField(max_length=200)
	original_image = models.TextField()
	processed_image = models.TextField()

	def __str__(self):
		return str(self.user)