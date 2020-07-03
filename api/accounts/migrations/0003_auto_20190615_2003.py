# Generated by Django 2.0.6 on 2019-06-15 14:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190615_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_role',
        ),
        migrations.AddField(
            model_name='user',
            name='login_attempts_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.BigIntegerField(db_index=True, unique=True, validators=[django.core.validators.MinValueValidator(5000000000), django.core.validators.MaxValueValidator(9999999999)]),
        ),
    ]
