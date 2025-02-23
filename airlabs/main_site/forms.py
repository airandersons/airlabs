from django import forms
from .models import Testimonials, PostComments

class TestimonialsForm(forms.ModelForm):
    class Meta:
        model = Testimonials
        fields = ['name', 'profession', 'comment', 'image']

class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComments
        fields = ['author_name', 'author_email', 'author_image', 'comment']
        widgets = {
            'author_name': forms.TextInput(attrs={'type': 'text', 'class': 'form-control', 'placeholder': 'Your Name'}),
            'author_email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control', 'placeholder': 'Email'}),
            'author_image': forms.ClearableFileInput(attrs={'type': 'file', 'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your comment here....', 'rows': '5'})
        }