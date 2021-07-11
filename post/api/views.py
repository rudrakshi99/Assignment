from post.models import Post, User
from .serializers import PostSerializer, UserSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from .permissions import UserPermission

class UserListView(ListAPIView):
    serializer_class    = UserSerializer


    def get_queryset(self):
        """Returns only the object related to current user"""
        user = self.request.user
        return User.objects.filter(username=user)
    
    
class UserCreateView(CreateAPIView):
    """Handles Create of a user object"""
    queryset            = User.objects.all()
    serializer_class    = UserSerializer
    permission_classes = [AllowAny]


class UserUpdateRetriveDeleteView(RetrieveUpdateDestroyAPIView):
    """Handles update, retrive and delete of user obj"""
    queryset            = User.objects.all()
    serializer_class    = UserSerializer

    permission_classes  = [ UserPermission]

class PostListView(ListAPIView):
    serializer_class    = PostSerializer
    permission_classes = [AllowAny]
   
    def get_queryset(self):
        """Returns only the object related to current user"""
        user = self.request.user
        return Post.objects.filter(user=user)
    
    
class PostCreateView(CreateAPIView):
    """Handles Create of a post object"""
    queryset            = Post.objects.all()
    serializer_class    = PostSerializer
    permission_classes = [AllowAny]
    
    
class PostUpdateRetriveDeleteView(RetrieveUpdateDestroyAPIView):
    queryset            = Post.objects.all()
    serializer_class    = PostSerializer
    permission_classes = [ UserPermission]
    