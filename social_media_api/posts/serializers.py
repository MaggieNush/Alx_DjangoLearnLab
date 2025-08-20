from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = 'author', 'title', 'content', 'created_at', 'updated_at'

        def validate(self, data):
            if not data.get('content', '').strip():
                raise serializers.ValidationError("Content cannot be empty.")
            return data

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = 'post', 'author', 'content', 'created_at', 'updated_at'

        def validate(self, data):
            if not data.get('content', '').strip():
                raise serializers.ValidationError("Content cannot be empty.")
            return data
