# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendkeywords',
            name='callback_url',
            field=models.URLField(null=True, verbose_name='\u56de\u8c03url', blank=True),
        ),
    ]
