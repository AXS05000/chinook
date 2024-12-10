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
        choices=CHOICES, blank=True, null=True, verbose_name="3.01 - Existem profissionais qualificados na recepção para receber e registrar os pais e convidados, que fiscalizam eficazmente as operações administrativas?"
    )
    profissionais_qualificados_comment = models.TextField(
        blank=True, null=True, verbose_name="3.01 - Comentário:"
    )
    profissionais_qualificados_file = models.FileField(
        upload_to=upload_to_administrativo,
        blank=True,
        null=True,
        verbose_name="3.01 - Arquivo sobre profissionais qualificados na recepção",
    )

    # 3.02
    sistema_administracao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="3.02 - O sistema de administração escolar está sendo usado de acordo com os padrões da Maple Bear?"
    )
    sistema_administracao_comment = models.TextField(
        blank=True, null=True, verbose_name="3.02 - Comentário:"
    )
    sistema_administracao_file = models.FileField(
        upload_to=upload_to_administrativo,
        blank=True,
        null=True,
        verbose_name="3.02 - Arquivo sobre uso do sistema de administração escolar",
    )

    # 3.03
    pagamentos_em_dia = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="3.03 - A escola está em dia com seus pagamentos de royalties, pagamentos de fundos de marketing e quaisquer outros pagamentos devidos à sede regional?"
    )
    pagamentos_em_dia_comment = models.TextField(
        blank=True, null=True, verbose_name="3.03 - Comentário:"
    )
    pagamentos_em_dia_file = models.FileField(
        upload_to=upload_to_administrativo,
        blank=True,
        null=True,
        verbose_name="3.03 - Arquivo sobre pagamentos à sede regional em dia",
    )

    # 3.04
    gerencia_queixas = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="3.04 - A escola tem um processo para gerenciar as queixas da comunidade escolar?"
    )
    gerencia_queixas_comment = models.TextField(
        blank=True, null=True, verbose_name="3.04 - Comentário:"
    )
    gerencia_queixas_file = models.FileField(
        upload_to=upload_to_administrativo,
        blank=True,
        null=True,
        verbose_name="3.04 - Arquivo sobre processo para gerenciar queixas da comunidade",
    )

    # 3.05
    desempenho_kpi = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="3.05 - O desempenho do KPI da escola está alinhado com as metas estabelecidas pela sede regional?"
    )
    desempenho_kpi_comment = models.TextField(
        blank=True, null=True, verbose_name="3.05 - Comentário:"
    )
    desempenho_kpi_file = models.FileField(
        upload_to=upload_to_administrativo,
        blank=True,
        null=True,
        verbose_name="3.05 - Arquivo sobre desempenho do KPI alinhado com metas regionais",
    )

    # 3.06
    politica_negocios = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="3.06 - A escola está aderente à Política de Negócios Maple Bear?"
    )
    politica_negocios_comment = models.TextField(
        blank=True, null=True, verbose_name="3.06 - Comentário:"
    )
    politica_negocios_file = models.FileField(
        upload_to=upload_to_administrativo,
        blank=True,
        null=True,
        verbose_name="3.06 - Arquivo sobre adesão à Política de Negócios Maple Bear",
    )

    # 3.07
    controle_inadimplencia = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="3.07 - A escola realiza o controle de inadimplência com os seus clientes?"
    )
    controle_inadimplencia_comment = models.TextField(
        blank=True, null=True, verbose_name="3.07 - Comentário:"
    )
    controle_inadimplencia_file = models.FileField(
        upload_to=upload_to_administrativo,
        blank=True,
        null=True,
        verbose_name="3.07 - Arquivo sobre controle de inadimplência com os clientes",
    )

    # 3.08
    balanco_dre = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="3.08 - Faz o Balanço Patrimonial e Demonstrativo de Resultado de Exercício (DRE)?"
    )
    balanco_dre_comment = models.TextField(
        blank=True, null=True, verbose_name="3.08 - Comentário:"
    )
    balanco_dre_file = models.FileField(
        upload_to=upload_to_administrativo,
        blank=True,
        null=True,
        verbose_name="3.08 - Arquivo sobre Balanço Patrimonial e DRE",
    )

    # 3.09
    planejamento_orcamento = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="3.09 - Faz planejamento de orçamento antes do início do próximo ano letivo?"
    )
    planejamento_orcamento_comment = models.TextField(
        blank=True, null=True, verbose_name="3.09 - Comentário:"
    )
    planejamento_orcamento_file = models.FileField(
        upload_to=upload_to_administrativo,
        blank=True,
        null=True,
        verbose_name="3.09 - Arquivo sobre planejamento de orçamento antes do próximo ano",
    )

    # 3.10
    compartilhamento_orcamento = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="3.10 - O planejamento de orçamento é compartilhado com as demais áreas operacionais?"
    )
    compartilhamento_orcamento_comment = models.TextField(
        blank=True, null=True, verbose_name="3.10 - Comentário:"
    )
    compartilhamento_orcamento_file = models.FileField(
        upload_to=upload_to_administrativo,
        blank=True,
        null=True,
        verbose_name="3.10 - Arquivo sobre compartilhamento do orçamento com áreas operacionais",
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
        choices=CHOICES, blank=True, null=True, verbose_name="4.01 - A escola está usando a Intranet da Maple Bear para acessar o currículo e os recursos operacionais em conformidade com os requisitos da Maple Bear?"
    )
    uso_intranet_comment = models.TextField(
        blank=True, null=True, verbose_name="4.01 - Comentário:"
    )
    uso_intranet_file = models.FileField(
        upload_to=upload_to_tecnologia,
        blank=True,
        null=True,
        verbose_name="4.01 - Arquivo sobre uso da Intranet Maple Bear",
    )

    # 4.02
    cadastro_lex = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="4.02 - Os colaboradores estão devidamente cadastrados na LEX?"
    )
    cadastro_lex_comment = models.TextField(
        blank=True, null=True, verbose_name="4.02 - Comentário:"
    )
    cadastro_lex_file = models.FileField(
        upload_to=upload_to_tecnologia,
        blank=True,
        null=True,
        verbose_name="4.02 - Arquivo sobre colaboradores cadastrados na LEX",
    )

    # 4.03
    crm_b2c = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="4.03 - Tem CRM B2C implementado?"
    )
    crm_b2c_comment = models.TextField(
        blank=True, null=True, verbose_name="4.03 - Comentário:"
    )
    crm_b2c_file = models.FileField(
        upload_to=upload_to_tecnologia,
        blank=True,
        null=True,
        verbose_name="4.03 - Arquivo sobre CRM B2C implementado",
    )

    # 4.04
    gestao_leads = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="4.04 - Faz a gestão dos leads plenamente pelo CRM?"
    )
    gestao_leads_comment = models.TextField(
        blank=True, null=True, verbose_name="4.04 - Comentário:"
    )
    gestao_leads_file = models.FileField(
        upload_to=upload_to_tecnologia,
        blank=True,
        null=True,
        verbose_name="4.04 - Arquivo sobre gestão de leads pelo CRM",
    )

    # 4.05
    tarefas_leads = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="4.05 - Organiza as tarefas relacionadas aos Leads e as mantém atualizadas no CRM?"
    )
    tarefas_leads_comment = models.TextField(
        blank=True, null=True, verbose_name="4.05 - Comentário:"
    )
    tarefas_leads_file = models.FileField(
        upload_to=upload_to_tecnologia,
        blank=True,
        null=True,
        verbose_name="4.05 - Arquivo sobre organização e atualização de tarefas no CRM",
    )

    # 4.06
    visitas_familias = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="4.06 - Organiza as visitas das famílias e as mantém atualizadas no CRM?"
    )
    visitas_familias_comment = models.TextField(
        blank=True, null=True, verbose_name="4.06 - Comentário:"
    )
    visitas_familias_file = models.FileField(
        upload_to=upload_to_tecnologia,
        blank=True,
        null=True,
        verbose_name="4.06 - Arquivo sobre organização e atualização de visitas no CRM",
    )

    # 4.07
    oportunidades_matriculas = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="4.07 - Gera oportunidades futuras de matrículas e as mantém atualizadas no CRM?"
    )
    oportunidades_matriculas_comment = models.TextField(
        blank=True, null=True, verbose_name="4.07 - Comentário:"
    )
    oportunidades_matriculas_file = models.FileField(
        upload_to=upload_to_tecnologia,
        blank=True,
        null=True,
        verbose_name="4.07 - Arquivo sobre geração e atualização de oportunidades no CRM",
    )

    # 4.08
    pedidos_matriculas = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="4.08 - Emite seus pedidos de matrículas pelo CRM?"
    )
    pedidos_matriculas_comment = models.TextField(
        blank=True, null=True, verbose_name="4.08 - Comentário:"
    )
    pedidos_matriculas_file = models.FileField(
        upload_to=upload_to_tecnologia,
        blank=True,
        null=True,
        verbose_name="4.08 - Arquivo sobre emissão de pedidos de matrículas pelo CRM",
    )

    # 4.09
    eventos_leads = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="4.09 - Os eventos criados pela sua escola convertem leads no CRM?"
    )
    eventos_leads_comment = models.TextField(
        blank=True, null=True, verbose_name="4.09 - Comentário:"
    )
    eventos_leads_file = models.FileField(
        upload_to=upload_to_tecnologia,
        blank=True,
        null=True,
        verbose_name="4.09 - Arquivo sobre conversão de leads através de eventos no CRM",
    )

    # 4.10
    toddle_habilitado = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="4.10 - O sistema homologado Toddle está habilitado para todas as turmas com o produto família?"
    )
    toddle_habilitado_comment = models.TextField(
        blank=True, null=True, verbose_name="4.10 - Comentário:"
    )
    toddle_habilitado_file = models.FileField(
        upload_to=upload_to_tecnologia,
        blank=True,
        null=True,
        verbose_name="4.10 - Arquivo sobre Toddle habilitado para todas as turmas",
    )

    # 4.11
    uso_sponte = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="4.11 - A escola utiliza o sistema homologado Sponte?"
    )
    uso_sponte_comment = models.TextField(
        blank=True, null=True, verbose_name="4.11 - Comentário:"
    )
    uso_sponte_file = models.FileField(
        upload_to=upload_to_tecnologia,
        blank=True,
        null=True,
        verbose_name="4.11 - Arquivo sobre uso do sistema homologado Sponte",
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
        choices=CHOICES, blank=True, null=True, verbose_name="5.01 - A escola executa campanhas de marketing voltadas para reconhecimento da marca e/ou geração de leads de acordo com a campanha vigente da Maple Bear Central?"
    )
    campanhas_marketing_comment = models.TextField(
        blank=True, null=True, verbose_name="5.01 - Comentário:"
    )
    campanhas_marketing_file = models.FileField(
        upload_to=upload_to_marketing,
        blank=True,
        null=True,
        verbose_name="5.01 - Arquivo sobre execução de campanhas de marketing",
    )

    # 5.02
    planejamento_eventos = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="5.02 - A escola possui um planejamento de eventos (Exemplo: Experience Day)?"
    )
    planejamento_eventos_comment = models.TextField(
        blank=True, null=True, verbose_name="5.02 - Comentário:"
    )
    planejamento_eventos_file = models.FileField(
        upload_to=upload_to_marketing,
        blank=True,
        null=True,
        verbose_name="5.02 - Arquivo sobre planejamento de eventos",
    )

    # 5.03
    comite_gestao_crise = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="5.03 - Existe um comitê de Gestão de Crise integrado por representantes permanentes da Alta Administração da Escola e com diretrizes de comunicação a cada situação de emergência?"
    )
    comite_gestao_crise_comment = models.TextField(
        blank=True, null=True, verbose_name="5.03 - Comentário:"
    )
    comite_gestao_crise_file = models.FileField(
        upload_to=upload_to_marketing,
        blank=True,
        null=True,
        verbose_name="5.03 - Arquivo sobre comitê de Gestão de Crise",
    )

    # 5.04
    newsletter_semanal = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="5.04 - A Diretoria da Escola disponibiliza semanalmente a Newsletter para os públicos estratégicos e colaboradores?"
    )
    newsletter_semanal_comment = models.TextField(
        blank=True, null=True, verbose_name="5.04 - Comentário:"
    )
    newsletter_semanal_file = models.FileField(
        upload_to=upload_to_marketing,
        blank=True,
        null=True,
        verbose_name="5.04 - Arquivo sobre disponibilização semanal de Newsletter",
    )

    # 5.05
    ambientacao_datas_especiais = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="5.05 - A escola faz ambientação e executa ações relacionadas a datas especiais/comemorativas (Exemplo: Festa Junina)?"
    )
    ambientacao_datas_especiais_comment = models.TextField(
        blank=True, null=True, verbose_name="5.05 - Comentário:"
    )
    ambientacao_datas_especiais_file = models.FileField(
        upload_to=upload_to_marketing,
        blank=True,
        null=True,
        verbose_name="5.05 - Arquivo sobre ambientação e ações para datas especiais",
    )

    # 5.06
    google_meu_negocio = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="5.06 - O recurso Google Meu Negócio está atualizado?"
    )
    google_meu_negocio_comment = models.TextField(
        blank=True, null=True, verbose_name="5.06 - Comentário:"
    )
    google_meu_negocio_file = models.FileField(
        upload_to=upload_to_marketing,
        blank=True,
        null=True,
        verbose_name="5.06 - Arquivo sobre Google Meu Negócio atualizado",
    )

    # 5.07
    uso_site_oficial = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="5.07 - A escola utiliza o site oficial da Maple Bear para divulgação da escola e da metodologia de ensino?"
    )
    uso_site_oficial_comment = models.TextField(
        blank=True, null=True, verbose_name="5.07 - Comentário:"
    )
    uso_site_oficial_file = models.FileField(
        upload_to=upload_to_marketing,
        blank=True,
        null=True,
        verbose_name="5.07 - Arquivo sobre uso do site oficial da Maple Bear",
    )

    # 5.08
    redes_sociais = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="5.08 - As redes sociais estão atualizadas e garantindo engajamento?"
    )
    redes_sociais_comment = models.TextField(
        blank=True, null=True, verbose_name="5.08 - Comentário:"
    )
    redes_sociais_file = models.FileField(
        upload_to=upload_to_marketing,
        blank=True,
        null=True,
        verbose_name="5.08 - Arquivo sobre atualização e engajamento nas redes sociais",
    )

    # 5.09
    participacao_congressos = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="5.09 - Os colaboradores compareceram a congressos e convenções promovidas pela Maple Bear Central (Exemplo: Webinars de ciclo)?"
    )
    participacao_congressos_comment = models.TextField(
        blank=True, null=True, verbose_name="5.09 - Comentário:"
    )
    participacao_congressos_file = models.FileField(
        upload_to=upload_to_marketing,
        blank=True,
        null=True,
        verbose_name="5.09 - Arquivo sobre participação em congressos e convenções",
    )

    # 5.10
    uso_testemunhos = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="5.10 - A escola utiliza testemunhos, evidências acadêmicas, depoimentos de membros da comunidade e cases de sucesso para destacar a metodologia, senso de pertencimento e conquistas dos alunos na Maple Bear?"
    )
    uso_testemunhos_comment = models.TextField(
        blank=True, null=True, verbose_name="5.10 - Comentário:"
    )
    uso_testemunhos_file = models.FileField(
        upload_to=upload_to_marketing,
        blank=True,
        null=True,
        verbose_name="5.10 - Arquivo sobre uso de testemunhos e evidências acadêmicas",
    )

    # 5.11
    registros_crm = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="5.11 - A escola utiliza o CRM para registros em geral?"
    )
    registros_crm_comment = models.TextField(
        blank=True, null=True, verbose_name="5.11 - Comentário:"
    )
    registros_crm_file = models.FileField(
        upload_to=upload_to_marketing,
        blank=True,
        null=True,
        verbose_name="5.11 - Arquivo sobre uso do CRM para registros",
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
        choices=CHOICES, blank=True, null=True, verbose_name="6.01 - A escola pode demonstrar claramente que está usando o currículo atual da Maple Bear?"
    )
    uso_curriculo_atual_comment = models.TextField(
        blank=True, null=True, verbose_name="6.01 - Comentário:"
    )
    uso_curriculo_atual_file = models.FileField(
        upload_to=upload_to_academico,
        blank=True,
        null=True,
        verbose_name="6.01 - Arquivo sobre uso do currículo atual da Maple Bear",
    )

    # 6.02
    resultado_qa = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="6.02 - A escola possui resultado de Q/A (Quality Assurance) acima de 70%?"
    )
    resultado_qa_comment = models.TextField(
        blank=True, null=True, verbose_name="6.02 - Comentário:"
    )
    resultado_qa_file = models.FileField(
        upload_to=upload_to_academico,
        blank=True,
        null=True,
        verbose_name="6.02 - Arquivo sobre resultado de Q/A acima de 70%",
    )

    # 6.03
    participacao_treinamento = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="6.03 - Os professores e liderança acadêmica participaram do treinamento do Programa Maple Bear?"
    )
    participacao_treinamento_comment = models.TextField(
        blank=True, null=True, verbose_name="6.03 - Comentário:"
    )
    participacao_treinamento_file = models.FileField(
        upload_to=upload_to_academico,
        blank=True,
        null=True,
        verbose_name="6.03 - Arquivo sobre participação no treinamento do Programa Maple Bear",
    )

    # 6.04
    guia_teacher_toddle = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="6.04 - Possui guia da Unidade ou Teacher Guide com as orientações de planejamento e aplicação do programa para o Professor (Toddle)?"
    )
    guia_teacher_toddle_comment = models.TextField(
        blank=True, null=True, verbose_name="6.04 - Comentário:"
    )
    guia_teacher_toddle_file = models.FileField(
        upload_to=upload_to_academico,
        blank=True,
        null=True,
        verbose_name="6.04 - Arquivo sobre guia da Unidade ou Teacher Guide (Toddle)",
    )

    # 6.05
    recursos_alunos_professores = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="6.05 - Os recursos para alunos e professores são disponibilizados e utilizados conforme plano do Programa Maple Bear?"
    )
    recursos_alunos_professores_comment = models.TextField(
        blank=True, null=True, verbose_name="6.05 - Comentário:"
    )
    recursos_alunos_professores_file = models.FileField(
        upload_to=upload_to_academico,
        blank=True,
        null=True,
        verbose_name="6.05 - Arquivo sobre recursos para alunos e professores utilizados",
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
        choices=CHOICES, blank=True, null=True, verbose_name="7.01 - A escola tem um Plano de Preparação para Emergências em vigor?"
    )
    plano_emergencia_comment = models.TextField(
        blank=True, null=True, verbose_name="7.01 - Comentário:"
    )
    plano_emergencia_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.01 - Arquivo sobre Plano de Preparação para Emergências",
    )

    # 7.02
    info_medicas_atualizadas = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.02 - A escola mantém informações atualizadas para apoiar alunos e funcionários com condições médicas prevalentes?"
    )
    info_medicas_atualizadas_comment = models.TextField(
        blank=True, null=True, verbose_name="7.02 - Comentário:"
    )
    info_medicas_atualizadas_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.02 - Arquivo sobre informações médicas atualizadas",
    )

    # 7.03
    contato_atualizado = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.03 - A escola mantém uma lista atualizada de informações de contato de alunos e funcionários? Essas informações estão prontamente disponíveis para a Equipe de Resposta a Emergências?"
    )
    contato_atualizado_comment = models.TextField(
        blank=True, null=True, verbose_name="7.03 - Comentário:"
    )
    contato_atualizado_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.03 - Arquivo sobre lista de contatos atualizada",
    )

    # 7.04
    seguranca_contra_incendio = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.04 - A escola possui equipamentos de prevenção e segurança contra incêndio adequados e de fácil acesso, instalados corretamente e inspecionados regularmente?"
    )
    seguranca_contra_incendio_comment = models.TextField(
        blank=True, null=True, verbose_name="7.04 - Comentário:"
    )
    seguranca_contra_incendio_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.04 - Arquivo sobre equipamentos de segurança contra incêndio",
    )

    # 7.05
    saidas_emergencia = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.05 - A escola tem saídas de emergência claramente marcadas e desobstruídas?"
    )
    saidas_emergencia_comment = models.TextField(
        blank=True, null=True, verbose_name="7.05 - Comentário:"
    )
    saidas_emergencia_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.05 - Arquivo sobre saídas de emergência marcadas e desobstruídas",
    )

    # 7.06
    kits_primeiros_socorros = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.06 - A escola tem kits de primeiros socorros totalmente abastecidos disponíveis?"
    )
    kits_primeiros_socorros_comment = models.TextField(
        blank=True, null=True, verbose_name="7.06 - Comentário:"
    )
    kits_primeiros_socorros_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.06 - Arquivo sobre kits de primeiros socorros disponíveis",
    )

    # 7.07
    funcionarios_treinados_primeiros_socorros = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.07 - A escola tem funcionários treinados em primeiros socorros e RCP?"
    )
    funcionarios_treinados_primeiros_socorros_comment = models.TextField(
        blank=True, null=True, verbose_name="7.07 - Comentário:"
    )
    funcionarios_treinados_primeiros_socorros_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.07 - Arquivo sobre funcionários treinados em primeiros socorros e RCP",
    )

    # 7.08
    simulacoes_emergencia = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.08 - A escola realiza exercícios de emergência variados para simular situações de emergência para testar procedimentos universais (bloqueios, evacuação, abrigo no local)?"
    )
    simulacoes_emergencia_comment = models.TextField(
        blank=True, null=True, verbose_name="7.08 - Comentário:"
    )
    simulacoes_emergencia_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.08 - Arquivo sobre simulações de emergência realizadas",
    )

    # 7.09
    recursos_maple_bear = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.09 - Os livros e os recursos da Maple Bear estão em condições e qualidade adequadas?"
    )
    recursos_maple_bear_comment = models.TextField(
        blank=True, null=True, verbose_name="7.09 - Comentário:"
    )
    recursos_maple_bear_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.09 - Arquivo sobre recursos Maple Bear em condições adequadas",
    )

    # 7.10
    garantia_qualidade = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.10 - A escola se envolveu em Garantia de Qualidade em alinhamento com o padrão Maple Bear?"
    )
    garantia_qualidade_comment = models.TextField(
        blank=True, null=True, verbose_name="7.10 - Comentário:"
    )
    garantia_qualidade_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.10 - Arquivo sobre envolvimento em Garantia de Qualidade",
    )

    # 7.11
    treinamento_academico = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.11 - A escola se envolveu em treinamento acadêmico em alinhamento com o padrão Maple Bear?"
    )
    treinamento_academico_comment = models.TextField(
        blank=True, null=True, verbose_name="7.11 - Comentário:"
    )
    treinamento_academico_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.11 - Arquivo sobre envolvimento em treinamento acadêmico",
    )

    # 7.12
    reunioes_lideranca = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.12 - A escola cumpriu o calendário de reuniões de Liderança?"
    )
    reunioes_lideranca_comment = models.TextField(
        blank=True, null=True, verbose_name="7.12 - Comentário:"
    )
    reunioes_lideranca_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.12 - Arquivo sobre cumprimento do calendário de reuniões de Liderança",
    )

    # 7.13
    processo_padronizado_atendimento = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.13 - A escola possui um processo definido e padronizado de atendimento aos pais, responsáveis e clientes?"
    )
    processo_padronizado_atendimento_comment = models.TextField(
        blank=True, null=True, verbose_name="7.13 - Comentário:"
    )
    processo_padronizado_atendimento_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.13 - Arquivo sobre processo padronizado de atendimento",
    )

    # 7.14
    controle_frequencia_alunos = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.14 - A escola possui controle diário de frequência dos alunos?"
    )
    controle_frequencia_alunos_comment = models.TextField(
        blank=True, null=True, verbose_name="7.14 - Comentário:"
    )
    controle_frequencia_alunos_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.14 - Arquivo sobre controle diário de frequência dos alunos",
    )

    # 7.15
    controle_media_alunos = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.15 - A escola possui controle e monitora a média de alunos por turma?"
    )
    controle_media_alunos_comment = models.TextField(
        blank=True, null=True, verbose_name="7.15 - Comentário:"
    )
    controle_media_alunos_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.15 - Arquivo sobre controle e monitoramento da média de alunos por turma",
    )

    # 7.16
    atividades_extracurriculares = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.16 - A escola possui atividades extracurriculares?"
    )
    atividades_extracurriculares_comment = models.TextField(
        blank=True, null=True, verbose_name="7.16 - Comentário:"
    )
    atividades_extracurriculares_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.16 - Arquivo sobre atividades extracurriculares disponíveis",
    )

    # 7.17
    analise_pontos_fortes = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.17 - A escola realizou análise dos pontos fortes, fracos, oportunidades e ameaças em relação à unidade?"
    )
    analise_pontos_fortes_comment = models.TextField(
        blank=True, null=True, verbose_name="7.17 - Comentário:"
    )
    analise_pontos_fortes_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.17 - Arquivo sobre análise de pontos fortes, fracos, oportunidades e ameaças",
    )

    # 7.18
    planos_acao_defasagens = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.18 - A escola desenvolve planos de ação para sanar as defasagens identificadas?"
    )
    planos_acao_defasagens_comment = models.TextField(
        blank=True, null=True, verbose_name="7.18 - Comentário:"
    )
    planos_acao_defasagens_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.18 - Arquivo sobre planos de ação para sanar defasagens",
    )

    # 7.19
    experiencia_professores = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.19 - Os professores possuem experiência mínima desejada de 1 ano como professor?"
    )
    experiencia_professores_comment = models.TextField(
        blank=True, null=True, verbose_name="7.19 - Comentário:"
    )
    experiencia_professores_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.19 - Arquivo sobre professores com experiência mínima de 1 ano",
    )

    # 7.20
    professores_por_turma = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.20 - Todas as turmas possuem professores?"
    )
    professores_por_turma_comment = models.TextField(
        blank=True, null=True, verbose_name="7.20 - Comentário:"
    )
    professores_por_turma_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.20 - Arquivo sobre professores por turma",
    )

    # 7.21
    observacao_aulas = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.21 - A liderança observa aulas ministradas pela equipe pedagógica?"
    )
    observacao_aulas_comment = models.TextField(
        blank=True, null=True, verbose_name="7.21 - Comentário:"
    )
    observacao_aulas_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.21 - Arquivo sobre observação de aulas pela liderança",
    )

    # 7.22
    lideranca_graduada = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.22 - A escola possui liderança graduada em pedagogia e gestão escolar que assine pela escola?"
    )
    lideranca_graduada_comment = models.TextField(
        blank=True, null=True, verbose_name="7.22 - Comentário:"
    )
    lideranca_graduada_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.22 - Arquivo sobre liderança graduada em pedagogia e gestão escolar",
    )

    # 7.23
    coordenacao_por_segmento = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.23 - A escola possui coordenação para cada segmento?"
    )
    coordenacao_por_segmento_comment = models.TextField(
        blank=True, null=True, verbose_name="7.23 - Comentário:"
    )
    coordenacao_por_segmento_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.23 - Arquivo sobre coordenação para cada segmento",
    )
    # 7.24
    cumprimento_legislacao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.24 - A escola segue a legislação de onde está localizada?"
    )
    cumprimento_legislacao_comment = models.TextField(
        blank=True, null=True, verbose_name="7.24 - Comentário:"
    )
    cumprimento_legislacao_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.24 - Arquivo sobre cumprimento da legislação local",
    )

    # 7.25
    guia_familia = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.25 - A escola possui Parents Handbook (Guia da Família)?"
    )
    guia_familia_comment = models.TextField(
        blank=True, null=True, verbose_name="7.25 - Comentário:"
    )
    guia_familia_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.25 - Arquivo sobre Parents Handbook (Guia da Família)",
    )

    # 7.26
    comunicacao_interna = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.26 - A escola possui esquema de comunicação interna?"
    )
    comunicacao_interna_comment = models.TextField(
        blank=True, null=True, verbose_name="7.26 - Comentário:"
    )
    comunicacao_interna_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.26 - Arquivo sobre esquema de comunicação interna",
    )

    # 7.27
    toddle_comunicacao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.27 - A escola utiliza a Toddle como recurso padrão de comunicação?"
    )
    toddle_comunicacao_comment = models.TextField(
        blank=True, null=True, verbose_name="7.27 - Comentário:"
    )
    toddle_comunicacao_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.27 - Arquivo sobre uso da Toddle como recurso padrão de comunicação",
    )

    # 7.28
    nps_acima_70 = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.28 - A escola tem NPS (Net Promoter Score) acima de 70 pontos?"
    )
    nps_acima_70_comment = models.TextField(
        blank=True, null=True, verbose_name="7.28 - Comentário:"
    )
    nps_acima_70_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.28 - Arquivo sobre NPS acima de 70 pontos",
    )

    # 7.29
    orientador_pedagogico = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.29 - A escola possui Orientador Pedagógico (a partir do Middle Year)?"
    )
    orientador_pedagogico_comment = models.TextField(
        blank=True, null=True, verbose_name="7.29 - Comentário:"
    )
    orientador_pedagogico_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.29 - Arquivo sobre Orientador Pedagógico (a partir do Middle Year)",
    )

    # 7.30
    certificado_lei_lucas = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="7.30 - A escola possui certificado da Lei de Primeiro Socorros (Lei Lucas)?"
    )
    certificado_lei_lucas_comment = models.TextField(
        blank=True, null=True, verbose_name="7.30 - Comentário:"
    )
    certificado_lei_lucas_file = models.FileField(
        upload_to=upload_to_gestao_escolar,
        blank=True,
        null=True,
        verbose_name="7.30 - Arquivo sobre certificado da Lei de Primeiro Socorros (Lei Lucas)",
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
        choices=CHOICES, blank=True, null=True, verbose_name="8.01 - Participou de todos os treinamentos pedagógicos promovidos pela Franqueadora?"
    )
    treinamentos_pedagogicos_comment = models.TextField(
        blank=True, null=True, verbose_name="8.01 - Comentário:"
    )
    treinamentos_pedagogicos_file = models.FileField(
        upload_to=upload_to_operacao_academica,
        blank=True,
        null=True,
        verbose_name="8.01 - Arquivo sobre participação em treinamentos pedagógicos",
    )

    # 8.02
    professores_nivel_superior = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="8.02 - Os professores possuem nível superior em humanas?"
    )
    professores_nivel_superior_comment = models.TextField(
        blank=True, null=True, verbose_name="8.02 - Comentário:"
    )
    professores_nivel_superior_file = models.FileField(
        upload_to=upload_to_operacao_academica,
        blank=True,
        null=True,
        verbose_name="8.02 - Arquivo sobre professores com nível superior em humanas",
    )

    # 8.03
    professores_certificacao_internacional = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="8.03 - Os professores possuem TOEIC acima de 800 pontos, exame de proficiência com nota equivalente, CELTA ou Certificação Internacional equivalente?"
    )
    professores_certificacao_internacional_comment = models.TextField(
        blank=True, null=True, verbose_name="8.03 - Comentário:"
    )
    professores_certificacao_internacional_file = models.FileField(
        upload_to=upload_to_operacao_academica,
        blank=True,
        null=True,
        verbose_name="8.03 - Arquivo sobre professores com certificação internacional",
    )

    # 8.04
    preparo_aulas_previo = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="8.04 - O professor prepara todas as aulas de forma prévia à aplicação?"
    )
    preparo_aulas_previo_comment = models.TextField(
        blank=True, null=True, verbose_name="8.04 - Comentário:"
    )
    preparo_aulas_previo_file = models.FileField(
        upload_to=upload_to_operacao_academica,
        blank=True,
        null=True,
        verbose_name="8.04 - Arquivo sobre preparo prévio das aulas pelo professor",
    )

    # 8.05
    metodologia_maple_bear = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="8.05 - O professor contempla aspectos da metodologia Maple Bear no plano de aula?"
    )
    metodologia_maple_bear_comment = models.TextField(
        blank=True, null=True, verbose_name="8.05 - Comentário:"
    )
    metodologia_maple_bear_file = models.FileField(
        upload_to=upload_to_operacao_academica,
        blank=True,
        null=True,
        verbose_name="8.05 - Arquivo sobre aspectos da metodologia Maple Bear no plano de aula",
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
        choices=CHOICES, blank=True, null=True, verbose_name="9.01 - O interior do prédio da Escola tem o logotipo da Maple Bear, o padrão e as cores, conforme definido pelo 'Manual de Identidade da Marca'?"
    )
    interior_logotipo_maple_bear_comment = models.TextField(
        blank=True, null=True, verbose_name="9.01 - Comentário:"
    )
    interior_logotipo_maple_bear_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.01 - Arquivo sobre logotipo no interior do prédio",
    )

    # 9.02
    exterior_logotipo_maple_bear = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.02 - O exterior do prédio da Escola tem o padrão e as cores do logotipo da Maple Bear, conforme definido pelo 'Manual de Identidade da Marca'?"
    )
    exterior_logotipo_maple_bear_comment = models.TextField(
        blank=True, null=True, verbose_name="9.02 - Comentário:"
    )
    exterior_logotipo_maple_bear_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.02 - Arquivo sobre logotipo no exterior do prédio",
    )

    # 9.03
    logotipo_estado_conservacao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.03 - Todos os padrões e cores do logotipo da Maple Bear estão em bom estado de conservação?"
    )
    logotipo_estado_conservacao_comment = models.TextField(
        blank=True, null=True, verbose_name="9.03 - Comentário:"
    )
    logotipo_estado_conservacao_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.03 - Arquivo sobre estado de conservação do logotipo",
    )

    # 9.04
    sistema_monitoramento_seguranca = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.04 - A escola possui um sistema de monitoramento de segurança totalmente funcional na data desta avaliação?"
    )
    sistema_monitoramento_seguranca_comment = models.TextField(
        blank=True, null=True, verbose_name="9.04 - Comentário:"
    )
    sistema_monitoramento_seguranca_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.04 - Arquivo sobre sistema de monitoramento de segurança",
    )

    # 9.05
    controle_acesso_predio = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.05 - A escola possui um processo de controle de acesso ao prédio para garantir que apenas visitantes autorizados possam entrar, em conformidade com os padrões regionais da Maple Bear?"
    )
    controle_acesso_predio_comment = models.TextField(
        blank=True, null=True, verbose_name="9.05 - Comentário:"
    )
    controle_acesso_predio_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.05 - Arquivo sobre controle de acesso ao prédio",
    )
    # 9.06
    sistema_alarme_emergencia = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.06 - A escola tem um sistema de alarme de emergência instalado e existe um procedimento de manutenção e teste periódico estabelecido para este sistema?"
    )
    sistema_alarme_emergencia_comment = models.TextField(
        blank=True, null=True, verbose_name="9.06 - Comentário:"
    )
    sistema_alarme_emergencia_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.06 - Arquivo sobre sistema de alarme de emergência",
    )

    # 9.07
    area_recreacao_conformidade = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.07 - A área de recreação interna/externa está em conformidade com os padrões da Maple Bear?"
    )
    area_recreacao_conformidade_comment = models.TextField(
        blank=True, null=True, verbose_name="9.07 - Comentário:"
    )
    area_recreacao_conformidade_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.07 - Arquivo sobre área de recreação",
    )

    # 9.08
    equipamento_recreacao_conservacao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.08 - O equipamento na área de recreação interna/externa está em bom estado de conservação e existe um processo de manutenção para confirmar isso?"
    )
    equipamento_recreacao_conservacao_comment = models.TextField(
        blank=True, null=True, verbose_name="9.08 - Comentário:"
    )
    equipamento_recreacao_conservacao_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.08 - Arquivo sobre equipamento de recreação",
    )

    # 9.09
    instalacoes_limpeza_organizacao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.09 - As instalações da escola estão limpas, higienizadas (quando apropriado) e bem organizadas?"
    )
    instalacoes_limpeza_organizacao_comment = models.TextField(
        blank=True, null=True, verbose_name="9.09 - Comentário:"
    )
    instalacoes_limpeza_organizacao_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.09 - Arquivo sobre limpeza e organização das instalações",
    )

    # 9.10
    seguranca_estrutural = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.10 - A escola tem guardas de segurança e sinalização adequados nas janelas, corredores e outras áreas da escola para evitar quedas?"
    )
    seguranca_estrutural_comment = models.TextField(
        blank=True, null=True, verbose_name="9.10 - Comentário:"
    )
    seguranca_estrutural_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.10 - Arquivo sobre segurança estrutural",
    )

    # 9.11
    sinalizacao_predio = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.11 - A escola tem sinalização clara e apropriada denotando as entradas e saídas do prédio?"
    )
    sinalizacao_predio_comment = models.TextField(
        blank=True, null=True, verbose_name="9.11 - Comentário:"
    )
    sinalizacao_predio_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.11 - Arquivo sobre sinalização do prédio",
    )

    # 9.12
    proporcao_adultos_alunos = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.12 - As salas de aula aderem às proporções de adultos para alunos, conforme aprovado pela Maple Bear Global?"
    )
    proporcao_adultos_alunos_comment = models.TextField(
        blank=True, null=True, verbose_name="9.12 - Comentário:"
    )
    proporcao_adultos_alunos_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.12 - Arquivo sobre proporção adulto-aluno",
    )

    # 9.13
    mobilia_salas_conservacao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.13 - A mobília da sala de aula está em bom estado de conservação e existe um processo para garantir a inspeção periódica?"
    )
    mobilia_salas_conservacao_comment = models.TextField(
        blank=True, null=True, verbose_name="9.13 - Comentário:"
    )
    mobilia_salas_conservacao_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.13 - Arquivo sobre mobília das salas",
    )
    # 9.14
    organizacao_corredores = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.14 - Os corredores da escola são organizados de forma que possam ser facilmente percorridos por alunos, funcionários e visitantes?"
    )
    organizacao_corredores_comment = models.TextField(
        blank=True, null=True, verbose_name="9.14 - Comentário:"
    )
    organizacao_corredores_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.14 - Arquivo sobre organização dos corredores",
    )

    # 9.15
    acessibilidade_pne = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.15 - A escola possui instalações que garantem acessibilidade adequada para pessoas com necessidades especiais e/ou mobilidade reduzida e estão em bom estado de conservação?"
    )
    acessibilidade_pne_comment = models.TextField(
        blank=True, null=True, verbose_name="9.15 - Comentário:"
    )
    acessibilidade_pne_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.15 - Arquivo sobre acessibilidade PNE",
    )

    # 9.16
    politica_embarque_desembarque = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.16 - A escola segue uma política e procedimento de embarque e desembarque?"
    )
    politica_embarque_desembarque_comment = models.TextField(
        blank=True, null=True, verbose_name="9.16 - Comentário:"
    )
    politica_embarque_desembarque_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.16 - Arquivo sobre política de embarque e desembarque",
    )

    # 9.17
    banheiros_conservacao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.17 - Os banheiros da escola para funcionários e alunos são mantidos separados e estão em bom estado de conservação?"
    )
    banheiros_conservacao_comment = models.TextField(
        blank=True, null=True, verbose_name="9.17 - Comentário:"
    )
    banheiros_conservacao_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.17 - Arquivo sobre conservação dos banheiros",
    )

    # 9.18
    conservacao_geral_instalacoes = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.18 - As instalações da escola estão em bom estado de conservação, de modo que todos os acessórios, incluindo aqueles relacionados à iluminação, portas e janelas, estejam totalmente funcionais?"
    )
    conservacao_geral_instalacoes_comment = models.TextField(
        blank=True, null=True, verbose_name="9.18 - Comentário:"
    )
    conservacao_geral_instalacoes_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.18 - Arquivo sobre conservação geral das instalações",
    )

    # 9.19
    danos_esteticos_instalacoes = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.19 - As instalações da escola estão em bom estado de conservação, de modo que não haja danos estéticos nas portas, janelas, pisos, tetos e paredes?"
    )
    danos_esteticos_instalacoes_comment = models.TextField(
        blank=True, null=True, verbose_name="9.19 - Comentário:"
    )
    danos_esteticos_instalacoes_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.19 - Arquivo sobre danos estéticos das instalações",
    )

    # 9.20
    danos_estruturais_eventuais = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.20 - As instalações da escola estão em bom estado de conservação, de modo que não haja danos estruturais visíveis em pisos, tetos, paredes, encanamentos ou sistemas elétricos que exijam reparos eventuais?"
    )
    danos_estruturais_eventuais_comment = models.TextField(
        blank=True, null=True, verbose_name="9.20 - Comentário:"
    )
    danos_estruturais_eventuais_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.20 - Arquivo sobre danos estruturais eventuais",
    )

    # 9.21
    danos_estruturais_risco = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.21 - As instalações da escola estão em bom estado de conservação, de modo que não haja danos estruturais visíveis no piso, teto, paredes, encanamentos ou sistemas elétricos que representem risco iminente para a segurança da comunidade escolar?"
    )
    danos_estruturais_risco_comment = models.TextField(
        blank=True, null=True, verbose_name="9.21 - Comentário:"
    )
    danos_estruturais_risco_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.21 - Arquivo sobre danos estruturais com risco iminente",
    )

    # 9.22
    pia_salas_infantil = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.22 - Todas as salas de aula do infantil possuem pia para uso dos alunos?"
    )
    pia_salas_infantil_comment = models.TextField(
        blank=True, null=True, verbose_name="9.22 - Comentário:"
    )
    pia_salas_infantil_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.22 - Arquivo sobre pia nas salas de infantil",
    )
    # 9.23
    banheiro_trocador_bear_care = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.23 - Salas de Bear Care/Toddler possuem banheiro com banheira e trocador?"
    )
    banheiro_trocador_bear_care_comment = models.TextField(
        blank=True, null=True, verbose_name="9.23 - Comentário:"
    )
    banheiro_trocador_bear_care_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.23 - Arquivo sobre banheiros nas salas de Bear Care/Toddler",
    )

    # 9.24
    banheiro_chuveiro_infantil = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.24 - Salas de Nursery, JK, SK possuem banheiro com chuveiro?"
    )
    banheiro_chuveiro_infantil_comment = models.TextField(
        blank=True, null=True, verbose_name="9.24 - Comentário:"
    )
    banheiro_chuveiro_infantil_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.24 - Arquivo sobre banheiros com chuveiro",
    )

    # 9.25
    playground_externo = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.25 - Playground externo em bom estado de conservação?"
    )
    playground_externo_comment = models.TextField(
        blank=True, null=True, verbose_name="9.25 - Comentário:"
    )
    playground_externo_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.25 - Arquivo sobre playground externo",
    )

    # 9.26
    rampas_corrimaos = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.26 - Possui rampas e escadas com corrimãos duplos?"
    )
    rampas_corrimaos_comment = models.TextField(
        blank=True, null=True, verbose_name="9.26 - Comentário:"
    )
    rampas_corrimaos_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.26 - Arquivo sobre rampas e corrimãos",
    )

    # 9.27
    sala_comercial_padroes = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.27 - A sala de atendimento comercial da Unidade segue o padrão da Franqueadora?"
    )
    sala_comercial_padroes_comment = models.TextField(
        blank=True, null=True, verbose_name="9.27 - Comentário:"
    )
    sala_comercial_padroes_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.27 - Arquivo sobre sala comercial",
    )

    # 9.28
    refeitório_conservacao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.28 - Refeitório atende 1/3 da capacidade e está em bom estado?"
    )
    refeitório_conservacao_comment = models.TextField(
        blank=True, null=True, verbose_name="9.28 - Comentário:"
    )
    refeitório_conservacao_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.28 - Arquivo sobre refeitório",
    )

    # 9.29
    cozinha_vigilancia_sanitaria = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.29 - Cozinha em conformidade com normas de vigilância sanitária?"
    )
    cozinha_vigilancia_sanitaria_comment = models.TextField(
        blank=True, null=True, verbose_name="9.29 - Comentário:"
    )
    cozinha_vigilancia_sanitaria_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.29 - Arquivo sobre cozinha",
    )

    # 9.30
    playground_interno = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.30 - Playground interno em bom estado de conservação?"
    )
    playground_interno_comment = models.TextField(
        blank=True, null=True, verbose_name="9.30 - Comentário:"
    )
    playground_interno_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.30 - Arquivo sobre playground interno",
    )

    # 9.31
    espaco_esportes = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.31 - Espaço para prática de esportes em bom estado?"
    )
    espaco_esportes_comment = models.TextField(
        blank=True, null=True, verbose_name="9.31 - Comentário:"
    )
    espaco_esportes_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.31 - Arquivo sobre espaço esportivo",
    )

    # 9.32
    quadra_poliesportiva = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.32 - Quadra poliesportiva em bom estado?"
    )
    quadra_poliesportiva_comment = models.TextField(
        blank=True, null=True, verbose_name="9.32 - Comentário:"
    )
    quadra_poliesportiva_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.32 - Arquivo sobre quadra poliesportiva",
    )

    # 9.33
    biblioteca_conservacao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.33 - Biblioteca em bom estado de conservação?"
    )
    biblioteca_conservacao_comment = models.TextField(
        blank=True, null=True, verbose_name="9.33 - Comentário:"
    )
    biblioteca_conservacao_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.33 - Arquivo sobre biblioteca",
    )

    # 9.34
    banheiros_pne_legislacao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.34 - Banheiros PNE de acordo com legislação local?"
    )
    banheiros_pne_legislacao_comment = models.TextField(
        blank=True, null=True, verbose_name="9.34 - Comentário:"
    )
    banheiros_pne_legislacao_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.34 - Arquivo sobre banheiros PNE",
    )
    # 9.35
    laboratorio_ciencias = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.35 - Laboratório de ciências em bom estado (Middle Years)?"
    )
    laboratorio_ciencias_comment = models.TextField(
        blank=True, null=True, verbose_name="9.35 - Comentário:"
    )
    laboratorio_ciencias_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.35 - Arquivo sobre laboratório de ciências",
    )

    # 9.36
    mobiliario_fornecedores_homologados = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.36 - Mobiliário adquirido com fornecedores homologados?"
    )
    mobiliario_fornecedores_homologados_comment = models.TextField(
        blank=True, null=True, verbose_name="9.36 - Comentário:"
    )
    mobiliario_fornecedores_homologados_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.36 - Arquivo sobre fornecedores homologados",
    )

    # 9.37
    mobiliario_salas_admin_professores = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.37 - Mobiliário das salas administrativas e de professores em bom estado?"
    )
    mobiliario_salas_admin_professores_comment = models.TextField(
        blank=True, null=True, verbose_name="9.37 - Comentário:"
    )
    mobiliario_salas_admin_professores_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.37 - Arquivo sobre mobiliário administrativo",
    )

    # 9.38
    sala_coordenacao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.38 - Sala de Coordenação em bom estado de conservação?"
    )
    sala_coordenacao_comment = models.TextField(
        blank=True, null=True, verbose_name="9.38 - Comentário:"
    )
    sala_coordenacao_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.38 - Arquivo sobre sala de coordenação",
    )

    # 9.39
    sala_professores = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.39 - Sala de Professores em bom estado de conservação?"
    )
    sala_professores_comment = models.TextField(
        blank=True, null=True, verbose_name="9.39 - Comentário:"
    )
    sala_professores_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.39 - Arquivo sobre sala de professores",
    )

    # 9.40
    vagas_estacionamento = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.40 - Vagas de estacionamento conforme legislação?"
    )
    vagas_estacionamento_comment = models.TextField(
        blank=True, null=True, verbose_name="9.40 - Comentário:"
    )
    vagas_estacionamento_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.40 - Arquivo sobre estacionamento",
    )

    # 9.41
    iluminacao_ventilacao = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.41 - Atendimento ao padrão de iluminação e ventilação?"
    )
    iluminacao_ventilacao_comment = models.TextField(
        blank=True, null=True, verbose_name="9.41 - Comentário:"
    )
    iluminacao_ventilacao_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.41 - Arquivo sobre iluminação e ventilação",
    )

    # 9.42
    paredes_balcao_logos = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.42 - Paredes, balcão e logos da recepção no padrão da Franqueadora?"
    )
    paredes_balcao_logos_comment = models.TextField(
        blank=True, null=True, verbose_name="9.42 - Comentário:"
    )
    paredes_balcao_logos_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.42 - Arquivo sobre recepção",
    )

    # 9.43
    salas_55m2 = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.43 - Salas de aula com no mínimo 55m², incluindo banheiro?"
    )
    salas_55m2_comment = models.TextField(
        blank=True, null=True, verbose_name="9.43 - Comentário:"
    )
    salas_55m2_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.43 - Arquivo sobre salas de aula",
    )

    # 9.44
    copa_colaboradores = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="9.44 - Copa para os Colaboradores em bom estado de conservação?"
    )
    copa_colaboradores_comment = models.TextField(
        blank=True, null=True, verbose_name="9.44 - Comentário:"
    )
    copa_colaboradores_file = models.FileField(
        upload_to=upload_to_implantacao,
        blank=True,
        null=True,
        verbose_name="9.44 - Arquivo sobre copa dos colaboradores",
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
        choices=CHOICES, blank=True, null=True, verbose_name="10.01 - A escola tem um processo de matrícula robusto?"
    )
    processo_matricula_robusto_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.01"
    )
    processo_matricula_robusto_file = models.FileField(
        upload_to=upload_to_comercial, blank=True, null=True, verbose_name="Arquivo para 10.01"
    )

    # 10.02
    plano_marketing_matricula = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.02 - A escola tem um plano de marketing de matrícula ativo?"
    )
    plano_marketing_matricula_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.02"
    )
    plano_marketing_matricula_file = models.FileField(
        upload_to=upload_to_comercial, blank=True, null=True, verbose_name="Arquivo para 10.02"
    )

    # 10.03
    materiais_marketing_padroes = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.03 - Materiais de marketing alinhados aos padrões da Maple Bear"
    )
    materiais_marketing_padroes_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.03"
    )
    materiais_marketing_padroes_file = models.FileField(
        upload_to=upload_to_comercial, blank=True, null=True, verbose_name="Arquivo para 10.03"
    )

    # 10.04
    equipe_lideranca_comercial = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.04 - Possui uma liderança e equipe comercial na unidade?"
    )
    equipe_lideranca_comercial_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.04"
    )
    equipe_lideranca_comercial_file = models.FileField(
        upload_to=upload_to_comercial, blank=True, null=True, verbose_name="Arquivo para 10.04"
    )

    # 10.05
    reunioes_lideranca_comercial = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.05 - A liderança realiza reunião semanal com o seu time comercial?"
    )
    reunioes_lideranca_comercial_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.05"
    )
    reunioes_lideranca_comercial_file = models.FileField(
        upload_to=upload_to_comercial, blank=True, null=True, verbose_name="Arquivo para 10.05"
    )

    # 10.06
    recepcao_visitantes = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.06 - Recepção cortês e afável a visitantes, pais e colaboradores?"
    )
    recepcao_visitantes_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.06"
    )
    recepcao_visitantes_file = models.FileField(
        upload_to=upload_to_comercial, blank=True, null=True, verbose_name="Arquivo para 10.06"
    )

    # 10.07
    metas_matriculas_rematriculas = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.07 - Desdobramento das metas de matrículas e rematrículas?"
    )
    metas_matriculas_rematriculas_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.07"
    )
    metas_matriculas_rematriculas_file = models.FileField(
        upload_to=upload_to_comercial, blank=True, null=True, verbose_name="Arquivo para 10.07"
    )

    # 10.08
    metas_nps = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.08 - Desdobramento da meta da pesquisa NPS?"
    )
    metas_nps_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.08"
    )
    metas_nps_file = models.FileField(
        upload_to=upload_to_comercial, blank=True, null=True, verbose_name="Arquivo para 10.08"
    )

    # 10.09
    mentoria_vendas = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.09 - Participação da equipe comercial em mentoria de vendas?"
    )
    mentoria_vendas_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.09"
    )
    mentoria_vendas_file = models.FileField(
        upload_to=upload_to_comercial, blank=True, null=True, verbose_name="Arquivo para 10.09"
    )

    # 10.10
    trilha_treinamento_vendas = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.10 - Conclusão da trilha de treinamento de vendas?"
    )
    trilha_treinamento_vendas_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.10"
    )
    trilha_treinamento_vendas_file = models.FileField(
        upload_to=upload_to_comercial, blank=True, null=True, verbose_name="Arquivo para 10.10"
    )

    # 10.11
    funil_vendas_crm = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.11 - Etapas do funil de vendas registradas no CRM?"
    )
    funil_vendas_crm_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.11"
    )
    funil_vendas_crm_file = models.FileField(
        upload_to=upload_to_comercial, blank=True, null=True, verbose_name="Arquivo para 10.11"
    )

    # 10.12
    cliente_oculto = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.12 - Pontuação acima de 70% no cliente oculto?"
    )
    cliente_oculto_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.12"
    )
    cliente_oculto_file = models.FileField(
        upload_to=upload_to_comercial, blank=True, null=True, verbose_name="Arquivo para 10.12"
    )
    # 10.13
    participacao_campanhas_acoes = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.13 - Participou de 70% das campanhas e ações comerciais promovidas pela marca?"
    )
    participacao_campanhas_acoes_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.13"
    )
    participacao_campanhas_acoes_file = models.FileField(
        upload_to=upload_to_comercial, blank=True, null=True, verbose_name="Arquivo para 10.13"
    )

    # 10.14
    pesquisas_mercado = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.14 - Realiza pesquisas de mercado e conhece concorrentes?"
    )
    pesquisas_mercado_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.14"
    )
    pesquisas_mercado_file = models.FileField(
        upload_to=upload_to_comercial, blank=True, null=True, verbose_name="Arquivo para 10.14"
    )

    # 10.15
    conversao_leads_marketing = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.15 - Converteu 5% dos leads gerados no marketing online comprovados no CRM?"
    )
    conversao_leads_marketing_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.15"
    )
    conversao_leads_marketing_file = models.FileField(
        upload_to=upload_to_comercial, blank=True, null=True, verbose_name="Arquivo para 10.15"
    )

    # 10.16
    capacitacao_exposicao_metodologia = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.16 - Capacitou as equipes para exposição correta da metodologia?"
    )
    capacitacao_exposicao_metodologia_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.16"
    )
    capacitacao_exposicao_metodologia_file = models.FileField(
        upload_to=upload_to_comercial, blank=True, null=True, verbose_name="Arquivo para 10.16"
    )

    # 10.17
    politica_comissionamento = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.17 - Adota política de comissionamento/bônus para área Comercial?"
    )
    politica_comissionamento_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.17"
    )
    politica_comissionamento_file = models.FileField(
        upload_to=upload_to_comercial, blank=True, null=True, verbose_name="Arquivo para 10.17"
    )

    # 10.18
    calendario_trade_marketing = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.18 - Possui calendário de Trade Marketing definido e implementado?"
    )
    calendario_trade_marketing_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.18"
    )
    calendario_trade_marketing_file = models.FileField(
        upload_to=upload_to_comercial, blank=True, null=True, verbose_name="Arquivo para 10.18"
    )

    # 10.19
    equipe_marketing = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.19 - Possui equipe de Marketing ou agência responsável?"
    )
    equipe_marketing_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.19"
    )
    equipe_marketing_file = models.FileField(
        upload_to=upload_to_comercial, blank=True, null=True, verbose_name="Arquivo para 10.19"
    )

    # 10.20
    entrega_kits_rematricula = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.20 - Entrega às famílias kits de rematrícula homologados?"
    )
    entrega_kits_rematricula_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.20"
    )
    entrega_kits_rematricula_file = models.FileField(
        upload_to=upload_to_comercial, blank=True, null=True, verbose_name="Arquivo para 10.20"
    )

    # 10.21
    entrega_kits_visita = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.21 - Entrega às famílias visitantes kits de visita homologados?"
    )
    entrega_kits_visita_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.21"
    )
    entrega_kits_visita_file = models.FileField(
        upload_to=upload_to_comercial, blank=True, null=True, verbose_name="Arquivo para 10.21"
    )

    # 10.22
    leads_atraso_crm = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="10.22 - Menos de 10% dos leads em atraso no CRM?"
    )
    leads_atraso_crm_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 10.22"
    )
    leads_atraso_crm_file = models.FileField(
        upload_to=upload_to_comercial, blank=True, null=True, verbose_name="Arquivo para 10.22"
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
        choices=CHOICES, blank=True, null=True, verbose_name="11.01 - A escola mede a taxa de retenção (rematrícula) e a taxa de rotatividade (desistência) dos alunos?"
    )
    taxa_retenção_rotatividade_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 11.01"
    )
    taxa_retenção_rotatividade_file = models.FileField(
        upload_to=upload_to_resultado,
        blank=True, null=True,
        verbose_name="Arquivo para 11.01",
    )

    # 11.02
    meta_rematricula_carta = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="11.02 - Atingiu a meta de rematricula definida em carta meta?"
    )
    meta_rematricula_carta_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 11.02"
    )
    meta_rematricula_carta_file = models.FileField(
        upload_to=upload_to_resultado,
        blank=True, null=True,
        verbose_name="Arquivo para 11.02",
    )

    # 11.03
    meta_matricula_carta = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="11.03 - Atingiu a meta de matrícula definida em carta meta?"
    )
    meta_matricula_carta_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 11.03"
    )
    meta_matricula_carta_file = models.FileField(
        upload_to=upload_to_resultado,
        blank=True, null=True,
        verbose_name="Arquivo para 11.03",
    )

    # 11.04
    compras_slm_conjuntas = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="11.04 - As compras de SLM ocorreram de forma conjunta com as matrículas e rematrículas em pelo menos 70% dos casos?"
    )
    compras_slm_conjuntas_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 11.04"
    )
    compras_slm_conjuntas_file = models.FileField(
        upload_to=upload_to_resultado,
        blank=True, null=True,
        verbose_name="Arquivo para 11.04",
    )

    # 11.05
    resultado_financeiro_bp = models.IntegerField(
        choices=CHOICES, blank=True, null=True, verbose_name="11.05 - A Escola atingiu o resultado financeiro de receita e lucratividade de acordo com o BP planejado?"
    )
    resultado_financeiro_bp_comment = models.TextField(
        blank=True, null=True, verbose_name="Comentário para 11.05"
    )
    resultado_financeiro_bp_file = models.FileField(
        upload_to=upload_to_resultado,
        blank=True,
        null=True,
        verbose_name="Arquivo para 11.05",
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
    