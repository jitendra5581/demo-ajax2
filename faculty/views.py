from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def  faculty_home_view(request):
    return HttpResponse("welcome on faculty page")