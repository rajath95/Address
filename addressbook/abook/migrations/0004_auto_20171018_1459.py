# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abook', '0003_auto_20171017_1929'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
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
            model_name='office',
            name='aadhaar',
        ),
        migrations.DeleteModel(
            name='Office',
        ),
    ]
