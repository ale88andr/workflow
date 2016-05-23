from django import forms
from .models import Resolution

import re


class ResolutionForm(forms.ModelForm):
    title = forms.CharField(label='Текст резолюции', max_length=250)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 3 or not re.compile("^(\w+)$").match(title):
            raise forms.ValidationError('Текст резолюции не должен быть меньше 3-х символов и не содержит спецсимволов')
        return title

    class Meta:
        model = Resolution
        fields = ('title',)


class ResolutionSearchForm(forms.Form):

    SORTED_FIELDS = (
        ('id', '#'),
        ('title', 'Наименование')
    )

    sorted_by = forms.ChoiceField(
        choices=SORTED_FIELDS,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
