# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shifr', models.CharField(max_length=256)),
                ('deshifr', models.CharField(max_length=256)),
                ('ROT', models.IntegerField()),
            ],
        ),
    ]
