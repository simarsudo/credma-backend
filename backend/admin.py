from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import CustomUser, Student, Employ, Skill, Company, Project
# Register your models here.


admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Employ)
admin.site.register(Skill)
admin.site.register(Company)
admin.site.register(Project)