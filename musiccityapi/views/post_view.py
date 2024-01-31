from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import  status

from musiccityapi.models.post import Post
from musiccityapi.serializers.post_serializer import PostSerializer

    
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
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def create(self, request):
    """Handles POST request for a new Post"""
    
    post = Post.objects.create(
      post_title = request.data.get['post_title'],
      post_author = request.data.get['post_author'],
      post_content = request.data.get['post_content'],
      image_url = request.data.get['image_url'],
      categories = request.data.get['categories']
    )
    
    serializer = PostSerializer(post)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  
  def update(self, request, pk):
    """Handles PUT for a Post"""
    
    try:
      post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
      return Response({'error': "Post Does Not Exist"}, status=status.HTTP_404_NOT_FOUND)
    
    if 'post_title' in request.data:
      post.post_title = request.data['post_title']
      
    if 'post_author' in request.data:
      post.post_author = request.data['post_author']

    if 'post_content' in request.data:
      post.post_content = request.data['post_content']
      
    if 'image_url' in request.data:
      post.image_url = request.data['image_url']
      
    if 'categories' in request.data:
      post.categories = request.data['categories']  
      
    post.save()  
    serializer = PostSerializer(post)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  
  def destroy(self, request, pk):
    """Handles DELETE for a Post"""
    
    post = Post.Objects.get(pk=pk)
    post.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
