from django.db import models

# Create your models here.


class Patient(models.Model):
	Firstname = models.CharField(max_length=30)
	Lastname = models.CharField(max_length=30)
	Username = models.CharField(max_length=30)
	Password = models.CharField(max_length=30)
	Address = models.CharField(max_length=30)
	Mobile = models.IntegerField(null=True)
	Symptoms = models.CharField(max_length=20)

