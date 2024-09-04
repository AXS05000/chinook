from django.urls import path
from .views import (chat_view, generate_excel_report, ControleEscolasSearchView, ExcelImportView, EscolaSearchView, ImportPlanificadorView, PlanificadorCreateView, PlanificadorUpdateView,hr_assistant_view,
    import_crm_fui,
    import_resposta,
    filtered_chat_view,
    import_cliente_oculto_2024,
    import_vendas_slm_2024,
    import_vendas_slm_2025,
    download_excel_report_slm_2024,
    download_excel_report_slm_2025,
    gerar_resumo_nps,
    gerar_resumos_todas_escolas,
    import_vendas_slm_2025_json,
    import_crm_fui_json,
    import_vendas_slm_2024_json,
    import_ticket_sprinklr,
    gerar_resumo_cliente_oculto,
    gerar_resumos_cliente_oculto_todas_escolas,
    )

urlpatterns = [
    path("generate_report/", generate_excel_report, name="generate_report"),
    path("importar_nps/", ExcelImportView.as_view(), name="importar_nps"),
    path("hr/", hr_assistant_view, name="hr_assistant"),
    path("import_crm_fui/", import_crm_fui, name="import_crm_fui"),
    path("import_respostas_nps/", import_resposta, name="import_respostas_nps"),
    path("chinook-mb/", filtered_chat_view, name="filtered_chat"),
    path(
        "import_ticket_sprinklr/", import_ticket_sprinklr, name="import_ticket_sprinklr"
    ),

    path(
        "import_vendas_slm_2024/", import_vendas_slm_2024, name="import_vendas_slm_2024"
    ),
    path(
        "import_vendas_slm_2025/", import_vendas_slm_2025, name="import_vendas_slm_2025"
    ),
    path(
        "import_cliente_oculto_2024/", import_cliente_oculto_2024, name="import_cliente_oculto_2024"
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
    path('import_planificador/', ImportPlanificadorView.as_view(), name='import_planificador'),
    path('planificador/create/', PlanificadorCreateView.as_view(), name='planificador_create'),
    path('planificador/<int:pk>/editar/', PlanificadorUpdateView.as_view(), name='editar_planificador'),
    path('search_escolas/', EscolaSearchView.as_view(), name='buscar_escolas'),
    path('controle_escolas/', ControleEscolasSearchView.as_view(), name='controle_escolas'),
    path('gerar_resumo_nps/<int:school_id>/', gerar_resumo_nps, name='gerar_resumo_nps'),
    path('gerar-resumos-todas-escolas/', gerar_resumos_todas_escolas, name='gerar_resumos_todas_escolas'),
    path('gerar-resumo-cliente-oculto/<int:school_id>/', gerar_resumo_cliente_oculto, name='gerar_resumo_cliente_oculto'),
    path('gerar-resumos-cliente-oculto-todas-escolas/', gerar_resumos_cliente_oculto_todas_escolas, name='gerar_resumos_cliente_oculto_todas_escolas'),
    path('api/import-vendas-slm-2025/', import_vendas_slm_2025_json, name='import_vendas_slm_2025_json'),
    path('api/import-crm-fui/', import_crm_fui_json, name='import_crm_fui_json'),
    path('api/import-vendas-slm-2024/', import_vendas_slm_2024_json, name='import_vendas_slm_2024_json'),
]
