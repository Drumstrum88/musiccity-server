from rest_framework import serializers
from musiccityapi.models import Category

class ReactionSerializer(serializers.ModelSerializer):
  """JSON serializer for all categories"""
  class Meta:
    model = Category
    fields = ('id', 'label', 'image_url')
    depth = 0
