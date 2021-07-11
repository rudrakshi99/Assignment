from post.models import Post, User
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'created_at', 'updated_at')
        
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        
        extra_kwargs = {
                'password': {'write_only': True},
                'style' : {'read_only': True}
            }
        
    def create(self, validated_data):
        return super().create(validated_data)
    
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance, validated_data)