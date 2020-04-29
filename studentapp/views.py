from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *
import json

def home(request):
   
    names=['Amit','Rahul','Aman']
    emails=['Amit@gmail.com','Rahul@gmail.com','Aman@gmail.com']
    
    context = {
       'names': names,
       'emails':emails,
       'islogin': True

    }
    return render(request, 'student/index.html', context)


def login_view(request):
    
    return render(request,'student/login.html')


def add_student(request):
    # if(request.method =='POST'): 
    #     student_name = request.POST['name']
    #     student_fname = request.POST['fname']
    #     student_email = request.POST['email']
    #     student_class = request.POST['class']
    #     student_city = request.POST['city']
    #     print("student name>>>",student_name)
    #     print("student fname>>>",student_fname)
    #     print("student email>>>",student_email)
    #     print("student class>>>",student_class)


    #     print("button has clicked")


    return render(request,'student/addstudent.html')

def new_student(request):
    context = dict()
    if(request.method =='POST'): 
        student_name = request.POST['name']
        student_fname = request.POST['fname']
        student_email = request.POST['email']
        student_class = request.POST['class']
        student_city = request.POST['city']
       
        # student = Student();
        # student.name = student_name
        # student.father_name = student_fname
        # student.email = student_email
        # student.student_class = student_class
        # student.city=student_city
        # student.save()

         #or 
        # student = Student(
        #     name=student_name,
        #     father_name=student_fname,
        #     email=student_email,
        #     student_class=student_class,
        #     city=student_city
        #          ) 
        # student.save() 

        student=Student.objects.create( 
            name=student_name,
            father_name=student_fname,
            email=student_email,
            student_class=student_class,
            city=student_city
            )
            
        student.save()    




        context={'msg': 'student record has been added'}
        


       
    return  render(request,'student/addstudent.html', context)    


def all_students(request):

    # res=Student.objects.all()
  context = dict()  
  try:  
    res=Student.objects.get(id=1)
    context ={'info' : res}
  except   Student.DoesNotExist :
      print("record not found")
   
  return render(request, 'student/allstudent.html' , context)


def all_city(request, **kw):
    stid= kw.get("stateid")
    cities = CityDetails.objects.filter(state_id=stid)
    all_cities = list()
    if(cities.exists()):
        
        for city in cities:
            city_info = dict()
            city_info['id'] = city.id
            city_info['name'] = city.city_name 
            all_cities.append(city_info)
        
        print(all_cities)
    return HttpResponse(json.dumps(all_cities))

  
def search_students(request):
    
    #name_initial = kwargs.get("name")
    if(request.method=='POST'):

        name_initial = request.POST["in_name"]
        res=Student.objects.filter(name__icontains=name_initial)
        all_students = list()
        if(res.exists()):
            for st in res:
                student_dict = dict()
                student_dict["name"] = st.name
                student_dict["email"] = st.email
                student_dict["city"] = st.city
                all_students.append(student_dict)    
    return HttpResponse(json.dumps(all_students))



