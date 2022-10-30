from rest_framework.response import Response
from rest_framework import permissions
from main.permissions import IsAdminOrWriteOnly
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
from member.serializers import MemberListSerializer, MemberUpdateSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.exceptions import NotFound

# Create your views here.
class MemberListView(ListAPIView, CreateAPIView):
    """
    # Lists all the members
    ## Another Smaller Heading
    - Awesome
    - Great
        - Listed
        - Awesome
    """

    serializer_class = MemberUpdateSerializer
    queryset = Member.objects.all()
    permission_classes = (IsAdminOrWriteOnly,)


class MemberDetailView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    serializer_class = MemberListSerializer

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
            raise NotFound(detail="Member not Found/Already Verified")

    def get(self, request, *args, **kwargs):
        member = self.get_object()
        member.is_verified = True
        member.save()
        return Response({"error": False, "message": "Member Verified"})
