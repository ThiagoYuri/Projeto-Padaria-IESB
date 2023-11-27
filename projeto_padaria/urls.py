"""
URL configuration for projeto_padaria project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_padaria import views

urlpatterns = [
    # rota, view responsavel. nome de referência
    path("", views.home, name="home"),
    # Clientes
    path("clientesAdd/", views.clientesAdd, name="add_clientes"),
    path("clientesAddPost/", views.clientesAddPost, name="clientesAddPost"),
    path("clientes/", views.clientes, name="listagem_clientes"),
    # Pedidos
    path("pedidosAdd/", views.pedidosAdd, name="add_pedidos"),
    path("pedidosAddPost/", views.pedidosAddPost, name="pedidosAddPost"),
    path("pedidos/", views.pedidos, name="listagem_pedidos"),

    # Produtos
    path("produtosAdd/", views.produtosAdd, name="add_produtos"),
    path("produtosAddPost/", views.produtosAddPost, name="produtosAddPost"),
    path("produtos/", views.produtos, name="listagem_produtos"),
]
