# from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person , Country
from home.serializers import PeopleSerializer, LoginSerializer

# person.objects.all()
@api_view([ 'POST'])
def login(request):
    data = request.data
    serializer = LoginSerializer(data = data)
    if serializer.is_valid():
        data = serializer.validated_data
        print(data)
        return Response({'Messsage' : 'Success'})
    return Response(serializer.errors)




@api_view(['GET', 'POST', 'PUT'])
def index(request):
    courses = {
        'course_name' : 'Python',
        'learn' : ['flask', 'Django', 'FastAPI', 'Gp'],
        'course_provider' : 'Mirza'
    }
        
    if request.method == 'GET':
        print ("Get")
        return Response(courses)
    elif request.method == 'POST':
        data = request.data
        print (data['age'])
        print (data['name'])
        return Response(courses)
    elif request.method == 'PUT':
        print ("PUt")
        return Response(courses)
    
@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request):
    if request.method == 'GET':
        object = Person.objects.filter(country__isnull = False)
        serializer = PeopleSerializer(object , many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PATCH':
        data = request.data
        object = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(object, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    else:
        data = request.data
        object = Person.objects.get(id = data['id'])
        object.delete()
        return Response("Deleted")

        