# Generated by Django 3.2.9 on 2022-01-31 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climbing_ligue', '0007_auto_20220131_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='route_group',
            field=models.IntegerField(verbose_name='Grupa'),
        ),
    ]
