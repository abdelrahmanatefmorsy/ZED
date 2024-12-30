from django.shortcuts import render
from .models import  CourseDay , Course
from .forms import CourseForm, UserForm, LoginForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

def index(request):
    return render(request, 'index.html')

def Home(request):
    courses = Course.objects.all()
    return render(request, 'Home/Home.html', {'courses': courses})

def login_view(request):
    loginform = LoginForm()
    if request.method == 'POST':
        loginform = LoginForm(request.POST)
        if loginform.is_valid():
            username = loginform.cleaned_data['username']
            password = loginform.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('Home'))
    return render(request, 'Forms/Login/Login.html', {'form': loginform})


def signup_view(request):
    userform = UserForm()
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']
            user = User.objects.create_user(username=username, password=password, email=email)
            login(request, user)
            return HttpResponseRedirect('/')
    return render(request, 'Forms/Signup/Signup.html', {'form': userform})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')