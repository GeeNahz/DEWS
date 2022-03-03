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


class SpeiSerializer(serializers.Serializer):
    year = serializers.IntegerField()
    spei_drought_index = serializers.CharField(max_length=100)
    region = serializers.CharField(max_length=100)
