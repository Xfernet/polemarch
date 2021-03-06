# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 22:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('playbook', models.CharField(max_length=256)),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('stop_time', models.DateTimeField(blank=True, null=True)),
                ('raw_args', models.TextField(default='')),
                ('raw_inventory', models.TextField(default='')),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'default_related_name': 'history',
            },
        ),
        migrations.CreateModel(
            name='HistoryLines',
            fields=[
                ('id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('line', models.TextField(default='')),
                ('line_number', models.IntegerField(default=0)),
                ('history', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='raw_history_line', related_query_name='raw_history_line', to='main.History')),
            ],
            options={
                'default_related_name': 'raw_history_line',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(default=uuid.uuid1, max_length=512)),
            ],
            options={
                'default_related_name': 'inventories',
            },
        ),
        migrations.CreateModel(
            name='PeriodicTask',
            fields=[
                ('id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(default=uuid.uuid1, max_length=512)),
                ('playbook', models.CharField(max_length=256)),
                ('schedule', models.CharField(max_length=4096)),
                ('type', models.CharField(max_length=10)),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='periodic_tasks', related_query_name='periodic_tasks', to='main.Inventory')),
            ],
            options={
                'default_related_name': 'periodic_tasks',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(default=uuid.uuid1, max_length=512)),
                ('repository', models.CharField(max_length=2048)),
                ('status', models.CharField(default='NEW', max_length=32)),
            ],
            options={
                'default_related_name': 'projects',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(default=uuid.uuid1, max_length=256)),
                ('playbook', models.CharField(max_length=256)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', related_query_name='tasks', to='main.Project')),
            ],
            options={
                'default_related_name': 'tasks',
            },
        ),
        migrations.CreateModel(
            name='TypesPermissions',
            fields=[
                ('id', models.AutoField(max_length=20, primary_key=True, serialize=False)),
            ],
            options={
                'default_related_name': 'related_objects',
            },
        ),
        migrations.RemoveField(
            model_name='host',
            name='environment',
        ),
        migrations.AddField(
            model_name='group',
            name='children',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='group',
            name='parents',
            field=models.ManyToManyField(blank=True, null=True, related_name='groups', related_query_name='childrens', to='main.Group'),
        ),
        migrations.AlterField(
            model_name='variable',
            name='value',
            field=models.CharField(max_length=2048, null=True),
        ),
        migrations.AlterIndexTogether(
            name='group',
            index_together=set([('children', 'id'), ('children',)]),
        ),
        migrations.DeleteModel(
            name='Environment',
        ),
        migrations.AddField(
            model_name='typespermissions',
            name='groups',
            field=models.ManyToManyField(blank=True, null=True, related_name='related_objects', related_query_name='related_objects', to='main.Group'),
        ),
        migrations.AddField(
            model_name='typespermissions',
            name='history',
            field=models.ManyToManyField(blank=True, null=True, related_name='related_objects', related_query_name='related_objects', to='main.History'),
        ),
        migrations.AddField(
            model_name='typespermissions',
            name='hosts',
            field=models.ManyToManyField(blank=True, null=True, related_name='related_objects', related_query_name='related_objects', to='main.Host'),
        ),
        migrations.AddField(
            model_name='typespermissions',
            name='inventories',
            field=models.ManyToManyField(blank=True, null=True, related_name='related_objects', related_query_name='related_objects', to='main.Inventory'),
        ),
        migrations.AddField(
            model_name='typespermissions',
            name='periodic_tasks',
            field=models.ManyToManyField(blank=True, null=True, related_name='related_objects', related_query_name='related_objects', to='main.PeriodicTask'),
        ),
        migrations.AddField(
            model_name='typespermissions',
            name='projects',
            field=models.ManyToManyField(blank=True, null=True, related_name='related_objects', related_query_name='related_objects', to='main.Project'),
        ),
        migrations.AddField(
            model_name='typespermissions',
            name='tasks',
            field=models.ManyToManyField(blank=True, null=True, related_name='related_objects', related_query_name='related_objects', to='main.Task'),
        ),
        migrations.AddField(
            model_name='typespermissions',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_objects', related_query_name='related_objects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project',
            name='groups',
            field=models.ManyToManyField(blank=True, null=True, related_name='projects', to='main.Group'),
        ),
        migrations.AddField(
            model_name='project',
            name='hosts',
            field=models.ManyToManyField(blank=True, null=True, related_name='projects', to='main.Host'),
        ),
        migrations.AddField(
            model_name='project',
            name='inventories',
            field=models.ManyToManyField(blank=True, null=True, related_name='projects', to='main.Inventory'),
        ),
        migrations.AddField(
            model_name='periodictask',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='periodic_tasks', related_query_name='periodic_tasks', to='main.Project'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='groups',
            field=models.ManyToManyField(related_name='inventories', to='main.Group'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='hosts',
            field=models.ManyToManyField(related_name='inventories', to='main.Host'),
        ),
        migrations.AddField(
            model_name='history',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', related_query_name='history', to='main.Project'),
        ),
        migrations.AlterIndexTogether(
            name='historylines',
            index_together=set([('line_number',), ('history',), ('history', 'line_number')]),
        ),
        migrations.AlterIndexTogether(
            name='history',
            index_together=set([('id', 'project', 'playbook', 'status', 'start_time', 'stop_time')]),
        ),
    ]
