from django.db import models
from django.utils import timezone
from enum import IntEnum


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.TextField()
    telefone = models.IntegerField()


class PedidoStatus(IntEnum):
    Aguardando = 1
    Finalizado = 2
    Cancelado = 3

class Pedidos(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    status_pedido = models.IntegerField(choices=[(member.value, member.name) for member in PedidoStatus], default=PedidoStatus.Aguardando.value)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT) ## No cascate

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.TextField()
    preco = models.FloatField()


class ItensPedido(models.Model):
    pedido = models.ForeignKey(Pedidos, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()







