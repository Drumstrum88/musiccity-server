from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from musiccityapi.models import Category
from musiccityapi.serializers import CategorySerializer

class CategoryView(ViewSet):
  """Post Category View"""
  
  def retrieve(self, request, pk):
    """Handles GET request for single category"""
    
    try:
      category = Category.objects.get(pk=pk)
      serializer = CategorySerializer(category)
      return Response(serializer.data)
    except Category.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

  def list(self, request):
    """Handles GET request for all category options"""
    
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)
