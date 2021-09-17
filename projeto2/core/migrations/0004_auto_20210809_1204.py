# Generated by Django 3.2.5 on 2021-08-09 15:04

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_produto_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='codigo',
            field=models.CharField(error_messages={'required': 'Preencha o código'}, max_length=30, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='imagens',
            field=stdimage.models.StdImageField(error_messages={'required': 'Arquivo necessário'}, upload_to='produtos', verbose_name='Imagem'),
        ),
    ]