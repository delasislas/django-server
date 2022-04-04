from django import forms
from . import models

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = [
            'title',
            'content',
            'slug',
            'thumb',
        ]
