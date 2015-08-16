# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20150812_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='avatar',
            field=models.ImageField(height_field=600, upload_to=products.models.get_image_path, width_field=600, null=True),
        ),
    ]
