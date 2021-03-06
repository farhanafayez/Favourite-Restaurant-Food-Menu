# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-21 00:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('picky_menu_picker', '0008_auto_20171018_1834'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('contents', models.TextField(help_text='separate by comma', max_length=120)),
                ('excludes', models.TextField(blank=True, help_text='separate by comma', max_length=120, null=True)),
                ('public', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='picky_menu_picker.RestaurantLocation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated', '-timestamp'],
            },
        ),
    ]
