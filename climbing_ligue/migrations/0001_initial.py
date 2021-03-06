# Generated by Django 3.2.9 on 2022-01-28 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_name', models.CharField(max_length=60, verbose_name='Nazwa Drogi')),
                ('route_grade', models.CharField(max_length=5, verbose_name='Wycena')),
                ('points', models.FloatField(max_length=30, verbose_name='Punktacja')),
                ('edition', models.CharField(max_length=5, verbose_name='Edycja')),
                ('round', models.CharField(max_length=5, verbose_name='Runda')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='Data dodania')),
            ],
        ),
    ]
