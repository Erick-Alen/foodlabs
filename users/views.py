from rest_framework.views import status, Response, Request, APIView
from django.forms import model_to_dict
from ipdb import set_trace
from .models import User
from addresses.models import Address
from .serializers import UserSerializer


class UserView(APIView):
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
        # converted_users = [model_to_dict(user) for user in users]
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserDetailedView(APIView):
    def get(self, request: Request, user_id: int) -> Response:
        return Response({"message": "GET"}, status=status.HTTP_200_OK)
        users = User.objects.all()
        # converted_users = [model_to_dict(user) for user in users]
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def patch(self, request: Request, user_id: int) -> Response:
        return Response({"message": "patch"}, status=status.HTTP_204_NO_CONTENT)

        users = User.objects.all()
        # converted_users = [model_to_dict(user) for user in users]
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self, request: Request, user_id: int) -> Response:
        return Response({"message": "DELETE"}, status=status.HTTP_204_NO_CONTENT)

        users = User.objects.all()
        # converted_users = [model_to_dict(user) for user in users]
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
