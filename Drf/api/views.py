from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

# Create your views here.

@csrf_exempt
def singleobj(req, id):
    data = Person.objects.get(id=id)
    if req.method == "PUT":
        stream = io.BytesIO(req.body)
        parsed_data = JSONParser().parse(stream)
        serializer = PersonSerializer(data, data=parsed_data) #first data is model object and second data is the our db data that we shared
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"Update":"Success"})
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    if req.method == "PATCH":
        stream = io.BytesIO(req.body)
        parsed_data = JSONParser().parse(stream)
        serializer = PersonSerializer(data, data=parsed_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"update":"success"})
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    serializer = PersonSerializer(data)
    # print(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type = 'application/json')
    return JsonResponse(serializer.data)
    
@csrf_exempt
def multipleobj(req):
    if req.method == "POST":
        # json = req.body ===> req.body 
        stream = io.BytesIO(req.body)
        parsed_data = JSONParser().parse(stream)
        serializer = PersonSerializer(data=parsed_data)  #here the data=arguments are dentoed as the serializer know, it wil deserialize the client requested raw data
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"Created":"Successful"}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
        # print(parsed_data)
        # print(type(parsed_data))



    data = Person.objects.all()
    serializer = PersonSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)
