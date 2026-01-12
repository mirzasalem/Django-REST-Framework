# from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person , Country
from home.serializers import PeopleSerializer, LoginSerializer, RegisterSerializer
from rest_framework import viewsets
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.paginator import Paginator
from rest_framework.decorators import action




class RegisterAPI(APIView):
    
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data =data)
        
        if not serializer.is_valid():# HTTP_400_BAD_REQUEST
            return Response({
                'status' : False,
                'msg' : serializer.errors
            },status.HTTP_400_BAD_REQUEST)
        serializer.save()
        User = authenticate(username= serializer.data['username'], password= serializer.data['password'])
        token = Token.objects.get_or_create(user= User)
        return Response({
                'status' : True,
                'token' : str(token)
            },status.HTTP_201_CREATED)

class LoginAPI(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data = data)
        if serializer.is_valid():
            data = serializer.validated_data
            print(data)
            return Response({'Messsage' : 'Success'})
        return Response(serializer.errors)



class PersonAPI(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        object = Person.objects.filter(country__isnull = False)
        # page = request.GET.get('page', 1)
        # pag_size = 3
        serializer = PeopleSerializer(object , many = True)
        return Response(serializer.data)
        return Response({'message' : 'This is a get request'})
    
    
    def post(self, request):
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            # return Response({'message' : 'This is a POST request'})
        return Response(serializer.errors)
    
    
    def put(self, request):
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        # return Response({'message' : 'This is a put request'})
    
    
    def patch(self, request):
        data = request.data
        object = Person.objects.get(id = data['id'])
        serializer = PeopleSerializer(object, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        # return Response({'message' : 'This is a PATCH request'})
    
    
    def delete(self, request):
        data = request.data
        object = Person.objects.get(id = data['id'])
        object.delete()
        return Response("Deleted")
        # return Response({'message' : 'This is a Delete request'})
    

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


#viewset with a router, and allow the urlconf to be automatically generated.
class PeopleViewSet(viewsets.ModelViewSet):
    serializer_class = PeopleSerializer
    queryset = Person.objects.all()
    def list(self, request):
        search = request.GET.get('search')
        queryset = self.queryset
        if search:
            queryset = queryset.filter(name__istartswith=search)
        serializer = PeopleSerializer(queryset , many= True)
        return Response({'status' : 200 , 'data': serializer.data}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['post'])
    def send_mail_to_person(self, request):
        return Response({
            'status'  : True,
            'msg' : 'Emailed'
        })
    
    
    
