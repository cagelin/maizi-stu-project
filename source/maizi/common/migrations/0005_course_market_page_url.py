# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_course_career'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='market_page_url',
            field=models.URLField(null=True, verbose_name='\u5730\u5740', blank=True),
        ),
    ]
