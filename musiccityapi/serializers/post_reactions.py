from rest_framework import serializers
from musiccityapi.models.postReactions import PostReaction

class PostReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostReaction
        fields = ['id', 'user_id', 'post_id', 'reaction_id']
        depth = 1
