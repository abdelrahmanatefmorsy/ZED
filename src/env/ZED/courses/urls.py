from django.contrib import admin
from django.urls import path
from django.urls import include
from.views import index, CourseDay, CourseForm , login_view, signup_view, logout_view, Home,ShowAllCourses, Course_detail,add_course_view
from.views import update_profile_view , Profile_view , apply_to_course , update_course , upload_video ,view_course_videos ,watch_video
from .views import Edit_Video , delete_course_confirmation ,delete_video_confirmation
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
    path('update-profile/', update_profile_view, name='update_profile'),
    path('profile/<str:username>/', Profile_view, name='profile'),
    path('apply/<int:course_id>/', apply_to_course, name='apply_to_course'),
    path('update-course/<int:course_id>/', update_course, name='update_course'),
    path('course/<int:course_id>/upload_video/', upload_video, name='upload_video'),
    path('course/<int:course_id>/videos/', view_course_videos, name='view_course_videos'),
    path('video/<int:video_id>/', watch_video, name='watch_video'),
    path('video/<int:video_id>/edit/', Edit_Video, name='edit_video'),
    path('course/<int:course_id>/delete/', delete_course_confirmation, name='delete_course_confirmation'),
    path('video/<int:video_id>/delete/', delete_video_confirmation, name='delete_video_confirmation'),
]
