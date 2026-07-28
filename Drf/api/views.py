from django.shortcuts import render, HttpResponse
from .models import Person
from .serializers import PersonSerializer
from rest_framework.renderers import JSONRenderer
# Create your views here.

def singleobj(req):
    data = Person.objects.get(id=1)
    serializer = PersonSerializer(data)
    # print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
        
    return HttpResponse(json_data, content_type = 'application/json')
   

def multipleobj(req):
    data = Person.objects.all()
    serializer = PersonSerializer(data, many=True)
    json_data = JSONRenderer().render(serializer.data)
    # print(json_data)
    return HttpResponse(json_data, content_type = 'application/json')
