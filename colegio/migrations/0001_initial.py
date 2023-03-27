# Generated by Django 4.1.7 on 2023-03-27 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='curso',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'duenomascota',
            },
        ),
        migrations.CreateModel(
            name='estudiante',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('materia', models.TextField()),
                ('estado', models.BooleanField(default=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colegio.curso')),
            ],
            options={
                'db_table': 'animal',
            },
        ),
    ]
