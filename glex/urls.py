from django.urls import path
from .views import (
    HomeGlex,
    Glex,
    TabelaFormsGlex,
    AdministrativoCreateView,
    ComercialCreateView,
)

urlpatterns = [
    path("home_glex", HomeGlex.as_view(), name="home_glex"),
    path("glex", Glex.as_view(), name="glex"),
    path("tabel_forms_glex", TabelaFormsGlex.as_view(), name="table_forms_glex"),
    path(
        "administrativo/",
        AdministrativoCreateView.as_view(),
        name="administrativo_form",
    ),
    path("comercial/", ComercialCreateView.as_view(), name="comercial_form"),
]
