from django.urls import path
from .views import (
    HomeGlex,
    Glex,
    TabelaFormsGlex,
    AdministrativoCreateView,
    AdministrativoUpdateView,
    ComercialCreateView,
    ComercialUpdateView,
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
    path("glex_comercial/editar/", ComercialUpdateView.as_view(), name="comercial_form_edit"),
]
