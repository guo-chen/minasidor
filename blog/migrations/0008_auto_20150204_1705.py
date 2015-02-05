# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150119_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='number_of_clicks',
        ),
        migrations.AddField(
            model_name='article',
            name='hit_count',
            field=models.IntegerField(default=0, verbose_name='Hits', editable=False),
            preserve_default=True,
        ),
    ]
