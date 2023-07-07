from django import forms
from .models import Contents
from django.core.exceptions import ValidationError

class ContentBaseForm(forms.ModelForm):
    class Meta:
        model = Contents
        fields = '__all__'