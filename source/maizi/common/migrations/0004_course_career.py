# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_remove_recommendkeywords_callback_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='career',
            field=models.ForeignKey(verbose_name='\u4ece\u5c5e\u804c\u4e1a\u8bfe\u7a0b', blank=True, to='common.CareerCourse', null=True),
        ),
    ]
