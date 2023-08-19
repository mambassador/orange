from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Comment
        fields = ["id", "author", "post", "text", "pub_date", "is_published"]
        extra_kwargs = {
            "url": {"view_name": "api:comment-detail"},
        }

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            "url",
            "id",
            "title",
            "description",
            "pub_date",
            "author",
            "text",
            "is_published",
            "is_approved",
            "photo",
            "comments",
        ]
        extra_kwargs = {
            "url": {"view_name": "api:post-detail"},
        }

    def create(self, validated_data):
        validated_data["author"] = self.context["request"].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if instance.author == self.context["request"].user:
            return super().update(instance, validated_data)
        raise serializers.ValidationError("You don't have permission to update this post.")
