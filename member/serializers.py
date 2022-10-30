from rest_framework import serializers
from member.models import Member


class MemberListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

