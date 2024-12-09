from django.shortcuts import render, redirect
from django.utils.timezone import now
from bs4 import BeautifulSoup
from .models import Base_de_Conhecimento_Geral

def upload_html_view(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('arquivo_html')
        if uploaded_file:
            # Lê o conteúdo do arquivo HTML enviado
            html_content = uploaded_file.read().decode('utf-8')
            soup = BeautifulSoup(html_content, 'html.parser')

            # Variáveis para controle
            titulo_atual = None
            topico_atual = None
            sub_topico_atual = None
            conteudo_atual = []
            elementos_processados = set()  # Para evitar duplicação

            # Itera pelos elementos relevantes no corpo do HTML
            for element in soup.body.find_all(['h9', 'h8', 'h1', 'p', 'ul', 'li', 'ol']):
                # Obtém o texto do elemento
                texto_elemento = element.get_text(strip=True)
                if texto_elemento in elementos_processados or not texto_elemento:
                    continue  # Ignora elementos duplicados ou vazios
                elementos_processados.add(texto_elemento)

                # Processa os títulos e seções
                if element.name == 'h9':  # Novo título
                    if conteudo_atual:
                        salvar_registro(titulo_atual, topico_atual, sub_topico_atual, conteudo_atual)
                    titulo_atual = texto_elemento
                    topico_atual, sub_topico_atual, conteudo_atual = None, None, []
                elif element.name == 'h8':  # Novo tópico
                    if conteudo_atual:
                        salvar_registro(titulo_atual, topico_atual, sub_topico_atual, conteudo_atual)
                    topico_atual = texto_elemento
                    sub_topico_atual, conteudo_atual = None, []
                elif element.name == 'h1':  # Novo subtópico
                    if conteudo_atual:
                        salvar_registro(titulo_atual, topico_atual, sub_topico_atual, conteudo_atual)
                    sub_topico_atual = texto_elemento
                    conteudo_atual = []
                elif element.name in ['p', 'ul', 'li', 'ol']:  # Conteúdo
                    conteudo_atual.append(texto_elemento)

            # Salva o último registro após o loop
            if conteudo_atual:
                salvar_registro(titulo_atual, topico_atual, sub_topico_atual, conteudo_atual)

            return redirect('upload_html')
    return render(request, 'upload_html.html')


def salvar_registro(titulo, topico, sub_topico, conteudo):
    """Função para salvar um registro na model."""
    if titulo or topico or sub_topico or conteudo:
        Base_de_Conhecimento_Geral.objects.create(
            titulo=titulo,
            topico=topico,
            sub_topico=sub_topico,
            conteudo='\n'.join(conteudo),  # Junta os textos com quebra de linha
            criado_em=now()
        )
