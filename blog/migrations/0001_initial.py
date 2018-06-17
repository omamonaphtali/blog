# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import blog.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(blank=True, height_field='height_field', width_field='width_field', null=True, upload_to=blog.models.upload_location)),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('updated', models.TimeField(auto_now=True)),
                ('timestamp', models.TimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-id', '-timestamp', '-updated'],
            },
        ),
    ]
