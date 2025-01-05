from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect ,get_list_or_404, get_object_or_404
from .models import  CourseDay , Course, UserProfile
from .forms import CourseForm, UserForm, LoginForm, UserProfileForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import AppliedCourse
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
@login_required
def add_course_view(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.publisher = request.user
            course.save()
            return redirect('showAllCourses')  # Redirect to a course list view or any other view
    else:
        form = CourseForm()
    return render(request, 'Forms/Course/index.html', {'form': form})

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
            return redirect('update_profile')
    return render(request, 'Forms/Signup/Signup.html', {'form': userform})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
def ShowAllCourses(request):
    data = []
    courses = Course.objects.all()
    profiles = UserProfile.objects.all()
    for course in courses:
        for profile in profiles:
            if course.publisher == profile.user:
                data.append((course, profile))
    print(data[0][0].publisher)
    return render(request, 'Courses/Courses.html', {'courses': data})

def Course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'Courses/Course.html', {'course': course})
@login_required
def update_profile_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to a profile view or any other view
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'Forms/Profile/update_profile.html', {'form': form})
@login_required
def Profile_view(request, username):
    my_courses = []
    apllied_courses = AppliedCourse.objects.all();
    courses = Course.objects.all()
    if request.user.username == username:
        print(request.user.username)
        for course in courses:
            for applied_course in apllied_courses:
                if applied_course.course == course and applied_course.user == request.user:
                    course.applied = True
                    my_courses.append(course)
    user = get_object_or_404(User, username=username)
    user_profile = get_object_or_404(UserProfile, user=user)
    user_courses = Course.objects.filter(publisher=user)
    return render(request, 'User/Profile.html', {'profile': user_profile, 'courses': user_courses,'my_courses': my_courses})
