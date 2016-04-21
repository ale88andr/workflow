from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from documents.models import Department, Organisation
from .models import Employee
from .forms import UserChangeForm
from .forms import UserCreationForm


class UserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = [
        'firstname',
        'lastname',
        'middlename',
        'date_of_birth',
        'email',
        'is_superuser',
    ]

    list_filter = ('is_superuser',)

    fieldsets = (
                (None, {'fields': ('firstname', 'password')}),
                ('Персональная информация:', {
                 'fields': (
                     'lastname',
                     'middlename',
                     'date_of_birth',
                     'email',
                     'phone_number',
                     'can_set_resolution',
                     'department',
                     'organisation'
                 )}),
                ('Привилегии', {'fields': ('is_superuser',)}),
                ('События аккаунта', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'date_of_birth',
                'email',
                'password1',
                'password2'
            )}
         ),
    )

    search_fields = ('firstname',)
    ordering = ('firstname',)
    filter_horizontal = ()

# Регистрация нашей модели
admin.site.register(Employee, UserAdmin)
admin.site.register([Department, Organisation])
admin.site.unregister(Group)
