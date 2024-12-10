from django.contrib import admin
from .models import (
    Base_de_Conhecimento_Geral,
    GlexGestaoDeParceria,
    GlexGente,
    GlexAdministrativo,
    GlexTecnologia,
    GlexMarketing,
    GlexAcademico,
    GlexGestaoEscolar,
    GlexOperacaoAcademica,
    GlexImplantacao,
    GlexComercial,
    GlexResultado,
    Dominio1,
    Dominio2,
    Dominio3,
    Dominio4,
)


admin.site.register(Base_de_Conhecimento_Geral)
admin.site.register(GlexGestaoDeParceria)
