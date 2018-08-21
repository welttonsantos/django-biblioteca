from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.db.models import Q


def index(request):
    return render(request, 'controle/index.html')

def criar_clientes(request):

    if request.method == 'POST':
        form = ClienteForm(request.POST or None)
        context = {'form': form}
        if form.is_valid():
            form.save()
        return redirect("cliente")
    else:
        form = ClienteForm()
    context = {'form': form}
    return render(request, 'controle/criar_clientes.html', context)

def criar_funcionario(request):

    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
        return redirect("funcionario")
    else:
        form = FuncionarioForm()
    context = {'form': form}
    return render(request, 'controle/criar_funcionario.html', context)

def criar_livro(request):

    if request.method == 'POST':
        form = LivrosForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
        return redirect("livros")
    else:
        form = LivrosForm()
    context = {'form': form}
    return render(request, 'controle/criar_livro.html', context)

def processo(request):

    if request.method == 'POST':
        form = ProcessoForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
        return redirect("processo")
    else:
        form = ProcessoForm()
    context = {'form': form}
    return render(request, 'controle/processo.html', context)

def busca_cliente(request):
    form=BuscaForm()
    if request.method == 'POST':
        nome = request.POST.get('nome')
        clientes = Cliente.objects.filter(nome__icontains=nome)
        return render(request,'controle/busca_cliente.html',{'form':form, 'nome': nome, 'clientes': clientes})
    return render(request,'controle/busca_cliente.html',{'form':form})

def busca_funcionario(request):
    form=BuscaForm()
    if request.method == 'POST':
        nome = request.POST.get('nome')
        funcionarios = Funcionario.objects.filter(nome__icontains=nome)
        return render(request,'controle/busca_funcionario.html',{'form':form, 'nome': nome, 'funcionarios': funcionarios})
    return render(request,'controle/busca_funcionario.html',{'form':form})

def busca_livro(request):
    form=BuscaForm()
    if request.method == 'POST':
        nome = request.POST.get('nome')
        livros = Livros.objects.filter(nome__icontains=nome)
        return render(request,'controle/busca_livro.html',{'form':form, 'nome': nome, 'livros': livros})
    return render(request,'controle/busca_livro.html',{'form':form})

def busca_processo(request):
    form=BuscaForm()
    if request.method == 'POST':
        cliente = request.POST.get('nome')
        processos = Processo.objects.filter(cliente__nome__icontains=cliente)
        return render(request,'controle/busca_processo.html',{'form':form, 'cliente': cliente, 'processos': processos})
    return render(request,'controle/busca_processo.html',{'form':form})

def update_processo(request,processo_id):
    try:
        processos = Processo.objects.get(pk=processo_id)
    except processos.DoesExist:
        raise Http404("Empréstimo não encontrado")

    form=ClienteForm(request.POST or None,instance=processo)
    if form.is_valid():
        form.save()
        return redirect("busca_processo")
    return render (request,'controle/update_processo.html',{'processos':processos, 'form':form})


def update_cliente(request,cliente_id):
    try:
        cliente = Cliente.objects.get(pk=cliente_id)
    except cliente.DoesExist:
        raise Http404("Cliente não encontrado")

    form=ClienteForm(request.POST or None,instance=cliente)
    if form.is_valid():
        form.save()
        return redirect("busca_cliente")
    return render (request,'controle/update_cliente.html',{'cliente':cliente, 'form':form})

def update_funcionario(request,funcionario_id):
    try:
        funcionario = Funcionario.objects.get(pk=funcionario_id)
    except funcionario.DoesNotExist:
        raise Http404("Funcionario não encontrado")

    form=FuncionarioForm(request.POST or None,instance=funcionario)
    if form.is_valid():
        form.save()
        return redirect("busca_funcionario")
    return render (request,'controle/update_funcionario.html',{'funcionario':funcionario, 'form':form})

def update_livro(request,livro_id):
    try:
        livro = Livros.objects.get(pk=livro_id)
    except livro.DoesNotExist:
        raise Http404("Livro não encontrado")

    form=LivrosForm(request.POST or None,instance=livro)
    if form.is_valid():
        form.save()
        return redirect("busca_livros")
    return render (request,'controle/update_livro.html',{'livro':livro, 'form':form})

def delete_cliente(request,cliente_id):
        try:
            cliente = Cliente.objects.get(pk=cliente_id)
        except cliente.DoesNotExist:
            raise Http404("Cliente nao existe")
        cliente.delete()
        return redirect("busca_cliente")

def delete_funcionario(request,funcionario_id):
        try:
            funcionario = Funcionario.objects.get(pk=funcionario_id)
        except funcionario.DoesNotExist:
            raise Http404("Funcionario não existe")
        funcionario.delete()
        return redirect("busca_funcionario")

def delete_livro(request,livro_id):
        try:
            livro = Livros.objects.get(pk=livro_id)
        except livro.DoesNotExist:
            raise Http404("livro não existe")
        livro.delete()
        return redirect("busca_livro")
