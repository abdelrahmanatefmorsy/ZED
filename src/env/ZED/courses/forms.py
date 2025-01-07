from django import forms
from .models import  CourseDay, Course , UserProfile , Video
from django.contrib.auth.models import User



class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_description', 'course_duration', 'course_image','State']
        widgets = {
            'course_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course Name'}),
            'course_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Course Description'}),
            'course_duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Course Duration'}),
            'course_image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Course Image'}),
            'State': forms.Select(attrs={'class': 'form-control', 'placeholder': 'State'}),
        }
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'data_birth']
        widgets = {
            'profile_picture': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Profile Picture'}),
            'data_birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Data Birth'}),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'type': 'Password'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        }
        help_texts = {
            'username': None,
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    class Meta:
        fields = ['username', 'password']
        wedgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        }
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['video_title', 'video_description', 'video','State']
        widgets = {
            'video_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Video Title'}),
            'video_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Video Description'}),
            'video': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Video'}),
            'State': forms.Select(attrs={'class': 'form-control', 'placeholder': 'State'}),
        }
