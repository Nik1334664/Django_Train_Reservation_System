# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('check_seat_availability/', views.check_seat_availability, name='check_seat_availability'),
    path('select_cabin/<str:cabin_name>/<str:num_members>/', views.select_cabin, name='select_cabin'),
    path('make_payment/<str:total_fare>/', views.make_payment, name='make_payment'),
    path('error_msg/<str:msg>/', views.error_msg, name='error_msg'),
]
