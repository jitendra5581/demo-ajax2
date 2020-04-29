
from django.urls import path
from .views import *

urlpatterns = [
    path('', faculty_home_view),
   
]
