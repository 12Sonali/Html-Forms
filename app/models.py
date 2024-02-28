from django.db import models

# Create your models here.
class School(models.Model):
    Schoolname=models.CharField(max_length=100)
    Schoollocation=models.CharField(max_length=100)
    Schoolprincipal=models.CharField(max_length=100)
    email=models.EmailField(default='hey@gmail.com')
    reenteremail=models.EmailField(default='hey@gmail.com')


    def __str__(self):
        return self.schoolname
