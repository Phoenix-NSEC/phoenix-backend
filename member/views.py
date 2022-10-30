from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from member.models import Member
from member.serializers import MemberListSerializer

# Create your views here.
class MemberListView(ListAPIView, CreateAPIView):
    serializer_class = MemberListSerializer

    def get_queryset(self):
        return Member.objects.all()

class MemberDetailView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    serializer_class = MemberListSerializer()

    def set_queryset(self, request):
        serializer = MemberListSerializer(data=request.data,context={"request": request})
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


