# Generated by Django 4.1.13 on 2024-05-22 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_peliculas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app_peliculas.genero'),
        ),
    ]
