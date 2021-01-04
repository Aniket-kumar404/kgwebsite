from django.db import models

# Create your models here.
class employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email= models.CharField(max_length=50)
    date_of_birth=models.DateField()
    state= models.CharField(max_length=50)
    designation= models.CharField(max_length=50)
    

