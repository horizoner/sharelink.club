# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=256)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('flag', models.SmallIntegerField(default=b'0', max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
