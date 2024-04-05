import time

from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response

from hillelDjango3.serializers import RegistrationSerializer, ObtainAuthTokenSerializer
from products.models import Product


@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def registration(request):
    serializer = RegistrationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([])
@authentication_classes([])
def obtain_auth_token(request):
    serializer = ObtainAuthTokenSerializer(data=request.data)

    if serializer.is_valid():
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


stats_view = []


def long_view(request):
    print("Start")
    time.sleep(10)
    print("End")
    return HttpResponse("OK")
