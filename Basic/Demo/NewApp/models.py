from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
