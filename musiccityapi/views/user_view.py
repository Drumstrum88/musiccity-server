from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response
from musiccityapi.models import User
from musiccityapi.serializers import UserSerializer

class UserView(ViewSet):
  
  def list(self, request):
    """GET request for a list of all registered users"""
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
  
  def retrieve(self, request, pk):
    
    try:
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    except User.DoesNotExist as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
