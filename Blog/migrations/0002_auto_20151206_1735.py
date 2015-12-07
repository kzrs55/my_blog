# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('author', models.CharField(max_length=100)),
                ('author_email', models.CharField(max_length=100)),
                ('author_ip', models.CharField(max_length=100)),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('hided', models.BooleanField(default=False)),
                ('duoshuo_id', models.CharField(blank=True, max_length=50, null=True)),
                ('duoshuo_user_id', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('url', models.CharField(default='', blank=True, max_length=255, null=True)),
                ('path', models.ImageField(upload_to='upload/images/', blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='comment_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='views_count',
            field=models.IntegerField(default=0),
        ),
    ]
