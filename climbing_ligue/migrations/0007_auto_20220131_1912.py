# Generated by Django 3.2.9 on 2022-01-31 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climbing_ligue', '0006_alter_route_edition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='points',
            field=models.FloatField(verbose_name='Punktacja'),
        ),
        migrations.AlterField(
            model_name='route',
            name='route_group',
            field=models.IntegerField(default='1', verbose_name='Grupa'),
        ),
    ]
