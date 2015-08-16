# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20150812_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='view',
            field=models.IntegerField(default=0),
        ),
    ]
