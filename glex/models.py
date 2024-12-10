from django.db import models
from usuarios.models import CustomUsuario
from ia.models import CRM_FUI

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



################################## GLEX ##############################################


def upload_to_gestao_parceria(instance, filename):
    return f"glex/{instance.escola.id_escola}/gestao_parceria/{filename}"

CHOICES = [
    (1, "Sim"),
    (2, "Não"),
    (3, "Não Aplicável"),
]

class GlexGestaoDeParceria(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="gestao_de_parceria",
        verbose_name="Nome da Escola",
    )

    # 1.01
    registros_documentacao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="1.01 - A escola possui registros atualizados de toda a documentação, registro, negócios e licenças educacionais necessárias para operar como uma escola de acordo com os requisitos regionais?"
    )
    registros_documentacao_comment = models.TextField(
        blank=True, null=True, verbose_name="1.01 - Comentário:"
    )
    registros_documentacao_file = models.FileField(
        upload_to=upload_to_gestao_parceria,
        blank=True,
        null=True,
        verbose_name="1.01 - Arquivo de registros atualizados de documentação",
    )

    # 1.02
    polices_seguro = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="1.02 - A escola tem registro de apólices de seguro ativas que estão de acordo com os requisitos regionais?"
    )
    polices_seguro_comment = models.TextField(
        blank=True, null=True, verbose_name="1.02 - Comentário:"
    )
    polices_seguro_file = models.FileField(
        upload_to=upload_to_gestao_parceria,
        blank=True,
        null=True,
        verbose_name="1.02 - Arquivo de apólices de seguro ativas",
    )

    # 1.03
    registros_legais = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="1.03 - A escola pode demonstrar que não há registros de processos judiciais, penalidades ou multas em vista de seus registros ou operações aplicadas pelas autoridades locais?"
    )
    registros_legais_comment = models.TextField(
        blank=True, null=True, verbose_name="1.03 - Comentário:"
    )
    registros_legais_file = models.FileField(
        upload_to=upload_to_gestao_parceria,
        blank=True,
        null=True,
        verbose_name="1.03 - Arquivo de ausência de registros de processos legais",
    )

    # 1.04
    contrato_franquia = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="1.04 - O franqueado conhece e cumpre as disposições do contrato de Franquia?"
    )
    contrato_franquia_comment = models.TextField(
        blank=True, null=True, verbose_name="1.04 - Comentário:"
    )
    contrato_franquia_file = models.FileField(
        upload_to=upload_to_gestao_parceria,
        blank=True,
        null=True,
        verbose_name="1.04 - Arquivo sobre contrato de franquia",
    )

    # 1.05
    senso_franquia = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="1.05 - Preenchimento do senso de Franchising anual?"
    )
    senso_franquia_comment = models.TextField(
        blank=True, null=True, verbose_name="1.05 - Comentário:"
    )
    senso_franquia_file = models.FileField(
        upload_to=upload_to_gestao_parceria,
        blank=True,
        null=True,
        verbose_name="1.05 - Arquivo do senso de Franchising anual",
    )

    # 1.06
    reclamacoes_defesa_consumidor = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="1.06 - O franqueado evita reclamações junto aos órgãos de defesa do consumidor?"
    )
    reclamacoes_defesa_consumidor_comment = models.TextField(
        blank=True, null=True, verbose_name="1.06 - Comentário:"
    )
    reclamacoes_defesa_consumidor_file = models.FileField(
        upload_to=upload_to_gestao_parceria,
        blank=True,
        null=True,
        verbose_name="1.06 - Arquivo de reclamações em órgãos de defesa do consumidor",
    )

    # 1.07
    envio_cases_sucesso = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="1.07 - Faz o envio dos cases de sucesso no ano vigente?"
    )
    envio_cases_sucesso_comment = models.TextField(
        blank=True, null=True, verbose_name="1.07 - Comentário:"
    )
    envio_cases_sucesso_file = models.FileField(
        upload_to=upload_to_gestao_parceria,
        blank=True,
        null=True,
        verbose_name="1.07 - Arquivo sobre envio de cases de sucesso",
    )

    # 1.08
    cadastro_crm = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="1.08 - Mantém o cadastro atualizado no CRM B2C?"
    )
    cadastro_crm_comment = models.TextField(
        blank=True, null=True, verbose_name="1.08 - Comentário:"
    )
    cadastro_crm_file = models.FileField(
        upload_to=upload_to_gestao_parceria,
        blank=True,
        null=True,
        verbose_name="1.08 - Arquivo sobre manutenção do cadastro no CRM B2C",
    )

    # 1.09
    avcb_atualizado = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="1.09 - A escola possui o AVCB (Auto de Vistoria do Corpo de Bombeiros) atualizado?"
    )
    avcb_atualizado_comment = models.TextField(
        blank=True, null=True, verbose_name="1.09 - Comentário:"
    )
    avcb_atualizado_file = models.FileField(
        upload_to=upload_to_gestao_parceria,
        blank=True,
        null=True,
        verbose_name="1.09 - Arquivo do AVCB atualizado",
    )

    # 1.10
    alvara_sanitaria = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="1.10 - O alvará de vigilância sanitária da escola está vigente pela prefeitura do município?"
    )
    alvara_sanitaria_comment = models.TextField(
        blank=True, null=True, verbose_name="1.10 - Comentário:"
    )
    alvara_sanitaria_file = models.FileField(
        upload_to=upload_to_gestao_parceria,
        blank=True,
        null=True,
        verbose_name="1.10 - Arquivo do alvará de vigilância sanitária vigente",
    )

    # 1.11
    encontros_lideres = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="1.11 - Participou de pelo menos 8 'Encontros de líderes' nos últimos 12 meses?"
    )
    encontros_lideres_comment = models.TextField(
        blank=True, null=True, verbose_name="1.11 - Comentário:"
    )
    encontros_lideres_file = models.FileField(
        upload_to=upload_to_gestao_parceria,
        blank=True,
        null=True,
        verbose_name="1.11 - Arquivo sobre participação em Encontros de Líderes",
    )

    def __str__(self):
        return f"{self.escola} - Gestão de Parceria"


def upload_to_gente(instance, filename):
    return f"glex/{instance.escola.id_escola}/gente/{filename}"

class GlexGente(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="gente",
        verbose_name="Nome da Escola",
    )

    # 2.01
    funcionarios_presentes = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="2.01 - A escola pode demonstrar que está com todos os funcionários - que todo o pessoal administrativo, acadêmico e de manutenção necessário está no local?"
    )
    funcionarios_presentes_comment = models.TextField(
        blank=True, null=True, verbose_name="2.01 - Comentário:"
    )
    funcionarios_presentes_file = models.FileField(
        upload_to=upload_to_gente,
        blank=True,
        null=True,
        verbose_name="2.01 - Arquivo de funcionários presentes no local",
    )

    # 2.02
    registros_licencas = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="2.02 - A escola pode produzir registros atualizados que demonstrem que todos os funcionários (incluindo terceirizados / contratados) possuem as licenças e qualificações necessárias para suas funções?"
    )
    registros_licencas_comment = models.TextField(
        blank=True, null=True, verbose_name="2.02 - Comentário:"
    )
    registros_licencas_file = models.FileField(
        upload_to=upload_to_gente,
        blank=True,
        null=True,
        verbose_name="2.02 - Arquivo de registros de licenças e qualificações atualizados",
    )

    # 2.03
    uso_uniformes = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="2.03 - Todos os funcionários e alunos estão usando uniformes em conformidade com a Política de Uniformes da Maple Bear?"
    )
    uso_uniformes_comment = models.TextField(
        blank=True, null=True, verbose_name="2.03 - Comentário:"
    )
    uso_uniformes_file = models.FileField(
        upload_to=upload_to_gente,
        blank=True,
        null=True,
        verbose_name="2.03 - Arquivo sobre uso de uniformes conforme a política",
    )

    # 2.04
    desenvolvimento_profissional = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="2.04 - A escola pode demonstrar que realiza desenvolvimento profissional contínuo e treinamento relevante para funcionários em todas as áreas da Escola, em intervalos apropriados?"
    )
    desenvolvimento_profissional_comment = models.TextField(
        blank=True, null=True, verbose_name="2.04 - Comentário:"
    )
    desenvolvimento_profissional_file = models.FileField(
        upload_to=upload_to_gente,
        blank=True,
        null=True,
        verbose_name="2.04 - Arquivo sobre desenvolvimento profissional contínuo",
    )

    # 2.05
    controle_absenteismo = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="2.05 - Controla a taxa de absenteísmo, turnover e as horas extras trabalhadas?"
    )
    controle_absenteismo_comment = models.TextField(
        blank=True, null=True, verbose_name="2.05 - Comentário:"
    )
    controle_absenteismo_file = models.FileField(
        upload_to=upload_to_gente,
        blank=True,
        null=True,
        verbose_name="2.05 - Arquivo sobre controle de absenteísmo, turnover e horas extras",
    )

    # 2.06
    plano_carreira = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="2.06 - Tem estabelecido um Plano e Carreira/Cargos e Salários com critérios que envolvam as performances, as competências e os desenvolvimentos entre as avaliações de desempenho?"
    )
    plano_carreira_comment = models.TextField(
        blank=True, null=True, verbose_name="2.06 - Comentário:"
    )
    plano_carreira_file = models.FileField(
        upload_to=upload_to_gente,
        blank=True,
        null=True,
        verbose_name="2.06 - Arquivo sobre Plano de Carreira e Salários estruturado",
    )

    # 2.07
    entrevista_desligamento = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="2.07 - Realizou entrevista de desligamento com todos os ex-colaboradores?"
    )
    entrevista_desligamento_comment = models.TextField(
        blank=True, null=True, verbose_name="2.07 - Comentário:"
    )
    entrevista_desligamento_file = models.FileField(
        upload_to=upload_to_gente,
        blank=True,
        null=True,
        verbose_name="2.07 - Arquivo sobre entrevistas de desligamento realizadas",
    )

    # 2.08
    comunicacao_interna = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="2.08 - Possuí pelo menos um canal de comunicação interna para seus Colaboradores e Prestadores de Serviços e este material é compartilhado com todos?"
    )
    comunicacao_interna_comment = models.TextField(
        blank=True, null=True, verbose_name="2.08 - Comentário:"
    )
    comunicacao_interna_file = models.FileField(
        upload_to=upload_to_gente,
        blank=True,
        null=True,
        verbose_name="2.08 - Arquivo sobre canal de comunicação interna disponível",
    )

    # 2.09
    legislacao_trabalhista = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="2.09 - Cumpre a legislação trabalhista quanto às obrigações em relação aos Colaboradores?"
    )
    legislacao_trabalhista_comment = models.TextField(
        blank=True, null=True, verbose_name="2.09 - Comentário:"
    )
    legislacao_trabalhista_file = models.FileField(
        upload_to=upload_to_gente,
        blank=True,
        null=True,
        verbose_name="2.09 - Arquivo sobre cumprimento da legislação trabalhista",
    )

    # 2.10
    descricao_cargos = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="2.10 - Disponibiliza de forma visual as Descrições dos Cargos existentes na Unidade?"
    )
    descricao_cargos_comment = models.TextField(
        blank=True, null=True, verbose_name="2.10 - Comentário:"
    )
    descricao_cargos_file = models.FileField(
        upload_to=upload_to_gente,
        blank=True,
        null=True,
        verbose_name="2.10 - Arquivo sobre disponibilização visual de descrições de cargos",
    )
    # 2.11
    onboarding_colaboradores = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="2.11 - Todos os Colaboradores passaram pelo onboarding referente a sua função no mês de sua contratação?"
    )
    onboarding_colaboradores_comment = models.TextField(
        blank=True, null=True, verbose_name="2.11 - Comentário:"
    )
    onboarding_colaboradores_file = models.FileField(
        upload_to=upload_to_gente,
        blank=True,
        null=True,
        verbose_name="2.11 - Arquivo sobre onboarding realizado no mês de contratação",
    )

    # 2.12
    acesso_academy = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="2.12 - Todos os Colaboradores da Franquia, aptos a receber treinamentos, têm acesso à Maple Bear Academy?"
    )
    acesso_academy_comment = models.TextField(
        blank=True, null=True, verbose_name="2.12 - Comentário:"
    )
    acesso_academy_file = models.FileField(
        upload_to=upload_to_gente,
        blank=True,
        null=True,
        verbose_name="2.12 - Arquivo sobre acesso à Maple Bear Academy",
    )

    # 2.13
    identificacao_colaboradores = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="2.13 - Os Colaboradores trabalham com identificação?"
    )
    identificacao_colaboradores_comment = models.TextField(
        blank=True, null=True, verbose_name="2.13 - Comentário:"
    )
    identificacao_colaboradores_file = models.FileField(
        upload_to=upload_to_gente,
        blank=True,
        null=True,
        verbose_name="2.13 - Arquivo sobre identificação dos colaboradores",
    )

    # 2.14
    pesquisa_clima = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="2.14 - Aplicou a pesquisa de Clima Organizacional e desenvolveu Plano de Ação com intuito de obter melhores resultados?"
    )
    pesquisa_clima_comment = models.TextField(
        blank=True, null=True, verbose_name="2.14 - Comentário:"
    )
    pesquisa_clima_file = models.FileField(
        upload_to=upload_to_gente,
        blank=True,
        null=True,
        verbose_name="2.14 - Arquivo sobre pesquisa de Clima Organizacional aplicada",
    )

    # 2.15
    recrutamento_selecao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="2.15 - Tem e aplica um processo de Recrutamento e Seleção estruturado e padronizado?"
    )
    recrutamento_selecao_comment = models.TextField(
        blank=True, null=True, verbose_name="2.15 - Comentário:"
    )
    recrutamento_selecao_file = models.FileField(
        upload_to=upload_to_gente,
        blank=True,
        null=True,
        verbose_name="2.15 - Arquivo sobre processo de Recrutamento e Seleção estruturado",
    )

    # 2.16
    avaliacao_desempenho = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="2.16 - Implementa e comunica os funcionários sobre avaliação de desempenho e comportamento dos Colaboradores?"
    )
    avaliacao_desempenho_comment = models.TextField(
        blank=True, null=True, verbose_name="2.16 - Comentário:"
    )
    avaliacao_desempenho_file = models.FileField(
        upload_to=upload_to_gente,
        blank=True,
        null=True,
        verbose_name="2.16 - Arquivo sobre avaliação de desempenho comunicada",
    )

    def __str__(self):
        return f"{self.escola} - Gente"




def upload_to_administrativo(instance, filename):
    return f"glex/{instance.escola.id_escola}/administrativo/{filename}"

class GlexAdministrativo(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="administrativo",
        verbose_name="Nome da Escola",
    )

    # 3.01
    profissionais_qualificados = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="3.01 Profissionais qualificados na recepção"
    )
    profissionais_qualificados_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 3.01"
    )
    profissionais_qualificados_file = models.FileField(
        upload_to=upload_to_administrativo,
        blank=True,
        null=True,
        verbose_name="3.01 Profissionais qualificados na recepção",
    )

    # 3.02
    sistema_administracao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="3.02 Uso do sistema de administração escolar"
    )
    sistema_administracao_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 3.02"
    )
    sistema_administracao_file = models.FileField(
        upload_to=upload_to_administrativo,
        blank=True,
        null=True,
        verbose_name="3.02 Uso do sistema de administração escolar",
    )

    # 3.03
    pagamentos_em_dia = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="3.03 Pagamentos à sede regional em dia"
    )
    pagamentos_em_dia_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 3.03"
    )
    pagamentos_em_dia_file = models.FileField(
        upload_to=upload_to_administrativo,
        blank=True,
        null=True,
        verbose_name="3.03 Pagamentos à sede regional em dia",
    )

    # 3.04
    gerencia_queixas = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="3.04 Processo para gerenciar queixas da comunidade"
    )
    gerencia_queixas_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 3.04"
    )
    gerencia_queixas_file = models.FileField(
        upload_to=upload_to_administrativo,
        blank=True,
        null=True,
        verbose_name="3.04 Processo para gerenciar queixas da comunidade",
    )

    # 3.05
    desempenho_kpi = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="3.05 Desempenho do KPI alinhado com metas regionais"
    )
    desempenho_kpi_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 3.05"
    )
    desempenho_kpi_file = models.FileField(
        upload_to=upload_to_administrativo,
        blank=True,
        null=True,
        verbose_name="3.05 Desempenho do KPI alinhado com metas regionais",
    )

    # 3.06
    politica_negocios = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="3.06 Adesão à Política de Negócios Maple Bear"
    )
    politica_negocios_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 3.06"
    )
    politica_negocios_file = models.FileField(
        upload_to=upload_to_administrativo,
        blank=True,
        null=True,
        verbose_name="3.06 Adesão à Política de Negócios Maple Bear",
    )

    # 3.07
    controle_inadimplencia = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="3.07 Controle de inadimplência com os clientes"
    )
    controle_inadimplencia_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 3.07"
    )
    controle_inadimplencia_file = models.FileField(
        upload_to=upload_to_administrativo,
        blank=True,
        null=True,
        verbose_name="3.07 Controle de inadimplência com os clientes",
    )

    # 3.08
    balanco_dre = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="3.08 Realiza Balanço Patrimonial e DRE"
    )
    balanco_dre_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 3.08"
    )
    balanco_dre_file = models.FileField(
        upload_to=upload_to_administrativo,
        blank=True,
        null=True,
        verbose_name="3.08 Realiza Balanço Patrimonial e DRE",
    )

    # 3.09
    planejamento_orcamento = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="3.09 Planejamento de orçamento antes do próximo ano"
    )
    planejamento_orcamento_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 3.09"
    )
    planejamento_orcamento_file = models.FileField(
        upload_to=upload_to_administrativo,
        blank=True,
        null=True,
        verbose_name="3.09 Planejamento de orçamento antes do próximo ano",
    )

    # 3.10
    compartilhamento_orcamento = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="3.10 Compartilhamento do orçamento com áreas operacionais"
    )
    compartilhamento_orcamento_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 3.10"
    )
    compartilhamento_orcamento_file = models.FileField(
        upload_to=upload_to_administrativo,
        blank=True,
        null=True,
        verbose_name="3.10 Compartilhamento do orçamento com áreas operacionais",
    )

    def __str__(self):
        return f"{self.escola} - Administrativo"


def upload_to_tecnologia(instance, filename):
    return f"glex/{instance.escola.id_escola}/tecnologia/{filename}"

class GlexTecnologia(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="tecnologia",
        verbose_name="Nome da Escola",
    )

    # 4.01
    uso_intranet = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="4.01 Uso da Intranet Maple Bear"
    )
    uso_intranet_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 4.01"
    )
    uso_intranet_file = models.FileField(
        upload_to=upload_to_tecnologia,
        blank=True,
        null=True,
        verbose_name="4.01 Uso da Intranet Maple Bear",
    )

    # 4.02
    cadastro_lex = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="4.02 Colaboradores cadastrados na LEX"
    )
    cadastro_lex_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 4.02"
    )
    cadastro_lex_file = models.FileField(
        upload_to=upload_to_tecnologia,
        blank=True,
        null=True,
        verbose_name="4.02 Colaboradores cadastrados na LEX",
    )

    # 4.03
    crm_b2c = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="4.03 CRM B2C implementado"
    )
    crm_b2c_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 4.03"
    )
    crm_b2c_file = models.FileField(
        upload_to=upload_to_tecnologia,
        blank=True,
        null=True,
        verbose_name="4.03 CRM B2C implementado",
    )

    # 4.04
    gestao_leads = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="4.04 Gestão de Leads pelo CRM"
    )
    gestao_leads_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 4.04"
    )
    gestao_leads_file = models.FileField(
        upload_to=upload_to_tecnologia,
        blank=True,
        null=True,
        verbose_name="4.04 Gestão de Leads pelo CRM",
    )

    # 4.05
    tarefas_leads = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="4.05 Organização e atualização de tarefas no CRM"
    )
    tarefas_leads_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 4.05"
    )
    tarefas_leads_file = models.FileField(
        upload_to=upload_to_tecnologia,
        blank=True,
        null=True,
        verbose_name="4.05 Organização e atualização de tarefas no CRM",
    )

    # 4.06
    visitas_familias = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="4.06 Organização e atualização de visitas no CRM"
    )
    visitas_familias_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 4.06"
    )
    visitas_familias_file = models.FileField(
        upload_to=upload_to_tecnologia,
        blank=True,
        null=True,
        verbose_name="4.06 Organização e atualização de visitas no CRM",
    )

    # 4.07
    oportunidades_matriculas = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="4.07 Geração e atualização de oportunidades no CRM"
    )
    oportunidades_matriculas_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 4.07"
    )
    oportunidades_matriculas_file = models.FileField(
        upload_to=upload_to_tecnologia,
        blank=True,
        null=True,
        verbose_name="4.07 Geração e atualização de oportunidades no CRM",
    )

    # 4.08
    pedidos_matriculas = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="4.08 Emissão de pedidos de matrículas pelo CRM"
    )
    pedidos_matriculas_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 4.08"
    )
    pedidos_matriculas_file = models.FileField(
        upload_to=upload_to_tecnologia,
        blank=True,
        null=True,
        verbose_name="4.08 Emissão de pedidos de matrículas pelo CRM",
    )

    # 4.09
    eventos_leads = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="4.09 Conversão de leads através de eventos no CRM"
    )
    eventos_leads_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 4.09"
    )
    eventos_leads_file = models.FileField(
        upload_to=upload_to_tecnologia,
        blank=True,
        null=True,
        verbose_name="4.09 Conversão de leads através de eventos no CRM",
    )

    # 4.10
    toddle_habilitado = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="4.10 Toddle habilitado para todas as turmas"
    )
    toddle_habilitado_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 4.10"
    )
    toddle_habilitado_file = models.FileField(
        upload_to=upload_to_tecnologia,
        blank=True,
        null=True,
        verbose_name="4.10 Toddle habilitado para todas as turmas",
    )

    # 4.11
    uso_sponte = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="4.11 Uso do sistema homologado Sponte"
    )
    uso_sponte_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 4.11"
    )
    uso_sponte_file = models.FileField(
        upload_to=upload_to_tecnologia,
        blank=True,
        null=True,
        verbose_name="4.11 Uso do sistema homologado Sponte",
    )

    def __str__(self):
        return f"{self.escola} - Tecnologia"


def upload_to_marketing(instance, filename):
    return f"glex/{instance.escola.id_escola}/marketing/{filename}"

class GlexMarketing(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="marketing",
        verbose_name="Nome da Escola",
    )

    # 5.01
    campanhas_marketing = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="5.01 Execução de campanhas de marketing"
    )
    campanhas_marketing_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 5.01"
    )
    campanhas_marketing_file = models.FileField(
        upload_to=upload_to_marketing,
        blank=True,
        null=True,
        verbose_name="5.01 Execução de campanhas de marketing",
    )

    # 5.02
    planejamento_eventos = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="5.02 Planejamento de eventos"
    )
    planejamento_eventos_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 5.02"
    )
    planejamento_eventos_file = models.FileField(
        upload_to=upload_to_marketing,
        blank=True,
        null=True,
        verbose_name="5.02 Planejamento de eventos",
    )

    # 5.03
    comite_gestao_crise = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="5.03 Comitê de Gestão de Crise"
    )
    comite_gestao_crise_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 5.03"
    )
    comite_gestao_crise_file = models.FileField(
        upload_to=upload_to_marketing,
        blank=True,
        null=True,
        verbose_name="5.03 Comitê de Gestão de Crise",
    )

    # 5.04
    newsletter_semanal = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="5.04 Disponibilização semanal de Newsletter"
    )
    newsletter_semanal_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 5.04"
    )
    newsletter_semanal_file = models.FileField(
        upload_to=upload_to_marketing,
        blank=True,
        null=True,
        verbose_name="5.04 Disponibilização semanal de Newsletter",
    )

    # 5.05
    ambientacao_datas_especiais = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="5.05 Ambientação e ações para datas especiais"
    )
    ambientacao_datas_especiais_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 5.05"
    )
    ambientacao_datas_especiais_file = models.FileField(
        upload_to=upload_to_marketing,
        blank=True,
        null=True,
        verbose_name="5.05 Ambientação e ações para datas especiais",
    )

    # 5.06
    google_meu_negocio = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="5.06 Google Meu Negócio atualizado"
    )
    google_meu_negocio_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 5.06"
    )
    google_meu_negocio_file = models.FileField(
        upload_to=upload_to_marketing,
        blank=True,
        null=True,
        verbose_name="5.06 Google Meu Negócio atualizado",
    )

    # 5.07
    uso_site_oficial = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="5.07 Uso do site oficial da Maple Bear"
    )
    uso_site_oficial_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 5.07"
    )
    uso_site_oficial_file = models.FileField(
        upload_to=upload_to_marketing,
        blank=True,
        null=True,
        verbose_name="5.07 Uso do site oficial da Maple Bear",
    )

    # 5.08
    redes_sociais = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="5.08 Atualização e engajamento nas redes sociais"
    )
    redes_sociais_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 5.08"
    )
    redes_sociais_file = models.FileField(
        upload_to=upload_to_marketing,
        blank=True,
        null=True,
        verbose_name="5.08 Atualização e engajamento nas redes sociais",
    )

    # 5.09
    participacao_congressos = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="5.09 Participação em congressos e convenções"
    )
    participacao_congressos_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 5.09"
    )
    participacao_congressos_file = models.FileField(
        upload_to=upload_to_marketing,
        blank=True,
        null=True,
        verbose_name="5.09 Participação em congressos e convenções",
    )

    # 5.10
    uso_testemunhos = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="5.10 Uso de testemunhos e evidências acadêmicas"
    )
    uso_testemunhos_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 5.10"
    )
    uso_testemunhos_file = models.FileField(
        upload_to=upload_to_marketing,
        blank=True,
        null=True,
        verbose_name="5.10 Uso de testemunhos e evidências acadêmicas",
    )

    # 5.11
    registros_crm = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="5.11 Uso do CRM para registros"
    )
    registros_crm_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 5.11"
    )
    registros_crm_file = models.FileField(
        upload_to=upload_to_marketing,
        blank=True,
        null=True,
        verbose_name="5.11 Uso do CRM para registros",
    )

    def __str__(self):
        return f"{self.escola} - Marketing"


def upload_to_academico(instance, filename):
    return f"glex/{instance.escola.id_escola}/academico/{filename}"

class GlexAcademico(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="academico",
        verbose_name="Nome da Escola",
    )

    # 6.01
    uso_curriculo_atual = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="6.01 Uso do currículo atual da Maple Bear"
    )
    uso_curriculo_atual_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 6.01"
    )
    uso_curriculo_atual_file = models.FileField(
        upload_to=upload_to_academico,
        blank=True,
        null=True,
        verbose_name="6.01 Uso do currículo atual da Maple Bear",
    )

    # 6.02
    resultado_qa = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="6.02 Resultado de Q/A acima de 70%"
    )
    resultado_qa_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 6.02"
    )
    resultado_qa_file = models.FileField(
        upload_to=upload_to_academico,
        blank=True,
        null=True,
        verbose_name="6.02 Resultado de Q/A acima de 70%",
    )

    # 6.03
    participacao_treinamento = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="6.03 Participação no treinamento do Programa Maple Bear"
    )
    participacao_treinamento_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 6.03"
    )
    participacao_treinamento_file = models.FileField(
        upload_to=upload_to_academico,
        blank=True,
        null=True,
        verbose_name="6.03 Participação no treinamento do Programa Maple Bear",
    )

    # 6.04
    guia_teacher_toddle = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="6.04 Possui guia da Unidade ou Teacher Guide (Toddle)"
    )
    guia_teacher_toddle_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 6.04"
    )
    guia_teacher_toddle_file = models.FileField(
        upload_to=upload_to_academico,
        blank=True,
        null=True,
        verbose_name="6.04 Possui guia da Unidade ou Teacher Guide (Toddle)",
    )

    # 6.05
    recursos_alunos_professores = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="6.05 Recursos para Alunos e Professores utilizados"
    )
    recursos_alunos_professores_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 6.05"
    )
    recursos_alunos_professores_file = models.FileField(
        upload_to=upload_to_academico,
        blank=True,
        null=True,
        verbose_name="6.05 Recursos para Alunos e Professores utilizados",
    )

    def __str__(self):
        return f"{self.escola} - Acadêmico"


def upload_to_gestao_escolar(instance, filename):
    return f"glex/{instance.escola.id_escola}/gestao_escolar/{filename}"

class GlexGestaoEscolar(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="gestao_escolar",
        verbose_name="Nome da Escola",
    )

    # 7.01
    plano_emergencia = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.01 Plano de Preparação para Emergências"
    )
    plano_emergencia_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.01"
    )
    plano_emergencia_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.01 Plano de Preparação para Emergências",
    )

    # 7.02
    info_medicas_atualizadas = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.02 Informações médicas atualizadas"
    )
    info_medicas_atualizadas_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.02"
    )
    info_medicas_atualizadas_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.02 Informações médicas atualizadas",
    )

    # 7.03
    contato_atualizado = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.03 Lista de contatos atualizada e disponível"
    )
    contato_atualizado_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.03"
    )
    contato_atualizado_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.03 Lista de contatos atualizada e disponível",
    )

    # 7.04
    seguranca_contra_incendio = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.04 Equipamentos de segurança contra incêndio"
    )
    seguranca_contra_incendio_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.04"
    )
    seguranca_contra_incendio_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.04 Equipamentos de segurança contra incêndio",
    )

    # 7.05
    saidas_emergencia = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.05 Saídas de emergência marcadas e desobstruídas"
    )
    saidas_emergencia_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.05"
    )
    saidas_emergencia_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.05 Saídas de emergência marcadas e desobstruídas",
    )

    # 7.06
    kits_primeiros_socorros = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.06 Kits de primeiros socorros disponíveis"
    )
    kits_primeiros_socorros_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.06"
    )
    kits_primeiros_socorros_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.06 Kits de primeiros socorros disponíveis",
    )

    # 7.07
    funcionarios_treinados_primeiros_socorros = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.07 Funcionários treinados em primeiros socorros e RCP"
    )
    funcionarios_treinados_primeiros_socorros_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.07"
    )
    funcionarios_treinados_primeiros_socorros_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.07 Funcionários treinados em primeiros socorros e RCP",
    )

    # 7.08
    simulacoes_emergencia = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.08 Simulações de emergência realizadas"
    )
    simulacoes_emergencia_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.08"
    )
    simulacoes_emergencia_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.08 Simulações de emergência realizadas",
    )

    # 7.09
    recursos_maple_bear = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.09 Recursos Maple Bear em condições adequadas"
    )
    recursos_maple_bear_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.09"
    )
    recursos_maple_bear_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.09 Recursos Maple Bear em condições adequadas",
    )

    # 7.10
    garantia_qualidade = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.10 Envolvimento em Garantia de Qualidade"
    )
    garantia_qualidade_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.10"
    )
    garantia_qualidade_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.10 Envolvimento em Garantia de Qualidade",
    )

    # 7.11
    treinamento_academico = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.11 Envolvimento em treinamento acadêmico"
    )
    treinamento_academico_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.11"
    )
    treinamento_academico_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.11 Envolvimento em treinamento acadêmico",
    )

    # 7.12
    reunioes_lideranca = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.12 Cumprimento do calendário de reuniões de Liderança"
    )
    reunioes_lideranca_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.12"
    )
    reunioes_lideranca_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.12 Cumprimento do calendário de reuniões de Liderança",
    )

    # 7.13
    processo_padronizado_atendimento = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.13 Processo padronizado de atendimento"
    )
    processo_padronizado_atendimento_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.13"
    )
    processo_padronizado_atendimento_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.13 Processo padronizado de atendimento",
    )
    # 7.14
    controle_frequencia_alunos = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.14 Controle diário de frequência dos Alunos"
    )
    controle_frequencia_alunos_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.14"
    )
    controle_frequencia_alunos_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.14 Controle diário de frequência dos Alunos",
    )

    # 7.15
    controle_media_alunos = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.15 Controle e monitoramento da média de Alunos por turma"
    )
    controle_media_alunos_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.15"
    )
    controle_media_alunos_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.15 Controle e monitoramento da média de Alunos por turma",
    )

    # 7.16
    atividades_extracurriculares = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.16 Atividades extracurriculares disponíveis"
    )
    atividades_extracurriculares_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.16"
    )
    atividades_extracurriculares_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.16 Atividades extracurriculares disponíveis",
    )

    # 7.17
    analise_pontos_fortes = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.17 Análise de pontos fortes, fracos, oportunidades e ameaças"
    )
    analise_pontos_fortes_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.17"
    )
    analise_pontos_fortes_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True, null=True,
        verbose_name="7.17 Análise de pontos fortes, fracos, oportunidades e ameaças",
    )

    # 7.18
    planos_acao_defasagens = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.18 Planos de ação para sanar defasagens"
    )
    planos_acao_defasagens_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.18"
    )
    planos_acao_defasagens_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True, null=True,
        verbose_name="7.18 Planos de ação para sanar defasagens",
    )

    # 7.19
    experiencia_professores = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.19 Professores com experiência mínima de 1 ano"
    )
    experiencia_professores_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.19"
    )
    experiencia_professores_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True, null=True,
        verbose_name="7.19 Professores com experiência mínima de 1 ano",
    )

    # 7.20
    professores_por_turma = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.20 Todas as turmas possuem Professores"
    )
    professores_por_turma_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.20"
    )
    professores_por_turma_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True, null=True,
        verbose_name="7.20 Todas as turmas possuem Professores",
    )

    # 7.21
    observacao_aulas = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.21 Liderança observa aulas ministradas pela Equipe Pedagógica"
    )
    observacao_aulas_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.21"
    )
    observacao_aulas_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True, null=True,
        verbose_name="7.21 Liderança observa aulas ministradas pela Equipe Pedagógica",
    )

    # 7.22
    lideranca_graduada = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.22 Liderança graduada em pedagogia e gestão escolar"
    )
    lideranca_graduada_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.22"
    )
    lideranca_graduada_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True, null=True,
        verbose_name="7.22 Liderança graduada em pedagogia e gestão escolar",
    )

    # 7.23
    coordenacao_por_segmento = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.23 Coordenação para cada segmento"
    )
    coordenacao_por_segmento_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.23"
    )
    coordenacao_por_segmento_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True, null=True,
        verbose_name="7.23 Coordenação para cada segmento",
    )

    # 7.24
    cumprimento_legislacao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.24 Cumprimento da legislação local"
    )
    cumprimento_legislacao_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.24"
    )
    cumprimento_legislacao_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True, null=True,
        verbose_name="7.24 Cumprimento da legislação local",
    )

    # 7.25
    guia_familia = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.25 Possui Parents Handbook (Guia da Família)"
    )
    guia_familia_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.25"
    )
    guia_familia_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True, null=True,
        verbose_name="7.25 Possui Parents Handbook (Guia da Família)",
    )

    # 7.26
    comunicacao_interna = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.26 Possui esquema de comunicação interna"
    )
    comunicacao_interna_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.26"
    )
    comunicacao_interna_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True, null=True,
        verbose_name="7.26 Possui esquema de comunicação interna",
    )

    # 7.27
    toddle_comunicacao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.27 Utiliza a Toddle como recurso padrão de comunicação"
    )
    toddle_comunicacao_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.27"
    )
    toddle_comunicacao_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True, null=True,
        verbose_name="7.27 Utiliza a Toddle como recurso padrão de comunicação",
    )

    # 7.28
    nps_acima_70 = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.28 NPS acima de 70 pontos"
    )
    nps_acima_70_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.28"
    )
    nps_acima_70_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True, null=True,
        verbose_name="7.28 NPS acima de 70 pontos",
    )

    # 7.29
    orientador_pedagogico = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.29 Possui Orientador Pedagógico (a partir do Middle Year)"
    )
    orientador_pedagogico_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.29"
    )
    orientador_pedagogico_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True, null=True,
        verbose_name="7.29 Possui Orientador Pedagógico (a partir do Middle Year)",
    )

    # 7.30
    certificado_lei_lucas = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.30 Certificado da Lei de Primeiro Socorros (Lei Lucas)"
    )
    certificado_lei_lucas_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 7.30"
    )
    certificado_lei_lucas_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True, null=True,
        verbose_name="7.30 Certificado da Lei de Primeiro Socorros (Lei Lucas)",
    )

    def __str__(self):
        return f"{self.escola} - Gestão Escolar"


def upload_to_operacao_academica(instance, filename):
    return f"glex/{instance.escola.id_escola}/operacao_academica/{filename}"

class GlexOperacaoAcademica(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="operacao_academica",
        verbose_name="Nome da Escola",
    )

    # 8.01
    treinamentos_pedagogicos = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="8.01 Participação em treinamentos pedagógicos"
    )
    treinamentos_pedagogicos_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 8.01"
    )
    treinamentos_pedagogicos_file = models.FileField(
        upload_to=upload_to_operacao_academica,
        blank=True,
        null=True,
        verbose_name="8.01 Participação em treinamentos pedagógicos",
    )

    # 8.02
    professores_nivel_superior = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="8.02 Professores com nível superior em humanas"
    )
    professores_nivel_superior_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 8.02"
    )
    professores_nivel_superior_file = models.FileField(
        upload_to=upload_to_operacao_academica,
        blank=True, null=True,
        verbose_name="8.02 Professores com nível superior em humanas",
    )

    # 8.03
    professores_certificacao_internacional = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="8.03 Professores com certificação internacional"
    )
    professores_certificacao_internacional_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 8.03"
    )
    professores_certificacao_internacional_file = models.FileField(
        upload_to=upload_to_operacao_academica,
        blank=True,
        null=True,
        verbose_name="8.03 Professores com certificação internacional",
    )

    # 8.04
    preparo_aulas_previo = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="8.04 Preparo prévio das aulas pelo Professor"
    )
    preparo_aulas_previo_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 8.04"
    )
    preparo_aulas_previo_file = models.FileField(
        upload_to=upload_to_operacao_academica,
        blank=True, null=True,
        verbose_name="8.04 Preparo prévio das aulas pelo Professor",
    )

    # 8.05
    metodologia_maple_bear = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="8.05 Aspectos da metodologia Maple Bear no plano de aula"
    )
    metodologia_maple_bear_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 8.05"
    )
    metodologia_maple_bear_file = models.FileField(
        upload_to=upload_to_operacao_academica,
        blank=True, null=True,
        verbose_name="8.05 Aspectos da metodologia Maple Bear no plano de aula",
    )

    def __str__(self):
        return f"{self.escola} - Operação Acadêmica"


def upload_to_implantacao(instance, filename):
    return f"glex/{instance.escola.id_escola}/implantacao/{filename}"

class GlexImplantacao(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="implantacao",
        verbose_name="Nome da Escola",
    )

    # 9.01
    interior_logotipo_maple_bear = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.01 Interior do prédio com logotipo Maple Bear"
    )
    interior_logotipo_maple_bear_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.01"
    )
    interior_logotipo_maple_bear_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.01 Interior do prédio com logotipo Maple Bear",
    )

    # 9.02
    exterior_logotipo_maple_bear = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.02 Exterior do prédio com logotipo Maple Bear"
    )
    exterior_logotipo_maple_bear_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.02"
    )
    exterior_logotipo_maple_bear_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.02 Exterior do prédio com logotipo Maple Bear",
    )

    # 9.03
    logotipo_estado_conservacao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.03 Logotipo em bom estado de conservação"
    )
    logotipo_estado_conservacao_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.03"
    )
    logotipo_estado_conservacao_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.03 Logotipo em bom estado de conservação",
    )

    # 9.04
    sistema_monitoramento_seguranca = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.04 Sistema de monitoramento de segurança funcional"
    )
    sistema_monitoramento_seguranca_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.04"
    )
    sistema_monitoramento_seguranca_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.04 Sistema de monitoramento de segurança funcional",
    )

    # 9.05
    controle_acesso_predio = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.05 Processo de controle de acesso ao prédio"
    )
    controle_acesso_predio_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.05"
    )
    controle_acesso_predio_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.05 Processo de controle de acesso ao prédio",
    )

    # 9.06
    sistema_alarme_emergencia = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.06 Sistema de alarme de emergência instalado"
    )
    sistema_alarme_emergencia_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.06"
    )
    sistema_alarme_emergencia_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.06 Sistema de alarme de emergência instalado",
    )

    # 9.07
    area_recreacao_conformidade = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.07 Área de recreação em conformidade"
    )
    area_recreacao_conformidade_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.07"
    )
    area_recreacao_conformidade_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.07 Área de recreação em conformidade",
    )

    # 9.08
    equipamento_recreacao_conservacao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.08 Equipamento de recreação em bom estado"
    )
    equipamento_recreacao_conservacao_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.08"
    )
    equipamento_recreacao_conservacao_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.08 Equipamento de recreação em bom estado",
    )

    # 9.09
    instalacoes_limpeza_organizacao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.09 Instalações limpas e organizadas"
    )
    instalacoes_limpeza_organizacao_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.09"
    )
    instalacoes_limpeza_organizacao_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.09 Instalações limpas e organizadas",
    )
    # 9.10
    seguranca_estrutural = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.10 Guardas e sinalizações adequadas para segurança"
    )
    seguranca_estrutural_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.10"
    )
    seguranca_estrutural_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.10 Guardas e sinalizações adequadas para segurança",
    )

    # 9.11
    sinalizacao_predio = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.11 Sinalização clara para entradas e saídas"
    )
    sinalizacao_predio_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.11"
    )
    sinalizacao_predio_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.11 Sinalização clara para entradas e saídas",
    )

    # 9.12
    proporcao_adultos_alunos = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.12 Proporção adulto-aluno aprovada pela Maple Bear"
    )
    proporcao_adultos_alunos_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.12"
    )
    proporcao_adultos_alunos_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.12 Proporção adulto-aluno aprovada pela Maple Bear",
    )

    # 9.13
    mobilia_salas_conservacao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.13 Mobília das salas em bom estado de conservação"
    )
    mobilia_salas_conservacao_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.13"
    )
    mobilia_salas_conservacao_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.13 Mobília das salas em bom estado de conservação",
    )

    # 9.14
    organizacao_corredores = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.14 Corredores organizados e acessíveis"
    )
    organizacao_corredores_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.14"
    )
    organizacao_corredores_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.14 Corredores organizados e acessíveis",
    )

    # 9.15
    acessibilidade_pne = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.15 Instalações acessíveis para pessoas com necessidades especiais"
    )
    acessibilidade_pne_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.15"
    )
    acessibilidade_pne_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.15 Instalações acessíveis para pessoas com necessidades especiais",
    )

    # 9.16
    politica_embarque_desembarque = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.16 Política de embarque e desembarque seguida"
    )
    politica_embarque_desembarque_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.16"
    )
    politica_embarque_desembarque_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.16 Política de embarque e desembarque seguida",
    )

    # 9.17
    banheiros_conservacao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.17 Banheiros separados e em bom estado de conservação"
    )
    banheiros_conservacao_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.17"
    )
    banheiros_conservacao_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.17 Banheiros separados e em bom estado de conservação",
    )

    # 9.18
    conservacao_geral_instalacoes = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.18 Instalações em bom estado de conservação geral"
    )
    conservacao_geral_instalacoes_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.18"
    )
    conservacao_geral_instalacoes_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.18 Instalações em bom estado de conservação geral",
    )

    # 9.19
    danos_esteticos_instalacoes = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.19 Ausência de danos estéticos nas instalações"
    )
    danos_esteticos_instalacoes_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.19"
    )
    danos_esteticos_instalacoes_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.19 Ausência de danos estéticos nas instalações",
    )

    # 9.20
    danos_estruturais_eventuais = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.20 Ausência de danos estruturais eventuais"
    )
    danos_estruturais_eventuais_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.20"
    )
    danos_estruturais_eventuais_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.20 Ausência de danos estruturais eventuais",
    )

    # 9.21
    danos_estruturais_risco = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.21 Ausência de danos estruturais com risco iminente"
    )
    danos_estruturais_risco_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.21"
    )
    danos_estruturais_risco_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.21 Ausência de danos estruturais com risco iminente",
    )
    # 9.22
    pia_salas_infantil = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.22 Todas as salas de aula do infantil possuem pia"
    )
    pia_salas_infantil_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.22"
    )
    pia_salas_infantil_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.22 Todas as salas de aula do infantil possuem pia",
    )

    # 9.23
    banheiro_trocador_bear_care = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.23 Salas de Bear Care/Toddler possuem banheiro com trocador"
    )
    banheiro_trocador_bear_care_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.23"
    )
    banheiro_trocador_bear_care_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.23 Salas de Bear Care/Toddler possuem banheiro com trocador",
    )

    # 9.24
    banheiro_chuveiro_infantil = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.24 Salas de Nursery, JK, SK possuem banheiro com chuveiro"
    )
    banheiro_chuveiro_infantil_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.24"
    )
    banheiro_chuveiro_infantil_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.24 Salas de Nursery, JK, SK possuem banheiro com chuveiro",
    )

    # 9.25
    playground_externo = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.25 Playground externo em bom estado de conservação"
    )
    playground_externo_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.25"
    )
    playground_externo_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.25 Playground externo em bom estado de conservação",
    )

    # 9.26
    rampas_corrimaos = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.26 Possui rampas e escadas com corrimãos duplos"
    )
    rampas_corrimaos_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.26"
    )
    rampas_corrimaos_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.26 Possui rampas e escadas com corrimãos duplos",
    )

    # 9.27
    sala_comercial_padroes = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.27 Sala de atendimento comercial segue padrões"
    )
    sala_comercial_padroes_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.27"
    )
    sala_comercial_padroes_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.27 Sala de atendimento comercial segue padrões",
    )

    # 9.28
    refeitório_conservacao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.28 Refeitório atende 1/3 da capacidade e está em bom estado"
    )
    refeitório_conservacao_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.28"
    )
    refeitório_conservacao_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.28 Refeitório atende 1/3 da capacidade e está em bom estado",
    )

    # 9.29
    cozinha_vigilancia_sanitaria = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.29 Cozinha em conformidade com normas de vigilância sanitária"
    )
    cozinha_vigilancia_sanitaria_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.29"
    )
    cozinha_vigilancia_sanitaria_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.29 Cozinha em conformidade com normas de vigilância sanitária",
    )

    # 9.30
    playground_interno = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.30 Playground interno em bom estado de conservação"
    )
    playground_interno_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.30"
    )
    playground_interno_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.30 Playground interno em bom estado de conservação",
    )

    # 9.31
    espaco_esportes = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.31 Espaço para prática de esportes em bom estado"
    )
    espaco_esportes_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.31"
    )
    espaco_esportes_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.31 Espaço para prática de esportes em bom estado",
    )

    # 9.32
    quadra_poliesportiva = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.32 Quadra poliesportiva em bom estado"
    )
    quadra_poliesportiva_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.32"
    )
    quadra_poliesportiva_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.32 Quadra poliesportiva em bom estado",
    )

    # 9.33
    biblioteca_conservacao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.33 Biblioteca em bom estado de conservação"
    )
    biblioteca_conservacao_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.33"
    )
    biblioteca_conservacao_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.33 Biblioteca em bom estado de conservação",
    )

    # 9.34
    banheiros_pne_legislacao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.34 Banheiros PNE de acordo com legislação local"
    )
    banheiros_pne_legislacao_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.34"
    )
    banheiros_pne_legislacao_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.34 Banheiros PNE de acordo com legislação local",
    )

    # 9.35
    laboratorio_ciencias = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.35 Laboratório de ciências em bom estado (Middle Years)"
    )
    laboratorio_ciencias_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.35"
    )
    laboratorio_ciencias_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.35 Laboratório de ciências em bom estado (Middle Years)",
    )
    # 9.36
    mobiliario_fornecedores_homologados = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.36 Mobiliário adquirido com fornecedores homologados"
    )
    mobiliario_fornecedores_homologados_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.36"
    )
    mobiliario_fornecedores_homologados_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.36 Mobiliário adquirido com fornecedores homologados",
    )

    # 9.37
    mobiliario_salas_admin_professores = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.37 Mobiliário das salas administrativas e de professores em bom estado"
    )
    mobiliario_salas_admin_professores_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.37"
    )
    mobiliario_salas_admin_professores_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.37 Mobiliário das salas administrativas e de professores em bom estado",
    )

    # 9.38
    sala_coordenacao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.38 Sala de Coordenação em bom estado de conservação"
    )
    sala_coordenacao_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.38"
    )
    sala_coordenacao_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.38 Sala de Coordenação em bom estado de conservação",
    )

    # 9.39
    sala_professores = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.39 Sala de Professores em bom estado de conservação"
    )
    sala_professores_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.39"
    )
    sala_professores_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.39 Sala de Professores em bom estado de conservação",
    )

    # 9.40
    vagas_estacionamento = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.40 Vagas de estacionamento conforme legislação"
    )
    vagas_estacionamento_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.40"
    )
    vagas_estacionamento_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.40 Vagas de estacionamento conforme legislação",
    )

    # 9.41
    iluminacao_ventilacao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.41 Atendimento ao padrão de iluminação e ventilação"
    )
    iluminacao_ventilacao_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.41"
    )
    iluminacao_ventilacao_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.41 Atendimento ao padrão de iluminação e ventilação",
    )

    # 9.42
    paredes_balcao_logos = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.42 Paredes, balcão e logos da recepção no padrão da Franqueadora"
    )
    paredes_balcao_logos_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.42"
    )
    paredes_balcao_logos_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.42 Paredes, balcão e logos da recepção no padrão da Franqueadora",
    )

    # 9.43
    salas_55m2 = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.43 Salas de aula com no mínimo 55m², incluindo banheiro"
    )
    salas_55m2_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.43"
    )
    salas_55m2_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.43 Salas de aula com no mínimo 55m², incluindo banheiro",
    )

    # 9.44
    copa_colaboradores = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.44 Copa para os Colaboradores em bom estado de conservação"
    )
    copa_colaboradores_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 9.44"
    )
    copa_colaboradores_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True, null=True,
        verbose_name="9.44 Copa para os Colaboradores em bom estado de conservação",
    )

    def __str__(self):
        return f"{self.escola} - Implantação"


def upload_to_comercial(instance, filename):
    return f"glex/{instance.escola.id_escola}/comercial/{filename}"

class GlexComercial(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="comercial",
        verbose_name="Nome da Escola",
    )

    # 10.01
    processo_matricula_robusto = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.01 Processo de matrícula robusto"
    )
    processo_matricula_robusto_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.01"
    )
    processo_matricula_robusto_file = models.FileField(
        upload_to=upload_to_comercial,
        blank=True,
        null=True,
        verbose_name="10.01 Processo de matrícula robusto",
    )

    # 10.02
    plano_marketing_matricula = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.02 Plano de marketing de matrícula ativo"
    )
    plano_marketing_matricula_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.02"
    )
    plano_marketing_matricula_file = models.FileField(
        upload_to=upload_to_comercial,
        blank=True, null=True,
        verbose_name="10.02 Plano de marketing de matrícula ativo",
    )

    # 10.03
    materiais_marketing_padroes = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.03 Materiais de marketing alinhados aos padrões da Maple Bear"
    )
    materiais_marketing_padroes_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.03"
    )
    materiais_marketing_padroes_file = models.FileField(
        upload_to=upload_to_comercial,
        blank=True, null=True,
        verbose_name="10.03 Materiais de marketing alinhados aos padrões da Maple Bear",
    )

    # 10.04
    equipe_lideranca_comercial = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.04 Possui liderança e equipe comercial"
    )
    equipe_lideranca_comercial_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.04"
    )
    equipe_lideranca_comercial_file = models.FileField(
        upload_to=upload_to_comercial,
        blank=True, null=True,
        verbose_name="10.04 Possui liderança e equipe comercial",
    )

    # 10.05
    reunioes_lideranca_comercial = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.05 Reuniões semanais da liderança com a equipe comercial"
    )
    reunioes_lideranca_comercial_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.05"
    )
    reunioes_lideranca_comercial_file = models.FileField(
        upload_to=upload_to_comercial,
        blank=True, null=True,
        verbose_name="10.05 Reuniões semanais da liderança com a equipe comercial",
    )

    # 10.06
    recepcao_visitantes = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.06 Recepção cortês e afável a visitantes, pais e colaboradores"
    )
    recepcao_visitantes_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.06"
    )
    recepcao_visitantes_file = models.FileField(
        upload_to=upload_to_comercial,
        blank=True, null=True,
        verbose_name="10.06 Recepção cortês e afável a visitantes, pais e colaboradores",
    )

    # 10.07
    metas_matriculas_rematriculas = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.07 Desdobramento das metas de matrículas e rematrículas"
    )
    metas_matriculas_rematriculas_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.07"
    )
    metas_matriculas_rematriculas_file = models.FileField(
        upload_to=upload_to_comercial,
        blank=True, null=True,
        verbose_name="10.07 Desdobramento das metas de matrículas e rematriculas",
    )

    # 10.08
    metas_nps = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.08 Desdobramento da meta da pesquisa NPS"
    )
    metas_nps_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.08"
    )
    metas_nps_file = models.FileField(
        upload_to=upload_to_comercial,
        blank=True, null=True,
        verbose_name="10.08 Desdobramento da meta da pesquisa NPS",
    )

    # 10.09
    mentoria_vendas = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.09 Participação da equipe comercial em mentoria de vendas"
    )
    mentoria_vendas_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.09"
    )
    mentoria_vendas_file = models.FileField(
        upload_to=upload_to_comercial,
        blank=True, null=True,
        verbose_name="10.09 Participação da equipe comercial em mentoria de vendas",
    )

    # 10.10
    trilha_treinamento_vendas = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.10 Conclusão da trilha de treinamento de vendas"
    )
    trilha_treinamento_vendas_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.10"
    )
    trilha_treinamento_vendas_file = models.FileField(
        upload_to=upload_to_comercial,
        blank=True, null=True,
        verbose_name="10.10 Conclusão da trilha de treinamento de vendas",
    )

    # 10.11
    funil_vendas_crm = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.11 Etapas do funil de vendas registradas no CRM"
    )
    funil_vendas_crm_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.11"
    )
    funil_vendas_crm_file = models.FileField(
        upload_to=upload_to_comercial,
        blank=True, null=True,
        verbose_name="10.11 Etapas do funil de vendas registradas no CRM",
    )

    # 10.12
    cliente_oculto = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.12 Pontuação acima de 70% no cliente oculto"
    )
    cliente_oculto_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.12"
    )
    cliente_oculto_file = models.FileField(
        upload_to=upload_to_comercial,
        blank=True, null=True,
        verbose_name="10.12 Pontuação acima de 70% no cliente oculto",
    )

    # 10.13
    participacao_campanhas_acoes = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.13 Participação em 70% das campanhas comerciais promovidas"
    )
    participacao_campanhas_acoes_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.13"
    )
    participacao_campanhas_acoes_file = models.FileField(
        upload_to=upload_to_comercial,
        blank=True, null=True,
        verbose_name="10.13 Participação em 70% das campanhas comerciais promovidas",
    )

    # 10.14
    pesquisas_mercado = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.14 Realiza pesquisas de mercado e conhece concorrentes"
    )
    pesquisas_mercado_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.14"
    )
    pesquisas_mercado_file = models.FileField(
        upload_to=upload_to_comercial,
        blank=True, null=True,
        verbose_name="10.14 Realiza pesquisas de mercado e conhece concorrentes",
    )

    # 10.15
    conversao_leads_marketing = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.15 Converteu 5% dos leads gerados no marketing online"
    )
    conversao_leads_marketing_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.15"
    )
    conversao_leads_marketing_file = models.FileField(
        upload_to=upload_to_comercial,
        blank=True, null=True,
        verbose_name="10.15 Converteu 5% dos leads gerados no marketing online",
    )

    # 10.16
    capacitacao_exposicao_metodologia = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.16 Capacitou equipes para exposição correta da metodologia"
    )
    capacitacao_exposicao_metodologia_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.16"
    )
    capacitacao_exposicao_metodologia_file = models.FileField(
        upload_to=upload_to_comercial,
        blank=True, null=True,
        verbose_name="10.16 Capacitou equipes para exposição correta da metodologia",
    )

    # 10.17
    politica_comissionamento = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.17 Adota política de comissionamento/bônus para área Comercial"
    )
    politica_comissionamento_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.17"
    )
    politica_comissionamento_file = models.FileField(
        upload_to=upload_to_comercial,
        blank=True, null=True,
        verbose_name="10.17 Adota política de comissionamento/bônus para área Comercial",
    )

    # 10.18
    calendario_trade_marketing = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.18 Possui calendário de Trade Marketing definido"
    )
    calendario_trade_marketing_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.18"
    )
    calendario_trade_marketing_file = models.FileField(
        upload_to=upload_to_comercial,
        blank=True, null=True,
        verbose_name="10.18 Possui calendário de Trade Marketing definido",
    )

    # 10.19
    equipe_marketing = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.19 Possui equipe de Marketing ou agência responsável"
    )
    equipe_marketing_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.19"
    )
    equipe_marketing_file = models.FileField(
        upload_to=upload_to_comercial,
        blank=True, null=True,
        verbose_name="10.19 Possui equipe de Marketing ou agência responsável",
    )

    # 10.20
    entrega_kits_rematricula = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.20 Entrega às famílias kits de rematrícula homologados"
    )
    entrega_kits_rematricula_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.20"
    )
    entrega_kits_rematricula_file = models.FileField(
        upload_to=upload_to_comercial,
        blank=True, null=True,
        verbose_name="10.20 Entrega às famílias kits de rematrícula homologados",
    )

    # 10.21
    entrega_kits_visita = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.21 Entrega às famílias visitantes kits de visita homologados"
    )
    entrega_kits_visita_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.21"
    )
    entrega_kits_visita_file = models.FileField(
        upload_to=upload_to_comercial,
        blank=True, null=True,
        verbose_name="10.21 Entrega às famílias visitantes kits de visita homologados",
    )

    # 10.22
    leads_atraso_crm = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.22 Menos de 10% dos leads em atraso no CRM"
    )
    leads_atraso_crm_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.22"
    )
    leads_atraso_crm_file = models.FileField(
        upload_to=upload_to_comercial,
        blank=True, null=True,
        verbose_name="10.22 Menos de 10% dos leads em atraso no CRM",
    )

    def __str__(self):
        return f"{self.escola} - Comercial"

def upload_to_resultado(instance, filename):
    return f"glex/{instance.escola.id_escola}/resultado/{filename}"

class GlexResultado(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="resultado",
        verbose_name="Nome da Escola",
    )

    # 11.01
    taxa_retenção_rotatividade = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="11.01 Mede taxa de retenção e rotatividade dos alunos"
    )
    taxa_retenção_rotatividade_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 11.01"
    )
    taxa_retenção_rotatividade_file = models.FileField(
        upload_to=upload_to_resultado,
        blank=True,
        null=True,
        verbose_name="11.01 Mede taxa de retenção e rotatividade dos alunos",
    )

    # 11.02
    meta_rematricula_carta = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="11.02 Atingiu meta de rematrícula definida em carta meta"
    )
    meta_rematricula_carta_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 11.02"
    )
    meta_rematricula_carta_file = models.FileField(
        upload_to=upload_to_resultado,
        blank=True, null=True,
        verbose_name="11.02 Atingiu meta de rematrícula definida em carta meta",
    )

    # 11.03
    meta_matricula_carta = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="11.03 Atingiu meta de matrícula definida em carta meta"
    )
    meta_matricula_carta_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 11.03"
    )
    meta_matricula_carta_file = models.FileField(
        upload_to=upload_to_resultado,
        blank=True, null=True,
        verbose_name="11.03 Atingiu meta de matrícula definida em carta meta",
    )

    # 11.04
    compras_slm_conjuntas = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="11.04 Compras de SLM ocorreram conjuntamente com matrículas e rematrículas em 70% dos casos"
    )
    compras_slm_conjuntas_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 11.04"
    )
    compras_slm_conjuntas_file = models.FileField(
        upload_to=upload_to_resultado,
        blank=True, null=True,
        verbose_name="11.04 Compras de SLM ocorreram conjuntamente com matrículas e rematrículas em 70% dos casos",
    )

    # 11.05
    resultado_financeiro_bp = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="11.05 Atingiu resultado financeiro conforme BP planejado"
    )
    resultado_financeiro_bp_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 11.05"
    )
    resultado_financeiro_bp_file = models.FileField(
        upload_to=upload_to_resultado,
        blank=True, null=True,
        verbose_name="11.05 Atingiu resultado financeiro conforme BP planejado",
    )

    def __str__(self):
        return f"{self.escola} - Resultado"






################################## BASE DE CONHECIMENTO ##############################################


class Base_de_Conhecimento_Geral(models.Model):
    titulo = models.CharField(max_length=255)
    topico = models.CharField(max_length=255, null=True, blank=True)
    sub_topico = models.CharField(max_length=255, null=True, blank=True)
    conteudo = models.TextField()
    resumo = models.TextField(null=True, blank=True)
    criado_em = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.topico} - {self.sub_topico}"
    