# Generated by Django 2.0.6 on 2018-08-21 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoonmenLogin', '0005_auto_20180821_2352'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaveCounterAdvanced',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueId', models.IntegerField(default=1)),
                ('saveCount', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='SaveCounter',
        ),
    ]
