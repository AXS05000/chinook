from django.urls import path
from .views import chat_view, generate_excel_report, ExcelImportView

urlpatterns = [
    path("chat/", chat_view, name="chat"),
    path("generate_report/", generate_excel_report, name="generate_report"),
    path("importar_nps/", ExcelImportView.as_view(), name="importar_nps"),
]
