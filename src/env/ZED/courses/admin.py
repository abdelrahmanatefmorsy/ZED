from django.contrib import admin
from .models import Course , CourseDay , Video,UserProfile , AppliedCourse
admin.site.register(Course)
admin.site.register(UserProfile)
admin.site.register(AppliedCourse)
admin.site.register(Video)
