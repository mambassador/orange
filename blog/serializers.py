from rest_framework import serializers
from .models import Post, Comment, User


class CommentSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), write_only=True, source='author')

    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'text', 'pub_date', 'is_published']
        extra_kwargs = {
            'url': {'view_name': 'api:comment-detail'},
        }


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['url', 'id', 'title', 'description', 'pub_date', 'author', 'text', 'is_published', 'is_approved', 'photo', 'comments']
        extra_kwargs = {
            'url': {'view_name': 'api:post-detail'},  # Set the correct view name for post detail view
        }

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if instance.author == self.context['request'].user:
            return super().update(instance, validated_data)
        raise serializers.ValidationError("You don't have permission to update this post.")


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'first_name', 'last_name', 'description', 'photo', 'posts']
        extra_kwargs = {
            'url': {'view_name': 'api:user-detail'},  # Set the correct view name for user detail view
        }
