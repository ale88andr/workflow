from django import forms
from .models import Resolution


class ResolutionForm(forms.ModelForm):
    title = forms.CharField(label='Текст резолюции', max_length=250)

    class Meta:
        model = Resolution
        fields = ('title',)