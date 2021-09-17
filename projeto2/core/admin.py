from django.contrib import admin

from .models import Produto

# Register your models here.


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'preco', 'estoque',
                    'slug', 'dt_inclui', 'dt_altera', 'ativo')
