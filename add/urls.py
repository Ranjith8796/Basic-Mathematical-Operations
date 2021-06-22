from django.urls import path
from add import views

urlpatterns=[
   
    path('',views.home),
    path('ad/',views.adding),
    path('sub/', views.subtracting),
    path('multi/', views.multiplication),
    path('divi/', views.division),


]