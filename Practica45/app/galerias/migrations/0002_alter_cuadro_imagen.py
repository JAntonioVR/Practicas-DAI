# Generated by Django 3.2 on 2021-12-09 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galerias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuadro',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
    ]
