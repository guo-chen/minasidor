# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_article_number_of_clicks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='number_of_clicks',
            field=models.IntegerField(default=0, verbose_name='Clicks', editable=False),
        ),
    ]
