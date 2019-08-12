from django import forms

from .models import Post

class PostForm(forms.ModelForm): # Tell Django that it is a ModelForm

    class Meta: # Our class that will tell for which form this model is.
        model = Post
        fields = ('title', 'text',)