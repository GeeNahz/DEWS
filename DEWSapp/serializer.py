from rest_framework import serializers


class TextSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField(default=4)


class PredictSerializer(serializers.Serializer):
    year = serializers.IntegerField()
    drought_index = serializers.CharField(max_length=100)
    ocean_temperature = serializers.CharField(max_length=100)
    climate_direction = serializers.CharField(max_length=100)
    SPEI_april = serializers.CharField(max_length=100)
    SPEI_may = serializers.CharField(max_length=100)
    SPEI_june = serializers.CharField(max_length=100)
    SPEI_july = serializers.CharField(max_length=100)
    SPEI_aug = serializers.CharField(max_length=100)
    SPEI_sept = serializers.CharField(max_length=100)
    SPEI_oct = serializers.CharField(max_length=100)
    region = serializers.CharField(max_length=100)


class PredictSerializerRequest(serializers.Serializer):
    state = serializers.CharField(max_length=255)
    year = serializers.IntegerField(default=2023)
    lga = serializers.CharField(max_length=200)


class PredictionModelSerializerRequest(serializers.Serializer):
    month = serializers.IntegerField()
    year = serializers.IntegerField()


class PredictionModelSerializerResponse(serializers.Serializer):
    month = serializers.IntegerField()
    year = serializers.IntegerField()
    spei = serializers.FloatField()
    drought_index = serializers.CharField()


class SpeiSerializer(serializers.Serializer):
    year = serializers.IntegerField()
    spei_drought_index = serializers.CharField(max_length=100)
    region = serializers.CharField(max_length=100)
