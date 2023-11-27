from django.shortcuts import render, redirect
from app_padaria_aa.models import Cliente
from app_padaria_aa.forms import ClienteForm 

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes') 
    else:
        form = ClienteForm()

    return render(request, 'cadastrar_cliente.html', {'form': form})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})

#estoque
from app_padaria_aa.models import Estoque

def listar_estoque(request):
    estoque = Estoque.objects.all()
    return render(request, 'listar_estoque.html', {'estoque': estoque})

#Reclamações
from django.shortcuts import render, redirect
from app_padaria_aa.models import Reclamacao
from app_padaria_aa.forms import ReclamacaoForm 

def cadastrar_reclamacao(request):
    if request.method == 'POST':
        form = ReclamacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_reclamacoes') 
    else:
        form = ReclamacaoForm()

    return render(request, 'cadastrar_reclamacao.html', {'form': form})

def lista_reclamacoes(request):
    reclamacoes = Reclamacao.objects.all()
    return render(request, 'lista_reclamacoes.html', {'reclamacoes': reclamacoes})

#encomendas
from app_padaria_aa.models import Encomenda
from app_padaria_aa.forms import EncomendaForm  # Você precisa criar um formulário para encomendas

def agendar_encomenda(request):
    if request.method == 'POST':
        form = EncomendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_encomendas')  # Redireciona para a lista de encomendas após o agendamento
    else:
        form = EncomendaForm()
    return render(request, 'agendar_encomenda.html', {'form': form})

def lista_encomendas(request):
    encomendas = Encomenda.objects.all()
    return render(request, 'lista_encomendas.html', {'encomendas': encomendas})

#Pedidos
from app_padaria_aa.models import Pedido
from app_padaria_aa.forms import PedidoForm 

def cadastrar_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            # Obtém a encomenda associada ao pedido
            encomenda = form.cleaned_data['encomenda']
            
            # Salva o pedido associado à encomenda
            pedido = form.save(commit=False)
            pedido.encomenda = encomenda
            pedido.save()

            return redirect('lista_pedidos')
    else:
        form = PedidoForm()

    return render(request, 'cadastrar_pedido.html', {'form': form})

def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'lista_pedidos.html', {'pedidos': pedidos})

