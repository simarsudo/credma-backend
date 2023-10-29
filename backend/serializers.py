from rest_framework import serializers
from .models import CustomUser, Student, Employ, Skill, Company, Project


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password']
    

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ['id', 'name', 'college', 'course', 'Field', 'p_info']
        fields = '__all__'


class EmploySerializer(serializers.ModelSerializer):
    class Meta:
        model = Employ
        # fields = ['id', 'name', 'p_info']
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        field = '__all__'


