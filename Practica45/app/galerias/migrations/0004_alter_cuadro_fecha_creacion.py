# Generated by Django 3.2 on 2021-12-09 19:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('galerias', '0003_alter_cuadro_fecha_creacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuadro',
            name='fecha_creacion',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
