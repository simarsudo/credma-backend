from rest_framework import generics
# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import CustomUser, Employ, Student
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, StudentSerializer, EmploySerializer

class UserView(generics.ListCreateAPIView):
    @api_view(['GET'])
    def Get_User(request):
        response = {'status':200}
        user_obj = CustomUser.objects.all()
        serial = UserSerializer(user_obj, many=True)
        response['data'] = serial.data
        return Response(response)


    @api_view(['POST'])
    def CreateUser(request):
        response = {'status':200}
        data = request.data
        # head = request.headers
        serial = UserSerializer(data=data)
        if serial.is_valid():
            serial.save()
            user = CustomUser.objects.get(email=data['email'])
            token = Token.objects.create(user=user)
            print(token.key)
            response['token'] = token.key
            # response['head'] = head
            return Response(response)
        return Response(serial.errors)
    
class StudentView(generics.ListCreateAPIView):
    @api_view(['GET'])
    def Get_Student(request):
        response = {'status':200}
        student_obj = Student.objects.all()
        serial = StudentSerializer(student_obj, many=True)
        response['data'] = serial.data
        return Response(response)
    
    @api_view(['POST'])
    def Create_Student(request):
        response = {'status':200}
        data = request.data
        # head_token = request.headers('token')
        head_token = 'ddab9be11e367548fa341dad3d7e825f0598534a'
        user = Token.objects.get(key=head_token).user_id
        data['p_info'] = user
        print(data)
        serial = StudentSerializer(data=data)
        if serial.is_valid():
            serial.save()
            return Response(response)
        return Response(serial.errors)

class EmployView(generics.ListCreateAPIView):
    @api_view(['GET'])
    def Get_Employ(request):
        response = {'status':200}
        employ_obj = Employ.objects.all()
        serial = StudentSerializer(employ_obj, many=True)
        response['data'] = serial.data
        return Response(response)
    
    @api_view(['POST'])
    def Create_Employ(request):
        response = {'status':200}
        data = request.data
        # head_token = request.headers('token')
        head_token = '5f602059bfe65d4e8fa15044bcfd6ea397838e52'
        user = Token.objects.get(key=head_token).user_id
        data['p_info'] = user
        print(data)
        serial = EmploySerializer(data=data)
        if serial.is_valid():
            serial.save()
            return Response(response)
        return Response(serial.errors)