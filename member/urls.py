from django.urls import path
from member.views import MemberListView, MemberDetailView

urlpatterns = [
    path("", MemberListView.as_view()),  # GET, POST
    path("<int:pk>/", MemberDetailView.as_view()),  # GET PATCH DELETE
]
