# Generated by Django 5.0.4 on 2024-04-27 16:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clase', '0002_comision'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='curso',
        ),
        migrations.AddField(
            model_name='comision',
            name='curso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Clase.curso'),
        ),
        migrations.AlterField(
            model_name='comision',
            name='nombre',
            field=models.PositiveBigIntegerField(unique=True),
        ),
    ]