# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 18:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20170624_1944'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-posted',)},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_date',
            new_name='posted',
        ),
    ]
