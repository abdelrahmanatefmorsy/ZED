from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect ,get_list_or_404, get_object_or_404
from .models import  CourseDay , Course, UserProfile
from .forms import CourseForm, UserForm, LoginForm, UserProfileForm ,VideoForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse , HttpResponseForbidden
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import AppliedCourse , Video
from django.db.models import Q
def index(request):
    return render(request, 'index.html')

def Home(request):
    courses = Course.objects.all().filter(State = 'active')
    return render(request, 'Home/Home.html', {'courses': courses[0:3]})

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
            return redirect('showAllCourses')
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
    courses = Course.objects.filter(State = 'active')
    profiles = UserProfile.objects.all()
    for course in courses:
        for profile in profiles:
            if course.publisher == profile.user:
                data.append((course, profile))
    print(data[0][0].publisher)
    return render(request, 'Courses/Courses.html', {'courses': data})

def search_courses(request):
    query = request.GET.get('q')
    data = []
    if query:
        courses = Course.objects.filter(Q(course_name__icontains=query) ,State = 'active')
        profiles = UserProfile.objects.all()
        for course in courses:
            for profile in profiles:
                if course.publisher == profile.user:
                    data.append((course, profile))
    return render(request, 'Courses/Courses.html', {'courses': data})


def Course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    if request.user != course.publisher and course.State != 'active':
        return HttpResponseForbidden('You are not allowed to view this course')
    return render(request, 'Courses/Course.html', {'course': course})


@login_required
def update_profile_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return Profile_view(request, request.user.username)
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
                if applied_course.course == course and applied_course.user == request.user and course.State == 'active':
                    course.applied = True
                    my_courses.append(course)
    user = get_object_or_404(User, username=username)
    user_profile = get_object_or_404(UserProfile, user=user)
    if request.user.username == username:
        user_courses = Course.objects.filter(publisher=user)
    else:
        user_courses = Course.objects.filter(publisher=user, State = 'active')
    return render(request, 'User/Profile.html', {'profile': user_profile, 'courses': user_courses,'my_courses': my_courses})


@login_required
def apply_to_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if course.publisher != request.user:
        if not AppliedCourse.objects.filter(course=course, user=request.user).exists():
            AppliedCourse.objects.get_or_create(course=course, user=request.user)
    return redirect('profile', username=request.user.username)

@login_required
def update_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if course.publisher != request.user:
        return HttpResponse('You are not allowed to update this course')
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return Course_detail(request, course_id)
    else:
        form = CourseForm(instance=course)
    return render(request, 'Forms/Course/index.html', {'form': form})


@login_required
def view_course_videos(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if not AppliedCourse.objects.filter(course=course, user=request.user).exists() and course.publisher != request.user:
        return HttpResponseForbidden('You are not allowed to view these videos')
    if course.publisher == request.user:
        videos = Video.objects.filter(Course=course)
    else:
        videos = Video.objects.filter(Course=course ,State = 'active')
    return render(request, 'Courses/Videos.html', {'videos': videos})

@login_required
def watch_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if request.user != video.Course.publisher and video.State != 'active':
        return HttpResponseForbidden('You are not allowed to view this video')
    if not AppliedCourse.objects.filter(course=video.Course, user=request.user).exists() and video.Course.publisher != request.user:
        return HttpResponseForbidden('You are not allowed to view this video')
    return render(request, 'Courses/Video.html', {'video': video})

@login_required
def upload_video(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if course.publisher == request.user:
        if request.method == 'POST':
            form = VideoForm(request.POST, request.FILES)
            if form.is_valid():
                video = form.save(commit=False)
                video.Course = course
                video.save()
                return view_course_videos(request, course_id)
        else:
            form = VideoForm()
    else:
        return HttpResponse('You are not allowed to upload videos to this course')
    return render(request, 'Forms/Course/Videos.html', {'form': form})


@login_required
def Edit_Video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if video.Course.publisher != request.user:
        return HttpResponse('You are not allowed to update this course')
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            return view_course_videos(request, video.Course.id)
    else:
        form = VideoForm(instance=video)
    return render(request, 'Forms/Course/Videos.html', {'form': form})

@login_required
def delete_course_confirmation(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if course.publisher != request.user:
        return HttpResponse('You are not allowed to delete this course')
    if request.method == 'POST':
        course.delete()
        return ShowAllCourses(request)
    return render(request, 'Courses/delete_course_confirmation.html', {'course': course})

@login_required
def delete_video_confirmation(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if video.Course.publisher != request.user:
        return HttpResponse('You are not allowed to delete this course')
    if request.method == 'POST':
        video.delete()
        return view_course_videos(request, video.Course.id)
    return render(request, 'Courses/delete_video.html', {'video': video})
