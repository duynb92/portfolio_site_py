from django.db import models
from django import forms
from .models import BlogComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ('name', 'email', 'content',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email address'}),
            'content': forms.Textarea(
                attrs={'placeholder': 'Comment'}),
        }
        error_messages = {
            'name': {
                'max_length': ("Name is too long."),
                'empty' : ("Name is empty."),
            },
        }