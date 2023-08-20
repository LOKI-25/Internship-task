from rest_framework import serializers
from .models import Blog, Comment
from users.serializers import UserSerializer


class BlogSerializer(serializers.ModelSerializer):
    author=UserSerializer(read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    author=UserSerializer(read_only=True)
    post=BlogSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
