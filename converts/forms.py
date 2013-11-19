from django import forms
from converts.models import Income


class NewIncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        exclude = ('user',)