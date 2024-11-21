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


EXPECTATION_CHOICES = [
    (1, '1 - Below Expectations'),
    (2, '2 - Approaching Expectations'),
    (3, '3 - Meeting Expectations'),
    (4, '4 - Exceeding Expectations'),
]

class Dominio1(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="dominio1",
        verbose_name="Nome da Escola"
    )
    
    # Campos com Choices Reutilizáveis
    program_implementation = models.IntegerField(choices=EXPECTATION_CHOICES, verbose_name="Program Implementation")
    program_implementation_pdf = models.FileField(upload_to='pdfs/dominio1/', blank=True, null=True, verbose_name="Program Implementation (PDF)")

    staffing_instructional_program = models.IntegerField(choices=EXPECTATION_CHOICES, verbose_name="Staffing the Instructional Program")
    staffing_instructional_program_pdf = models.FileField(upload_to='pdfs/dominio1/', blank=True, null=True, verbose_name="Staffing the Instructional Program (PDF)")

    resource_allocation = models.IntegerField(choices=EXPECTATION_CHOICES, verbose_name="Resource Allocation")
    resource_allocation_pdf = models.FileField(upload_to='pdfs/dominio1/', blank=True, null=True, verbose_name="Resource Allocation (PDF)")

    implementation_supervision_instructional_program = models.IntegerField(choices=EXPECTATION_CHOICES, verbose_name="Implementation and Supervision of the Instructional Program")
    implementation_supervision_instructional_program_pdf = models.FileField(upload_to='pdfs/dominio1/', blank=True, null=True, verbose_name="Implementation and Supervision (PDF)")

    professional_learning_opportunities = models.IntegerField(choices=EXPECTATION_CHOICES, verbose_name="Professional Learning Opportunities")
    professional_learning_opportunities_pdf = models.FileField(upload_to='pdfs/dominio1/', blank=True, null=True, verbose_name="Professional Learning Opportunities (PDF)")

    commitment_to_bilingual_education = models.IntegerField(choices=EXPECTATION_CHOICES, verbose_name="Commitment to Bilingual Education")
    commitment_to_bilingual_education_pdf = models.FileField(upload_to='pdfs/dominio1/', blank=True, null=True, verbose_name="Commitment to Bilingual Education (PDF)")

    strategic_planning = models.IntegerField(choices=EXPECTATION_CHOICES, verbose_name="Strategic Planning")
    strategic_planning_pdf = models.FileField(upload_to='pdfs/dominio1/', blank=True, null=True, verbose_name="Strategic Planning (PDF)")

    def __str__(self):
        return f"{self.escola} - Dominio1"
