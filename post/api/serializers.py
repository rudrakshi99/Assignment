from post.models import Post
from django.contrib.auth.models import User
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'created_at', 'updated_at','user')
        
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'firstname', 'lastname', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], 
                                        validated_data['email'], 
                                        validated_data['password'])

        return user
       
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'firstname', 'lastname', 'email')
        
        extra_kwargs = {
                'password': {'write_only': True},
                'style' : {'read_only': True}
            }
        
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)