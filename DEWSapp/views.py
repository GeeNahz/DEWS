import json
from django.http import HttpResponse

from django.views.decorators.csrf import ensure_csrf_cookie

from rest_framework import status, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .utils.openapi_response import response_schema

from .serializer import (
    PredictSerializer,
    PredictSerializerRequest,
    PredictionModelSerializerRequest,
    SpeiSerializer,
    TextSerializer,
)
from .dataset import (
    TextDetails,
    PredictDetails,
    SpeiDetails,
)
# import json

from .predictions import predict, spei_predict
from .model_prediction import ModelPrediction

# Create your views here.


def homepage(request):
    return HttpResponse('<h2>Welcome!</h2>')


@response_schema(serializer=PredictSerializer)
class PredictGenericAPIView(GenericAPIView):
    serializer_class = PredictSerializerRequest
    permission_classes = [permissions.AllowAny]
    
    def get(self, request):
        """
        Test endpoint with default hard-coded values. It only provides the response based on those default values.
        """
        
        year = 2025
        state = 'borno'.upper()

        with open("statesAndLgas.json") as j:
            data = json.load(j)

        for states in data:
            if states["state"].upper() == state:
                current_state = states

        lgas = current_state["lgas"]
        lga = lgas[5].upper()
        
        drought_index, oceanTemp, climate_direction = predict(state, year)
        SPEIA, SPEIM, SPEIJN, SPEIJY, SPEIAG, SPEIS, SPEIO, region = spei_predict(lga, year)

        results = PredictDetails(year, drought_index, oceanTemp, climate_direction, SPEIA, SPEIM, SPEIJN, SPEIJY, SPEIAG, SPEIS, SPEIO, region)

        serializer = PredictSerializer(results)

        return Response(serializer.data)

    def post(self, request):
        """
        The drought prediction endpoint to predict drought using ITCZ5, ITCZ10 and SPEI.

        Requires the state, year and lga for the prediction.
        """
        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        year = serializer.data["year"]
        lga = serializer.data["lga"].upper()
        state = serializer.data["state"].upper()
        
        drought_index, oceanTemp, climate_direction = predict(state, year)
        SPEIA, SPEIM, SPEIJN, SPEIJY, SPEIAG, SPEIS, SPEIO, region = spei_predict(lga, year)

        results = PredictDetails(year, drought_index, oceanTemp, climate_direction, SPEIA, SPEIM, SPEIJN, SPEIJY, SPEIAG, SPEIS, SPEIO, region)

        serializer = PredictSerializer(results)

        return Response(serializer.data, status=status.HTTP_200_OK)


class PredictModelAPIView(APIView):
    serializer_class = PredictionModelSerializerRequest

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        year = serializer.data["year"]
        month = serializer.data["month"]

        ModelPrediction.predict(month, year)

        return Response(status=status.HTTP_200_OK)


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
