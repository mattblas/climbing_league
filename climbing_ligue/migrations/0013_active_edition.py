# Generated by Django 3.2.9 on 2022-02-06 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climbing_ligue', '0012_alter_user_routes_user_routes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Active_edition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edition', models.IntegerField(verbose_name='Edycja')),
                ('current_edition', models.BooleanField(verbose_name='Bieżąca')),
            ],
        ),
    ]
