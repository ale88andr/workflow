from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.db import models


class Department(models.Model):
    """
    Implement organisation department catalog.
    """
    title = models.CharField(max_length=250, unique=True)

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class Organisation(models.Model):
    """
    Implement resolution catalog.
    """

    TYPE_CHOISES = (
        ('entity', 'Индивидуальный предприниматель'),
        ('organisation', 'Организация'),
        ('individual', 'Физическое лицо'),
    )

    title = models.CharField(max_length=250, unique=True)
    title_short = models.CharField(max_length=50, unique=True)
    entity_type = models.CharField(max_length=50,choices=TYPE_CHOISES)
    okpo = models.IntegerField('ОКПО', max_length=14)
    inn = models.IntegerField('ИНН', max_length=10)
    address = models.CharField('Адресс', max_length=250)
    phone = models.CharField('Телефон', max_length=20)
    mobile = models.CharField('Моб.', max_length=20)
    email = models.EmailField('Электронная почта')

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class UserManager(BaseUserManager):
    """
    Custom user manager
    """
    def create_user(self, firstname, password=None):
        if not firstname:
            raise ValueError('Необходимо указать фамилию')

        user = self.model(
            firstname=firstname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, firstname, password):
        user = self.create_user(firstname, password)
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Employee(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model, which describes organisation employee
    """
    email = models.EmailField(
        'Электронная почта',
        max_length=255,
        unique=True,
        null=True,
        blank=True
    )
    # avatar = models.ImageField(
    #     'Аватар',
    #     blank=True,
    #     null=True,
    #     upload_to="user/avatar"
    # )
    firstname = models.CharField(
        'Фамилия',
        max_length=40,
        unique=True,
        db_index=True
    )
    lastname = models.CharField(
        'Имя',
        max_length=40,
        null=True,
        blank=True
    )
    middlename = models.CharField(
        'Отчество',
        max_length=40,
        null=True,
        blank=True
    )
    date_of_birth = models.DateField(
        'Дата рождения',
        null=True,
        blank=True
    )
    created_at = models.DateField(
        'Дата регистрации',
        auto_now_add=True
    )
    is_active = models.BooleanField(
        'Активен',
        default=True
    )
    organisation = models.ForeignKey(
        Organisation,
        verbose_name='Сотрудник организации',
        null=True,
        blank=True
    )
    department = models.ForeignKey(
        Department,
        verbose_name='Сотрудник отдела',
        null=True,
        blank=True
    )
    can_set_resolution = models.BooleanField(
        'Имеет право накладывать резолюцию?',
        default=False
    )
    phone_number = models.CharField(
        'Номер телефона',
        max_length=20,
        null=True,
        blank=True
    )

    def get_full_name(self):
        return '%s %s. %s.' % (self.firstname, self.lastname[:1], self.middlename[:1])

    def get_username(self):
        if self.lastname:
            return '%s %s' % (self.firstname, self.lastname)
        return self.firstname

    # for backend
    @property
    def is_staff(self):
        return self.is_superuser

    def get_short_name(self):
        return self.firstname

    def __str__(self):
        return self.firstname

    USERNAME_FIELD = 'firstname'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
