from django import forms
from django.core.exceptions import ValidationError

import re


def validate_search(value):
    reg = re.compile('^(\w+)$')
    if not reg.match(value):
        raise ValidationError('%(value)s search does not comply', params={'value': value})


class QuestionForm(forms.Form):

    SORT_FIELD = (
        ('id', 'Id'),
        ('title', 'Заголовок'),
    )

    search = forms.CharField(required=False)
    sort = forms.ChoiceField(choices=SORT_FIELD, required=False)

    def clean_search(self):
        search = self.cleaned_data.get('search')
        if len(search) < 4:
            raise forms.ValidationError('Block!')
        elif not re.compile('^(\w+)$').match(search):
            raise forms.ValidationError('Regexp')

        return search


class NewQuestionForm(forms.Form):

    title = forms.CharField(max_length=150)
    text = forms.CharField()
