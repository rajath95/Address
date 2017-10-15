# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('emp_role', models.CharField(max_length=20)),
                ('emp_salary', models.IntegerField(verbose_name='Enter Salary')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=1000)),
                ('aadhaar', models.IntegerField(verbose_name='Enter Aadhaar')),
            ],
        ),
        migrations.AddField(
            model_name='office',
            name='aadhaar',
            field=models.ForeignKey(to='abook.Person'),
        ),
    ]
