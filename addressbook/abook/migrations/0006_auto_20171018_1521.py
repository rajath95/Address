# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abook', '0005_auto_20171018_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stat',
            name='hundreds',
            field=models.IntegerField(null=True),
        ),
    ]
