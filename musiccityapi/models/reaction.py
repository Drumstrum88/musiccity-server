from django.db import models

class Reaction(models.Model):
  
  label = models.CharField(max_length=20, default='')
  image_url = models.CharField(max_length=400, default='')
