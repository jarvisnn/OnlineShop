# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('customer', models.CharField(max_length=200)),
                ('phoneNumber', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('note', models.TextField()),
                ('status', models.CharField(max_length=200)),
                ('products', models.CharField(max_length=200)),
            ],
        ),
    ]
