from django import forms
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
    """
    Форма для обновления данных пользователей. Нужна только для того, чтобы не
    видеть постоянных ошибок "Не заполнено поле password" при обновлении данных
    пользователя.
    """

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
    Log in form
    """
    username = forms.CharField()
    password = forms.CharField()


class EnterpriseForm(forms.ModelForm):

    class Meta:
        abstract = True

    title = forms.CharField(
        label='Полное наименование',
        max_length=120,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text='Полное наименование огранизации, не менее 3-х символов'
    )
    short_title = forms.CharField(
        label='Краткое наименование',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    address_city = forms.CharField(
        label='Город',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    address_street = forms.CharField(
        label='Улица',
        max_length=75,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    address_index = forms.IntegerField(
        label='Индекс',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
    )
    phone = forms.CharField(
        label='Контактный телефон',
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    fax = forms.CharField(
        label='Факс',
        max_length=10,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    ogrn = forms.IntegerField(
        label='ОГРН',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=False
    )
    inn = forms.IntegerField(
        label='ИНН',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=False
    )
    kpp = forms.IntegerField(
        label='КПП',
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        required=False
    )

    # Custom form fields validation

    def clean_address_index(self):
        index = self.cleaned_data.get('address_index')

        if len(str(index)) != 6:
            raise forms.ValidationError('Индекс должен содержать 6 цифр')

        return index

    def clean_ogrn(self):
        ogrn = str(self.cleaned_data.get('ogrn'))

        if len(ogrn) != 13:
            raise forms.ValidationError('ОГРН должен содержать 13 цифр')

        return ogrn

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if len(title) < 3:
            raise forms.ValidationError('Наименование должно быть не менее 3-х символов')

        return title


class MainEnterpriseForm(EnterpriseForm):
    """
    Form for main enterprise
    """

    enterprise_type = forms.ChoiceField(
        label='Организационная форма',
        choices=Enterprise.ENTERPRISE_TYPES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        help_text='В соответствии с гражданским кодексом РФ в России могут создаваться следующие организационные формы предприятий'
    )

    class Meta:
        model = Enterprise
        exclude = ('parent',)


class BranchEnterpriseForm(EnterpriseForm):
    """
    Form for enterprises branch
    """

    enterprise_type = forms.ChoiceField(
        label='Организационная форма',
        choices=Enterprise.BRANCH_TYPES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    parent = forms.ModelChoiceField(
        label='Является филлиалом',
        queryset=Enterprise.objects.all(),
        empty_label=None,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Enterprise
        fields = '__all__'
