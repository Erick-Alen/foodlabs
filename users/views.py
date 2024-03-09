from rest_framework.views import status, Response, Request, APIView
from django.forms import model_to_dict
from ipdb import set_trace
from .models import User
from addresses.models import Address
from .serializers import UserSerializer
from rest_framework.pagination import PageNumberPagination


class UserView(APIView, PageNumberPagination):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # remove address data and store
        address_data = serializer.validated_data.pop("address")

        # create user
        user = User.objects.create(**serializer.validated_data)

        # create address
        address = Address.objects.create(**address_data, user=user)

        serializer = UserSerializer(user)
        # converted_user = model_to_dict(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        users = User.objects.all()
        result = self.paginate_queryset(users, request)
        # converted_users = [model_to_dict(user) for user in users]
        serializer = UserSerializer(users, many=True)
        return self.get_paginated_response(serializer.data)


class UserDetailedView(APIView):

    def get(self, request: Request, user_id: int) -> Response:
        try:
            found_user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(
                {"message": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = UserSerializer(found_user)
        return Response(serializer.data, status=status.HTTP_200_OK)
        users = User.objects.all()
        # converted_users = [model_to_dict(user) for user in users]
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request: Request, user_id: int) -> Response:
        try:
            found_user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(
                {"message": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = UserSerializer(data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # converted_users = [model_to_dict(user) for user in users]
        for key, value in serializer.validated_data.items():
            setattr(found_user, key, value)
        # make changes into database
        found_user.save()
        serializer = UserSerializer(found_user)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request: Request, user_id: int) -> Response:
        try:
            found_user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(
                {"message": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        found_user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
        # converted_users = [model_to_dict(user) for user in users]
