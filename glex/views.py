from django.views.generic import TemplateView, CreateView, UpdateView, View
from .forms import (
    GlexGestaoDeParceriaForm,
    GlexGenteForm,
    GlexAdministrativoForm,
    GlexTecnologiaForm,
    GlexMarketingForm,
    GlexAcademicoForm,
    GlexGestaoEscolarForm,
    GlexOperacaoAcademicaForm,
    GlexImplantacaoForm,
    GlexComercialForm,
    GlexResultadoForm,
    Dominio1Form,
    Dominio2Form,
    Dominio3Form,
    Dominio4Form,
)
from django.utils.html import strip_tags
from .models import (
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
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from ia.models import CRM_FUI
from django.http import Http404


# class HomeGlex(TemplateView):
#     template_name = "glex/home_glex.html"


# class Glex(TemplateView):
#     template_name = "glex/glex.html"


# class TabelaFormsGlex(LoginRequiredMixin, TemplateView):
#     template_name = "glex/tabela_forms_glex.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         # Lógica para Administrativo
#         try:
#             administrativo_form = Administrativo.objects.get(
#                 usuario_modificacao=self.request.user
#             )
#             is_complete_adm = all(
#                 [
#                     administrativo_form.lideranca_equipe,
#                     administrativo_form.reunioes_comerciais,
#                     administrativo_form.uniformes_crachas,
#                     administrativo_form.pagamento_boletos,
#                     administrativo_form.conta_bancaria_pj,
#                     administrativo_form.fluxo_caixa,
#                     administrativo_form.inadimplencia,
#                     administrativo_form.controle_balanco,
#                     administrativo_form.planejamento_orcamento,
#                     administrativo_form.orcamento_compartilhado,
#                 ]
#             )
#             context["administrativo_form"] = administrativo_form
#             context["administrativo_form_is_complete"] = is_complete_adm
#             context["administrativo_form_score"] = sum(
#                 1
#                 for field in [
#                     administrativo_form.lideranca_equipe,
#                     administrativo_form.reunioes_comerciais,
#                     administrativo_form.uniformes_crachas,
#                     administrativo_form.pagamento_boletos,
#                     administrativo_form.conta_bancaria_pj,
#                     administrativo_form.fluxo_caixa,
#                     administrativo_form.inadimplencia,
#                     administrativo_form.controle_balanco,
#                     administrativo_form.planejamento_orcamento,
#                     administrativo_form.orcamento_compartilhado,
#                 ]
#                 if field
#             )
#         except Administrativo.DoesNotExist:
#             context["administrativo_form"] = None
#             context["administrativo_form_is_complete"] = False
#             context["administrativo_form_score"] = 0

#         # Lógica para Comercial
#         try:
#             comercial_form = Comercial.objects.get(
#                 usuario_modificacao=self.request.user
#             )
#             is_complete_com = all(
#                 [
#                     comercial_form.cortesia_visitantes,
#                     comercial_form.participacao_mentoria,
#                     comercial_form.equipe_comercial_contratada,
#                     comercial_form.trilha_treinamento,
#                     comercial_form.participacao_encontros_lideres,
#                     comercial_form.funil_vendas_crm,
#                     comercial_form.pontuacao_cliente_oculto,
#                     comercial_form.participacao_campanhas,
#                     comercial_form.pesquisa_concorrentes,
#                     comercial_form.conversao_leads,
#                     comercial_form.politica_comissionamento,
#                     comercial_form.orcamento_mkt,
#                     comercial_form.profissional_mkt,
#                     comercial_form.entrega_kit_rematricula,
#                     comercial_form.entrega_kit_visita,
#                     comercial_form.leads_atraso_crm,
#                 ]
#             )
#             context["comercial_form"] = comercial_form
#             context["comercial_form_is_complete"] = is_complete_com
#             context["comercial_form_score"] = sum(
#                 1
#                 for field in [
#                     comercial_form.cortesia_visitantes,
#                     comercial_form.participacao_mentoria,
#                     comercial_form.equipe_comercial_contratada,
#                     comercial_form.trilha_treinamento,
#                     comercial_form.participacao_encontros_lideres,
#                     comercial_form.funil_vendas_crm,
#                     comercial_form.pontuacao_cliente_oculto,
#                     comercial_form.participacao_campanhas,
#                     comercial_form.pesquisa_concorrentes,
#                     comercial_form.conversao_leads,
#                     comercial_form.politica_comissionamento,
#                     comercial_form.orcamento_mkt,
#                     comercial_form.profissional_mkt,
#                     comercial_form.entrega_kit_rematricula,
#                     comercial_form.entrega_kit_visita,
#                     comercial_form.leads_atraso_crm,
#                 ]
#                 if field
#             )
#         except Comercial.DoesNotExist:
#             context["comercial_form"] = None
#             context["comercial_form_is_complete"] = False
#             context["comercial_form_score"] = 0

#         # Calculando a pontuação geral
#         context["pontuacao_geral"] = (
#             context["administrativo_form_score"] + context["comercial_form_score"]
#         )

#         return context


# class AdministrativoCreateView(LoginRequiredMixin, CreateView):
#     model = Administrativo
#     form_class = AdministrativoForm
#     template_name = "glex/adm-form.html"
#     success_url = reverse_lazy("table_forms_glex")

#     def form_valid(self, form):
#         form.instance.usuario_modificacao = self.request.user
#         return super().form_valid(form)


# class AdministrativoUpdateView(LoginRequiredMixin, UpdateView):
#     model = Administrativo
#     form_class = AdministrativoForm
#     template_name = "glex/adm-form-edit.html"
#     success_url = reverse_lazy("table_forms_glex")

#     def get_object(self, queryset=None):
#         return get_object_or_404(Administrativo, usuario_modificacao=self.request.user)

#     def form_valid(self, form):
#         form.instance.usuario_modificacao = self.request.user

#         # Verifica se os campos de arquivo estão preenchidos antes de acessar suas propriedades
#         for field in self.form_class.Meta.fields:
#             file_field = form.cleaned_data.get(field)
#             if file_field and hasattr(file_field, "name"):
#                 pass  # Aqui você pode adicionar alguma lógica se precisar

#         return super().form_valid(form)



#######################  QA ##########################
class Dominio1View(CreateView):
    model = Dominio1
    form_class = Dominio1Form
    template_name = "pages/dominio1_form.html"

    def dispatch(self, request, *args, **kwargs):
        escola_id = request.GET.get("escola_id")
        if not escola_id:
            messages.error(request, "Escola não identificada.")
            return redirect("buscar_escola")

        self.escola_id = escola_id
        self.instance = Dominio1.objects.filter(escola_id=escola_id).first()

        if self.instance:
            return redirect(reverse("dominio1_update", kwargs={"pk": self.instance.pk}))

        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial["escola"] = self.escola_id
        return initial

    def form_valid(self, form):
        form.instance.escola_id = self.escola_id
        messages.success(self.request, "Dominio 1 foi salvo com sucesso!")
        self.success_url = reverse("tabela_qa", kwargs={"escola_id": self.escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao salvar Dominio 1: {formatted_errors}")
        return super().form_invalid(form)


class Dominio1UpdateView(UpdateView):
    model = Dominio1
    form_class = Dominio1Form
    template_name = "pages/dominio1_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Dominio 1 foi atualizado com sucesso!")
        escola_id = form.instance.escola_id
        self.success_url = reverse("tabela_qa", kwargs={"escola_id": escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao atualizar Dominio 1: {formatted_errors}")
        return super().form_invalid(form)


# Dominio2 Views
class Dominio2View(CreateView):
    model = Dominio2
    form_class = Dominio2Form
    template_name = "pages/dominio2_form.html"

    def dispatch(self, request, *args, **kwargs):
        escola_id = request.GET.get("escola_id")
        if not escola_id:
            messages.error(request, "Escola não identificada.")
            return redirect("buscar_escola")

        self.escola_id = escola_id
        self.instance = Dominio2.objects.filter(escola_id=escola_id).first()

        if self.instance:
            return redirect(reverse("dominio2_update", kwargs={"pk": self.instance.pk}))

        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial["escola"] = self.escola_id
        return initial

    def form_valid(self, form):
        form.instance.escola_id = self.escola_id
        messages.success(self.request, "Dominio 2 foi salvo com sucesso!")
        self.success_url = reverse("tabela_qa", kwargs={"escola_id": self.escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao salvar Dominio 2: {formatted_errors}")
        return super().form_invalid(form)


class Dominio2UpdateView(UpdateView):
    model = Dominio2
    form_class = Dominio2Form
    template_name = "pages/dominio2_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Dominio 2 foi atualizado com sucesso!")
        escola_id = form.instance.escola_id
        self.success_url = reverse("tabela_qa", kwargs={"escola_id": escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao atualizar Dominio 2: {formatted_errors}")
        return super().form_invalid(form)


# Dominio3 Views
class Dominio3View(CreateView):
    model = Dominio3
    form_class = Dominio3Form
    template_name = "pages/dominio3_form.html"

    def dispatch(self, request, *args, **kwargs):
        escola_id = request.GET.get("escola_id")
        if not escola_id:
            messages.error(request, "Escola não identificada.")
            return redirect("buscar_escola")

        self.escola_id = escola_id
        self.instance = Dominio3.objects.filter(escola_id=escola_id).first()

        if self.instance:
            return redirect(reverse("dominio3_update", kwargs={"pk": self.instance.pk}))

        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial["escola"] = self.escola_id
        return initial

    def form_valid(self, form):
        form.instance.escola_id = self.escola_id
        messages.success(self.request, "Dominio 3 foi salvo com sucesso!")
        self.success_url = reverse("tabela_qa", kwargs={"escola_id": self.escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao salvar Dominio 3: {formatted_errors}")
        return super().form_invalid(form)


class Dominio3UpdateView(UpdateView):
    model = Dominio3
    form_class = Dominio3Form
    template_name = "pages/dominio3_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Dominio 3 foi atualizado com sucesso!")
        escola_id = form.instance.escola_id
        self.success_url = reverse("tabela_qa", kwargs={"escola_id": escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao atualizar Dominio 3: {formatted_errors}")
        return super().form_invalid(form)


# Dominio4 Views
class Dominio4View(CreateView):
    model = Dominio4
    form_class = Dominio4Form
    template_name = "pages/dominio4_form.html"

    def dispatch(self, request, *args, **kwargs):
        escola_id = request.GET.get("escola_id")
        if not escola_id:
            messages.error(request, "Escola não identificada.")
            return redirect("buscar_escola")

        self.escola_id = escola_id
        self.instance = Dominio4.objects.filter(escola_id=escola_id).first()

        if self.instance:
            return redirect(reverse("dominio4_update", kwargs={"pk": self.instance.pk}))

        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial["escola"] = self.escola_id
        return initial

    def form_valid(self, form):
        form.instance.escola_id = self.escola_id
        messages.success(self.request, "Dominio 4 foi salvo com sucesso!")
        self.success_url = reverse("tabela_qa", kwargs={"escola_id": self.escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao salvar Dominio 4: {formatted_errors}")
        return super().form_invalid(form)


class Dominio4UpdateView(UpdateView):
    model = Dominio4
    form_class = Dominio4Form
    template_name = "pages/dominio4_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Dominio 4 foi atualizado com sucesso!")
        escola_id = form.instance.escola_id
        self.success_url = reverse("tabela_qa", kwargs={"escola_id": escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao atualizar Dominio 4: {formatted_errors}")
        return super().form_invalid(form)


class TabelaQAView(TemplateView):
    template_name = "pages/tabela_qa.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        escola_id = kwargs.get("escola_id")

        # Busca a escola correspondente
        try:
            escola = CRM_FUI.objects.get(id_escola=escola_id)
        except CRM_FUI.DoesNotExist:
            raise Http404("Escola não encontrada.")

        # Função auxiliar para calcular pontuação e status
        def calcular_pontuacao_e_status(model, escola):
            instance = model.objects.filter(escola=escola).first()
            if not instance:
                total_perguntas = len(
                    [
                        field
                        for field in model._meta.fields
                        if getattr(
                            field, "choices", None
                        )  # Inclui apenas campos com `choices`
                    ]
                )
                return f"0/{total_perguntas}", "pending"

            respostas_preenchidas = sum(
                bool(getattr(instance, field.name))
                for field in model._meta.fields
                if getattr(field, "choices", None)  # Inclui apenas campos com `choices`
            )
            total_perguntas = len(
                [
                    field
                    for field in model._meta.fields
                    if getattr(
                        field, "choices", None
                    )  # Inclui apenas campos com `choices`
                ]
            )
            status = (
                "complete" if respostas_preenchidas == total_perguntas else "pending"
            )
            return f"{respostas_preenchidas}/{total_perguntas}", status

        # Informações dos domínios com pontuações e status
        dominios = [
            {
                "dominio": "D1 - Integrity of Maple Bear & Local Programming",
                "pontuacao": calcular_pontuacao_e_status(Dominio1, escola)[0],
                "status": calcular_pontuacao_e_status(Dominio1, escola)[1],
                "url": reverse("dominio1_create"),
            },
            {
                "dominio": "D2 - Leadership and Management",
                "pontuacao": calcular_pontuacao_e_status(Dominio2, escola)[0],
                "status": calcular_pontuacao_e_status(Dominio2, escola)[1],
                "url": reverse("dominio2_create"),
            },
            {
                "dominio": "D3 - Quality of Instruction and Learning",
                "pontuacao": calcular_pontuacao_e_status(Dominio3, escola)[0],
                "status": calcular_pontuacao_e_status(Dominio3, escola)[1],
                "url": reverse("dominio3_create"),
            },
            {
                "dominio": "D4 - Assessment, Evaluation and Reporting",
                "pontuacao": calcular_pontuacao_e_status(Dominio4, escola)[0],
                "status": calcular_pontuacao_e_status(Dominio4, escola)[1],
                "url": reverse("dominio4_create"),
            },
        ]

        context["dominios"] = dominios
        context["escola"] = escola
        return context

    def get_pontuacao(self, model, escola):
        """Calcula a pontuação com base nas perguntas respondidas."""
        instance = model.objects.filter(escola=escola).first()
        if not instance:
            return "0/0"  # Nenhum dado preenchido
        total_perguntas = len(model._meta.fields) - 2  # Remove 'id' e 'escola'
        respostas_preenchidas = sum(
            bool(getattr(instance, field.name))
            for field in model._meta.fields
            if field.name not in ["id", "escola"]
        )
        return f"{respostas_preenchidas}/{total_perguntas}"

    def get_status(self, model, escola):
        """Verifica se todas as perguntas foram respondidas."""
        instance = model.objects.filter(escola=escola).first()
        if not instance:
            return "pending"  # Sem dados preenchidos
        total_perguntas = len(model._meta.fields) - 2  # Remove 'id' e 'escola'
        respostas_preenchidas = sum(
            bool(getattr(instance, field.name))
            for field in model._meta.fields
            if field.name not in ["id", "escola"]
        )
        return "complete" if respostas_preenchidas == total_perguntas else "pending"


class BuscarEscolaView(TemplateView):
    template_name = (
        "pages/buscar_escola.html"  # Nome do seu template para busca do CNPJ
    )

    def post(self, request, *args, **kwargs):
        cnpj = request.POST.get("cnpj")
        try:
            escola = CRM_FUI.objects.get(CNPJ=cnpj)
            return redirect(
                reverse("tabela_qa", kwargs={"escola_id": escola.id_escola})
            )
        except CRM_FUI.DoesNotExist:
            messages.error(request, "Escola com o CNPJ fornecido não encontrada.")
            return redirect("buscar_escola")


#######################  GLEX ##########################



class GlexGestaoDeParceriaCreateView(CreateView):
    model = GlexGestaoDeParceria
    form_class = GlexGestaoDeParceriaForm
    template_name = "pages/forms_glex.html"

    def dispatch(self, request, *args, **kwargs):
        escola_id = request.GET.get("escola_id")
        if not escola_id:
            messages.error(request, "Escola não identificada.")
            return redirect("glex_2025")

        self.escola_id = escola_id
        self.instance = GlexGestaoDeParceria.objects.filter(escola_id=escola_id).first()

        if self.instance:
            return redirect(reverse("glex_gestao_de_parceria_update", kwargs={"pk": self.instance.pk}))

        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial["escola"] = self.escola_id
        return initial

    def form_valid(self, form):
        form.instance.escola_id = self.escola_id
        messages.success(self.request, "Gestão de Parceria foi salva com sucesso!")
        self.success_url = reverse("tabela_glex", kwargs={"escola_id": self.escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao salvar Gestão de Parceria: {formatted_errors}")
        return super().form_invalid(form)


class GlexGestaoDeParceriaUpdateView(UpdateView):
    model = GlexGestaoDeParceria
    form_class = GlexGestaoDeParceriaForm
    template_name = "pages/forms_glex.html"

    def form_valid(self, form):
        messages.success(self.request, "Gestão de Parceria foi atualizada com sucesso!")
        escola_id = form.instance.escola_id
        self.success_url = reverse("tabela_glex", kwargs={"escola_id": escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao atualizar Gestão de Parceria: {formatted_errors}")
        return super().form_invalid(form)


class GlexGenteCreateView(CreateView):
    model = GlexGente
    form_class = GlexGenteForm
    template_name = "pages/forms_glex.html"

    def dispatch(self, request, *args, **kwargs):
        escola_id = request.GET.get("escola_id")
        if not escola_id:
            messages.error(request, "Escola não identificada.")
            return redirect("glex_2025")

        self.escola_id = escola_id
        self.instance = GlexGente.objects.filter(escola_id=escola_id).first()

        if self.instance:
            return redirect(reverse("glex_gente_update", kwargs={"pk": self.instance.pk}))

        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial["escola"] = self.escola_id
        return initial

    def form_valid(self, form):
        form.instance.escola_id = self.escola_id
        messages.success(self.request, "Gente foi salvo com sucesso!")
        self.success_url = reverse("tabela_glex", kwargs={"escola_id": self.escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao salvar Gente: {formatted_errors}")
        return super().form_invalid(form)


class GlexGenteUpdateView(UpdateView):
    model = GlexGente
    form_class = GlexGenteForm
    template_name = "pages/forms_glex.html"

    def form_valid(self, form):
        messages.success(self.request, "Gente foi atualizado com sucesso!")
        escola_id = form.instance.escola_id
        self.success_url = reverse("tabela_glex", kwargs={"escola_id": escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao atualizar Gente: {formatted_errors}")
        return super().form_invalid(form)


class GlexAdministrativoCreateView(CreateView):
    model = GlexAdministrativo
    form_class = GlexAdministrativoForm
    template_name = "pages/forms_glex.html"

    def dispatch(self, request, *args, **kwargs):
        escola_id = request.GET.get("escola_id")
        if not escola_id:
            messages.error(request, "Escola não identificada.")
            return redirect("glex_2025")

        self.escola_id = escola_id
        self.instance = GlexAdministrativo.objects.filter(escola_id=escola_id).first()

        if self.instance:
            return redirect(reverse("glex_administrativo_update", kwargs={"pk": self.instance.pk}))

        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial["escola"] = self.escola_id
        return initial

    def form_valid(self, form):
        form.instance.escola_id = self.escola_id
        messages.success(self.request, "Administrativo foi salvo com sucesso!")
        self.success_url = reverse("tabela_glex", kwargs={"escola_id": self.escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao salvar Administrativo: {formatted_errors}")
        return super().form_invalid(form)


class GlexAdministrativoUpdateView(UpdateView):
    model = GlexAdministrativo
    form_class = GlexAdministrativoForm
    template_name = "pages/forms_glex.html"

    def form_valid(self, form):
        messages.success(self.request, "Administrativo foi atualizado com sucesso!")
        escola_id = form.instance.escola_id
        self.success_url = reverse("tabela_glex", kwargs={"escola_id": escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao atualizar Administrativo: {formatted_errors}")
        return super().form_invalid(form)


class GlexTecnologiaCreateView(CreateView):
    model = GlexTecnologia
    form_class = GlexTecnologiaForm
    template_name = "pages/forms_glex.html"

    def dispatch(self, request, *args, **kwargs):
        escola_id = request.GET.get("escola_id")
        if not escola_id:
            messages.error(request, "Escola não identificada.")
            return redirect("glex_2025")

        self.escola_id = escola_id
        self.instance = GlexTecnologia.objects.filter(escola_id=escola_id).first()

        if self.instance:
            return redirect(reverse("glex_tecnologia_update", kwargs={"pk": self.instance.pk}))

        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial["escola"] = self.escola_id
        return initial

    def form_valid(self, form):
        form.instance.escola_id = self.escola_id
        messages.success(self.request, "Tecnologia foi salvo com sucesso!")
        self.success_url = reverse("tabela_glex", kwargs={"escola_id": self.escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao salvar Tecnologia: {formatted_errors}")
        return super().form_invalid(form)


class GlexTecnologiaUpdateView(UpdateView):
    model = GlexTecnologia
    form_class = GlexTecnologiaForm
    template_name = "pages/forms_glex.html"

    def form_valid(self, form):
        messages.success(self.request, "Tecnologia foi atualizado com sucesso!")
        escola_id = form.instance.escola_id
        self.success_url = reverse("tabela_glex", kwargs={"escola_id": escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao atualizar Tecnologia: {formatted_errors}")
        return super().form_invalid(form)


class GlexMarketingCreateView(CreateView):
    model = GlexMarketing
    form_class = GlexMarketingForm
    template_name = "pages/forms_glex.html"

    def dispatch(self, request, *args, **kwargs):
        escola_id = request.GET.get("escola_id")
        if not escola_id:
            messages.error(request, "Escola não identificada.")
            return redirect("glex_2025")

        self.escola_id = escola_id
        self.instance = GlexMarketing.objects.filter(escola_id=escola_id).first()

        if self.instance:
            return redirect(reverse("glex_marketing_update", kwargs={"pk": self.instance.pk}))

        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial["escola"] = self.escola_id
        return initial

    def form_valid(self, form):
        form.instance.escola_id = self.escola_id
        messages.success(self.request, "Marketing foi salvo com sucesso!")
        self.success_url = reverse("tabela_glex", kwargs={"escola_id": self.escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao salvar Marketing: {formatted_errors}")
        return super().form_invalid(form)


class GlexMarketingUpdateView(UpdateView):
    model = GlexMarketing
    form_class = GlexMarketingForm
    template_name = "pages/forms_glex.html"

    def form_valid(self, form):
        messages.success(self.request, "Marketing foi atualizado com sucesso!")
        escola_id = form.instance.escola_id
        self.success_url = reverse("tabela_glex", kwargs={"escola_id": escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao atualizar Marketing: {formatted_errors}")
        return super().form_invalid(form)


class GlexAcademicoCreateView(CreateView):
    model = GlexAcademico
    form_class = GlexAcademicoForm
    template_name = "pages/forms_glex.html"

    def dispatch(self, request, *args, **kwargs):
        escola_id = request.GET.get("escola_id")
        if not escola_id:
            messages.error(request, "Escola não identificada.")
            return redirect("glex_2025")

        self.escola_id = escola_id
        self.instance = GlexAcademico.objects.filter(escola_id=escola_id).first()

        if self.instance:
            return redirect(reverse("glex_academico_update", kwargs={"pk": self.instance.pk}))

        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial["escola"] = self.escola_id
        return initial

    def form_valid(self, form):
        form.instance.escola_id = self.escola_id
        messages.success(self.request, "Acadêmico foi salvo com sucesso!")
        self.success_url = reverse("tabela_glex", kwargs={"escola_id": self.escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao salvar Acadêmico: {formatted_errors}")
        return super().form_invalid(form)


class GlexAcademicoUpdateView(UpdateView):
    model = GlexAcademico
    form_class = GlexAcademicoForm
    template_name = "pages/forms_glex.html"

    def form_valid(self, form):
        messages.success(self.request, "Acadêmico foi atualizado com sucesso!")
        escola_id = form.instance.escola_id
        self.success_url = reverse("tabela_glex", kwargs={"escola_id": escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao atualizar Acadêmico: {formatted_errors}")
        return super().form_invalid(form)


class GlexGestaoEscolarCreateView(CreateView):
    model = GlexGestaoEscolar
    form_class = GlexGestaoEscolarForm
    template_name = "pages/forms_glex.html"

    def dispatch(self, request, *args, **kwargs):
        escola_id = request.GET.get("escola_id")
        if not escola_id:
            messages.error(request, "Escola não identificada.")
            return redirect("glex_2025")

        self.escola_id = escola_id
        self.instance = GlexGestaoEscolar.objects.filter(escola_id=escola_id).first()

        if self.instance:
            return redirect(reverse("glex_gestao_escolar_update", kwargs={"pk": self.instance.pk}))

        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial["escola"] = self.escola_id
        return initial

    def form_valid(self, form):
        form.instance.escola_id = self.escola_id
        messages.success(self.request, "Gestão Escolar foi salvo com sucesso!")
        self.success_url = reverse("tabela_glex", kwargs={"escola_id": self.escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao salvar Gestão Escolar: {formatted_errors}")
        return super().form_invalid(form)


class GlexGestaoEscolarUpdateView(UpdateView):
    model = GlexGestaoEscolar
    form_class = GlexGestaoEscolarForm
    template_name = "pages/forms_glex.html"

    def form_valid(self, form):
        messages.success(self.request, "Gestão Escolar foi atualizado com sucesso!")
        escola_id = form.instance.escola_id
        self.success_url = reverse("tabela_glex", kwargs={"escola_id": escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao atualizar Gestão Escolar: {formatted_errors}")
        return super().form_invalid(form)


class GlexOperacaoAcademicaCreateView(CreateView):
    model = GlexOperacaoAcademica
    form_class = GlexOperacaoAcademicaForm
    template_name = "pages/forms_glex.html"

    def dispatch(self, request, *args, **kwargs):
        escola_id = request.GET.get("escola_id")
        if not escola_id:
            messages.error(request, "Escola não identificada.")
            return redirect("glex_2025")

        self.escola_id = escola_id
        self.instance = GlexOperacaoAcademica.objects.filter(escola_id=escola_id).first()

        if self.instance:
            return redirect(reverse("glex_operacao_academica_update", kwargs={"pk": self.instance.pk}))

        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial["escola"] = self.escola_id
        return initial

    def form_valid(self, form):
        form.instance.escola_id = self.escola_id
        messages.success(self.request, "Operação Acadêmica foi salvo com sucesso!")
        self.success_url = reverse("tabela_glex", kwargs={"escola_id": self.escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao salvar Operação Acadêmica: {formatted_errors}")
        return super().form_invalid(form)


class GlexOperacaoAcademicaUpdateView(UpdateView):
    model = GlexOperacaoAcademica
    form_class = GlexOperacaoAcademicaForm
    template_name = "pages/forms_glex.html"

    def form_valid(self, form):
        messages.success(self.request, "Operação Acadêmica foi atualizado com sucesso!")
        escola_id = form.instance.escola_id
        self.success_url = reverse("tabela_glex", kwargs={"escola_id": escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao atualizar Operação Acadêmica: {formatted_errors}")
        return super().form_invalid(form)


class GlexImplantacaoCreateView(CreateView):
    model = GlexImplantacao
    form_class = GlexImplantacaoForm
    template_name = "pages/forms_glex.html"

    def dispatch(self, request, *args, **kwargs):
        escola_id = request.GET.get("escola_id")
        if not escola_id:
            messages.error(request, "Escola não identificada.")
            return redirect("glex_2025")

        self.escola_id = escola_id
        self.instance = GlexImplantacao.objects.filter(escola_id=escola_id).first()

        if self.instance:
            return redirect(reverse("glex_implantacao_update", kwargs={"pk": self.instance.pk}))

        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial["escola"] = self.escola_id
        return initial

    def form_valid(self, form):
        form.instance.escola_id = self.escola_id
        messages.success(self.request, "Implantação foi salvo com sucesso!")
        self.success_url = reverse("tabela_glex", kwargs={"escola_id": self.escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao salvar Implantação: {formatted_errors}")
        return super().form_invalid(form)


class GlexImplantacaoUpdateView(UpdateView):
    model = GlexImplantacao
    form_class = GlexImplantacaoForm
    template_name = "pages/forms_glex.html"

    def form_valid(self, form):
        messages.success(self.request, "Implantação foi atualizado com sucesso!")
        escola_id = form.instance.escola_id
        self.success_url = reverse("tabela_glex", kwargs={"escola_id": escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao atualizar Implantação: {formatted_errors}")
        return super().form_invalid(form)


class GlexComercialCreateView(CreateView):
    model = GlexComercial
    form_class = GlexComercialForm
    template_name = "pages/forms_glex.html"

    def dispatch(self, request, *args, **kwargs):
        escola_id = request.GET.get("escola_id")
        if not escola_id:
            messages.error(request, "Escola não identificada.")
            return redirect("glex_2025")

        self.escola_id = escola_id
        self.instance = GlexComercial.objects.filter(escola_id=escola_id).first()

        if self.instance:
            return redirect(reverse("glex_comercial_update", kwargs={"pk": self.instance.pk}))

        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial["escola"] = self.escola_id
        return initial

    def form_valid(self, form):
        form.instance.escola_id = self.escola_id
        messages.success(self.request, "Comercial foi salvo com sucesso!")
        self.success_url = reverse("tabela_glex", kwargs={"escola_id": self.escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao salvar Comercial: {formatted_errors}")
        return super().form_invalid(form)


class GlexComercialUpdateView(UpdateView):
    model = GlexComercial
    form_class = GlexComercialForm
    template_name = "pages/glex_comercial_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Comercial foi atualizado com sucesso!")
        escola_id = form.instance.escola_id
        self.success_url = reverse("tabela_glex", kwargs={"escola_id": escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao atualizar Comercial: {formatted_errors}")
        return super().form_invalid(form)


class GlexResultadoCreateView(CreateView):
    model = GlexResultado
    form_class = GlexResultadoForm
    template_name = "pages/forms_glex.html"

    def dispatch(self, request, *args, **kwargs):
        escola_id = request.GET.get("escola_id")
        if not escola_id:
            messages.error(request, "Escola não identificada.")
            return redirect("glex_2025")

        self.escola_id = escola_id
        self.instance = GlexResultado.objects.filter(escola_id=escola_id).first()

        if self.instance:
            return redirect(reverse("glex_resultado_update", kwargs={"pk": self.instance.pk}))

        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial["escola"] = self.escola_id
        return initial

    def form_valid(self, form):
        form.instance.escola_id = self.escola_id
        messages.success(self.request, "Resultado foi salvo com sucesso!")
        self.success_url = reverse("tabela_glex", kwargs={"escola_id": self.escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao salvar Resultado: {formatted_errors}")
        return super().form_invalid(form)


class GlexResultadoUpdateView(UpdateView):
    model = GlexResultado
    form_class = GlexResultadoForm
    template_name = "pages/forms_glex.html"

    def form_valid(self, form):
        messages.success(self.request, "Resultado foi atualizado com sucesso!")
        escola_id = form.instance.escola_id
        self.success_url = reverse("tabela_glex", kwargs={"escola_id": escola_id})
        return super().form_valid(form)

    def form_invalid(self, form):
        errors = form.errors.get_json_data()
        formatted_errors = " ".join(
            f"{field}: {strip_tags(errors[field][0]['message'])}" for field in errors
        )
        messages.error(self.request, f"Erro ao atualizar Resultado: {formatted_errors}")
        return super().form_invalid(form)


class TabelaGlexView(TemplateView):
    template_name = "pages/tabela_glex.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        escola_id = kwargs.get("escola_id")

        # Busca a escola correspondente
        try:
            escola = CRM_FUI.objects.get(id_escola=escola_id)
        except CRM_FUI.DoesNotExist:
            raise Http404("Escola não encontrada.")

        # Função auxiliar para calcular pontuação e status
        def calcular_pontuacao_e_status(model, escola):
            instance = model.objects.filter(escola=escola).first()
            if not instance:
                total_perguntas = len(
                    [
                        field
                        for field in model._meta.fields
                        if getattr(field, "choices", None)  # Inclui apenas campos com `choices`
                    ]
                )
                return f"0/{total_perguntas}", "pending"

            respostas_preenchidas = sum(
                bool(getattr(instance, field.name))
                for field in model._meta.fields
                if getattr(field, "choices", None)  # Inclui apenas campos com `choices`
            )
            total_perguntas = len(
                [
                    field
                    for field in model._meta.fields
                    if getattr(field, "choices", None)  # Inclui apenas campos com `choices`
                ]
            )
            status = "complete" if respostas_preenchidas == total_perguntas else "pending"
            return f"{respostas_preenchidas}/{total_perguntas}", status

        # Informações das models com pontuações e status
        models = [
            ("Gestão de Parceria", GlexGestaoDeParceria, "glex_gestao_de_parceria_create"),
            ("Gente", GlexGente, "glex_gente_create"),
            ("Administrativo", GlexAdministrativo, "glex_administrativo_create"),
            ("Tecnologia", GlexTecnologia, "glex_tecnologia_create"),
            ("Marketing", GlexMarketing, "glex_marketing_create"),
            ("Acadêmico", GlexAcademico, "glex_academico_create"),
            ("Gestão Escolar", GlexGestaoEscolar, "glex_gestao_escolar_create"),
            ("Operação Acadêmica", GlexOperacaoAcademica, "glex_operacao_academica_create"),
            ("Implantação", GlexImplantacao, "glex_implantacao_create"),
            ("Comercial", GlexComercial, "glex_comercial_create"),
            ("Resultado", GlexResultado, "glex_resultado_create"),
        ]

        glex_data = [
            {
                "nome": nome,
                "pontuacao": calcular_pontuacao_e_status(model, escola)[0],
                "status": calcular_pontuacao_e_status(model, escola)[1],
                "url": reverse(url_name),
            }
            for nome, model, url_name in models
        ]

        context["glex_data"] = glex_data
        context["escola"] = escola
        return context



class BuscarEscolaGlexView(TemplateView):
    template_name = (
        "pages/buscar_escola_glex.html"  # Nome do seu template para busca do CNPJ
    )

    def post(self, request, *args, **kwargs):
        cnpj = request.POST.get("cnpj")
        try:
            escola = CRM_FUI.objects.get(CNPJ=cnpj)
            return redirect(
                reverse("tabela_glex", kwargs={"escola_id": escola.id_escola})
            )
        except CRM_FUI.DoesNotExist:
            messages.error(request, "Escola com o CNPJ fornecido não encontrada.")
            return redirect("glex_2025")


















