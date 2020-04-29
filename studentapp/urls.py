
from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home),
    path('login/',login_view),
    path('addstudent/',add_student),
    path('newstudent/', new_student),
    path('allstudent/', all_students),
    path('city/<stateid>', all_city),
    path('search', search_students),
]
