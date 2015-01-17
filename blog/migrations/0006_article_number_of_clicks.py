# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20141217_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='number_of_clicks',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
