# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_recommendkeywords_callback_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommendkeywords',
            name='callback_url',
        ),
    ]
