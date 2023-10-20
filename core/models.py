from django.db import models

# Create your models here.
class Review(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    review = models.CharField(max_length=10000)
    created_on = models.DateTimeField(auto_now=True)