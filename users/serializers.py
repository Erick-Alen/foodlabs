from rest_framework import serializers
from addresses.serializers import AddressSerializer

class UserSerializer(serializers.Serializer):
    # USER
    # username = serializers.CharField(max_length=100)
    # password = serializers.CharField(max_length=100)
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    # created_at = serializers.DateTimeField(read_only=True)
    # updated_at = serializers.DateTimeField(read_only=True)

    # nested serialization
    address = AddressSerializer(read_only=True)

    # def create(self, validated_data):
    #     return User.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.username = validated_data.get("username", instance.username)
    #     instance.email = validated_data.get("email", instance.email)
    #     instance.password = validated_data.get("password", instance.password)
    #     instance.first_name = validated_data.get("first_name", instance.first_name)
    #     instance.last_name = validated_data.get("last_name", instance.last_name)
    #     instance.save()
    #     return instance

    # def to_representation(self, instance):
    #     return {
    #         "id": instance.id,
    #         "username": instance.username,
    #         "email": instance.email,
    #         "password": instance.password,
    #         "first_name": instance.first_name,
    #         "last_name": instance.last_name,
    #         "date_joined": instance.date_joined,
    #         "last_login": instance.last_login,
    #     }

    # def to_internal_value(self, data):
    #     return {
    #         "id": data.get("id"),
    #         "username": data.get("username"),
    #         "email": data.get("email"),
    #         "password": data.get("password"),
    #         "first_name": data.get("first_name"),
    #         "last_name": data.get("last_name"),
    #         "date_joined": data.get("date_joined"),
    #         "last_login": data.get("last_login"),
    #     }

    # def to_internal_value(self, data):
    #     return {
    #         "id": data.get("id"),
    #         "username": data.get("username"),
    #         "email": data.get("email"),
    #         "password": data.get("password"),
    #         "first_name": data.get("first_name"),
    #         "last_name": data.get("last_name"),
    #         "date_joined": data.get("date_joined"),
    #         "last_login": data.get("last_login"),
    #     }

    # def to_internal_value(self, data):
    #     return {
    #         "id": data.get("id"),
    #         "username": data.get("username"),
    #         "email": data.get("email")
    #     }
