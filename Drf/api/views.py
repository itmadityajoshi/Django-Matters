
from django.shortcuts import render
from .models import Person
from .serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET','PUT','PATCH'])
def singleobj(req, id):
    data = Person.objects.get(id=id)
    if req.method == "PUT":
        stream = io.BytesIO(req.body)
        parsed_data = JSONParser().parse(stream)
        serializer = PersonSerializer(data, data=parsed_data) #first data is model object and second data is the our db data that we shared
        if serializer.is_valid():
            serializer.save()
            return Response({"Update":"Success"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    if req.method == "PATCH":
        stream = io.BytesIO(req.body)
        parsed_data = JSONParser().parse(stream)
        serializer = PersonSerializer(data, data=parsed_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"update":"success"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if req.method == 'GET':
        serializer = PersonSerializer(data)
        # print(serializer.data)
        # json_data = JSONRenderer().render(serializer.data)
        # return HttpResponse(json_data, content_type = 'application/json')
        return Response(serializer.data)
    
@api_view(['GET','POST'])
def multipleobj(req):
    if req.method == "POST":
        # json = req.body ===> req.body 
        # stream = io.BytesIO(req.body)
        # parsed_data = JSONParser().parse(stream)
        parsed_data = req.data
        serializer = PersonSerializer(data=parsed_data)  #here the data=arguments are dentoed as the serializer know, it wil deserialize the client requested raw data
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response({"Created":"Successful"}, status=status.HTTP_201_CREATED)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(({"created":":successfull"}), status= status.HTTP_400_BAD_REQUEST)
        # print(parsed_data)
        # print(type(parsed_data))


    if req.method == "GET":
        data = Person.objects.all()
        serializer = PersonSerializer(data, many=True)
        return Response(serializer.data)
