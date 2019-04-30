# Generated by Django 2.1.7 on 2019-04-30 02:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20190429_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2019, 4, 30, 2, 29, 29, 59519, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event_archive',
            name='ev_start_date',
            field=models.DateField(default=datetime.datetime(2019, 4, 30, 2, 29, 29, 61826, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 30, 2, 29, 29, 64384, tzinfo=utc)),
        ),
    ]