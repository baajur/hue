# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-01-02 06:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaInstall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installed_example', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='QueryHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.TextField()),
                ('last_state', models.IntegerField(db_index=True)),
                ('has_results', models.BooleanField(default=False)),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('server_id', models.CharField(max_length=1024, null=True)),
                ('server_guid', models.CharField(default=None, max_length=1024, null=True)),
                ('statement_number', models.SmallIntegerField(default=0)),
                ('operation_type', models.SmallIntegerField(null=True)),
                ('modified_row_count', models.FloatField(null=True)),
                ('log_context', models.CharField(max_length=1024, null=True)),
                ('server_host', models.CharField(default='', help_text='Host of the query server.', max_length=128)),
                ('server_port', models.PositiveIntegerField(default=10000, help_text='Port of the query server.')),
                ('server_name', models.CharField(default='', help_text='Name of the query server.', max_length=128)),
                ('server_type', models.CharField(choices=[('beeswax', 'Beeswax'), ('hiveserver2', 'Hive Server 2'), ('mysql', 'MySQL'), ('postgresql', 'PostgreSQL'), ('sqlite', 'sqlite'), ('oracle', 'oracle')], default='beeswax', help_text='Type of the query server.', max_length=128)),
                ('query_type', models.SmallIntegerField(choices=[(0, 'HQL'), (1, 'IMPALA')], default=0, help_text='Type of the query.')),
                ('notify', models.BooleanField(default=False)),
                ('is_redacted', models.BooleanField(default=False)),
                ('extra', models.TextField(default='{}')),
                ('is_cleared', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-submission_date'],
            },
        ),
        migrations.CreateModel(
            name='SavedQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('data', models.TextField(max_length=65536)),
                ('name', models.CharField(max_length=80)),
                ('desc', models.TextField(max_length=1024)),
                ('mtime', models.DateTimeField(auto_now=True)),
                ('is_auto', models.BooleanField(db_index=True, default=False)),
                ('is_trashed', models.BooleanField(db_index=True, default=False, help_text='If this query is trashed.', verbose_name='Is trashed')),
                ('is_redacted', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-mtime'],
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_code', models.PositiveSmallIntegerField()),
                ('secret', models.TextField(max_length='100')),
                ('guid', models.TextField(max_length='100')),
                ('server_protocol_version', models.SmallIntegerField(default=0)),
                ('last_used', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Last used')),
                ('application', models.CharField(default='beeswax', help_text='Application we communicate with.', max_length=128)),
                ('properties', models.TextField(default='{}')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='queryhistory',
            name='design',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beeswax.SavedQuery'),
        ),
        migrations.AddField(
            model_name='queryhistory',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='HiveServerQueryHistory',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('beeswax.queryhistory',),
        ),
    ]