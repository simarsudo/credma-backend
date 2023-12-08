from rest_framework import generics, status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from .models import CustomUser, Employ, Student, Project, Company
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, StudentSerializer, EmploySerializer, ProjectSerializer, CompanySerializer

class UserView(generics.RetrieveAPIView):

    @api_view(['POST','GET'])
    @renderer_classes([TemplateHTMLRenderer])
    def Get_User(request):
        response = {"status":200}
        # data = request.data
        # Email = data.email
        # Password = data.password
        Email = 'lallu2@gmail.com'
        Password = '1'
        user_obj = CustomUser.objects.get(email=Email, password=Password)

        print("hohoh:   ", user_obj)
        if user_obj:
            user_token = Token.objects.get(user_id=user_obj).key
            serial = UserSerializer(user_obj)
            response["token"] = user_token
            response["data"] = serial.data
        else:
            response = {"status":status.HTTP_401_UNAUTHORIZED}
        
        return Response(data=response, template_name = 'sim.html',)



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


class ProjectView(generics.ListCreateAPIView):
    @api_view(['GET'])
    def Get_Project(request):
        response = {'status':200}
        project_obj = Project.objects.all()
        serial = ProjectSerializer(project_obj, many=True)
        response['data'] = serial.data
        return Response(response)
    
    @api_view(['POST'])
    def Create_Project(request):
        response = {'status':200}
        data = request.data
        serial = ProjectSerializer(data=data)
        if serial.is_valid():
            serial.save()
            return Response(response)
        return Response(serial.errors)


class CompanyView(generics.ListCreateAPIView):
    @api_view(['GET'])
    def Get_Company(request):
        response = {'status':200}
        company_obj = Company.objects.all()
        serial = CompanySerializer(company_obj, many=True)
        response['data'] = serial.data
        return Response(response)
    
    @api_view(['POST'])
    def Create_Company(request):
        response = {'status':200}
        data = request.data
        serial = CompanySerializer(data=data)
        if serial.is_valid():
            serial.save()
            return Response(response)
        return Response(serial.errors)
    


