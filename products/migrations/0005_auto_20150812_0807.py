# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20150812_0340'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='avatar',
            field=models.ImageField(null=True, upload_to=products.models.get_image_path),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to=products.models.get_image_path),
        ),
    ]
