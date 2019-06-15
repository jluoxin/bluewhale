# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('iwork', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workrecord',
            name='record_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 14, 16, 44, 25, 780000), verbose_name='\u4f1a\u8bae\u65f6\u95f4'),
        ),
    ]
