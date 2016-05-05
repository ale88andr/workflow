# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('foundation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incoming',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('identifier', models.CharField(db_index=True, max_length=50, verbose_name='Номер')),
                ('subject', models.CharField(max_length=255, verbose_name='Тема')),
                ('description', models.TextField(verbose_name='Краткое содержание')),
                ('created_at', models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('register_at', models.DateField(verbose_name='Дата регистрации')),
                ('closed', models.BooleanField(verbose_name='В архиве', default=False)),
                ('comment', models.TextField(verbose_name='Комментарии')),
                ('deadline_at', models.DateTimeField(verbose_name='Срок исполнения')),
                ('method_of_dispatch', models.CharField(choices=[('email', 'Email'), ('post', 'Почтой'), ('courier', 'Курьером'), ('self', 'Лично')], verbose_name='Способ получения', default='email', max_length=10)),
                ('completed_at', models.DateTimeField(verbose_name='Дата исполнения')),
                ('sign_of_control', models.BooleanField(db_index=True, verbose_name='Контроль', default=False)),
                ('author', models.ForeignKey(related_name='out_created_by', verbose_name='Автор', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'incoming_documents',
                'verbose_name_plural': 'Входящая корреспонденция',
                'verbose_name': 'Входящий документ',
            },
        ),
        migrations.CreateModel(
            name='Outbound',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('identifier', models.CharField(db_index=True, max_length=50, verbose_name='Номер')),
                ('subject', models.CharField(max_length=255, verbose_name='Тема')),
                ('description', models.TextField(verbose_name='Краткое содержание')),
                ('created_at', models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('register_at', models.DateField(verbose_name='Дата регистрации')),
                ('closed', models.BooleanField(verbose_name='В архиве', default=False)),
                ('comment', models.TextField(verbose_name='Комментарии')),
                ('method_of_forwarding', models.CharField(choices=[('email', 'Email'), ('post', 'Почтой'), ('courier', 'Курьером'), ('self', 'Лично')], verbose_name='Способ отправки', default='email', max_length=10)),
                ('author', models.ForeignKey(related_name='inc_created_by', verbose_name='Автор', to=settings.AUTH_USER_MODEL)),
                ('recipient', models.ForeignKey(related_name='+', verbose_name='Получатель', to='foundation.Organisation')),
                ('reporter', models.ForeignKey(verbose_name='Исполнитель', to=settings.AUTH_USER_MODEL)),
                ('reporter_department', models.ForeignKey(verbose_name='Отдел', to='foundation.Department')),
                ('reporter_organisation', models.ForeignKey(related_name='+', verbose_name='Организация', to='foundation.Organisation')),
            ],
            options={
                'db_table': 'outbound_documents',
                'verbose_name_plural': 'Исходящая корреспонденция',
                'verbose_name': 'Исходящий документ',
            },
        ),
        migrations.CreateModel(
            name='Resolution',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Резолюции, накладываемые на документы',
                'verbose_name': 'Резолюция',
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
            field=models.ForeignKey(related_name='+', verbose_name='Организация', to='foundation.Organisation'),
        ),
        migrations.AddField(
            model_name='incoming',
            name='resolution',
            field=models.ForeignKey(verbose_name='Резолюция', to='documents.Resolution'),
        ),
        migrations.AddField(
            model_name='incoming',
            name='resolution_author',
            field=models.ForeignKey(related_name='resolution_by', verbose_name='Автор резюлюции', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='incoming',
            name='sender',
            field=models.ForeignKey(verbose_name='Отправитель', to='foundation.Organisation'),
        ),
    ]
