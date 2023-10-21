from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import CustomUser, Student, Employ
# Register your models here.


admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Employ)