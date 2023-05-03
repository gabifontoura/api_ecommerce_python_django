from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)

urlpatterns = [
    path("users/", views.UserView.as_view()),
    path("users/all/", views.UserAllView.as_view()),
    path("users/<int:user_id>/", views.UserViewDetail.as_view()),
    path("users/login/", TokenObtainPairView.as_view()),
] 