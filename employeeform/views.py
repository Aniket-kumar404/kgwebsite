from django.shortcuts import render,redirect
from employeeform.models import employee
import json
from django.core import serializers
# Create your views here.
def home(request):
    emp=employee.objects.all()
   
    
   
    return render(request,'home.html',{'dict':emp})


def add(request):
    return render(request,'employee.html')
def submit(request):
    first_name=request.POST['firstName']
    last_name=request.POST['lastName']
    email=request.POST['email']
    date_of_birth=request.POST['date_of_birth']
    state=request.POST['state']
    designation=request.POST['designation']

    e= employee(first_name=first_name,last_name=last_name,email=email,date_of_birth=date_of_birth,state=state,designation=designation)
    e.save()

    return redirect('/')


def viewinfo(request,data):
  
    d=employee.objects.filter(first_name=data)
    print(type(d))
    data = serializers.serialize('json', d)
    
 #  json_str = json.dumps(d, indent=2)
    return render(request,'view.html',{'data':data})    