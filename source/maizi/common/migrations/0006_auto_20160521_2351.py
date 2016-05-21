# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_course_market_page_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_color',
            field=models.CharField(default=b'#429FDA', max_length=50, verbose_name='\u8bfe\u7a0b\u914d\u8272'),
        ),
        migrations.AlterField(
            model_name='careercourse',
            name='course_color',
            field=models.CharField(default=b'#429ADA', max_length=50, verbose_name='\u8bfe\u7a0b\u914d\u8272'),
        ),
    ]
