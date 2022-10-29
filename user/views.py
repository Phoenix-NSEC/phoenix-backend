from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from user.models import User
from user.serializers import UserListSerializer

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView


class UserListView(ListAPIView, CreateAPIView):
    serializer_class = UserListSerializer

    def get_queryset(self):
        return User.objects.all()


class UserDetailView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    serializer_class = UserListSerializer

    def get_queryset(self):
        return User.objects.all()
