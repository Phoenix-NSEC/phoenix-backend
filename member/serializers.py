from rest_framework import serializers
from member.models import Member

class MemberListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at', 'is_verified')

class MemberUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'