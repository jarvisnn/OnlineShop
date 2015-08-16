# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20150812_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='avatar',
            field=models.ImageField(upload_to=products.models.get_image_path, null=True),
        ),
    ]
