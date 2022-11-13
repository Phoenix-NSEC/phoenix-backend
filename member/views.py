from rest_framework.response import Response
from rest_framework import permissions
from main.permissions import IsAdminOrWriteOnly, IsAdminOrReadOnly
from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.exceptions import NotFound
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from member.models import Member
from member.serializers import MemberListSerializer, MemberUpdateSerializer
from member.filters import MemberFilter

# Create your views here.
class MemberListView(ListAPIView, CreateAPIView):
    serializer_class = MemberListSerializer
    queryset = Member.objects.all()
    permission_classes = (IsAdminOrWriteOnly,)
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = MemberFilter
    ordering = ["updated_at"]
    ordering_fields = ("graduation", "updated_at", "department")

    def get_queryset(self):
        queryset = super().get_queryset()
        print("hehe:", queryset.values("id"))
        return queryset


class MemberDetailView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = MemberUpdateSerializer

    def get_object(self):
        try:
            return Member.objects.get(id=self.kwargs["pk"])
        except Member.DoesNotExist:
            raise NotFound(detail="Member not Found")

    # def set_queryset(self, request):
    #     serializer = MemberListSerializer(data=request.data,context={"request": request})
    #     if(serializer.is_valid()):
    #         serializer.save()
    #         return Response({error:false,message:"Form Submitted",data:serializer.data})
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MemberVerifyView(APIView):
    def get_object(self):
        try:
            return Member.objects.get(id=self.kwargs["pk"], is_verified=False)
        except Member.DoesNotExist:
            raise NotFound(detail="Member not Found/Already Verified")  # type: ignore

    def get(self, request, *args, **kwargs):
        member = self.get_object()
        member.is_verified = True
        member.save()
        return Response({"error": False, "message": "Member Verified"})
