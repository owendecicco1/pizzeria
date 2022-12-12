from django import forms 
from .models import *

class PizzaCommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        labels = {'comment': 'Comments'}


