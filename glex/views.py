from django.views.generic import TemplateView, CreateView
from .forms import AdministrativoForm, ComercialForm
from .models import Administrativo, Comercial
from django.urls import reverse_lazy


class HomeGlex(TemplateView):
    template_name = "glex/home_glex.html"


class Glex(TemplateView):
    template_name = "glex/glex.html"


class TabelaFormsGlex(TemplateView):
    template_name = "glex/tabel_forms_glex.html"


class AdministrativoCreateView(CreateView):
    model = Administrativo
    form_class = AdministrativoForm
    template_name = "formulario.html"
    success_url = reverse_lazy("administrativo_form")


class ComercialCreateView(CreateView):
    model = Comercial
    form_class = ComercialForm
    template_name = "formulario.html"
    success_url = reverse_lazy("comercial_form")
