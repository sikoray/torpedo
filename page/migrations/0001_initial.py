# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text1', models.TextField()),
                ('image1', models.ImageField(upload_to='', blank=True)),
                ('text2', models.TextField()),
                ('image2', models.ImageField(upload_to='', blank=True)),
                ('text3', models.TextField()),
                ('image3', models.ImageField(upload_to='', blank=True)),
                ('text4', models.TextField()),
                ('image4', models.ImageField(upload_to='', blank=True)),
                ('text5', models.TextField()),
                ('image5', models.ImageField(upload_to='', blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trademark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('tm1', models.ImageField(upload_to='', blank=True)),
                ('tm2', models.ImageField(upload_to='', blank=True)),
                ('tm3', models.ImageField(upload_to='', blank=True)),
                ('tm4', models.ImageField(upload_to='', blank=True)),
                ('tm5', models.ImageField(upload_to='', blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
