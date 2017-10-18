# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abook', '0002_auto_20171017_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='fifties',
        ),
        migrations.RemoveField(
            model_name='person',
            name='hundreds',
        ),
    ]
