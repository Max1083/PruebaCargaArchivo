# Generated by Django 3.2.6 on 2021-08-26 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_centro', models.IntegerField()),
                ('Nom_Centro', models.CharField(max_length=100)),
                ('Region', models.CharField(max_length=100)),
                ('Zona_Centro', models.CharField(max_length=100)),
                ('Cod_Encargado', models.IntegerField()),
            ],
        ),
    ]