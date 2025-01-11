# Generated by Django 5.1.3 on 2025-01-03 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0017_rename_registrocamion_registrocamiones'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registroadministrativos',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='registrocamiones',
            name='egreso',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='registrocamiones',
            name='egreso2',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='registrocamiones',
            name='egreso3',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='registrocamiones',
            name='ingreso',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='registrocamiones',
            name='ingreso2',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='registrocamiones',
            name='ingreso3',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
