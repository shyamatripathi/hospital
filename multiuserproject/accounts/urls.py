from django.urls import path,include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('admin/', admin.site.urls), 
    path('signup/', views.signup_view, name='signup_view'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('patient_dashboard/', views.patient_dashboard, name='patient_dashboard'),
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
]
