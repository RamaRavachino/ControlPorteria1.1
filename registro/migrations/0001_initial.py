# Generated by Django 5.1.3 on 2024-11-28 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroVehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chofer_dni', models.CharField(max_length=20)),
                ('transporte', models.CharField(max_length=100)),
                ('patente_tractor', models.CharField(max_length=20)),
                ('patente_semi', models.CharField(blank=True, max_length=20, null=True)),
                ('remito_ingreso', models.CharField(blank=True, max_length=50, null=True)),
                ('bultos_ingreso', models.IntegerField(blank=True, null=True)),
                ('remito_egreso', models.CharField(blank=True, max_length=50, null=True)),
                ('bultos_egreso', models.IntegerField(blank=True, null=True)),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True)),
                ('fecha_salida', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
