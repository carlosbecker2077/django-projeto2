# Generated by Django 3.2.5 on 2021-08-09 16:00

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210809_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='codigo',
            field=models.CharField(max_length=30, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='imagens',
            field=stdimage.models.StdImageField(upload_to='produtos', verbose_name='Imagem'),
        ),
    ]