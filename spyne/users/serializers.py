from rest_framework import serializers
from .models import SpyneUser as User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "mobile_no", "email"]

    def update(self, instance, validated_data):
        """
        Handle partial updates.
        """
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
