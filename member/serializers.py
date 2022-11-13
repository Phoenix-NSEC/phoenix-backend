from rest_framework import serializers
from member.models import Member
from rest_framework import permissions


class MemberListSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Member
        read_only_fields = ("id", "created_at", "updated_at", "is_verified")
        fields = "__all__"


class MemberUpdateSerializer(serializers.ModelSerializer):
    """
    Returns all data if superuser or staff
    Returns only not sensitive data if anyone else
    """

    id = serializers.CharField(read_only=True)

    class Meta:
        model = Member
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        user = self.context["request"].user
        if not (user.is_superuser or user.is_staff):
            ret.pop("email")
            ret.pop("whatsapp")
            ret.pop("contact")
            ret.pop("student_id")
            ret.pop("payment_image")
        return ret
