# Generated by Django 2.0.6 on 2019-06-15 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190615_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='reporting_manager',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]
