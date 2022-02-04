from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import ensure_csrf_cookie
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
    details = TextDetails('Godswill', 20)
    serializer = TextSerializer(details)

    month = 'jan'
    excel_doc = 'PARAsst'
    # required values should be the month and the excel document
    # result, prediction = predict(month, excel_doc, 2018)
    answer = predict(month, 2025)
    # print(answer)

    return Response(serializer.data)


@ensure_csrf_cookie
@api_view(['GET', 'POST'])
def predictView(request):
    if request == 'POST':
        data = json.loads(request.data)

        month = values['month']
        year = values['year']
        # value = values['value'] ==== may not need this since I'll be hard coding its value. Not the best but should work for now ;)
        excel_doc = values['doc']

        result, prediction = predict(month, excel_doc, year)

        values = PredictDetails(result, prediction)
        serializer = PredictSerializer(values)

        return Response(serializer.data)

    if request == 'GET':
        return HttpResponse("<h2>Wanna Predict?</h2><br/><p>Results coming soon to you</p>")
