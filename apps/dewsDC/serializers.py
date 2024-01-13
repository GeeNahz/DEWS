from rest_framework import serializers



from .models import (
    SensorData,
    # Precipitation,
    # Temperature,
    # SoilMoisture,
)


class SensorDataSerializerIn(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'
        # exclude = ('id', 'created', 'modified',)


class SensorDataSerializerOut(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = '__all__'


# class TemperatureSerializerIn(serializers.ModelSerializer):
#     class Meta:
#         model = Temperature
#         include = ('temperature',)


# class TemperatureSerializerOut(serializers.ModelSerializer):
#     class Meta:
#         model = Temperature
#         fields = '__all__'


# class PrecipitaionSerializerIn(serializers.ModelSerializer):
#     class Meta:
#         model = Precipitation
#         include = ('precipitaion',)


# class PrecipitaionSerializerOut(serializers.ModelSerializer):
#     class Meta:
#         model = Precipitation
#         fields = '__all__'


# class SoilMoistureSerializerIn(serializers.ModelSerializer):
#     class Meta:
#         model = SoilMoisture
#         include = ('soil_moisture',)


# class SoilMoistureSerializerOut(serializers.ModelSerializer):
#     class Meta:
#         model = SoilMoisture
#         fields = '__all__'


# class DataCollectionSerializerIn(serializers.Serializer):
#     temperature = serializers.FloatField()
#     precipitation = serializers.FloatField()
#     soil_moisture = serializers.FloatField()

#     def create(self, validated_data):        
#         temp_data = validated_data.pop('temperature')
#         precip_data = validated_data.pop('precipitation')
#         soil_data = validated_data.pop('soil_moisture')

#         temperature = Temperature.objects.create(temperature=temp_data)
#         precipitation = Precipitation.objects.create(precipitation=precip_data)
#         soil_moisture = SoilMoisture.objects.create(soil_moisture=soil_data)

#         return {
#             'temperature': temperature.temperature,
#             'precipitation': precipitation.precipitation,
#             'soil_moisture': soil_moisture.soil_moisture,
#         }


# class DataCollectionSerializerOut(serializers.Serializer):
#     temperature = TemperatureSerializerOut(many=True)
#     precipitation = PrecipitaionSerializerOut(many=True)
#     soil_moisture = SoilMoistureSerializerOut(many=True)
