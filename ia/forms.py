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
            'data_inicio_reunioes_rematricula': DateInput(),
            'data_contato_familias_pendentes_rematricula': DateInput(),
            'data_ativacao_alunos_rematriculados_sem_slm': DateInput(),


        }


class ReclamacaoForm(forms.ModelForm):
    class Meta:
        model = Reclamacao
        fields = '__all__'
        widgets = {
            'data_reclamacao': DateInput(),
            'data_conclusao': DateInput(),
            'descricao_reclamacao': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'investigacao': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'parecer_final': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),  # Atualizado
            'resposta_enviada_reclamante': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),  # Novo campo
        }

    def __init__(self, *args, **kwargs):
        super(ReclamacaoForm, self).__init__(*args, **kwargs)
        # Define todos os campos como não obrigatórios
        for field in self.fields:
            self.fields[field].required = False
        self.fields['escola'].required = True
        self.fields['nome_responsavel'].required = True
        self.fields['data_reclamacao'].required = True
        self.fields['origem_reclamacao'].required = True
        self.fields['prioridade'].required = True
        self.fields['titulo'].required = True
        self.fields['email'].required = True
        self.fields['status'].required = True
        self.fields['descricao_reclamacao'].required = True
        self.fields['investigacao'].required = True


    def clean(self):
        cleaned_data = super().clean()
        prioridade = cleaned_data.get('prioridade')

        # Se "Sim" for selecionado na pergunta grave, força a prioridade como "Alta"
        if self.data.get('reclamacao-grave') == 'sim':
            cleaned_data['prioridade'] = 'alta'  # Preenche automaticamente com "Alta"

        return cleaned_data



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