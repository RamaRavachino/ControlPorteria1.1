# Generated by Django 5.1.3 on 2024-12-11 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0005_alter_registrovehiculo_apellido_nombre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='registroadministrativos',
            name='entrada_admin2',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registroadministrativos',
            name='salida_admin1',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='registroadministrativos',
            name='salida_admin2',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
