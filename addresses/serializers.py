from rest_framework import serializers

class AddressSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    # street = serializers.CharField()
    number = serializers.IntegerField()
    # city = serializers.CharField()
    # state = serializers.CharField()
    # zip_code = serializers.IntegerField()
