# Generated by Django 2.0.6 on 2020-06-19 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20200619_2327'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='location',
            new_name='job_location',
        ),
    ]
