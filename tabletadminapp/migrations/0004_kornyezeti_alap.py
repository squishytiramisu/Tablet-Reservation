# Generated by Django 3.2.5 on 2021-08-16 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabletadminapp', '0003_kornyezeti'),
    ]

    operations = [
        migrations.AddField(
            model_name='kornyezeti',
            name='alap',
            field=models.IntegerField(default=1),
        ),
    ]
