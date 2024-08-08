from django import forms
from .models import Planificador_2024
from datetime import datetime

class DateInput(forms.DateInput):
    input_type = 'date'
    
    def format_value(self, value):
        if value is None:
            return ''
        if isinstance(value, str):
            try:
                value = datetime.fromisoformat(value)
            except ValueError:
                return ''
        return value.strftime('%Y-%m-%d')

class PlanificadorForm(forms.ModelForm):
    class Meta:
        model = Planificador_2024
        fields = '__all__'
        widgets = {
            'ultima_data_atualizacao_bloc_drivers_comerciais_estrategicos': DateInput(),
            'data_abertura_matricula_2025': DateInput(),
            'data_de_abertura_da_circular_2025': DateInput(),
            'data_implementacao_arvore': DateInput(),
            'ultima_data_atualizacao_bloc_funil_comercial': DateInput(),
            'ultima_data_atualizacao_bloc_drivers_comerciais_meio': DateInput(),
            'data_atualizacao_resultados': DateInput(),
        }
