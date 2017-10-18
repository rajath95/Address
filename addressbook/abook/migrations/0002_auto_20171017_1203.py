# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='fifties',
            field=models.IntegerField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='person',
            name='hundreds',
            field=models.IntegerField(default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='aadhaar',
            field=models.IntegerField(verbose_name='Player No.'),
        ),
    ]
