# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20151206_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='photo_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 10, 12, 21, 18, 268392, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
