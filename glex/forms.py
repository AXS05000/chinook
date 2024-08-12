from django import forms
from .models import Administrativo, Comercial
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
