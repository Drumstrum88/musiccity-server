from rest_framework import serializers
from musiccityapi.models.postReactions import PostReaction

class PostReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostReaction
        fields = ['id', 'user', 'post', 'reaction', 'posted_reaction']
        depth = 1
