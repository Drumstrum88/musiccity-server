from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from musiccityapi.models import Category
from musiccityapi.models import Post
from musiccityapi.models import PostReaction
from musiccityapi.models import User
from musiccityapi.serializers import PostReactionSerializer
from musiccityapi.serializers import PostSerializer
from django.db.models import Count
from rest_framework import serializers

    
class PostView(ViewSet):
  """Post View"""
  
  """Handles GET for single post"""
  
  def retrieve(self, request, pk):
    try: 
      post = Post.objects.get(pk=pk)
      serializer = PostSerializer(post)
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Post.DoesNotExist as ex:
      return Response({'message' : ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)


  def list(self, request):
    """Handles GET request for all Posts"""
    
    posts = Post.objects.all()
    post = Post.objects.annotate(reaction_count=Count('post_reactions'))
    serializer = ViewPostReactionSerializer(post, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def create(self, request):
        """Handles POST request for a new Post"""

        post_author = User.objects.get(pk=request.data.get('post_author'))
        categories = Category.objects.get(pk=request.data.get('categories'))

        post = Post.objects.create(
            post_author=post_author,
            categories=categories,
            post_title=request.data.get('post_title'),
            post_content=request.data.get('post_content'),
            image_url=request.data.get('image_url'),
            created_on=request.data.get('created_on')
        )

        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

  def update(self, request, pk):
        """Handles PUT for a Post"""

        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response({'error': "Post Does Not Exist"}, status=status.HTTP_404_NOT_FOUND)

        post_author = User.objects.get(pk=request.data.get('post_author', post.post_author.pk))
        category = Category.objects.get(pk=request.data.get('categories', post.categories.pk))

        post.post_author = post_author
        post.category = category

        if 'post_title' in request.data:
            post.post_title = request.data['post_title']

        if 'post_content' in request.data:
            post.post_content = request.data['post_content']

        if 'image_url' in request.data:
            post.image_url = request.data['image_url']

        if 'created_on' in request.data:
            post.created_on = request.data['created_on']

        post.save()
        serializer = PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)
  
  
  def destroy(self, request, pk):
    """Handles DELETE for a Post"""
    
    post = Post.objects.get(pk=pk)
    post.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
  
  @action(methods=['get'], detail=True)
  def reactions(self, request, pk):
        """Method to get all the reactions associated with a single post"""
        reactions = PostReaction.objects.filter(post_id=pk)

        serializer = PostReactionSerializer(reactions, many=True)
        return Response(serializer.data)

class ViewPostReactionSerializer(serializers.ModelSerializer):
  reaction_count = serializers.IntegerField(default=None)
  created_on = serializers.DateTimeField(format="%Y-%m-%d")
  reactions = PostReactionSerializer(many=True, read_only=True)
  class Meta:
    model = Post
    fields = ('id', 'post_title', 'post_author', 'post_content', 'created_on', 'image_url', 'categories', 'reactions', 'reaction_count')
    depth = 1
