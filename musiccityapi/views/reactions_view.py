from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from musiccityapi.models import Reaction
from musiccityapi.serializers import ReactionSerializer

class ReactionsView(ViewSet):
  """Post Reactions View"""
  
  def retrieve(self, request, pk):
    """Handles GET request for single reaction"""
    
    try:
      reaction = Reaction.objects.get(pk=pk)
      serializer = ReactionSerializer(reaction)
      return Response(serializer.data)
    except Reaction.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

  def list(self, request):
    """Handles GET request for all reactions"""
    
    reaction = Reaction.objects.all()
    serializer = ReactionSerializer(reaction, many=True)
    return Response(serializer.data)
