from django.urls import path
from .views import (
    HomeGlex,
    Glex,
    TabelaFormsGlex,
    AdministrativoCreateView,
    AdministrativoUpdateView,
    ComercialCreateView,
    ComercialUpdateView,
    Dominio1CreateView,
    Dominio2CreateView,
    Dominio3CreateView,
    Dominio4CreateView,
    TabelaQAView,
    BuscarEscolaView,
)

urlpatterns = [
    path("home_glex", HomeGlex.as_view(), name="home_glex"),
    path("glex", Glex.as_view(), name="glex"),
    path("tabel_forms_glex", TabelaFormsGlex.as_view(), name="table_forms_glex"),
    path(
        "glex_administrativo/",
        AdministrativoCreateView.as_view(),
        name="administrativo_form",
    ),
    path(
        "glex_administrativo/editar/",
        AdministrativoUpdateView.as_view(),
        name="administrativo_form_edit",
    ),
    path("glex_comercial/", ComercialCreateView.as_view(), name="comercial_form"),
    path(
        "glex_comercial/editar/",
        ComercialUpdateView.as_view(),
        name="comercial_form_edit",
    ),
    path("dominio1/create/", Dominio1CreateView.as_view(), name="dominio1_create"),
    path("dominio2/create/", Dominio2CreateView.as_view(), name="dominio2_create"),
    path("dominio3/create/", Dominio3CreateView.as_view(), name="dominio3_create"),
    path("dominio4/create/", Dominio4CreateView.as_view(), name="dominio4_create"),
    path("tabela_qa/<int:escola_id>/", TabelaQAView.as_view(), name="tabela_qa"),
    path("buscar_escola/", BuscarEscolaView.as_view(), name="buscar_escola"),
]
