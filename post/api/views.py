from post.models import Post, User
from .serializers import PostSerializer, UserSerializer, RegisterSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import UserPermission

# Register API
class RegisterAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    

class UserListView(ListAPIView):
    serializer_class    = UserSerializer
    queryset            = User.objects.all()



class UserUpdateRetriveDeleteView(RetrieveUpdateDestroyAPIView):
    """Handles update, retrive and delete of user obj"""
    queryset            = User.objects.all()
    serializer_class    = UserSerializer

    permission_classes  = [ UserPermission, IsAuthenticated]


class PostListView(ListAPIView):
    serializer_class    = PostSerializer
    queryset            = Post.objects.all()
    
    
class PostCreateView(CreateAPIView):
    """Handles Create of a post object"""
    queryset            = Post.objects.all()
    serializer_class    = PostSerializer
    permission_classes = [IsAuthenticated]
    
    
class PostUpdateRetriveDeleteView(RetrieveUpdateDestroyAPIView):
    queryset            = Post.objects.all()
    serializer_class    = PostSerializer
    permission_classes = [ UserPermission, IsAuthenticated]
    