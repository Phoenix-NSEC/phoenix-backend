from django.urls import path
from member.views import MemberListView, MemberDetailView,MemberVerifyView

urlpatterns = [
    path("", MemberListView.as_view()),  # GET
    path("<int:pk>/", MemberDetailView.as_view()),  # GET PATCH DELETE
    path("<int:pk>/verify/", MemberVerifyView.as_view()),  # GET PATCH DELETE
]
