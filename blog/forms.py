from .models import Commnet
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Commnet
        filed = ('content',)