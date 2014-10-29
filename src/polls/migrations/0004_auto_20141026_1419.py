# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20141026_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='TatoebaEs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('transtext', models.CharField(max_length=200)),
                ('target', models.TextField()),
            ],
            options={
                'db_table': 'tatoeba_en_es',
                'managed': False,
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
            },
            bases=(models.Model,),
        ),
    ]
