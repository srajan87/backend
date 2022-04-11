from django.shortcuts import render

# Create your views here.

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from foodlogging.models import FoodLogs
from foodlogging.serializers import FoodLogsSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def foodlogs_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == 'GET':
        foodlogs = FoodLogs.objects.all()
        
        user = request.GET.get('user_id', None)
        if user is not None:
            foodlogs = foodlogs.filter(user_id__icontains=user)
        
        foodlogs_serializer = FoodLogsSerializer(foodlogs, many=True)
        return JsonResponse(foodlogs_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        foodlogs_data = JSONParser().parse(request)
        print("foodlogs_data:", foodlogs_data)
        foodlogs_serializer = FoodLogsSerializer(data=foodlogs_data)
        #print("foodlogs_serializer", foodlogs_serializer.data)
        if foodlogs_serializer.is_valid():
            foodlogs_serializer.save()
            return JsonResponse(foodlogs_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(foodlogs_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def foodlogs_detail(request, pk):
    # find tutorial by pk (id)
    try: 
        foodlog = FoodLogs.objects.get(pk=pk)
    except FoodLogs.DoesNotExist: 
        return JsonResponse({'message': 'The food log does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE tutorial
    if request.method == 'GET': 
        foodlog_serializer = FoodLogsSerializer(foodlog) 
        return JsonResponse(foodlog_serializer.data)
    elif request.method == 'PUT': 
        foodlog_data = JSONParser().parse(request) 
        foodlog_serializer = FoodLogsSerializer(foodlog, data=foodlog_data) 
        if foodlog_serializer.is_valid(): 
            foodlog_serializer.save() 
            return JsonResponse(foodlog_serializer.data) 
        return JsonResponse(foodlog_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE': 
        foodlog.delete() 
        return JsonResponse({'message': 'Food log was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
