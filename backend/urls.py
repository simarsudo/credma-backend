from rest_framework.authtoken import views
from django.urls import path, include
from django.contrib import admin
from .views import UserView, StudentView, EmployView, ProjectView, CompanyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UserView.Get_User),
    path('createuser/', UserView.CreateUser),
    path('createstu/', StudentView.Create_Student),
    path('student/', StudentView.Get_Student),
    path('createemp/', EmployView.Create_Employ),
    path('employ/', EmployView.Get_Employ),
    path('project/', ProjectView.Get_Project),
    path('createpro/', ProjectView.Create_Project),
    path('company/', CompanyView.Get_Company),
    path('createcom/', CompanyView.Create_Company),
    path('api-auth/', include('rest_framework.urls')),
]
