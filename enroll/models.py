from django.db import models

# Create your models here.
class Students(models.Model):
    stu_name =models.CharField(max_length=50)
    course=models.CharField(max_length=30)