from django.urls import path
from .views import index, contato, produto, produto_consulta, nao_logado

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/', produto, name='produto'),
    path('produto_consulta/', produto_consulta, name='produto_consulta'),
    path('naologado/', nao_logado, name='nao_logado')

]
