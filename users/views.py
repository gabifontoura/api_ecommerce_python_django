from rest_framework.views import APIView, Response, Request, status

from users.models import User
from users.serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from users.permissions import IsAdminOrReadOnly, HasAdminPermission
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)


class UserView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class UserViewDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [HasAdminPermission]

    def get(self, request: Request, user_id) -> Response:
        user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user)

        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request: Request, user_id: int) -> Response:
        user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(request, user)

        serializer = UserSerializer(user, request.data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)
