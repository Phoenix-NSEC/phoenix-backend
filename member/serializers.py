from rest_framework import serializers
from member.models import Member


class MemberListSerializer(serializers.ModelSerializer):
    id = serializers.CharField()

    class Meta:
        model = Member
        read_only_fields = ("id", "created_at", "updated_at", "is_verified")
        fields = "__all__"


class MemberUpdateSerializer(serializers.ModelSerializer):
    id = serializers.CharField()

    class Meta:
        model = Member
        fields = "__all__"
