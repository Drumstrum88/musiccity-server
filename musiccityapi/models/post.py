from django.db import models
from musiccityapi.models.category import Category
from musiccityapi.models.user import User

class Post(models.Model):
  post_title = models.CharField(max_length=50, default='')
  post_author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
  post_content = models.CharField(max_length=400, default='')
  created_on = models.DateTimeField(auto_now_add=True)
  image_url = models.CharField(max_length=400, default='')
  categories = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
