from django.db import models
from django import forms
from .models import BlogComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ('name', 'email', 'content', 'parent')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address'}),
            'content': forms.Textarea(attrs={'placeholder': 'Enter your comment'}),
        }