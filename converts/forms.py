from django import forms
from converts.models import Income, Expense


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        exclude = ('user',)


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        exclude = ('user',)