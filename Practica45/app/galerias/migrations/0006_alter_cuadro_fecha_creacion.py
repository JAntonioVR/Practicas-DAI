# Generated by Django 3.2 on 2021-12-10 00:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('galerias', '0005_alter_cuadro_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuadro',
            name='fecha_creacion',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]