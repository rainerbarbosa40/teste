from django.shortcuts import render
from .models import Humano  # Se estiver usando o modelo Humano

def index(request):
    # Lógica para a view 'index'
    return render(request, 'teste/index.html')  # Ajuste o caminho do template conforme necessário

def registrar_humano(request):
    if request.method == "POST":
        texto_pensamento = request.POST.get('texto_pensamento')
        texto_sonho = request.POST.get('texto_sonho')

        if texto_pensamento or texto_sonho:
            Humano.objects.create(
                texto_pensamento=texto_pensamento,
                texto_sonho=texto_sonho
            )

    return render(request, 'teste/registrar_pensamento.html', {'humanos': Humano.objects.all()})
