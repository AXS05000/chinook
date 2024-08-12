from django.views.generic import TemplateView, CreateView, UpdateView
from .forms import AdministrativoForm, ComercialForm
from .models import Administrativo, Comercial
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404

class HomeGlex(TemplateView):
    template_name = "glex/home_glex.html"


class Glex(TemplateView):
    template_name = "glex/glex.html"

class TabelaFormsGlex(LoginRequiredMixin, TemplateView):
    template_name = "glex/tabela_forms_glex.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            administrativo_form = Administrativo.objects.get(usuario_modificacao=self.request.user)
            
            # Verificar se o formulário está completo
            is_complete = all([
                administrativo_form.lideranca_equipe,
                administrativo_form.reunioes_comerciais,
                administrativo_form.uniformes_crachas,
                administrativo_form.pagamento_boletos,
                administrativo_form.conta_bancaria_pj,
                administrativo_form.fluxo_caixa,
                administrativo_form.inadimplencia,
                administrativo_form.controle_balanco,
                administrativo_form.planejamento_orcamento,
                administrativo_form.orcamento_compartilhado,
            ])
            
            # Adicionando `is_complete` ao contexto
            context['administrativo_form'] = administrativo_form
            context['administrativo_form_is_complete'] = is_complete
            
            # Aqui você pode calcular a pontuação (score)
            score = sum(1 for field in [
                administrativo_form.lideranca_equipe,
                administrativo_form.reunioes_comerciais,
                administrativo_form.uniformes_crachas,
                administrativo_form.pagamento_boletos,
                administrativo_form.conta_bancaria_pj,
                administrativo_form.fluxo_caixa,
                administrativo_form.inadimplencia,
                administrativo_form.controle_balanco,
                administrativo_form.planejamento_orcamento,
                administrativo_form.orcamento_compartilhado,
            ] if field)
            
            # Adicionando `score` ao contexto
            context['administrativo_form_score'] = score

        except Administrativo.DoesNotExist:
            context['administrativo_form'] = None
            context['administrativo_form_is_complete'] = False
            context['administrativo_form_score'] = 0
            
        return context


class AdministrativoCreateView(LoginRequiredMixin, CreateView):
    model = Administrativo
    form_class = AdministrativoForm
    template_name = "glex/adm-form.html"
    success_url = reverse_lazy("table_forms_glex")

    def form_valid(self, form):
        form.instance.usuario_modificacao = self.request.user
        return super().form_valid(form)

class AdministrativoUpdateView(LoginRequiredMixin, UpdateView):
    model = Administrativo
    form_class = AdministrativoForm
    template_name = "glex/adm-form-edit.html"
    success_url = reverse_lazy("table_forms_glex")

    def get_object(self, queryset=None):
        return get_object_or_404(Administrativo, usuario_modificacao=self.request.user)

    def form_valid(self, form):
        form.instance.usuario_modificacao = self.request.user
        return super().form_valid(form)


class ComercialCreateView(CreateView):
    model = Comercial
    form_class = ComercialForm
    template_name = "glex/formulario2.html"
    success_url = reverse_lazy("comercial_form")
