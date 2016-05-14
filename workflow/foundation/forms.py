from django import forms
# TODO! from django.forms import ModelForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model

from .models import Enterprise


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Подтверждение',
        widget=forms.PasswordInput
    )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Пароль и подтверждение не совпадают')
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['firstname', ]


class UserChangeForm(forms.ModelForm):

    '''
    Форма для обновления данных пользователей. Нужна только для того, чтобы не
    видеть постоянных ошибок "Не заполнено поле password" при обновлении данных
    пользователя.
    '''
    password = ReadOnlyPasswordHashField(
        widget=forms.PasswordInput,
        required=False
    )

    def save(self, commit=True):
        user = super(UserChangeForm, self).save(commit=False)
        password = self.cleaned_data["password"]
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['firstname', ]


class LoginForm(forms.Form):
    """
    Форма для входа в систему
    """
    username = forms.CharField()
    password = forms.CharField()


class EnterpriseForm(forms.ModelForm):
    title = forms.CharField(
        label='Полное наименование организации',
        max_length=120,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    short_title = forms.CharField(
        label='Краткое наименование',
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    address_city = forms.CharField(
        label='Город',
        max_length=50,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    address_street = forms.CharField(
        label='Улица',
        max_length=75,
        widget=forms.TextInput(attrs={'class':'form-control'})
    )
    address_index = forms.IntegerField(
        label='Индекс',
        widget=forms.NumberInput(attrs={'class':'form-control'})
    )
    phone = forms.CharField(
        label='Контактный телефон',
        max_length=10,
        widget=forms.TextInput(attrs={'class':'form-control'}),
        required=False
    )
    fax = forms.CharField(
        label='Факс',
        max_length=10,
        widget=forms.TextInput(attrs={'class':'form-control'}),
        required=False
    )
    ogrn = forms.IntegerField(
        label='ОГРН',
        widget=forms.NumberInput(attrs={'class':'form-control'})
    )
    inn = forms.IntegerField(
        label='ИНН',
        widget=forms.NumberInput(attrs={'class':'form-control'})
    )
    kpp = forms.IntegerField(
        label='КПП',
        widget=forms.NumberInput(attrs={'class':'form-control'}),
        required=False
    )

    class Meta:
        abstract = True


class MainEnterpriseForm(EnterpriseForm):
    enterprise_type = forms.ChoiceField(
        label='Организационная форма',
        choices=Enterprise.ENTERPRISE_TYPES,
        widget=forms.Select(attrs={'class':'form-control'})
    )

    class Meta:
        model = Enterprise
        exclude = ('parent', )


class BranchEnterpriseForm(EnterpriseForm):
    enterprise_type = forms.ChoiceField(
        label='Организационная форма',
        choices=Enterprise.BRANCH_TYPES,
        widget=forms.Select(attrs={'class':'form-control'})
    )
    parent = forms.ModelChoiceField(
        label='Является филлиалом',
        queryset=Enterprise.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class':'form-control'}),
    )

    class Meta:
        model = Enterprise
        fields = '__all__'
