# Generated by Django 4.2.7 on 2023-11-27 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_padaria', '0003_produto_pedidos_itenspedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidos',
            name='nome',
        ),
        migrations.AddField(
            model_name='pedidos',
            name='status_pedido',
            field=models.IntegerField(choices=[(1, 'Aguardando'), (2, 'Finalizado'), (3, 'Cancelado')], default=1),
        ),
    ]
