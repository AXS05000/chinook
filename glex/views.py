from django.views.generic import TemplateView, CreateView, UpdateView
from .forms import (
    AdministrativoForm,
    ComercialForm,
    Dominio1Form,
    Dominio2Form,
    Dominio3Form,
    Dominio4Form,
)
from django.utils.html import strip_tags
from .models import Administrativo, Comercial, Dominio1, Dominio2, Dominio3, Dominio4
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages


class HomeGlex(TemplateView):
    template_name = "glex/home_glex.html"


class Glex(TemplateView):
    template_name = "glex/glex.html"


class TabelaFormsGlex(LoginRequiredMixin, TemplateView):
    template_name = "glex/tabela_forms_glex.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Lógica para Administrativo
        try:
            administrativo_form = Administrativo.objects.get(
                usuario_modificacao=self.request.user
            )
            is_complete_adm = all(
                [
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
                ]
            )
            context["administrativo_form"] = administrativo_form
            context["administrativo_form_is_complete"] = is_complete_adm
            context["administrativo_form_score"] = sum(
                1
                for field in [
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
                ]
                if field
            )
        except Administrativo.DoesNotExist:
            context["administrativo_form"] = None
            context["administrativo_form_is_complete"] = False
            context["administrativo_form_score"] = 0

        # Lógica para Comercial
        try:
            comercial_form = Comercial.objects.get(
                usuario_modificacao=self.request.user
            )
            is_complete_com = all(
                [
                    comercial_form.cortesia_visitantes,
                    comercial_form.participacao_mentoria,
                    comercial_form.equipe_comercial_contratada,
                    comercial_form.trilha_treinamento,
                    comercial_form.participacao_encontros_lideres,
                    comercial_form.funil_vendas_crm,
                    comercial_form.pontuacao_cliente_oculto,
                    comercial_form.participacao_campanhas,
                    comercial_form.pesquisa_concorrentes,
                    comercial_form.conversao_leads,
                    comercial_form.politica_comissionamento,
                    comercial_form.orcamento_mkt,
                    comercial_form.profissional_mkt,
                    comercial_form.entrega_kit_rematricula,
                    comercial_form.entrega_kit_visita,
                    comercial_form.leads_atraso_crm,
                ]
            )
            context["comercial_form"] = comercial_form
            context["comercial_form_is_complete"] = is_complete_com
            context["comercial_form_score"] = sum(
                1
                for field in [
                    comercial_form.cortesia_visitantes,
                    comercial_form.participacao_mentoria,
                    comercial_form.equipe_comercial_contratada,
                    comercial_form.trilha_treinamento,
                    comercial_form.participacao_encontros_lideres,
                    comercial_form.funil_vendas_crm,
                    comercial_form.pontuacao_cliente_oculto,
                    comercial_form.participacao_campanhas,
                    comercial_form.pesquisa_concorrentes,
                    comercial_form.conversao_leads,
                    comercial_form.politica_comissionamento,
                    comercial_form.orcamento_mkt,
                    comercial_form.profissional_mkt,
                    comercial_form.entrega_kit_rematricula,
                    comercial_form.entrega_kit_visita,
                    comercial_form.leads_atraso_crm,
                ]
                if field
            )
        except Comercial.DoesNotExist:
            context["comercial_form"] = None
            context["comercial_form_is_complete"] = False
            context["comercial_form_score"] = 0

        # Calculando a pontuação geral
        context["pontuacao_geral"] = (
            context["administrativo_form_score"] + context["comercial_form_score"]
        )

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

        # Verifica se os campos de arquivo estão preenchidos antes de acessar suas propriedades
        for field in self.form_class.Meta.fields:
            file_field = form.cleaned_data.get(field)
            if file_field and hasattr(file_field, "name"):
                pass  # Aqui você pode adicionar alguma lógica se precisar

        return super().form_valid(form)


class ComercialCreateView(LoginRequiredMixin, CreateView):
    model = Comercial
    form_class = ComercialForm
    template_name = "glex/comercial-form.html"
    success_url = reverse_lazy("table_forms_glex")

    def form_valid(self, form):
        form.instance.usuario_modificacao = self.request.user
        return super().form_valid(form)


class ComercialUpdateView(LoginRequiredMixin, UpdateView):
    model = Comercial
    form_class = ComercialForm
    template_name = "glex/comercial-form-edit.html"
    success_url = reverse_lazy("table_forms_glex")

    def get_object(self, queryset=None):
        return get_object_or_404(Comercial, usuario_modificacao=self.request.user)

    def form_valid(self, form):
        form.instance.usuario_modificacao = self.request.user

        # Verifica se os campos de arquivo estão preenchidos antes de acessar suas propriedades
        for field in self.form_class.Meta.fields:
            file_field = form.cleaned_data.get(field)
            if file_field and hasattr(file_field, "name"):
                pass  # Aqui você pode adicionar alguma lógica se precisar

        return super().form_valid(form)


#######################  QA ##########################
class Dominio1CreateView(CreateView):
    model = Dominio1
    form_class = Dominio1Form
    template_name = "pages/dominio1_form.html"
    success_url = reverse_lazy("dominio1_list")

    def form_valid(self, form):
        messages.success(self.request, "Dominio 1 foi salvo com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao salvar Dominio 1: {formatted_errors}")
        return super().form_invalid(form)


class Dominio2CreateView(CreateView):
    model = Dominio2
    form_class = Dominio2Form
    template_name = "pages/dominio2_form.html"
    success_url = reverse_lazy("dominio2_list")

    def form_valid(self, form):
        messages.success(self.request, "Dominio 2 foi salvo com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao salvar Dominio 2: {formatted_errors}")
        return super().form_invalid(form)


class Dominio3CreateView(CreateView):
    model = Dominio3
    form_class = Dominio3Form
    template_name = "pages/dominio3_form.html"
    success_url = reverse_lazy("dominio3_list")

    def form_valid(self, form):
        messages.success(self.request, "Dominio 3 foi salvo com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao salvar Dominio 3: {formatted_errors}")
        return super().form_invalid(form)


class Dominio4CreateView(CreateView):
    model = Dominio4
    form_class = Dominio4Form
    template_name = "pages/dominio4_form.html"
    success_url = reverse_lazy("dominio4_list")

    def form_valid(self, form):
        messages.success(self.request, "Dominio 4 foi salvo com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao salvar Dominio 4: {formatted_errors}")
        return super().form_invalid(form)
