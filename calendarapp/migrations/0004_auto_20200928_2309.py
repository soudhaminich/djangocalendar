# Generated by Django 3.1 on 2020-09-28 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0003_auto_20200928_2253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventmember',
            old_name='name',
            new_name='first_name',
        ),
    ]
