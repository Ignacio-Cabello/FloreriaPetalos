# Generated by Django 2.2.6 on 2019-12-10 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cine', '0007_auto_20191210_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelicula',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
