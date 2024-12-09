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

            # Inicializa as variáveis para armazenar o último título, tópico e subtópico
            titulo_atual = None
            topico_atual = None
            conteudo_atual = []
            sub_topico_atual = None

            for element in soup.body.descendants:
                if element.name == 'h9':  # Novo título
                    # Salva o registro anterior, se existir
                    if conteudo_atual:
                        Base_de_Conhecimento_Geral.objects.create(
                            titulo=titulo_atual,
                            topico=topico_atual,
                            sub_topico=sub_topico_atual,
                            conteudo=' '.join(conteudo_atual).strip(),
                            criado_em=now()
                        )
                    # Atualiza para o novo título
                    titulo_atual = element.get_text(strip=True)
                    topico_atual = None
                    sub_topico_atual = None
                    conteudo_atual = []
                elif element.name == 'h8':  # Novo tópico
                    # Salva o conteúdo atual antes de mudar o tópico
                    if conteudo_atual:
                        Base_de_Conhecimento_Geral.objects.create(
                            titulo=titulo_atual,
                            topico=topico_atual,
                            sub_topico=sub_topico_atual,
                            conteudo=' '.join(conteudo_atual).strip(),
                            criado_em=now()
                        )
                    # Atualiza para o novo tópico
                    topico_atual = element.get_text(strip=True)
                    sub_topico_atual = None
                    conteudo_atual = []
                elif element.name == 'h1':  # Novo subtópico
                    # Salva o conteúdo atual antes de mudar o subtópico
                    if conteudo_atual:
                        Base_de_Conhecimento_Geral.objects.create(
                            titulo=titulo_atual,
                            topico=topico_atual,
                            sub_topico=sub_topico_atual,
                            conteudo=' '.join(conteudo_atual).strip(),
                            criado_em=now()
                        )
                    # Atualiza para o novo subtópico
                    sub_topico_atual = element.get_text(strip=True)
                    conteudo_atual = []
                elif element.name in ['p', 'ul', 'li', 'h3', 'h2', 'ol']:
                    # Acumula apenas o texto do conteúdo no subtópico atual
                    conteudo_atual.append(element.get_text(strip=True))

            # Salva o último registro após o loop
            if conteudo_atual:
                Base_de_Conhecimento_Geral.objects.create(
                    titulo=titulo_atual,
                    topico=topico_atual,
                    sub_topico=sub_topico_atual,
                    conteudo=' '.join(conteudo_atual).strip(),
                    criado_em=now()
                )

            return redirect('upload_html')
    return render(request, 'upload_html.html')
