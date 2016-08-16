# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20160805_0247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trademark',
            name='tm1',
            field=models.ImageField(upload_to=''),
        ),
    ]
