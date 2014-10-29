# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20141026_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('translation', models.TextField(max_length=120, null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'userinput',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='TatoebaEnEs',
        ),
        migrations.CreateModel(
            name='TatoebaEnEs',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('source', models.TextField()),
                ('target', models.TextField()),
            ],
            options={
                'db_table': 'tatoeba_en_es',
            },
            bases=(models.Model,),
        ),
    ]
