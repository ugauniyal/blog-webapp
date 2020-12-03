from django import forms
from .models import Post

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title For Your Blog'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content For Your Blog'}),
        }