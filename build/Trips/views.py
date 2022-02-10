from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import users
from .models import users_trip
from .serializer import userSerializer
from .serializer import usertripSerializer


@api_view(['GET', 'POST'])
def user_list_create_api_view(request):
    if request.method == 'GET':
        user = users.objects.all()
        serializer = userSerializer(user, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk):
    try:
        user_instance = users.objects.get(pk=pk)
    except user_instance.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = userSerializer(user_instance)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = userSerializer(user_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def usertrip_list_create_api_view(request):
    if request.method == 'GET':
        usertrip = users_trip.objects.all()
        serializer = usertripSerializer(usertrip, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = usertripSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def usertrip_detail_api_view(request, pk):
    try:
        usertrip_instance = users_trip.objects.filter(pk=pk).first()
    except usertrip_instance.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = usertripSerializer(usertrip_instance)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = usertripSerializer(usertrip_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        usertrip_instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT'])
def usertripwithuserid_detail_api_view(request, userid):
    try:
        usertrip_instance = users_trip.objects.filter(userId_id=userid)
    except usertrip_instance.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = usertripSerializer(usertrip_instance, many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = usertripSerializer(usertrip_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_204_NO_CONTENT)
