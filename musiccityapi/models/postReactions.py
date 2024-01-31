from django.db import models

from musiccityapi.models.post import Post
from musiccityapi.models.reaction import Reaction
from musiccityapi.models.user import User

class PostReaction(models.Model):
  
  user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
  post_id = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
  reaction_id = models.ForeignKey(Reaction, on_delete=models.CASCADE, default=None)
