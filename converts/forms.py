from django import forms
from converts import models


class IncomeForm(forms.ModelForm):
    class Meta:
        model = models.Income


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = models.Expense


class FundForm(forms.ModelForm):
    class Meta:
        model = models.Fund
