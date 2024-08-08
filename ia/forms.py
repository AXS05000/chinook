from django import forms
from .models import Planificador_2024

class PlanificadorForm(forms.ModelForm):
    class Meta:
        model = Planificador_2024
        fields = '__all__'
