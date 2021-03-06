# Generated by Django 2.0.6 on 2019-06-15 11:54

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='APIConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(max_length=128)),
                ('usage_type', models.CharField(choices=[('celery', 'CELERY'), ('init', 'INIT')], max_length=16)),
                ('value', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('text_value', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'verbose_name': 'APIConfig',
                'verbose_name_plural': "APIConfig's",
                'db_table': 'api_config',
            },
        ),
    ]
