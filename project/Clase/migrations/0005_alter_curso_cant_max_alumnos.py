# Generated by Django 5.0.4 on 2024-04-29 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clase', '0004_alter_curso_options_curso_cant_max_alumnos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='cant_max_alumnos',
            field=models.PositiveBigIntegerField(blank=True, default=1000, null=True, verbose_name='Cantidad máxima de alumnos'),
        ),
    ]
