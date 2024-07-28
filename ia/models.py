from django.db import models


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
        null=True, blank=True, verbose_name="SLM Vendidos"
    )
    alunos = models.IntegerField(null=True, blank=True, verbose_name="Alunos")
    meta = models.IntegerField(null=True, blank=True, verbose_name="Meta")
    cluster = models.CharField(
        max_length=100, null=True, blank=True, verbose_name="Cluster"
    )
    endereco = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Endereço Escola"
    )
    cep_escola = models.CharField(
        max_length=10, null=True, blank=True, verbose_name="CEP Escola"
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
        max_length=100, null=True, blank=True, verbose_name="Consultor Gestão Escoalr"
    )

    def __str__(self):

        return f"{self.id_escola} - {self.nome_da_escola}"


class Respostas_NPS(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="nome_escola",
        verbose_name="Nome da Escola",
    )
    nome = models.CharField(verbose_name="Nome")
    data_da_resposta = models.DateField(verbose_name="Data da Resposta")
    questao = models.TextField(verbose_name="Questão")
    nota = models.IntegerField(verbose_name="Nota")
    comentario = models.TextField(blank=True, null=True, verbose_name="Comentário")

    def __str__(self):
        return f"{self.nome} - {self.data_da_resposta}"


class Vendas_SLM_2024(models.Model):
    escola = models.ForeignKey(
        CRM_FUI,
        on_delete=models.CASCADE,
        related_name="nome_escola_venda_slm_2024",
        verbose_name="Nome da Escola Venda 2024",
    )
    data_do_pedido = models.DateField(verbose_name="Data do Pedido")
    quantidade = models.IntegerField(verbose_name="Quantidade Vendida")
    nome_pais = models.CharField(verbose_name="Nomes dos Pais")
    nome_do_aluno = models.CharField(verbose_name="Nome do Aluno")
    numero_do_pedido = models.CharField(verbose_name="Numero do Pedido")

    def __str__(self):
        return f"{self.numero_do_pedido} - {self.nome_pais} - {self.nome_do_aluno}"
