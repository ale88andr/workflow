# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foundation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150, verbose_name='Наименование ', unique=True)),
                ('short_title', models.CharField(max_length=75, verbose_name='Краткое наименование', unique=True)),
                ('enterprise_type', models.CharField(max_length=20, verbose_name='Организационная форма', default='gov', choices=[('gov', 'Государственное учреждение')])),
                ('address_city', models.CharField(max_length=50, verbose_name='Город')),
                ('address_street', models.CharField(max_length=75, verbose_name='Улица')),
                ('address_index', models.IntegerField(verbose_name='Индекс')),
                ('phone', models.CharField(max_length=20, verbose_name='Контактный телефон')),
                ('fax', models.CharField(max_length=20, verbose_name='Факс')),
                ('ogrn', models.IntegerField(verbose_name='ОГРН', blank=True, null=True)),
                ('inn', models.IntegerField(verbose_name='ИНН', blank=True, null=True)),
                ('kpp', models.IntegerField(verbose_name='КПП', blank=True, null=True)),
                ('parent', models.ForeignKey(to='foundation.Enterprise', default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='phone_main',
        ),
        migrations.RemoveField(
            model_name='organisation',
            name='phone_minor',
        ),
        migrations.AddField(
            model_name='organisation',
            name='date_of_birth',
            field=models.DateField(verbose_name='Дата рождения', default=None),
        ),
        migrations.AddField(
            model_name='organisation',
            name='entity_type',
            field=models.CharField(max_length=50, verbose_name='Форма', default='entity', choices=[('entity', 'Индивидуальный предприниматель'), ('organisation', 'Организация'), ('individual', 'Физическое лицо')]),
        ),
        migrations.AddField(
            model_name='organisation',
            name='gni',
            field=models.IntegerField(verbose_name='Код ГНИ', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='inn',
            field=models.IntegerField(max_length=10, verbose_name='ИНН', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='ip_firstname',
            field=models.CharField(max_length=50, verbose_name='Фамилия', default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organisation',
            name='ip_lastname',
            field=models.CharField(max_length=50, verbose_name='Имя', default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organisation',
            name='ip_middlename',
            field=models.CharField(max_length=50, verbose_name='Отчество', default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organisation',
            name='kpp',
            field=models.IntegerField(verbose_name='КПП', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='mobile',
            field=models.CharField(max_length=20, verbose_name='Моб.', default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organisation',
            name='okpo',
            field=models.IntegerField(max_length=14, verbose_name='ОКПО', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organisation',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Телефон', default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organisation',
            name='snils',
            field=models.CharField(max_length=14, verbose_name='СНИЛС', default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organisation',
            name='title_short',
            field=models.CharField(max_length=50, verbose_name='Краткое наименование', default=None, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='department',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Наименование отдела', unique=True),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='address',
            field=models.CharField(max_length=250, verbose_name='Адресс'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Наименование', unique=True),
        ),
    ]
