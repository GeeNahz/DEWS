from rest_framework import serializers


class TextSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField(default=4)


class PredictSerializer(serializers.Serializer):
    result = serializers.IntegerField(default=4)
    prediction = serializers.CharField(max_length=100)
