# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0003_auto_20150929_1305'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chat',
            options={'ordering': ['-submit_at']},
        ),
        migrations.AlterField(
            model_name='chat',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='chat',
            name='submit_at',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
