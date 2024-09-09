from django.db import models
from usuarios.models import CustomUsuario

class Informacao(models.Model):
    nome = models.CharField(max_length=100)
    persona = models.CharField(max_length=100)
    data_resposta = models.DateField()
    unidade = models.CharField(max_length=100)
    questao = models.TextField()
    resposta = models.IntegerField()
    comentario = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} ({self.persona}): {self.questao[:50]}"


class APIKey(models.Model):
    name = models.CharField(max_length=255)
    key = models.CharField(max_length=255)

    def __str__(self):
        return self.name





########################################################################################################


class Beneficio(models.Model):
    descricao = models.TextField()

    def __str__(self):
        return "Informações sobre Benefícios"


class FolhaPonto(models.Model):
    descricao = models.TextField()

    def __str__(self):
        return "Informações sobre Folha de Ponto"


class Salario(models.Model):
    descricao = models.TextField()

    def __str__(self):
        return "Informações sobre Salário"


class Ferias(models.Model):
    descricao = models.TextField()

    def __str__(self):
        return "Informações sobre Férias"


########################################################################################################


class CRM_FUI(models.Model):

    id_escola = models.IntegerField(primary_key=True, verbose_name="Id Escola")
    nome_da_escola = models.CharField(
        max_length=100, verbose_name="Nome da Escola", null=True, blank=True
    )
    CNPJ = models.CharField(max_length=18, verbose_name="CNPJ", null=True, blank=True)
    status_da_escola = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        verbose_name="Status da Escola",
    )
    slms_vendidos = models.IntegerField(
        null=True, blank=True, verbose_name="SLM Vendidos 2024"
    )
    slms_vendidos_25 = models.IntegerField(
        null=True, blank=True, verbose_name="SLM Vendidos 2025"
    )
    meta = models.IntegerField(null=True, blank=True, verbose_name="Meta 2024")
    meta_adiantamento_24_25 = models.IntegerField(null=True, blank=True, verbose_name="Meta Adiantamento 2024/2025")
    cluster = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Cluster"
    )
    endereco = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Endereço Escola"
    )
    cep_escola = models.CharField(
        max_length=10, null=True, blank=True, verbose_name="CEP Escola"
    )
    complemento_escola = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Complemento Escola"
    )
    bairro_escola = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Bairro Escola"
    )
    cidade_da_escola = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Cidade Escola"
    )
    estado_da_escola = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="Estado da Escola"
    )
    regiao_da_escola = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Região da Escola"
    )
    telefone_de_contato_da_escola = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="Telefone da Escola"
    )
    email_da_escola = models.EmailField(
        null=True, blank=True, verbose_name="E-mail da Escola"
    )
    segmento_da_escola = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Segmento"
    )
    atual_serie = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Atual Série"
    )
    avanco_segmento = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Avanço Segmento"
    )
    status_de_adimplencia = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Status de Adimplêcia/Inadimplência",
    )
    ticket_medio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Ticket Medio",
    )
    inadimplencia = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Total do Valor de Inadimplência",
    )
    valor_royalties = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Total do Valor dos Royalties",
    )
    valor_fdmp = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Total do Valor FDMP",
    )
    nps_pais_2024_1_onda = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="NPS Pais 2024 - 1° Onda",
    )
    cliente_oculto_2024 = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Cliente Oculto 2024",
    )
    quality_assurance_2024 = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        verbose_name="Quality Assurance 2024",
    )
    consultor_comercial = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Consultor Comercial"
    )
    consultor_gestao_escolar = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Consultor Gestão Escolar"
    )
    consultor_saf = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Consultor SAF"
    )
    consultor_academico = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Consultor Acadêmico"
    )
    dias_uteis_entrega_slm = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Dias Úteis para entrega do SLM"
    )

    def __str__(self):

        return f"{self.id_escola} - {self.nome_da_escola}"



class Visita_Escola(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="nome_escola_comentario_visista",
        verbose_name="Nome da Escola Comentario Visita",
    )
    comentario_visita = models.TextField()

    def __str__(self):
        return f"{self.escola} - {self.comentario_visita}"

class Resumo_Visita_Escola(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="resumos_visita_escola",
        verbose_name="Nome da Escola Visita"
    )
    visita = models.ForeignKey(
        Visita_Escola,
        on_delete=models.CASCADE,
        related_name="resumos_visita",
        verbose_name="Visita Escola"
    )
    resumo = models.TextField(blank=True, null=True, verbose_name="Resumo da Visita")

    def __str__(self):
        return f"Resumo da visita: {self.escola} - ID Visita: {self.visita.id}"

class Respostas_NPS(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="nome_escola",
        verbose_name="Nome da Escola",
    )
    nome = models.CharField(verbose_name="Nome", max_length=200)
    data_da_resposta = models.DateField(verbose_name="Data da Resposta")
    questao = models.TextField(verbose_name="Questão")
    nota = models.IntegerField(verbose_name="Nota")
    comentario = models.TextField(blank=True, null=True, verbose_name="Comentário")

    def __str__(self):
        return f"{self.nome} - {self.data_da_resposta}"
    
class Resumo_Respostas_NPS(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="nome_escola_resumo_nps",
        verbose_name="Nome da Escola do NPS",
    )
    resumo = models.TextField(blank=True, null=True, verbose_name="Resumo")

    def __str__(self):
        return f"{self.escola}"

class Avaliacao_Cliente_Oculto_24(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="nome_escola_co24",
        verbose_name="Nome da Escola Cliente Oculto 24",
    )
    categoria = models.TextField(verbose_name="Categoria CO24")
    pergunta = models.TextField(verbose_name="Pergunta CO24")
    resposta = models.TextField(blank=True, null=True, verbose_name="Comentário Cliente Oculto 24")

    def __str__(self):
        return f"{self.escola} - Avaliação Cliente Oculto 2024"
    
class Resumo_Respostas_ClienteOculto24(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="nome_escola_resumo_co24",
        verbose_name="Nome da Escola do resumo do Cliente Oculto 2024",
    )
    resumo = models.TextField(blank=True, null=True, verbose_name="Resumo Cliente Oculto")

    def __str__(self):
        return f"{self.escola}"


class Vendas_SLM_2024(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="nome_escola_venda_slm_2024",
        verbose_name="Nome da Escola Venda 2024",
    )
    data_do_pedido = models.DateField(verbose_name="Data do Pedido")
    quantidade = models.IntegerField(verbose_name="Quantidade Vendida")
    nome_pais = models.CharField(verbose_name="Nomes dos Pais", max_length=200)
    nome_do_aluno = models.CharField(verbose_name="Nome do Aluno", max_length=200)
    numero_do_pedido = models.CharField(verbose_name="Numero do Pedido", max_length=200)
    id_linha = models.BigIntegerField(verbose_name="Id da Linha 2024", blank=True, null=True)


    def __str__(self):
        return f"{self.numero_do_pedido} - {self.nome_pais} - {self.nome_do_aluno} - SLM 2024"
    
class Vendas_SLM_2025(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="nome_escola_venda_slm_2025",
        verbose_name="Nome da Escola Venda 2025",
    )
    data_do_pedido = models.DateField(verbose_name="Data do Pedido 2025")
    quantidade = models.IntegerField(verbose_name="Quantidade Vendida 2025")
    nome_pais = models.CharField(verbose_name="Nomes dos Pais 2025", max_length=200)
    nome_do_aluno = models.CharField(verbose_name="Nome do Aluno 2025", max_length=200)
    numero_do_pedido = models.CharField(verbose_name="Numero do Pedido 2025", max_length=200)
    id_linha = models.BigIntegerField(verbose_name="Id da Linha 2025", blank=True, null=True)

    def __str__(self):
        return f"{self.numero_do_pedido} - {self.nome_pais} - {self.nome_do_aluno} - SLM 2025"



class Base_de_Conhecimento(models.Model):
    titulo = models.CharField(blank=True, null=True, verbose_name="Título", max_length=200)
    assunto = models.CharField(blank=True, null=True, verbose_name="Assunto", max_length=200)
    sub_assunto = models.CharField(blank=True, null=True, verbose_name="Sub Assunto", max_length=200)
    texto = models.TextField(blank=True, null=True, verbose_name="Texto")

    def __str__(self):
        return f"{self.titulo} - {self.assunto} - {self.sub_assunto}"
    



class PedidosAlterados(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="pedidos_alterados",
        verbose_name="Escola"
    )
    nome_do_aluno = models.CharField(max_length=255, null=True, blank=True, verbose_name="Nome do Aluno")
    numero_do_pedido = models.CharField(max_length=50, null=True, blank=True, verbose_name="Número do Pedido")
    motivo = models.CharField(max_length=255, null=True, blank=True, verbose_name="Motivo")
    alterado_por = models.CharField(max_length=100, verbose_name="Alterado Por", null=True, blank=True)

    def __str__(self):
        return f"{self.nome_do_aluno} - {self.numero_do_pedido}"


class Ticket_Sprinklr(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="nome_escola_sprinklr",
        verbose_name="Nome da Escola da Sprinklr",
    )
    id_ticket = models.IntegerField()
    cliente = models.CharField(max_length=255)
    assunto = models.CharField(max_length=255,blank=True, null=True)
    data_ticket = models.DateField()

    def __str__(self):
        return f"{self.escola} - {self.id_ticket}"
    





################################## PLANIFICADOR ###############################################

class Planificador_2024(models.Model):
    
    SIM_NAO_CHOICES = [
        ('SIM', 'Sim'),
        ('NAO', 'Não'),
    ]
    usuario_modificacao = models.ForeignKey(
        CustomUsuario, on_delete=models.SET_NULL, null=True, blank=True
    )
    escola = models.ForeignKey(
            CRM_FUI,
            on_delete=models.CASCADE,
            related_name="nome_escola_planificador",
            verbose_name="Nome da Escola Planificador",
            null=True, blank=True
        )
    ultima_data_atualizacao_bloc_drivers_comerciais_estrategicos = models.DateField(null=True, blank=True)
    crm_b2c = models.CharField(max_length=3, choices=SIM_NAO_CHOICES, default='NAO')
    data_abertura_matricula_2025 = models.DateField(null=True, blank=True)
    circular_oferta_2025_publicado = models.CharField(max_length=3, choices=SIM_NAO_CHOICES, default='NAO')
    data_de_abertura_da_circular_2025 = models.DateField(null=True, blank=True)
    toddle = models.CharField(max_length=3, choices=SIM_NAO_CHOICES, default='NAO')
    toddle_planejamento = models.CharField(max_length=255, null=True, blank=True)
    toddle_portfolio = models.CharField(max_length=255, null=True, blank=True)
    arvore = models.CharField(max_length=3, choices=SIM_NAO_CHOICES, default='NAO')
    data_implementacao_arvore = models.DateField(null=True, blank=True)
    ultima_data_atualizacao_bloc_funil_comercial = models.DateField(null=True, blank=True)
    leads_central_ago_24 = models.IntegerField(null=True, blank=True)
    leads_escolas_ago_24 = models.IntegerField(null=True, blank=True)
    visitas_ago_24 = models.IntegerField(null=True, blank=True)
    taxa_conversao_atual_leads_visitas = models.FloatField(null=True, blank=True)
    matriculas_ago_24 = models.IntegerField(null=True, blank=True)
    taxa_conversao_atual_visitas_matriculas = models.FloatField(null=True, blank=True)
    taxa_conversao_leads_matriculas = models.FloatField(null=True, blank=True)
    ultima_data_atualizacao_bloc_drivers_comerciais_meio = models.DateField(null=True, blank=True)
    meta_alunos_5k_2024 = models.IntegerField(null=True, blank=True)
    setup_plano_comercial_segundo_semestre = models.CharField(max_length=3, choices=SIM_NAO_CHOICES, default='NAO')
    acao_1_elegivel_trade_marketing = models.CharField(max_length=3, choices=SIM_NAO_CHOICES, default='NAO')
    acao_1_trade_valor = models.FloatField(null=True, blank=True)
    acao_1_trade_marketing_acoes_alinhadas = models.CharField(max_length=255, null=True, blank=True)
    acao_2_experience_day_10_08_24 = models.CharField(max_length=3, choices=SIM_NAO_CHOICES, default='NAO')
    acao_2_experience_day_24_08_24 = models.CharField(max_length=3, choices=SIM_NAO_CHOICES, default='NAO')
    acao_2_experience_day_21_09_24 = models.CharField(max_length=3, choices=SIM_NAO_CHOICES, default='NAO')
    acao_2_experience_day_26_10_24 = models.CharField(max_length=3, choices=SIM_NAO_CHOICES, default='NAO')
    acao_2_experience_day_09_11_24 = models.CharField(max_length=3, choices=SIM_NAO_CHOICES, default='NAO')
    acao_3_friend_get_friend = models.CharField(max_length=3, choices=SIM_NAO_CHOICES, default='NAO')
    acao_4_webinars_com_autoridades_pre = models.CharField(max_length=3, choices=SIM_NAO_CHOICES, default='NAO')
    acao_4_webinars_com_autoridades_pos = models.CharField(max_length=3, choices=SIM_NAO_CHOICES, default='NAO')
    piloto_welcome_baby_bear = models.CharField(max_length=3, choices=SIM_NAO_CHOICES, default='NAO')
    acao_5_sdr_taxa_conversao_validacao_lead = models.FloatField(null=True, blank=True)
    acao_5_sdr_taxa_conversao_visitas = models.FloatField(null=True, blank=True)
    acao_6_alinhado_resgate_leads = models.CharField(max_length=3, choices=SIM_NAO_CHOICES, default='NAO')
    acao_6_quantidade_leads_resgatados = models.IntegerField(null=True, blank=True)
    acao_6_todos_leads_resgatados_contatados = models.CharField(max_length=3, choices=SIM_NAO_CHOICES, default='NAO')
    data_atualizacao_resultados = models.DateField(null=True, blank=True)
    slm_2022 = models.FloatField(null=True, blank=True)
    slm_2023 = models.FloatField(null=True, blank=True)
    meta_orcamentaria_2024 = models.FloatField(null=True, blank=True)
    base_rematriculaveis_2025 = models.IntegerField(null=True, blank=True)
    meta_rematricula_2025 = models.IntegerField(null=True, blank=True)
    real_rematriculas_2025 = models.IntegerField(null=True, blank=True)
    atingimento_rematriculas_2025 = models.FloatField(null=True, blank=True)
    meta_matricula_2025 = models.IntegerField(null=True, blank=True)
    real_matricula_2025 = models.IntegerField(null=True, blank=True)
    atingimento_matriculas_2025 = models.FloatField(null=True, blank=True)
    total_meta_alunos_2025 = models.IntegerField(null=True, blank=True)
    total_real_alunos_2025 = models.IntegerField(null=True, blank=True)
    atingimento_real_alunos_2025 = models.FloatField(null=True, blank=True)
    correlacao_alunos_slms_2025 = models.FloatField(null=True, blank=True)
    mc_2025 = models.FloatField(null=True, blank=True)
    slms_2025_m = models.FloatField(null=True, blank=True)
    pedidos_represados_logistica_2025 = models.IntegerField(null=True, blank=True)
    pedidos_faturados = models.IntegerField(null=True, blank=True)
    pedidos_entregues = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Dados Comerciais {self.escola}"

