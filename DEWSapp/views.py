from django.shortcuts import render
from django.http import HttpResponse
import json

from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import TextSerializer, PredictSerializer, SpeiSerializer
from .dataset import TextDetails, PredictDetails, SpeiDetails
# import json

from .predictions import predict, spei_predict

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
        return HttpResponse("<h1>Want to Predict? Here's how:</h1><br/><p>Make a POST request making the body of the request to have the object format as follows:</p><br/><p>{<br/>&nbsp;&nbsp;&nbsp;'year':&nbsp;year_value,<br/>&nbsp;&nbsp;&nbsp;'state':&nbsp;state_value<br/>}</p>")

    elif request.method == 'POST':
        data = json.loads(request.body)

        month = 'jan'
        state = data['state'].upper()
        year = int(data['year'])

        drought_index, oceanTemp, climate_direction = predict(state, month, year)

        results = PredictDetails(year, drought_index, oceanTemp, climate_direction)

        serializer = PredictSerializer(results)

        print(serializer.data)

        # if serializer.is_valid():
        #     serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@ensure_csrf_cookie
@api_view(['GET', 'POST'])
def speiView(request):
    
    month = 'nov'
    year = 2031
    # lga = 'Binji'.upper() # 1
    # lga = 'Gada'.upper() # 2
    # lga = 'Abadam'.upper() # 3

    lga = 'matazu'.upper() # 4 ====== does not calc for all the months

    # lga = 'Gusau'.upper() # 5
    # lga = 'Bama'.upper() # 6
    # lga = 'Katagum'.upper() # 7
    # lga = 'Birnin-Gwari'.upper() # 8
    # lga = 'Magama'.upper() # 9
    # lga = 'Igabi'.upper() # 10

    # lga = 'Bauchi'.upper() # 11 ====== does not have PARA files

    # lga = 'Mangu'.upper() # 12
    # lga = 'Suleja'.upper() # 13
    # lga = 'Demsa'.upper() # 14
    # lga = 'Edati'.upper() # 15
    # lga = 'Kokona'.upper() # 16
    # lga = 'Oyun'.upper() # 17
    # lga = 'Adavi'.upper() # 18
    # lga = 'Guma'.upper() # 19


    index, region = spei_predict(month, lga, year)

    if request.method == 'POST':
        data = json.loads(request.body)

        year = int(data['year'])
        month = data['month'].lower()
        lga = data['lga'].upper()

        index, region = spei_predict(month, lga, year)

        print("Index:", index)
        print("Region:", region)

        result = SpeiDetails(year, index, region)
        serializer = SpeiSerializer(result)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return HttpResponse('Nothing to show for now')