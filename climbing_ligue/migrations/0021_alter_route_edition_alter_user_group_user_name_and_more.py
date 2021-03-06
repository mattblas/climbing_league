# Generated by Django 4.0.2 on 2022-02-19 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('climbing_ligue', '0020_alter_active_edition_edition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='edition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='climbing_ligue.active_edition', verbose_name='Edycja'),
        ),
        migrations.AlterField(
            model_name='user_group',
            name='user_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='user_routes',
            name='user_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='user_routes',
            name='user_routes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='climbing_ligue.route', verbose_name='Routes'),
        ),
    ]
