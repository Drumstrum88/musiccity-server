from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from musiccityapi.models.post import Post
from musiccityapi.serializers.post_reactions import PostReactionSerializer
class PostSerializer(serializers.ModelSerializer):
  created_on = serializers.DateTimeField(format="%Y-%m-%d")
  reactions = PostReactionSerializer(many=True, read_only=True)
  
  class Meta:
    model = Post
    fields = ('id', 'post_title', 'post_author', 'post_content', 'created_on', 'image_url', 'categories', 'reactions')
    depth = 1
