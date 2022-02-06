from rest_framework import serializers


class TextSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField(default=4)


class PredictSerializer(serializers.Serializer):
    year = serializers.IntegerField()
    drought_index = serializers.CharField(max_length=100)
    ocean_temperature = serializers.CharField(max_length=100)
    climate_direction = serializers.CharField(max_length=100)
