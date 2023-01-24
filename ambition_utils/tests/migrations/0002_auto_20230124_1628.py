# Generated by Django 2.2.28 on 2023-01-24 16:28

import ambition_utils.fields
from django.db import migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ambition_utils_tests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fakemodel',
            name='cast_time_zone_field',
            field=ambition_utils.fields.TimeZoneField(default='utc'),
        ),
        migrations.AddField(
            model_name='fakemodel',
            name='no_cast_time_zone_field',
            field=timezone_field.fields.TimeZoneField(default='utc'),
        ),
    ]
