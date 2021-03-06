from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class Corse(models.Model):
# 	title = models.CharField(max_length=30)
class Course_details(models.Model):
	title = models.CharField(max_length=30)
	image = models.ImageField(upload_to='course_images/',null=True,blank=True)
	description = models.TextField(null=True)


class Course_Content(models.Model):
 	user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
 	video = models.FileField(upload_to='course_videos/')
 	theory = models.TextField(null=True)


 	def __str__(self):
 		return self.theory


