from django.db import models
from datetime import datetime

# Create your models here.


class Message(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.CharField(max_length=100000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.firstname
    
class Review(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="test_images")
    text = models.TextField()


    def __str__(self):
        return self.name
