from rest_framework.views import status, Response, Request, APIView
from django.forms import model_to_dict
from ipdb import set_trace
from .models import User
from .serializers import UserSerializer


class UserView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # set_trace()
        user = User.objects.create(**serializer.validated_data)
        serializer = UserSerializer(user)
        # converted_user = model_to_dict(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        users = User.objects.all()
        # converted_users = [model_to_dict(user) for user in users]
        serializer = UserSerializer(users, many=True)
        return Response(serializer, status=status.HTTP_200_OK)
