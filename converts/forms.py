from django import forms
from converts.models import Income, Expense


class NewIncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        exclude = ('user',)


class NewExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        exclude = ('user',)