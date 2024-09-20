from django.contrib import admin

from .models import (
    Informacao,
    APIKey,
    Beneficio,
    FolhaPonto,
    Salario,
    Ferias,
    CRM_FUI,
    Respostas_NPS,
    Vendas_SLM_2024,
    Ticket_Sprinklr,
    Vendas_SLM_2025,
    Base_de_Conhecimento,
    Planificador_2024,
    Avaliacao_Cliente_Oculto_24,
    Resumo_Respostas_NPS,
    PedidosAlterados,
    HistoricoAlteracoes,
    Visita_Escola,
    Resumo_Visita_Escola,
    ResumoAlteracoes_Planificador,
)

# Register your models here.
admin.site.register(Resumo_Visita_Escola)
admin.site.register(ResumoAlteracoes_Planificador)
admin.site.register(Informacao)
admin.site.register(HistoricoAlteracoes)
admin.site.register(PedidosAlterados)
admin.site.register(Ticket_Sprinklr)
admin.site.register(Visita_Escola)
admin.site.register(APIKey)
admin.site.register(Beneficio)
admin.site.register(FolhaPonto)
admin.site.register(Salario)
admin.site.register(Ferias)
admin.site.register(CRM_FUI)
admin.site.register(Respostas_NPS)
admin.site.register(Vendas_SLM_2024)
admin.site.register(Vendas_SLM_2025)
admin.site.register(Base_de_Conhecimento)
admin.site.register(Planificador_2024)
admin.site.register(Resumo_Respostas_NPS)


@admin.register(Avaliacao_Cliente_Oculto_24)
class AvaliacaoClienteOculto24Admin(admin.ModelAdmin):
    # Define quais campos podem ser pesquisados dentro da tabela
    search_fields = ['escola__nome_da_escola', 'categoria', 'pergunta', 'resposta']
    # Define quais colunas serão exibidas na listagem do admin
    list_display = ['escola', 'categoria', 'pergunta', 'resposta']