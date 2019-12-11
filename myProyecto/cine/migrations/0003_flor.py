# Generated by Django 2.2.6 on 2019-12-10 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cine', '0002_pelicula_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flor',
            fields=[
                ('name', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('valor', models.IntegerField()),
                ('duracion', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(null=True, upload_to='pelis')),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
