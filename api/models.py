from django.db import models

# Create your models here.

class Count_data(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	livename = models.CharField(max_length=100)
	count = models.IntegerField()
    
