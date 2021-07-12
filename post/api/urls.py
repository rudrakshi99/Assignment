from django.urls import path
from .views import (PostListView, PostCreateView, PostUpdateRetriveDeleteView, UserCreateView, UserListView, UserUpdateRetriveDeleteView,
UserCreateView)

app_name='post'

urlpatterns = [
    path('users/profile/', UserListView.as_view()),
    path('users/<int:pk>', UserUpdateRetriveDeleteView.as_view()),
    path('register/', UserCreateView.as_view()),
    
    path('', PostListView.as_view(), name='list'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('<int:pk>/', PostUpdateRetriveDeleteView.as_view(), name='update_delete'),
]
