from rest_framework import serializers
from .models import CustomUser, Student, Employ


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password']
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'college', 'course', 'Field', 'p_info']

class EmploySerializer(serializers.ModelSerializer):
    class Meta:
        model = Employ
        fields = ['id', 'name', 'p_info']