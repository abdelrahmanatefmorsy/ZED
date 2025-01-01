from django import forms
from .models import  CourseDay, Course
from django.contrib.auth.models import User



class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_description', 'course_duration', 'course_image', 'price', 'course_type']
        widgets = {
            'course_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course Name'}),
            'course_description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Course Description'}),
            'course_duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Course Duration'}),
            'course_image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Course Image'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'course_type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Course Type'}),
        }



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        wedgets = {
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
