# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-30 10:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentHall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=128, primary_key=True, serialize=False, unique=True)),
                ('tag', models.CharField(max_length=256, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='HallDistances',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distance', models.FloatField()),
                ('hallA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hallA', to='halls.Hall')),
                ('hallB', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hallB', to='halls.Hall')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, max_length=128, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=512)),
                ('brand', models.CharField(max_length=256)),
                ('price', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductHalls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='halls.Hall')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='halls.Product')),
            ],
        ),
        migrations.AddField(
            model_name='contenthall',
            name='hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='halls.Hall'),
        ),
    ]
