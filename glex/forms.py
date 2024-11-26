from django import forms
from .models import Administrativo, Comercial, Dominio1, Dominio2, Dominio3, Dominio4
from django.core.exceptions import ValidationError


class PDFFileField(forms.FileField):
    def validate(self, value):
        # Valida apenas se o campo tiver um arquivo (value não for None)
        if value and not value.name.endswith(".pdf"):
            raise ValidationError("Somente arquivos PDF são permitidos.")
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
        exclude = ["escola"]  # O campo escola será preenchido automaticamente
        widgets = {
            "program_implementation": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check"
                }
            ),
            "staffing_instructional_program": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check"
                }
            ),
            "resource_allocation": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check"
                }
            ),
            "implementation_supervision_instructional_program": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check"
                }
            ),
            "professional_learning_opportunities": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check"
                }
            ),
            "commitment_to_bilingual_education": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check"
                }
            ),
            "strategic_planning": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        escola_id = kwargs.pop("escola_id", None)
        super().__init__(*args, **kwargs)
        if escola_id:
            self.fields["escola"].initial = escola_id
        # Remove a opção "-------" de todos os campos de RadioSelect
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.RadioSelect):
                field.choices = list(field.choices)[1:]


class Dominio2Form(forms.ModelForm):
    class Meta:
        model = Dominio2
        exclude = ["escola"]
        widgets = {
            "culture": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check"
                }
            ),
            "safe_and_caring_school": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check"
                }
            ),
            "equity_diversity_inclusion": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check"
                }
            ),
            "stakeholder_communication": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check"
                }
            ),
            "stakeholder_engagement": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check"
                }
            ),
            "health_and_safety": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check"
                }
            ),
            "collection_interpretation_data": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        escola_id = kwargs.pop("escola_id", None)
        super().__init__(*args, **kwargs)
        if escola_id:
            self.fields["escola"].initial = escola_id
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.RadioSelect):
                field.choices = list(field.choices)[1:]


class Dominio3Form(forms.ModelForm):
    class Meta:
        model = Dominio3
        exclude = ["escola"]
        widgets = {
            "instructional_processes_practices": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check"
                }
            ),
            "learning_plans": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check"
                }
            ),
            "student_centered_learning": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check"
                }
            ),
            "inclusionary_practices": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check"
                }
            ),
            "teacher_collaboration": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check"
                }
            ),
            "classroom_management": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check"
                }
            ),
            "supervision_evaluation": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        escola_id = kwargs.pop("escola_id", None)
        super().__init__(*args, **kwargs)
        if escola_id:
            self.fields["escola"].initial = escola_id
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.RadioSelect):
                field.choices = list(field.choices)[1:]


class Dominio4Form(forms.ModelForm):
    class Meta:
        model = Dominio4
        exclude = ["escola"]
        widgets = {
            "learning_goals_success_criteria": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check"
                }
            ),
            "assessment_strategies_tools": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check"
                }
            ),
            "fair_assessment_practices": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check"
                }
            ),
            "assessment_triangulation_data": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check"
                }
            ),
            "reporting_student_achievement": forms.RadioSelect(
                attrs={
                    "class": "horizontal-radio form-check-label form-check-input form-check"
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        escola_id = kwargs.pop("escola_id", None)
        super().__init__(*args, **kwargs)
        if escola_id:
            self.fields["escola"].initial = escola_id
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.RadioSelect):
                field.choices = list(field.choices)[1:]
