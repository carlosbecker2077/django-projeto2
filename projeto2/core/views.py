from django.shortcuts import redirect, render
from django.contrib import messages

from .forms import ContatoForm, ProdutoModelForm
from .models import Produto

# Create your views here.


def index(request):
    return render(request, 'index.html')


def contato(request):
    form = ContatoForm(request.POST or None)
    if str(request.method) == 'POST':
        if form.is_valid:
            form.send_mail
            messages.success(request, 'Email enviado com sucesso!')
        else:
            messages.error(request, 'erro ao enviar email')
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):
    if request.user.is_authenticated:

        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid:
                form.save()
                messages.success(request, 'Formulário salvo com sucesso!')
                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao salvar formulário')
        else:
            form = ProdutoModelForm()

        context = {
            'form': form
        }

        return render(request, 'produto.html', context)
    else:
        return redirect('nao_logado')


def produto_consulta(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'produto_consulta.html', context)


def nao_logado(request):
    return render(request, 'nao_logado.html')
