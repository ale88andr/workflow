# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('foundation', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Incoming',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('identifier', models.CharField(verbose_name='Номер', max_length=50, db_index=True)),
                ('subject', models.CharField(verbose_name='Тема', max_length=255)),
                ('description', models.TextField(verbose_name='Краткое содержание')),
                ('created_at', models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='Дата обновления', auto_now=True)),
                ('register_at', models.DateField(verbose_name='Дата регистрации')),
                ('closed', models.BooleanField(verbose_name='В архиве', default=False)),
                ('comment', models.TextField(verbose_name='Комментарии')),
                ('deadline_at', models.DateTimeField(verbose_name='Срок исполнения')),
                ('method_of_dispatch', models.CharField(verbose_name='Способ получения', default='email', max_length=10, choices=[('email', 'Email'), ('post', 'Почтой'), ('courier', 'Курьером'), ('self', 'Лично')])),
                ('completed_at', models.DateTimeField(verbose_name='Дата исполнения')),
                ('sign_of_control', models.BooleanField(verbose_name='Контроль', default=False, db_index=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Автор', related_name='out_created_by')),
            ],
            options={
                'verbose_name': 'Входящий документ',
                'verbose_name_plural': 'Входящая корреспонденция',
                'db_table': 'incoming_documents',
            },
        ),
        migrations.CreateModel(
            name='Outbound',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('identifier', models.CharField(verbose_name='Номер', max_length=50, db_index=True)),
                ('subject', models.CharField(verbose_name='Тема', max_length=255)),
                ('description', models.TextField(verbose_name='Краткое содержание')),
                ('created_at', models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='Дата обновления', auto_now=True)),
                ('register_at', models.DateField(verbose_name='Дата регистрации')),
                ('closed', models.BooleanField(verbose_name='В архиве', default=False)),
                ('comment', models.TextField(verbose_name='Комментарии')),
                ('method_of_forwarding', models.CharField(verbose_name='Способ отправки', default='email', max_length=10, choices=[('email', 'Email'), ('post', 'Почтой'), ('courier', 'Курьером'), ('self', 'Лично')])),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Автор', related_name='inc_created_by')),
                ('recipient', models.ForeignKey(to='foundation.Organisation', verbose_name='Получатель', related_name='+')),
                ('reporter', models.ForeignKey(verbose_name='Исполнитель', to=settings.AUTH_USER_MODEL)),
                ('reporter_department', models.ForeignKey(verbose_name='Отдел', to='foundation.Department')),
                ('reporter_organisation', models.ForeignKey(to='foundation.Organisation', verbose_name='Организация', related_name='+')),
            ],
            options={
                'verbose_name': 'Исходящий документ',
                'verbose_name_plural': 'Исходящая корреспонденция',
                'db_table': 'outbound_documents',
            },
        ),
        migrations.CreateModel(
            name='Resolution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Резолюция',
                'verbose_name_plural': 'Резолюции, накладываемые на документы',
            },
        ),
        migrations.AddField(
            model_name='incoming',
            name='outbound_document',
            field=models.ForeignKey(verbose_name='Исполненный документ', to='documents.Outbound'),
        ),
        migrations.AddField(
            model_name='incoming',
            name='reporter',
            field=models.ForeignKey(verbose_name='Исполнитель', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='incoming',
            name='reporter_department',
            field=models.ForeignKey(verbose_name='Отдел', to='foundation.Department'),
        ),
        migrations.AddField(
            model_name='incoming',
            name='reporter_organisation',
            field=models.ForeignKey(to='foundation.Organisation', verbose_name='Организация', related_name='+'),
        ),
        migrations.AddField(
            model_name='incoming',
            name='resolution',
            field=models.ForeignKey(verbose_name='Резолюция', to='documents.Resolution'),
        ),
        migrations.AddField(
            model_name='incoming',
            name='resolution_author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Автор резюлюции', related_name='resolution_by'),
        ),
        migrations.AddField(
            model_name='incoming',
            name='sender',
            field=models.ForeignKey(verbose_name='Отправитель', to='foundation.Organisation'),
        ),
    ]
