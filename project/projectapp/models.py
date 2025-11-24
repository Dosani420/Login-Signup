from django.db import models

# Create your models here.

class person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100,default="Null")

    def __str__(self):
        return self.name