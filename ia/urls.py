from django.urls import path
from .views import (
    chat_view,
    hr_assistant_view,
    import_crm_fui,
    import_resposta,
    filtered_chat_view,
    import_vendas_slm_2024,
    download_excel_report_slm_2024,
    simple_chat_view,
)

urlpatterns = [
    path("chinook/", chat_view, name="chat"),
    path("hr/", hr_assistant_view, name="hr_assistant"),
    path("import_crm_fui/", import_crm_fui, name="import_crm_fui"),
    path("import_respostas_nps/", import_resposta, name="import_respostas_nps"),
    path("filtered_chat/", filtered_chat_view, name="filtered_chat"),
    path(
        "import_vendas_slm_2024/", import_vendas_slm_2024, name="import_vendas_slm_2024"
    ),
    path(
        "download_excel_report/",
        download_excel_report_slm_2024,
        name="download_excel_report",
    ),
    path("simple_chat/", simple_chat_view, name="simple_chat"),
]
