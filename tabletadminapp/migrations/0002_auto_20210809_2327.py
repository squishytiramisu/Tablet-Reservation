# Generated by Django 3.2.5 on 2021-08-09 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabletadminapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foglalas',
            name='tanar',
            field=models.CharField(default='test', max_length=64),
        ),
        migrations.AlterField(
            model_name='foglalas',
            name='mennyiseg',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='foglalas',
            name='oraszam',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='nap',
            name='ev',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='nap',
            name='ho',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='nap',
            name='nap',
            field=models.IntegerField(),
        ),
    ]
