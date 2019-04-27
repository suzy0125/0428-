from django import forms
from .models import Person

class PostForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = {'name','grade','age', 'major','hometown',}