from django.shortcuts import render
from django.contrib import messages

from .forms import ContatoForm, ProdutoModelForm

def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()

            messages.success(request, 'E-mail envidado com sucesso')
            form = ContatoForm()
        else:
            messages.success(request, 'Erro ao enviar o Email')

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):
    if str(request.method) == 'POST':
        form = ProdutoModelForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()

            messages.success(request, 'Produto salvo com sucesso.')
            form = ProdutoModelForm()
        else:
            messages.success(request, 'Erro ao salvar o produto.')
    else:
        form = ProdutoModelForm()
    context = {
        'form': form
    }
    return render(request, 'produto.html', context)

