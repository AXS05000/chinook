from django.contrib import admin

# Register your models here.
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
    Base_de_Conhecimento,
)

admin.site.register(Informacao)
admin.site.register(APIKey)
admin.site.register(Beneficio)
admin.site.register(FolhaPonto)
admin.site.register(Salario)
admin.site.register(Ferias)
admin.site.register(CRM_FUI)
admin.site.register(Respostas_NPS)
admin.site.register(Vendas_SLM_2024)
admin.site.register(Base_de_Conhecimento)
