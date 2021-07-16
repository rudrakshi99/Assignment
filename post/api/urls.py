from django.urls import path
from .views import (PostListView, PostCreateView, PostUpdateRetriveDeleteView, UserListView, UserUpdateRetriveDeleteView,
RegisterAPI)
from rest_framework.authtoken.views import obtain_auth_token

app_name='post'

urlpatterns = [
    path('users/profile/', UserListView.as_view()),
    path('users/<int:pk>', UserUpdateRetriveDeleteView.as_view()),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', obtain_auth_token),
    
    path('', PostListView.as_view(), name='list'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('<int:pk>/', PostUpdateRetriveDeleteView.as_view(), name='update_delete'),
]
