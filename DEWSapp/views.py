from django.shortcuts import render
from django.http import HttpResponse
import json

from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TextSerializer, PredictSerializer
from .dataset import TextDetails, PredictDetails
# import json

from .predictions import predict

# Create your views here.


def homepage(request):
    return HttpResponse('<h2>Welcome!</h2>')


@api_view(['GET'])
def listView(request):
    # details = TextDetails('Godswill', 20)
    # serializer = TextSerializer(details)

    if request.method == 'GET':

        month = 'jan'
        year = 2029
        state = 'borno'.upper()

        drought_index, oceanTemp, climate_direction = predict(state, month, year)

        # predict(state, month, year)

        results = PredictDetails(year, drought_index, oceanTemp, climate_direction)
        serializer = PredictSerializer(results)

        return Response(serializer.data)
        # return HttpResponse("Home page?")




@ensure_csrf_cookie
@api_view(['GET', 'POST'])
def predictView(request):
    if request.method == 'GET':
        return HttpResponse("<h2>Wanna Predict?</h2><br/><p>Results coming soon to you</p>")

    elif request.method == 'POST':
        data = json.loads(request.body)

        month = 'jan'
        state = data['state'].upper()
        year = data['year']

        drought_index, oceanTemp, climate_direction = predict(state, month, year)

        results = PredictDetails(year, drought_index, oceanTemp, climate_direction)

        serializer = PredictSerializer(results)

        print(serializer.data)

        # if serializer.is_valid():
        #     serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
