# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(null=True, max_length=255, unique=True, blank=True, verbose_name='Электронная почта')),
                ('firstname', models.CharField(max_length=40, unique=True, db_index=True, verbose_name='Фамилия')),
                ('lastname', models.CharField(null=True, max_length=40, blank=True, verbose_name='Имя')),
                ('middlename', models.CharField(null=True, max_length=40, blank=True, verbose_name='Отчество')),
                ('date_of_birth', models.DateField(null=True, blank=True, verbose_name='Дата рождения')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('can_set_resolution', models.BooleanField(default=False, verbose_name='Имеет право накладывать резолюцию?')),
                ('phone_number', models.CharField(null=True, max_length=20, blank=True, verbose_name='Номер телефона')),
            ],
            options={
                'verbose_name_plural': 'Пользователи',
                'verbose_name': 'Пользователь',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Отделы',
                'verbose_name': 'Отдел',
            },
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('address', models.CharField(max_length=250)),
                ('phone_main', models.CharField(max_length=20)),
                ('phone_minor', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name_plural': 'Организации',
                'verbose_name': 'Организация',
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(null=True, blank=True, to='foundation.Department', verbose_name='Сотрудник отдела'),
        ),
        migrations.AddField(
            model_name='employee',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups', related_name='user_set', to='auth.Group', related_query_name='user'),
        ),
        migrations.AddField(
            model_name='employee',
            name='organisation',
            field=models.ForeignKey(null=True, blank=True, to='foundation.Organisation', verbose_name='Сотрудник организации'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions', related_name='user_set', to='auth.Permission', related_query_name='user'),
        ),
    ]
