from rest_framework import serializers
from musiccityapi.models import Reaction

class ReactionSerializer(serializers.ModelSerializer):
  """JSON serializer for all reactions"""
  class Meta:
    model = Reaction
    fields = ('id', 'label', 'image_url')
    depth = 0
