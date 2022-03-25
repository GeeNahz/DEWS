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
    if request.method == 'POST':
        # dictionary of months
        # months = {
        #     "january": "jan",
        #     "february": "feb",
        #     "march": "march",
        #     "april": "april",
        #     "may": "may",
        #     "june": "june",
        #     "july": "july",
        #     "august": "aug",
        #     "september": "sept",
        #     "october": "oct",
        #     "november": "nov",
        #     "december": "dec",
        # }

        # data from request
        data = json.loads(request.body)

        # individual data
        # month_from_request = data['month'].lower()
        state = data['state'].upper()
        year = int(data['year'])
        lga = data['lga'].upper()

        # month = months[month_from_request]

        # calculations and prediction
        drought_index, oceanTemp, climate_direction = predict(state, year)
        SPEIA, SPEIM, SPEIJN, SPEIJY, SPEIAG, SPEIS, SPEIO, region = spei_predict(lga, year)

        # prepare the return values to be serialized
        results = PredictDetails(year, drought_index, oceanTemp, climate_direction, SPEIA, SPEIM, SPEIJN, SPEIJY, SPEIAG, SPEIS, SPEIO, region)

        # serializer the results
        serializer = PredictSerializer(results)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return HttpResponse("<h1>Want to Predict? Here's how:</h1><br/><p>Make a POST request making the body of the request to have the object format as follows:</p><br/><p>{<br/>&nbsp;&nbsp;&nbsp;'year':&nbsp;year_value,<br/>&nbsp;&nbsp;&nbsp;'state':&nbsp;state_value<br/>&nbsp;&nbsp;&nbsp;'lga':&nbsp;lga_value<br/>}</p>")


@ensure_csrf_cookie
@api_view(['GET', 'POST'])
def speiView(request):

    month = 'dec'
    year = 2025
    lga = 'Guma'.upper() # 19

    SPEIA, SPEIM, SPEIJN, SPEIJY, SPEIAG, SPEIS, SPEIO, region = spei_predict(month, lga, year)
    # index, region = spei_predict(month, lga, year)

    if request.method == 'POST':
        data = json.loads(request.body)

        year = int(data['year'])
        month = data['month'].lower()
        lga = data['lga'].upper()

        index, region = spei_predict(month, lga, year)

        result = SpeiDetails(year, index, region)
        serializer = SpeiSerializer(result)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return HttpResponse('Nothing to show for now')
