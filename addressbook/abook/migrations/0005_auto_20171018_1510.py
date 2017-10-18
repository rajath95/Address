# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abook', '0004_auto_20171018_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('hundreds', models.IntegerField()),
                ('fifties', models.IntegerField()),
                ('sixes', models.IntegerField()),
                ('fours', models.IntegerField()),
                ('strike_rate', models.IntegerField(verbose_name='Strike Rate')),
                ('average', models.IntegerField()),
                ('aadhaar', models.ForeignKey(to='abook.Person')),
            ],
        ),
        migrations.RemoveField(
            model_name='stats',
            name='aadhaar',
        ),
        migrations.DeleteModel(
            name='Stats',
        ),
    ]
