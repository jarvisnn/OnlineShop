# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20151206_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(default=None, blank=True, null=True, upload_to=products.models.get_image_path),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(default=None, blank=True, null=True, upload_to=products.models.get_image_path),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(default=None, blank=True, null=True, upload_to=products.models.get_image_path),
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(default=None, blank=True, null=True, upload_to=products.models.get_image_path),
        ),
        migrations.AddField(
            model_name='product',
            name='image5',
            field=models.ImageField(default=None, blank=True, null=True, upload_to=products.models.get_image_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='avatar',
            field=models.ImageField(default=None, upload_to=products.models.get_image_path, null=True),
        ),
    ]
