from django.db import models

from musiccityapi.models.post import Post
from musiccityapi.models.reaction import Reaction
from musiccityapi.models.user import User

class PostReaction(models.Model):
  
  user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
  post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None, related_name='post_reactions')
  reaction = models.ForeignKey(Reaction, on_delete=models.CASCADE, default=None)
  
  @property
  def posted_reaction(self):
    reaction_id = self.reaction.id
    post_id = self.post.id
    return PostReaction.objects.filter(reaction__id=reaction_id, post__id=post_id).count()
