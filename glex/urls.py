from django.urls import path
from .views import (
    HomeGlex,
    Glex,
    TabelaFormsGlex,
    AdministrativoCreateView,
    AdministrativoUpdateView,
    ComercialCreateView,
    ComercialUpdateView,
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
]
