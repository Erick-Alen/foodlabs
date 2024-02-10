from rest_framework import serializers

class AddressSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    street = serializers.StringField()
    number = serializers.IntegerField()
    city = models.CharField()
    state = models.CharField()
    zip_code = models.IntegerField()
