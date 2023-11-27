from django.contrib import admin
from .models import Cliente, Estoque, Reclamacao, Encomenda, Pedido

admin.site.register(Cliente)
admin.site.register(Estoque)
admin.site.register(Reclamacao)
admin.site.register(Encomenda)
admin.site.register(Pedido)