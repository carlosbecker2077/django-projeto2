# Generated by Django 3.2.5 on 2021-08-09 17:10

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210809_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='imagens',
        ),
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=stdimage.models.StdImageField(blank=True, upload_to='produtos', verbose_name='Imagem'),
        ),
    ]
