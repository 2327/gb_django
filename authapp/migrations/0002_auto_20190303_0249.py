# Generated by Django 2.0.13 on 2019-03-02 21:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 4, 21, 49, 58, 894806, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]