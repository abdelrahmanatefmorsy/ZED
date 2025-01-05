from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
class Video(models.Model):
    video_title = models.CharField(max_length=100)
    video_description = models.TextField()
    video_duration = models.IntegerField()
    video = models.FileField(upload_to='videos/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    course_day = models.ForeignKey('CourseDay', related_name='videos', on_delete=models.CASCADE)

    def str(self):
        return self.video_title

class CourseDay(models.Model):
    course = models.ForeignKey('Course', related_name='days', on_delete=models.CASCADE)
    day_title = models.CharField(max_length=100)
    day_description = models.TextField()

    def str(self):
        return self.day_title
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/%Y/%m/%d/', blank=True,null=True)
    data_birth = models.DateField(null=True, blank=True)
    def str(self):
        return self.user.username
class Course(models.Model):
    COURSE_TYPE_CHOICES = [
        ('user_created', 'User Created'),
        ('apply', 'Apply'),
    ]
    catogries_choicses = [
        ('programming', 'programming'),
        ('montage', 'montage'),
        ('design', 'design'),
        ('engineering', 'engineering'),
        ('marketing', 'marketing'),
        ('business', 'business'),
        ('photography', 'photography'),
        ('networking', 'networking'),
        ('security', 'security'),
        ('other', 'other'),
    ]
    publisher = models.ForeignKey(User, related_name='courses', on_delete=models.CASCADE, null=True, blank=True)
    course_name = models.CharField(max_length=100)
    course_description = models.TextField()
    course_duration = models.IntegerField()
    course_image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    price = models.IntegerField()
    course_type = models.CharField(max_length=20, choices=COURSE_TYPE_CHOICES, default='apply')
    def str(self):
        return self.course_name

class Video(models.Model):
    video_title = models.CharField(max_length=100)
    video_description = models.TextField()
    video_duration = models.IntegerField()
    video = models.FileField(upload_to='videos/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    Course = models.ForeignKey('Course', related_name='videos', on_delete=models.CASCADE, null=True, blank=True)
    def str(self):
        return self.data_title
class AppliedCourse(models.Model):
    course = models.ForeignKey('Course', related_name='applied_courses', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, related_name='applied_courses', on_delete=models.CASCADE, null=True, blank=True)
    def str(self):
        return self.course.course_name
