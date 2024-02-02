from rest_framework import serializers
from musiccityapi.models import Category

class CategorySerializer(serializers.ModelSerializer):
  """JSON serializer for all categories"""
  class Meta:
    model = Category
    fields = ('id', 'label')
    depth = 0
