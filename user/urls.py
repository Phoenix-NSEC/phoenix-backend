from django.urls import path
from user.views import UserListView, UserDetailView


urlpatterns = [
    path("", UserListView.as_view()),  # GET, POST
    path("<int:pk>/", UserDetailView.as_view()),  # GET PUT PATCH DELETE
]
