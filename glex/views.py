from django.views.generic import TemplateView


class HomeGlex(TemplateView):
    template_name = "glex/home_glex.html"


class Glex(TemplateView):
    template_name = "glex/glex.html"


class TabelaFormsGlex(TemplateView):
    template_name = "glex/tabel_forms_glex.html"
