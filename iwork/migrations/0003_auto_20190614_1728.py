# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('iwork', '0002_auto_20190614_1644'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workrecord',
            options={'verbose_name': '\u4f1a\u8bae\u8bb0\u5f55', 'verbose_name_plural': '\u4f1a\u8bae\u8bb0\u5f55p'},
        ),
        migrations.AlterField(
            model_name='workrecord',
            name='record_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 14, 17, 28, 3, 36000), verbose_name='\u4f1a\u8bae\u65f6\u95f4'),
        ),
    ]
