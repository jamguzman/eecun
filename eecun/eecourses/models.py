from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
	name = models.CharField(max_length=150)
	url_video = models.CharField(max_length=300)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now=True)
	subcriptors = models.ManyToManyField(User, through='Suscriptor')

	def __str__(self):
		return self.name

class Suscriptor(models.Model):
	user = models.ForeignKey(User)
	course = models.ForeignKey(Course)
	date_joined = models.DateTimeField(auto_now=True)