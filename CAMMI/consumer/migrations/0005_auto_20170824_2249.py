# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-24 22:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consumer', '0004_auto_20170817_2230'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ConsumerDatapoint',
            new_name='Profile',
        ),
    ]
