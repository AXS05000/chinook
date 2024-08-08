from django.urls import path
from .views import (chat_view, generate_excel_report, ExcelImportView, EscolaSearchView, ImportPlanificadorView, PlanificadorCreateView, PlanificadorUpdateView,hr_assistant_view,
    import_crm_fui,
    import_resposta,
    filtered_chat_view,
    import_vendas_slm_2024,
    import_vendas_slm_2025,
    download_excel_report_slm_2024,
    download_excel_report_slm_2025,
    simple_chat_view,
    )

urlpatterns = [
    path("chinook/", chat_view, name="chat"),
    path("generate_report/", generate_excel_report, name="generate_report"),
    path("importar_nps/", ExcelImportView.as_view(), name="importar_nps"),
    path("hr/", hr_assistant_view, name="hr_assistant"),
    path("import_crm_fui/", import_crm_fui, name="import_crm_fui"),
    path("import_respostas_nps/", import_resposta, name="import_respostas_nps"),
    path("chinook-mb/", filtered_chat_view, name="filtered_chat"),
    path(
        "import_vendas_slm_2024/", import_vendas_slm_2024, name="import_vendas_slm_2024"
    ),
    path(
        "import_vendas_slm_2025/", import_vendas_slm_2025, name="import_vendas_slm_2025"
    ),
    path(
        "download_excel_report/",
        download_excel_report_slm_2024,
        name="download_excel_report",
    ),
    path(
        "download_excel_report_25/",
        download_excel_report_slm_2025,
        name="download_excel_report_25",
    ),
    path("simple_chat/", simple_chat_view, name="simple_chat"),
    path('import_planificador/', ImportPlanificadorView.as_view(), name='import_planificador'),
    path('planificador/create/', PlanificadorCreateView.as_view(), name='planificador_create'),
    path('planificador/edit/<int:pk>/', PlanificadorUpdateView.as_view(), name='planificador_edit'),
    path('search_escolas/', EscolaSearchView.as_view(), name='search_escolas'),

]
