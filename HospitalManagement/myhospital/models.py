from django.db import models

# Create your models here.

class UserDetails(models.Model):
	Firstname = models.CharField(max_length=30)
	Lastname = models.CharField(max_length=30)
	Username = models.EmailField(max_length=40)
	Password = models.CharField(max_length=30)
	Address = models.CharField(max_length=50)
	Mobile = models.CharField(max_length=20,null=True)
	#Symptoms = models.CharField(m)
	#Image = models.ImageField(upload_to='Image/profilepic',null=True)

	

