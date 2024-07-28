from django.urls import path
from .views import (
    chat_view,
    generate_excel_report,
    hr_assistant_view,
    import_crm_fui,
    import_resposta,
    filtered_chat_view,
)

urlpatterns = [
    path("chinook/", chat_view, name="chat"),
    path("generate_report/", generate_excel_report, name="generate_report"),
    path("hr/", hr_assistant_view, name="hr_assistant"),
    path("import_crm_fui/", import_crm_fui, name="import_crm_fui"),
    path("import_respostas_nps/", import_resposta, name="import_respostas_nps"),
    path("filtered_chat/", filtered_chat_view, name="filtered_chat"),
]
