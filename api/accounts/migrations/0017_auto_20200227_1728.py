# Generated by Django 2.0.6 on 2020-02-27 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20200227_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpermissions',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]