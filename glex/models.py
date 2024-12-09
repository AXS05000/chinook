from django.db import models
from usuarios.models import CustomUsuario
from ia.models import CRM_FUI


class Administrativo(models.Model):

    usuario_modificacao = models.ForeignKey(
        CustomUsuario, on_delete=models.SET_NULL, null=True, blank=True
    )
    lideranca_equipe = models.FileField(
        upload_to="administrativo/", blank=True, null=True
    )
    reunioes_comerciais = models.FileField(
        upload_to="administrativo/", blank=True, null=True
    )
    uniformes_crachas = models.FileField(
        upload_to="administrativo/", blank=True, null=True
    )
    pagamento_boletos = models.FileField(
        upload_to="administrativo/", blank=True, null=True
    )
    conta_bancaria_pj = models.FileField(
        upload_to="administrativo/", blank=True, null=True
    )
    fluxo_caixa = models.FileField(upload_to="administrativo/", blank=True, null=True)
    inadimplencia = models.FileField(upload_to="administrativo/", blank=True, null=True)
    controle_balanco = models.FileField(
        upload_to="administrativo/", blank=True, null=True
    )
    planejamento_orcamento = models.FileField(
        upload_to="administrativo/", blank=True, null=True
    )
    orcamento_compartilhado = models.FileField(
        upload_to="administrativo/", blank=True, null=True
    )

    def __str__(self):

        return f"{self.usuario_modificacao.first_name} {self.usuario_modificacao.last_name}"


class Comercial(models.Model):
    usuario_modificacao = models.ForeignKey(
        CustomUsuario, on_delete=models.SET_NULL, null=True, blank=True
    )
    cortesia_visitantes = models.FileField(
        upload_to="comercial/", blank=True, null=True
    )
    participacao_mentoria = models.FileField(
        upload_to="comercial/", blank=True, null=True
    )
    equipe_comercial_contratada = models.FileField(
        upload_to="comercial/", blank=True, null=True
    )
    trilha_treinamento = models.FileField(upload_to="comercial/", blank=True, null=True)
    participacao_encontros_lideres = models.FileField(
        upload_to="comercial/", blank=True, null=True
    )
    funil_vendas_crm = models.FileField(upload_to="comercial/", blank=True, null=True)
    pontuacao_cliente_oculto = models.FileField(
        upload_to="comercial/", blank=True, null=True
    )
    participacao_campanhas = models.FileField(
        upload_to="comercial/", blank=True, null=True
    )
    pesquisa_concorrentes = models.FileField(
        upload_to="comercial/", blank=True, null=True
    )
    conversao_leads = models.FileField(upload_to="comercial/", blank=True, null=True)
    politica_comissionamento = models.FileField(
        upload_to="comercial/", blank=True, null=True
    )
    orcamento_mkt = models.FileField(upload_to="comercial/", blank=True, null=True)
    profissional_mkt = models.FileField(upload_to="comercial/", blank=True, null=True)
    entrega_kit_rematricula = models.FileField(
        upload_to="comercial/", blank=True, null=True
    )
    entrega_kit_visita = models.FileField(upload_to="comercial/", blank=True, null=True)
    leads_atraso_crm = models.FileField(upload_to="comercial/", blank=True, null=True)


#######################  QA ##########################


def upload_to_dominio1(instance, filename):
    return f"{instance.escola.id_escola}/escola/pdfs/dominio1/{filename}"


def upload_to_dominio2(instance, filename):
    return f"{instance.escola.id_escola}/escola/pdfs/dominio2/{filename}"


def upload_to_dominio3(instance, filename):
    return f"{instance.escola.id_escola}/escola/pdfs/dominio3/{filename}"


def upload_to_dominio4(instance, filename):
    return f"{instance.escola.id_escola}/escola/pdfs/dominio4/{filename}"


EXPECTATION_CHOICES = [
    (1, "1 - Below Expectations"),
    (2, "2 - Approaching Expectations"),
    (3, "3 - Meeting Expectations"),
    (4, "4 - Exceeding Expectations"),
]

class Dominio1(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="dominio1",
        verbose_name="Nome da Escola",
    )

    program_implementation = models.IntegerField(
        choices=EXPECTATION_CHOICES, blank=True, null=True, verbose_name="Program Implementation"
    )
    program_implementation_comment = models.TextField(
        blank=True, null=True, verbose_name="Comment for Program Implementation"
    )
    program_implementation_pdf = models.FileField(
        upload_to=upload_to_dominio1,
        blank=True,
        null=True,
        verbose_name="Program Implementation (PDF)",
    )

    staffing_instructional_program = models.IntegerField(
        choices=EXPECTATION_CHOICES, blank=True, null=True, verbose_name="Staffing the Instructional Program"
    )
    staffing_instructional_program_comment = models.TextField(
        blank=True, null=True, verbose_name="Comment for Staffing the Instructional Program"
    )
    staffing_instructional_program_pdf = models.FileField(
        upload_to=upload_to_dominio1,
        blank=True,
        null=True,
        verbose_name="Staffing the Instructional Program (PDF)",
    )

    resource_allocation = models.IntegerField(
        choices=EXPECTATION_CHOICES, blank=True, null=True, verbose_name="Resource Allocation"
    )
    resource_allocation_comment = models.TextField(
        blank=True, null=True, verbose_name="Comment for Resource Allocation"
    )
    resource_allocation_pdf = models.FileField(
        upload_to=upload_to_dominio1,
        blank=True,
        null=True,
        verbose_name="Resource Allocation (PDF)",
    )

    implementation_supervision_instructional_program = models.IntegerField(
        choices=EXPECTATION_CHOICES, blank=True, null=True,
        verbose_name="Implementation and Supervision of the Instructional Program",
    )
    implementation_supervision_instructional_program_comment = models.TextField(
        blank=True, null=True, verbose_name="Comment for Implementation and Supervision of the Instructional Program"
    )
    implementation_supervision_instructional_program_pdf = models.FileField(
        upload_to=upload_to_dominio1,
        blank=True,
        null=True,
        verbose_name="Implementation and Supervision (PDF)",
    )

    professional_learning_opportunities = models.IntegerField(
        choices=EXPECTATION_CHOICES, blank=True, null=True, verbose_name="Professional Learning Opportunities"
    )
    professional_learning_opportunities_comment = models.TextField(
        blank=True, null=True, verbose_name="Comment for Professional Learning Opportunities"
    )
    professional_learning_opportunities_pdf = models.FileField(
        upload_to=upload_to_dominio1,
        blank=True,
        null=True,
        verbose_name="Professional Learning Opportunities (PDF)",
    )

    commitment_to_bilingual_education = models.IntegerField(
        choices=EXPECTATION_CHOICES, blank=True, null=True, verbose_name="Commitment to Bilingual Education"
    )
    commitment_to_bilingual_education_comment = models.TextField(
        blank=True, null=True, verbose_name="Comment for Commitment to Bilingual Education"
    )
    commitment_to_bilingual_education_pdf = models.FileField(
        upload_to=upload_to_dominio1,
        blank=True,
        null=True,
        verbose_name="Commitment to Bilingual Education (PDF)",
    )

    strategic_planning = models.IntegerField(
        choices=EXPECTATION_CHOICES, blank=True, null=True, verbose_name="Strategic Planning"
    )
    strategic_planning_comment = models.TextField(
        blank=True, null=True, verbose_name="Comment for Strategic Planning"
    )
    strategic_planning_pdf = models.FileField(
        upload_to=upload_to_dominio1,
        blank=True,
        null=True,
        verbose_name="Strategic Planning (PDF)",
    )

    def __str__(self):
        return f"{self.escola} - Dominio1"


class Dominio2(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="dominio2",
        verbose_name="Nome da Escola",
    )

    culture = models.IntegerField(
        choices=EXPECTATION_CHOICES, blank=True, null=True, verbose_name="Culture"
    )
    culture_comment = models.TextField(
        blank=True, null=True, verbose_name="Comment for Culture"
    )
    culture_pdf = models.FileField(
        upload_to=upload_to_dominio2,
        blank=True,
        null=True,
        verbose_name="Culture (PDF)",
    )

    safe_and_caring_school = models.IntegerField(
        choices=EXPECTATION_CHOICES, blank=True, null=True, verbose_name="Safe and Caring School"
    )
    safe_and_caring_school_comment = models.TextField(
        blank=True, null=True, verbose_name="Comment for Safe and Caring School"
    )
    safe_and_caring_school_pdf = models.FileField(
        upload_to=upload_to_dominio2,
        blank=True,
        null=True,
        verbose_name="Safe and Caring School (PDF)",
    )

    equity_diversity_inclusion = models.IntegerField(
        choices=EXPECTATION_CHOICES, blank=True, null=True, verbose_name="Equity, Diversity and Inclusion"
    )
    equity_diversity_inclusion_comment = models.TextField(
        blank=True, null=True, verbose_name="Comment for Equity, Diversity and Inclusion"
    )
    equity_diversity_inclusion_pdf = models.FileField(
        upload_to=upload_to_dominio2,
        blank=True,
        null=True,
        verbose_name="Equity, Diversity and Inclusion (PDF)",
    )

    stakeholder_communication = models.IntegerField(
        choices=EXPECTATION_CHOICES, blank=True, null=True, verbose_name="Stakeholder Communication"
    )
    stakeholder_communication_comment = models.TextField(
        blank=True, null=True, verbose_name="Comment for Stakeholder Communication"
    )
    stakeholder_communication_pdf = models.FileField(
        upload_to=upload_to_dominio2,
        blank=True,
        null=True,
        verbose_name="Stakeholder Communication (PDF)",
    )

    stakeholder_engagement = models.IntegerField(
        choices=EXPECTATION_CHOICES, blank=True, null=True, verbose_name="Stakeholder Engagement"
    )
    stakeholder_engagement_comment = models.TextField(
        blank=True, null=True, verbose_name="Comment for Stakeholder Engagement"
    )
    stakeholder_engagement_pdf = models.FileField(
        upload_to=upload_to_dominio2,
        blank=True,
        null=True,
        verbose_name="Stakeholder Engagement (PDF)",
    )

    health_and_safety = models.IntegerField(
        choices=EXPECTATION_CHOICES, blank=True, null=True, verbose_name="Health and Safety"
    )
    health_and_safety_comment = models.TextField(
        blank=True, null=True, verbose_name="Comment for Health and Safety"
    )
    health_and_safety_pdf = models.FileField(
        upload_to=upload_to_dominio2,
        blank=True,
        null=True,
        verbose_name="Health and Safety (PDF)",
    )

    collection_interpretation_data = models.IntegerField(
        choices=EXPECTATION_CHOICES, blank=True, null=True,
        verbose_name="Collection and Interpretation of Whole School Assessment Data",
    )
    collection_interpretation_data_comment = models.TextField(
        blank=True, null=True,
        verbose_name="Comment for Collection and Interpretation of Whole School Assessment Data",
    )
    collection_interpretation_data_pdf = models.FileField(
        upload_to=upload_to_dominio2,
        blank=True,
        null=True,
        verbose_name="Collection and Interpretation of Whole School Assessment Data (PDF)",
    )

    def __str__(self):
        return f"{self.escola} - Dominio2"



class Dominio3(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="dominio3",
        verbose_name="Nome da Escola",
    )

    instructional_processes_practices = models.IntegerField(
        choices=EXPECTATION_CHOICES, blank=True, null=True,
        verbose_name="Instructional Processes and Practices",
    )
    instructional_processes_practices_comment = models.TextField(
        blank=True, null=True, verbose_name="Comment for Instructional Processes and Practices"
    )
    instructional_processes_practices_pdf = models.FileField(
        upload_to=upload_to_dominio3,
        blank=True,
        null=True,
        verbose_name="Instructional Processes and Practices (PDF)",
    )

    learning_plans = models.IntegerField(
        choices=EXPECTATION_CHOICES, blank=True, null=True, verbose_name="Learning Plans"
    )
    learning_plans_comment = models.TextField(
        blank=True, null=True, verbose_name="Comment for Learning Plans"
    )
    learning_plans_pdf = models.FileField(
        upload_to=upload_to_dominio3,
        blank=True,
        null=True,
        verbose_name="Learning Plans (PDF)",
    )

    student_centered_learning = models.IntegerField(
        choices=EXPECTATION_CHOICES, blank=True, null=True, verbose_name="Student Centered Learning"
    )
    student_centered_learning_comment = models.TextField(
        blank=True, null=True, verbose_name="Comment for Student Centered Learning"
    )
    student_centered_learning_pdf = models.FileField(
        upload_to=upload_to_dominio3,
        blank=True,
        null=True,
        verbose_name="Student Centered Learning (PDF)",
    )

    inclusionary_practices = models.IntegerField(
        choices=EXPECTATION_CHOICES, blank=True, null=True, verbose_name="Inclusionary Practices"
    )
    inclusionary_practices_comment = models.TextField(
        blank=True, null=True, verbose_name="Comment for Inclusionary Practices"
    )
    inclusionary_practices_pdf = models.FileField(
        upload_to=upload_to_dominio3,
        blank=True,
        null=True,
        verbose_name="Inclusionary Practices (PDF)",
    )

    teacher_collaboration = models.IntegerField(
        choices=EXPECTATION_CHOICES, blank=True, null=True, verbose_name="Teacher Collaboration"
    )
    teacher_collaboration_comment = models.TextField(
        blank=True, null=True, verbose_name="Comment for Teacher Collaboration"
    )
    teacher_collaboration_pdf = models.FileField(
        upload_to=upload_to_dominio3,
        blank=True,
        null=True,
        verbose_name="Teacher Collaboration (PDF)",
    )

    classroom_management = models.IntegerField(
        choices=EXPECTATION_CHOICES, blank=True, null=True, verbose_name="Classroom Management"
    )
    classroom_management_comment = models.TextField(
        blank=True, null=True, verbose_name="Comment for Classroom Management"
    )
    classroom_management_pdf = models.FileField(
        upload_to=upload_to_dominio3,
        blank=True,
        null=True,
        verbose_name="Classroom Management (PDF)",
    )

    supervision_evaluation = models.IntegerField(
        choices=EXPECTATION_CHOICES, blank=True, null=True, verbose_name="Supervision & Evaluation"
    )
    supervision_evaluation_comment = models.TextField(
        blank=True, null=True, verbose_name="Comment for Supervision & Evaluation"
    )
    supervision_evaluation_pdf = models.FileField(
        upload_to=upload_to_dominio3,
        blank=True,
        null=True,
        verbose_name="Supervision & Evaluation (PDF)",
    )

    def __str__(self):
        return f"{self.escola} - Dominio3"


class Dominio4(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="dominio4",
        verbose_name="Nome da Escola",
    )

    learning_goals_success_criteria = models.IntegerField(
        choices=EXPECTATION_CHOICES, blank=True, null=True, verbose_name="Learning Goals and Success Criteria"
    )
    learning_goals_success_criteria_comment = models.TextField(
        blank=True, null=True, verbose_name="Comment for Learning Goals and Success Criteria"
    )
    learning_goals_success_criteria_pdf = models.FileField(
        upload_to=upload_to_dominio4,
        blank=True,
        null=True,
        verbose_name="Learning Goals and Success Criteria (PDF)",
    )

    assessment_strategies_tools = models.IntegerField(
        choices=EXPECTATION_CHOICES, blank=True, null=True, verbose_name="Assessment Strategies and Tools"
    )
    assessment_strategies_tools_comment = models.TextField(
        blank=True, null=True, verbose_name="Comment for Assessment Strategies and Tools"
    )
    assessment_strategies_tools_pdf = models.FileField(
        upload_to=upload_to_dominio4,
        blank=True,
        null=True,
        verbose_name="Assessment Strategies and Tools (PDF)",
    )

    fair_assessment_practices = models.IntegerField(
        choices=EXPECTATION_CHOICES, blank=True, null=True, verbose_name="Fair Assessment Practices"
    )
    fair_assessment_practices_comment = models.TextField(
        blank=True, null=True, verbose_name="Comment for Fair Assessment Practices"
    )
    fair_assessment_practices_pdf = models.FileField(
        upload_to=upload_to_dominio4,
        blank=True,
        null=True,
        verbose_name="Fair Assessment Practices (PDF)",
    )

    assessment_triangulation_data = models.IntegerField(
        choices=EXPECTATION_CHOICES, blank=True, null=True,
        verbose_name="Assessment and the Triangulation of Data",
    )
    assessment_triangulation_data_comment = models.TextField(
        blank=True, null=True, verbose_name="Comment for Assessment and the Triangulation of Data"
    )
    assessment_triangulation_data_pdf = models.FileField(
        upload_to=upload_to_dominio4,
        blank=True,
        null=True,
        verbose_name="Assessment and the Triangulation of Data (PDF)",
    )

    reporting_student_achievement = models.IntegerField(
        choices=EXPECTATION_CHOICES, blank=True, null=True, verbose_name="Reporting Student Achievement"
    )
    reporting_student_achievement_comment = models.TextField(
        blank=True, null=True, verbose_name="Comment for Reporting Student Achievement"
    )
    reporting_student_achievement_pdf = models.FileField(
        upload_to=upload_to_dominio4,
        blank=True,
        null=True,
        verbose_name="Reporting Student Achievement (PDF)",
    )

    def __str__(self):
        return f"{self.escola} - Dominio4"




################################## BASE DE CONHECIMENTO ##############################################


class Base_de_Conhecimento_Geral(models.Model):
    titulo = models.CharField(max_length=255)
    topico = models.CharField(max_length=255, null=True, blank=True)
    sub_topico = models.CharField(max_length=255, null=True, blank=True)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.topico}"
    