from django import forms
from .models import Planificador_2024, CRM_FUI, Reclamacao
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


class ReclamacaoForm(forms.ModelForm):
    class Meta:
        model = Reclamacao
        fields = '__all__'
        widgets = {
            'data_reclamacao': DateInput(),
            'data_conclusao': DateInput(),
        }


class AtualizarIDEscolaForm(forms.Form):
    id_escola_atual = forms.ModelChoiceField(
        queryset=CRM_FUI.objects.all(),
        label="ID Escola Atual",
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    novo_id_escola = forms.IntegerField(
        label="Novo ID Escola",
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    def clean_novo_id_escola(self):
        novo_id = self.cleaned_data.get('novo_id_escola')
        if CRM_FUI.objects.filter(id_escola=novo_id).exists():
            raise forms.ValidationError("O novo ID Escola já existe. Escolha um ID único.")
        return novo_id