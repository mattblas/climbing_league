# Generated by Django 3.2.9 on 2022-01-31 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climbing_ligue', '0008_alter_route_route_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='route_group',
            field=models.CharField(max_length=60, verbose_name='Grupa'),
        ),
    ]