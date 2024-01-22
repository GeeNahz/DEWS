# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.utils import response_schema


from .models import (
    SensorData,
    # Temperature,
    # Precipitation,
    # SoilMoisture,
)

from .serializers import (
    SensorDataSerializerIn,
    SensorDataSerializerOut,
    # DataCollectionSerializerIn,
    # DataCollectionSerializerOut,
)

@response_schema(serializer=SensorDataSerializerOut)
class SensorDataAPIView(APIView):
    serializer_class = SensorDataSerializerIn
    def list(self, request, format=None):
        sensor_data = SensorData.objects.all()
        serializer = SensorDataSerializerOut(sensor_data, many=True)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def get(self, request, format=None):
        sensor_data = SensorData.objects.all()[:20]
        serializer = SensorDataSerializerOut(sensor_data, many=True)
        
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = SensorDataSerializerIn(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)


# class DataPrep:
#     def __init__(self, temperature, precipitation, soil_moisture):
#         self.temperature = temperature
#         self.precipitation = precipitation
#         self.soil_moisture = soil_moisture


# class DataCollection(APIView):
#     def get(self, request, format=None):
#         temperature = Temperature.objects.all()
#         precipitation = Precipitation.objects.all()
#         soil_moisture = SoilMoisture.objects.all()

#         data_prep = DataPrep(
#             temperature=temperature,
#             precipitation=precipitation,
#             soil_moisture=soil_moisture,
#         )
#         serializer = DataCollectionSerializerOut(
#             data_prep,
#         )

#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request, format=None):
#         serializer = DataCollectionSerializerIn(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         data = serializer.save()

#         return Response(data, status=status.HTTP_201_CREATED)
