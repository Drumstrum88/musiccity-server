from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from musiccityapi.models import PostReaction, User, Post, Reaction
from musiccityapi.serializers.post_reactions import PostReactionSerializer

class PostReactionView(ViewSet):
  """Post Reaction View"""
  
  def retrieve(self, request, pk):
    """Handles GET request for single post reaction"""
    
    try:
      post_reaction = PostReaction.objects.get(pk=pk)
      serializer = PostReactionSerializer(post_reaction)
      return Response(serializer.data)
    except PostReaction.DoesNotExist as ex:
      return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
  def list(self, request):
      """Handles GET request for all post reactions"""
      
      post_reactions = PostReaction.objects.all()
      serializer = PostReactionSerializer(post_reactions, many=True)
      return Response(serializer.data)
    
  def destroy(self, request, pk):
    """Handles DELETE request for post reaction"""
    
    post_reaction = PostReaction.objects.get(pk=pk)
    post_reaction.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  def create(self, request):
    """Handles POST request for adding reactions to a post"""
    
    user = User.objects.get(pk=request.data["user"])
    post = Post.objects.get(pk=request.data["post"])
    reaction = Reaction.objects.get(pk=request.data["reaction"])
    
    post_reaction = PostReaction.objects.create(
      user_id=user,
      post_id=post,
      reaction_id=reaction,
    )
    
    serializer = PostReactionSerializer(post_reaction)
    return Response(serializer.data)
    
