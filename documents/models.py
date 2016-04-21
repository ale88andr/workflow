from django.db import models

from foundation.models import Organisation, Department
from workflow.settings import base


class Resolution(models.Model):
    """
    Implement resolution catalog.
    """
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Резолюция'
        verbose_name_plural = 'Резолюции, накладываемые на документы'


class DocumentModel(models.Model):
    """
    An abstract base class model that provides documents fields.
    """

    # enum, list of document dispatches
    DISPATCH_CHOICES = (
        ('email', 'Email'),
        ('post', 'Почтой'),
        ('courier', 'Курьером'),
        ('self', 'Лично'),
    )

    # registry number for document
    identifier = models.CharField('Номер', max_length=50, db_index=True)

    # document subject
    subject = models.CharField('Тема', max_length=255)

    # description of document or text
    description = models.TextField('Краткое содержание')

    # date, when document will be created
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    # date, when document last edited
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    # registration date
    register_at = models.DateField('Дата регистрации')

    # document reporter
    reporter = models.ForeignKey(base.AUTH_USER_MODEL, verbose_name='Исполнитель')

    # department of document reporter
    reporter_department = models.ForeignKey(Department, verbose_name='Отдел')

    # organisation of document reporter
    reporter_organisation = models.ForeignKey(Organisation, verbose_name='Организация', related_name='+')

    # boolean, close sign
    closed = models.BooleanField('В архиве', default=False)

    # document comment
    comment = models.TextField('Комментарии')

    class Meta:
        abstract = True
        ordering = ['-register_at', 'identifier']


class Outbound(DocumentModel):
    """
    Describe structure of outbound correspondents.
    """

    # TODO! files - файлы

    # how document will be delivery, email by default
    method_of_forwarding = models.CharField('Способ отправки', max_length=10, choices=DocumentModel.DISPATCH_CHOICES, default='email')

    # who will be send the document
    recipient = models.ForeignKey(Organisation, verbose_name='Получатель', related_name='+')

    # document author
    author = models.ForeignKey(base.AUTH_USER_MODEL, verbose_name='Автор', related_name='inc_created_by')

    def __str__(self):
        return 'Исх. #%s %s (%s)' % (self.identifier, self.subject, self.author)

    class Meta:
        db_table = 'outbound_documents'
        verbose_name = 'Исходящий документ'
        verbose_name_plural = 'Исходящая корреспонденция'


class Incoming(DocumentModel):
    """
    Describe structure of incoming correspondents.
    """

    # TODO! files - файлы
    # TODO! doers - исполнители

    # shedule time
    deadline_at = models.DateTimeField('Срок исполнения')

    # dispatch method
    method_of_dispatch = models.CharField('Способ получения', max_length=10, choices=DocumentModel.DISPATCH_CHOICES, default='email')

    # document resolution
    resolution = models.ForeignKey(Resolution, verbose_name='Резолюция')

    # user, who will be set resolution
    resolution_author = models.ForeignKey(base.AUTH_USER_MODEL, verbose_name='Автор резюлюции', related_name='resolution_by')

    # date done
    completed_at = models.DateTimeField('Дата исполнения')

    # link to outbound document
    outbound_document = models.ForeignKey(Outbound, verbose_name='Исполненный документ')

    # mark of control
    sign_of_control = models.BooleanField('Контроль', default=False, db_index=True)

    # what organisation send the document
    sender = models.ForeignKey(Organisation, verbose_name='Отправитель')

    # document author
    author = models.ForeignKey(base.AUTH_USER_MODEL, verbose_name='Автор', related_name='out_created_by')

    def __str__(self):
        return 'Вх. #%s %s (%s)' % (self.identifier, self.subject, self.author)

    class Meta:
        db_table = 'incoming_documents'
        verbose_name = 'Входящий документ'
        verbose_name_plural = 'Входящая корреспонденция'
