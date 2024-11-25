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
        fields = [
            "escola",
            "program_implementation",
            "program_implementation_pdf",
            "staffing_instructional_program",
            "staffing_instructional_program_pdf",
            "resource_allocation",
            "resource_allocation_pdf",
            "implementation_supervision_instructional_program",
            "implementation_supervision_instructional_program_pdf",
            "professional_learning_opportunities",
            "professional_learning_opportunities_pdf",
            "commitment_to_bilingual_education",
            "commitment_to_bilingual_education_pdf",
            "strategic_planning",
            "strategic_planning_pdf",
        ]
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
        super().__init__(*args, **kwargs)
        # Remove a opção "-------" de todos os campos de RadioSelect
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.RadioSelect):
                field.choices = list(field.choices)[1:]


class Dominio2Form(forms.ModelForm):
    class Meta:
        model = Dominio2
        fields = [
            "escola",
            "culture",
            "culture_pdf",
            "safe_and_caring_school",
            "safe_and_caring_school_pdf",
            "equity_diversity_inclusion",
            "equity_diversity_inclusion_pdf",
            "stakeholder_communication",
            "stakeholder_communication_pdf",
            "stakeholder_engagement",
            "stakeholder_engagement_pdf",
            "health_and_safety",
            "health_and_safety_pdf",
            "collection_interpretation_data",
            "collection_interpretation_data_pdf",
        ]
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
        super().__init__(*args, **kwargs)
        # Remove a opção "-------" de todos os campos de RadioSelect
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.RadioSelect):
                field.choices = list(field.choices)[1:]


class Dominio3Form(forms.ModelForm):
    class Meta:
        model = Dominio3
        fields = [
            "escola",
            "instructional_processes_practices",
            "instructional_processes_practices_pdf",
            "learning_plans",
            "learning_plans_pdf",
            "student_centered_learning",
            "student_centered_learning_pdf",
            "inclusionary_practices",
            "inclusionary_practices_pdf",
            "teacher_collaboration",
            "teacher_collaboration_pdf",
            "classroom_management",
            "classroom_management_pdf",
            "supervision_evaluation",
            "supervision_evaluation_pdf",
        ]
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
        super().__init__(*args, **kwargs)
        # Remove a opção "-------" de todos os campos de RadioSelect
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.RadioSelect):
                field.choices = list(field.choices)[1:]


class Dominio4Form(forms.ModelForm):
    class Meta:
        model = Dominio4
        fields = [
            "escola",
            "learning_goals_success_criteria",
            "learning_goals_success_criteria_pdf",
            "assessment_strategies_tools",
            "assessment_strategies_tools_pdf",
            "fair_assessment_practices",
            "fair_assessment_practices_pdf",
            "assessment_triangulation_data",
            "assessment_triangulation_data_pdf",
            "reporting_student_achievement",
            "reporting_student_achievement_pdf",
        ]
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
        super().__init__(*args, **kwargs)
        # Remove a opção "-------" de todos os campos de RadioSelect
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.RadioSelect):
                field.choices = list(field.choices)[1:]
