from django.db import models

from stdimage import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify, upper


# Create your models here.


class Base(models.Model):
    dt_inclui = models.DateField('Data de Incluisão', auto_now_add=True)
    dt_altera = models.DateField('Data de Alteração', auto_now_add=True)
    ativo = models.BooleanField('Ativo?', default=True)
    # incluir depois os usu

    # serve para não ser criado no banco ao fazer o migrate, fica na hierarquia dentro da classe
    class Meta:
        abstract = True


class Produto(Base):
    codigo = models.CharField('Código', max_length=30)
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.DecimalField('Estoque', max_digits=10, decimal_places=3)
    imagem = StdImageField('Imagem', upload_to='produtos', variations={
                           'thumb': (124, 124)}, blank=True)
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return f'{self.codigo} {self.nome}'

    def produto_pre_save(signal, instance, sender, **kwargs):
        """Coisas a serem feitas antes de salvar no banco"""
        instance.slug = slugify(instance.nome)
        instance.codigo = upper(instance.codigo)


# quando o sender for Produto, antes de salvar executa o produto_pre_save
signals.pre_save.connect(Produto.produto_pre_save, sender=Produto)
