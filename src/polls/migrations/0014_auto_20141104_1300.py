# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20141027_1036'),
    ]

    operations = [
        migrations.CreateModel(
            name='EuconstEnEs',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('source', models.TextField()),
                ('target', models.TextField()),
                ('level', models.IntegerField()),
                ('entrydate', models.DateTimeField(db_column='entryDate')),
            ],
            options={
                'db_table': 'euconst_en_es',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubsEnEs',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('source', models.TextField()),
                ('target', models.TextField()),
                ('level', models.IntegerField()),
                ('entrydate', models.DateTimeField(db_column='entryDate')),
            ],
            options={
                'db_table': 'subs_en_es',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ThelittleprinceEnEs',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('source', models.TextField()),
                ('target', models.TextField()),
                ('level', models.IntegerField()),
                ('entrydate', models.DateTimeField(db_column='entryDate')),
            ],
            options={
                'db_table': 'thelittleprince_en_es',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='GeneralEnEs',
        ),
        migrations.CreateModel(
            name='GeneralEnEs',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('source', models.TextField()),
                ('target', models.TextField()),
                ('level', models.IntegerField()),
                ('entrydate', models.DateTimeField(db_column='entryDate')),
            ],
            options={
                'db_table': 'general_en_es',
            },
            bases=(models.Model,),
        ),
    ]
