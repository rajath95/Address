# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abook', '0007_auto_20171018_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stat',
            name='aadhaar',
            field=models.ForeignKey(null=True, to='abook.Person'),
        ),
    ]
