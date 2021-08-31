from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from .models import *
# Create your views here.
def index(request):
    comments = QNA.objects.all()
    return render(request, 'index.html',{'comments':comments})

def search(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        q1 = QNA1.objects.all().filter(answer=search).count()
        q2 = QNA2.objects.all().filter(answer=search).count()
        q3 = QNA3.objects.all().filter(answer=search).count()
        q4 = QNA4.objects.all().filter(answer=search).count()
        q5 = QNA5.objects.all().filter(answer=search).count()
        q6 = QNA6.objects.all().filter(answer=search).count()
        q7 = QNA7.objects.all().filter(answer=search).count()
        q8 = QNA8.objects.all().filter(answer=search).count()
        q9 = QNA9.objects.all().filter(answer=search).count() 
        if q1 > 0:
            messages.error(request, 'Your attendance is 60 %', extra_tags='alert')
            return redirect('index')
        elif q2 > 0:
            messages.error(request, '5/24/2021', extra_tags='alert')
            return redirect('index')
        elif q3 > 0:
            messages.error(request, 'Go through the given below  link....', extra_tags='alert')
            return redirect('index')
        elif q4 > 0:
            messages.error(request, 'Please tell me your department', extra_tags='alert')
            return redirect('index')
        elif q5 > 0:
            messages.error(request, 'Provide username and password', extra_tags='alert')
            return redirect('index')
        elif q6 > 0:
            messages.error(request, 'Provide username and password', extra_tags='alert')
            return redirect('index')
        elif q7 > 0:
            messages.error(request, 'Provide username and password', extra_tags='alert')
            return redirect('index')
        elif q8 > 0:
            messages.error(request, '12:30:00 PM', extra_tags='alert')
            return redirect('index')
        elif q9 > 0:
            messages.error(request, '9:15 AM to 5:00 PM', extra_tags='alert')
            return redirect('index')        
        else:    
            messages.error(request, 'Question is not in dataset', extra_tags='alert')
            return redirect('index')
    return render(request, 'search.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pass']
        user = auth.authenticate(username=u, password=p)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid Email or Password!')
            return redirect('login')                             
    return render(request, 'login.html') 

def signup(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect('signup')
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username taken!')
            return redirect('signup')
        if User.objects.filter(email=email).exists():
            messages.info(request, 'email already exist')
            return redirect('signup')
        else:
            user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
            messages.info(request, "Successfully registered!\n login now. ")
            user.save()
            return redirect('login')               
    return render(request, "signup.html")

def logout(request):
    if not request.user.is_authenticated:
        return redirect('login')
    auth.logout(request)
    return redirect('login')
