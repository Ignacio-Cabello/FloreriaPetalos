# Generated by Django 2.2.6 on 2019-10-02 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('name', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('calificacion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('name', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('precio', models.IntegerField()),
                ('duracion', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cine.Categoria')),
            ],
        ),
    ]