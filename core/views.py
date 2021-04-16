from django.shortcuts import render
from django.contrib import messages

from .forms import ContatoForm

def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoForm(request.POST or none)

    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            celular = form.cleaned_data['telefone']
            mensagem = form.cleaned_data['mensagem']

            messages.success(request, 'E-mail envidado com sucesso')
            form = ContatoForm()
        else:
            messages.success(request, 'Erro ao enviar o Email')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):
    return render(request, 'produto.html')

