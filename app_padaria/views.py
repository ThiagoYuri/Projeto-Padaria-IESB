from django.shortcuts import render
from .models import Cliente, Pedidos, Produto


# Home
def home(request):
    return render(request, "padaria/home.html")



#Cliente
def clientesAdd(request):
    return render(request, "padaria/cliente/clienteAdd.html")

def clientesAddPost(request):
    novo_cliente = Cliente()
    novo_cliente.nome = request.POST.get("nome")
    novo_cliente.telefone = request.POST.get("telefone")
    novo_cliente.save()
    return render(request, "padaria/cliente/clienteAdd.html")


def clientes(request):         
    # Exibir todos os clientes
    clientes = {"clientes": Cliente.objects.all()}
    # Retomar os dados
    return render(request, "padaria/cliente/clienteList.html", clientes)


#Pedidos
def pedidosAdd(request):
    return render(request, "padaria/pedido/pedidoAdd.html")

def pedidosAddPost(request):
    novo_pedido = Cliente()
    novo_pedido.nome = request.POST.get("nome")
    novo_pedido.telefone = request.POST.get("telefone")
    novo_pedido.save()
    return render(request, "padaria/pedido/pedidoAdd.html")


def pedidos(request):         
    # Exibir todos os pedidos
    pedidos = {"pedidos": Pedidos.objects.all()}
    # Retomar os dados
    return render(request, "padaria/pedido/pedidoList.html", pedidos)



#Produtos
def produtosAdd(request):
    return render(request, "padaria/produto/produtoAdd.html")

def produtosAddPost(request):
    novo_produto = Produto()
    novo_produto.nome = request.POST.get("nome")
    novo_produto.preco = int(request.POST.get("preco"))
    novo_produto.save()
    return render(request, "padaria/produto/produtoAdd.html")


def produtos(request):         
    # Exibir todos os pedidos
    produtos = {"produtos": Produto.objects.all()}
    # Retomar os dados
    return render(request, "padaria/produto/produtoList.html", produtos)