# Generated by Django 3.2.9 on 2022-02-01 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('climbing_ligue', '0011_auto_20220201_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_routes',
            name='user_routes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='climbing_ligue.route', verbose_name='Routes'),
        ),
    ]
