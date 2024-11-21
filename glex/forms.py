from django import forms
from .models import Administrativo, Comercial, Dominio1
from django.core.exceptions import ValidationError


class PDFFileField(forms.FileField):
    def validate(self, value):
        # Valida apenas se o campo tiver um arquivo (value não for None)
        if value and not value.name.endswith('.pdf'):
            raise ValidationError('Somente arquivos PDF são permitidos.')
        super().validate(value)


class AdministrativoForm(forms.ModelForm):
    lideranca_equipe = PDFFileField(required=False)
    reunioes_comerciais = PDFFileField(required=False)
    uniformes_crachas = PDFFileField(required=False)
    pagamento_boletos = PDFFileField(required=False)
    conta_bancaria_pj = PDFFileField(required=False)
    fluxo_caixa = PDFFileField(required=False)
    inadimplencia = PDFFileField(required=False)
    controle_balanco = PDFFileField(required=False)
    planejamento_orcamento = PDFFileField(required=False)
    orcamento_compartilhado = PDFFileField(required=False)

    class Meta:
        model = Administrativo
        fields = "__all__"


class ComercialForm(forms.ModelForm):
    cortesia_visitantes = PDFFileField(required=False)
    participacao_mentoria = PDFFileField(required=False)
    equipe_comercial_contratada = PDFFileField(required=False)
    trilha_treinamento = PDFFileField(required=False)
    participacao_encontros_lideres = PDFFileField(required=False)
    funil_vendas_crm = PDFFileField(required=False)
    pontuacao_cliente_oculto = PDFFileField(required=False)
    participacao_campanhas = PDFFileField(required=False)
    pesquisa_concorrentes = PDFFileField(required=False)
    conversao_leads = PDFFileField(required=False)
    politica_comissionamento = PDFFileField(required=False)
    orcamento_mkt = PDFFileField(required=False)
    profissional_mkt = PDFFileField(required=False)
    entrega_kit_rematricula = PDFFileField(required=False)
    entrega_kit_visita = PDFFileField(required=False)
    leads_atraso_crm = PDFFileField(required=False)

    class Meta:
        model = Comercial
        fields = "__all__"



class Dominio1Form(forms.ModelForm):
    class Meta:
        model = Dominio1
        fields = [
            'escola',
            'program_implementation',
            'program_implementation_pdf',
            'staffing_instructional_program',
            'staffing_instructional_program_pdf',
            'resource_allocation',
            'resource_allocation_pdf',
            'implementation_supervision_instructional_program',
            'implementation_supervision_instructional_program_pdf',
            'professional_learning_opportunities',
            'professional_learning_opportunities_pdf',
            'commitment_to_bilingual_education',
            'commitment_to_bilingual_education_pdf',
            'strategic_planning',
            'strategic_planning_pdf',
        ]
        widgets = {
            'program_implementation': forms.RadioSelect,
            'staffing_instructional_program': forms.RadioSelect,
            'resource_allocation': forms.RadioSelect,
            'implementation_supervision_instructional_program': forms.RadioSelect,
            'professional_learning_opportunities': forms.RadioSelect,
            'commitment_to_bilingual_education': forms.RadioSelect,
            'strategic_planning': forms.RadioSelect,
        }