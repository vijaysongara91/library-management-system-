from django.contrib.auth import authenticate, login 
from django.shortcuts import render
from .models import Contact
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def catalog(request):
    return render(request,'catalog.html')

def My_Account(request):
    return render(request,'My_Account.html')

def about(request):
    return render(request,'about.html')

def Register(request):
    return render(request,'Register.html')

def browse(request):
    return render(request,'browse.html')

def home(request):
    return render(request,'home.html')

def book(request):
    return render(request,'book.html')

def help(request):
    return render(request,'help.html')

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        obj=Contact()
        obj.name=name
        obj.email=email
        obj.subject=subject
        obj.message=message
        obj.save()
        return render(request,'index.html')
    else:
        return render(request,'contact.html')

def Register(request):
    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
      
        user=User.objects.create_user(username=username,first_name=fname,last_name=lname,password=password,email=email)
        user.save()
        return render(request,'login.html')
    else:
        return render(request,'Register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request,'index.html')
        else:
            return render(request,'login.html')
    else:
        return render(request, 'login.html')

