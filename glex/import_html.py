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

            # Inicializa as variáveis para armazenar o último título e conteúdo
            titulo_atual = None
            conteudo_atual = []

            # Itera pelos elementos relevantes do corpo
            for element in soup.body.find_all(['h9', 'p', 'ul', 'ol']):
                if element.name == 'h9':  # Novo título
                    # Salva o registro anterior, se existir
                    if titulo_atual and conteudo_atual:
                        Base_de_Conhecimento_Geral.objects.create(
                            titulo=titulo_atual,
                            conteudo=' '.join(conteudo_atual).strip(),
                            criado_em=now()
                        )
                    # Atualiza para o novo título
                    titulo_atual = element.get_text(strip=True)
                    conteudo_atual = []
                elif element.name in ['p', 'ul', 'ol']:
                    # Processa o conteúdo sem duplicar itens de lista
                    if element.name in ['ul', 'ol']:
                        list_items = [li.get_text(strip=True) for li in element.find_all('li', recursive=False)]
                        conteudo_atual.extend(list_items)
                    else:
                        # Adiciona o texto puro do parágrafo
                        conteudo_atual.append(element.get_text(strip=True))

            # Salva o último registro após o loop
            if titulo_atual and conteudo_atual:
                Base_de_Conhecimento_Geral.objects.create(
                    titulo=titulo_atual,
                    conteudo=' '.join(conteudo_atual).strip(),
                    criado_em=now()
                )

            return redirect('upload_html')
    return render(request, 'upload_html.html')
