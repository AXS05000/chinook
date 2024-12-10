from django.urls import path
from .views import (
    Dominio1View,
    Dominio1UpdateView,
    Dominio2View,
    Dominio2UpdateView,
    Dominio3View,
    Dominio3UpdateView,
    Dominio4View,
    Dominio4UpdateView,
    TabelaQAView,
    BuscarEscolaView,
    BuscarEscolaGlexView,
    TabelaGlexView,
    GlexGestaoDeParceriaCreateView,
    GlexGestaoDeParceriaUpdateView,
    GlexGenteCreateView,
    GlexGenteUpdateView,
    GlexAdministrativoCreateView,
    GlexAdministrativoUpdateView,
    GlexTecnologiaCreateView,
    GlexTecnologiaUpdateView,
    GlexMarketingCreateView,
    GlexMarketingUpdateView,
    GlexAcademicoCreateView,
    GlexAcademicoUpdateView,
    GlexGestaoEscolarCreateView,
    GlexGestaoEscolarUpdateView,
    GlexOperacaoAcademicaCreateView,
    GlexOperacaoAcademicaUpdateView,
    GlexImplantacaoCreateView,
    GlexImplantacaoUpdateView,
    GlexComercialCreateView,
    GlexComercialUpdateView,
    GlexResultadoCreateView,
    GlexResultadoUpdateView,
)

from .import_html import upload_html_view

urlpatterns = [
    path("dominio1/create/", Dominio1View.as_view(), name="dominio1_create"),
    path(
        "dominio1/update/<int:pk>/",
        Dominio1UpdateView.as_view(),
        name="dominio1_update",
    ),
    path("dominio2/create/", Dominio2View.as_view(), name="dominio2_create"),
    path(
        "dominio2/update/<int:pk>/",
        Dominio2UpdateView.as_view(),
        name="dominio2_update",
    ),
    path("dominio3/create/", Dominio3View.as_view(), name="dominio3_create"),
    path(
        "dominio3/update/<int:pk>/",
        Dominio3UpdateView.as_view(),
        name="dominio3_update",
    ),
    path("dominio4/create/", Dominio4View.as_view(), name="dominio4_create"),
    path(
        "dominio4/update/<int:pk>/",
        Dominio4UpdateView.as_view(),
        name="dominio4_update",
    ),
    path("tabela_qa/<int:escola_id>/", TabelaQAView.as_view(), name="tabela_qa"),
    path("buscar_escola/", BuscarEscolaView.as_view(), name="buscar_escola"),
    path('upload-html/', upload_html_view, name='upload_html'),




    path("glex-2025/", BuscarEscolaGlexView.as_view(), name="glex_2025"),
    path("tabela_glex/<int:escola_id>/", TabelaGlexView.as_view(), name="tabela_glex"),
    path(
        "glex-gestao-de-parceria/create/",
        GlexGestaoDeParceriaCreateView.as_view(),
        name="glex_gestao_de_parceria_create",
    ),
    path(
        "glex-gestao-de-parceria/update/<int:pk>/",
        GlexGestaoDeParceriaUpdateView.as_view(),
        name="glex_gestao_de_parceria_update",
    ),
    # GlexGente
    path("glex-gente/create/", GlexGenteCreateView.as_view(), name="glex_gente_create"),
    path("glex-gente/update/<int:pk>/", GlexGenteUpdateView.as_view(), name="glex_gente_update"),
    # GlexAdministrativo
    path(
        "glex-administrativo/create/",
        GlexAdministrativoCreateView.as_view(),
        name="glex_administrativo_create",
    ),
    path(
        "glex-administrativo/update/<int:pk>/",
        GlexAdministrativoUpdateView.as_view(),
        name="glex_administrativo_update",
    ),
    # GlexTecnologia
    path(
        "glex-tecnologia/create/",
        GlexTecnologiaCreateView.as_view(),
        name="glex_tecnologia_create",
    ),
    path(
        "glex-tecnologia/update/<int:pk>/",
        GlexTecnologiaUpdateView.as_view(),
        name="glex_tecnologia_update",
    ),
    # GlexMarketing
    path(
        "glex-marketing/create/",
        GlexMarketingCreateView.as_view(),
        name="glex_marketing_create",
    ),
    path(
        "glex-marketing/update/<int:pk>/",
        GlexMarketingUpdateView.as_view(),
        name="glex_marketing_update",
    ),
    # GlexAcademico
    path(
        "glex-academico/create/",
        GlexAcademicoCreateView.as_view(),
        name="glex_academico_create",
    ),
    path(
        "glex-academico/update/<int:pk>/",
        GlexAcademicoUpdateView.as_view(),
        name="glex_academico_update",
    ),
    # GlexGestaoEscolar
    path(
        "glex-gestao-escolar/create/",
        GlexGestaoEscolarCreateView.as_view(),
        name="glex_gestao_escolar_create",
    ),
    path(
        "glex-gestao-escolar/update/<int:pk>/",
        GlexGestaoEscolarUpdateView.as_view(),
        name="glex_gestao_escolar_update",
    ),
    # GlexOperacaoAcademica
    path(
        "glex-operacao-academica/create/",
        GlexOperacaoAcademicaCreateView.as_view(),
        name="glex_operacao_academica_create",
    ),
    path(
        "glex-operacao-academica/update/<int:pk>/",
        GlexOperacaoAcademicaUpdateView.as_view(),
        name="glex_operacao_academica_update",
    ),
    # GlexImplantacao
    path(
        "glex-implantacao/create/",
        GlexImplantacaoCreateView.as_view(),
        name="glex_implantacao_create",
    ),
    path(
        "glex-implantacao/update/<int:pk>/",
        GlexImplantacaoUpdateView.as_view(),
        name="glex_implantacao_update",
    ),
    # GlexComercial
    path(
        "glex-comercial/create/",
        GlexComercialCreateView.as_view(),
        name="glex_comercial_create",
    ),
    path(
        "glex-comercial/update/<int:pk>/",
        GlexComercialUpdateView.as_view(),
        name="glex_comercial_update",
    ),
    # GlexResultado
    path(
        "glex-resultado/create/",
        GlexResultadoCreateView.as_view(),
        name="glex_resultado_create",
    ),
    path(
        "glex-resultado/update/<int:pk>/",
        GlexResultadoUpdateView.as_view(),
        name="glex_resultado_update",
    ),


]



# urlpatterns = [
#     path("home_glex", HomeGlex.as_view(), name="home_glex"),
#     path("glex", Glex.as_view(), name="glex"),
#     path("tabel_forms_glex", TabelaFormsGlex.as_view(), name="table_forms_glex"),
#     path(
#         "glex_administrativo/",
#         AdministrativoCreateView.as_view(),
#         name="administrativo_form",
#     ),
#     path(
#         "glex_administrativo/editar/",
#         AdministrativoUpdateView.as_view(),
#         name="administrativo_form_edit",
#     ),
# ]
