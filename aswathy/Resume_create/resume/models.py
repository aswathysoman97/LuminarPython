from django.db import models

# Create your models here.
class Create(models.Model):
    email=models.CharField(max_length=120)
    fullname=models.CharField(max_length=120)
    dob=models.CharField(max_length=120)
    qualification=models.CharField(max_length=120)
    profile_picture=models.ImageField(upload_to="images")
    def __str__(self):
        return self.fullname