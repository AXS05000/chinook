from django.db import models


class Administrativo(models.Model):
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


class Comercial(models.Model):
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
