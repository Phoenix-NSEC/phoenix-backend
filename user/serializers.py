from rest_framework import serializers
from user.models import User
from django.contrib.auth.hashers import make_password


class UserListSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text="Leave empty if no change needed",
        style={"input_type": "password", "placeholder": "Password"},
    )

    class Meta:
        model = User
        fields = ("id", "name", "email", "avatar", "is_staff", "is_active", "password")

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return super().create(validated_data)


class UserDetailSerizlier(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    password = serializers.CharField(
        write_only=True,
        required=True,
        help_text="Leave empty if no change needed",
        style={"input_type": "password", "placeholder": "Password"},
    )

    class Meta:
        model = User
        fields = "__all__"

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        try:
            user.set_password(validated_data["password"])
            user.save()
        except KeyError:
            pass
        return user
