# Generated by Django 5.1.3 on 2024-11-07 15:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='ingresa solo texto', max_length=59, unique=True, verbose_name='Nombre: ')),
            ],
        ),
        migrations.CreateModel(
            name='CLiente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=10, unique=True, verbose_name='Cedula :')),
                ('nombre', models.CharField(max_length=50, verbose_name='Cliente :')),
                ('apellido', models.CharField(max_length=50, verbose_name='Cliente :')),
                ('edad', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
                ('domicilio', models.TextField(help_text='Esribe la referencia de tu domicilio', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre: ')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Precio')),
                ('stock', models.IntegerField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='ventas.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=4)),
                ('CLiente', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='ventas.cliente')),
                ('Producto', models.ManyToManyField(to='ventas.producto')),
            ],
        ),
    ]
