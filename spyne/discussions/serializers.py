from rest_framework import serializers
from .models import Discussion, Comment, Like
from django.utils import timezone

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "text", "user", "created_on"]


class DiscussionSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Discussion
        fields = ["id", "text", "image", "hashtags", "created_on", "user", "comments"]
        extra_kwargs = {
            "created_on": {"read_only": True},
            # "user": {"read_only": True},
        }

    def update(self, instance, validated_data):
        """
        Handle partial updates (PATCH requests).
        """
        print(str(instance))
        # Update fields only if provided in the request
        instance.text = validated_data.get("text", instance.text)
        instance.image = validated_data.get("image", instance.image)
        instance.hashtags = validated_data.get("hashtags", instance.hashtags)
        instance.created_on = validated_data.get("created_on", timezone.now())

        instance.save()
        return instance


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["id", "user", "post", "comment"]
