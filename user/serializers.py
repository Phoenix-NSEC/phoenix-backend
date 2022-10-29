from rest_framework import serializers
from user.models import User


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ("password",)


class UserDetailSerizlier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
