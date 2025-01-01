from django.contrib import admin
from django.urls import path
from django.urls import include
from.views import index, CourseDay, CourseForm , login_view, signup_view, logout_view, Home,ShowAllCourses, Course_detail,add_course_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/',login_view , name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('Home/', Home, name='Home'),
    path('courses/',ShowAllCourses, name='showAllCourses'),
    path('course/<int:course_id>/', Course_detail, name='course_detail'),
    path('add-course/', add_course_view, name='add_course'),

]
