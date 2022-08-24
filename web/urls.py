
from django.urls import path

from . import views

app_name='web'

urlpatterns = [
    path('', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('packages/', views.packages,name='packages'),
    path('package-details/', views.packageDetails,name='packageDetails'),
    path('gallary/', views.gallery,name='gallery'),
    path('contact/', views.contact,name='contact'),
]