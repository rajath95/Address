# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abook', '0006_auto_20171018_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stat',
            name='average',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='stat',
            name='fifties',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='stat',
            name='fours',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='stat',
            name='sixes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='stat',
            name='strike_rate',
            field=models.IntegerField(verbose_name='Strike Rate', null=True),
        ),
    ]
