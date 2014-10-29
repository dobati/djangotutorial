# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20141027_0925'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='userinput',
            table='polls_userinput',
        ),
    ]
