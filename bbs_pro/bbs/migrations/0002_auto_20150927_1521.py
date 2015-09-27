# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bbs',
            name='categray',
            field=models.ForeignKey(default=1, to='bbs.Categray'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bbs',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='bbs',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
