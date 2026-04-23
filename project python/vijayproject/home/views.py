from django.shortcuts import render
from .models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method=='POST':
            name=request.POST['name']
            email=request.POST['email']
            subject=subject.POST['subject']
            message=request.POST['message']
            obj=contact()
            obj.name=name
            obj.email=email
            obj.subject=subject
            obj.message=message
            obj.save()
            return render(request,'index.html')
    else:
            return render(request,'contact.html')
  
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





