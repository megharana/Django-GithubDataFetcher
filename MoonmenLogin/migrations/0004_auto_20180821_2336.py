# Generated by Django 2.0.6 on 2018-08-21 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoonmenLogin', '0003_savecounter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='savecounter',
            name='id',
        ),
        migrations.AddField(
            model_name='savecounter',
            name='countId',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]
