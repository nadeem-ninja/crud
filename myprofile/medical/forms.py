from django import forms
from .models import MedicalStore


class MedicalForm(forms.ModelForm):
    class Meta:
        model = MedicalStore
        fields = '__all__'
