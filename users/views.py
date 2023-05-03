from rest_framework.views import APIView, Response, Request, status

from users.models import User
from users.serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from users.permissions import IsAdminOrReadOnly, HasAdminPermission
from rest_framework import generics
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [HasAdminPermission]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    url_params_name = "user_id"