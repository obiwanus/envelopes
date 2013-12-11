from django import forms
from converts import models


class IncomeForm(forms.ModelForm):
    class Meta:
        model = models.Income
        exclude = ('user',)


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = models.Expense
        exclude = ('user',)


class GoalForm(forms.ModelForm):
    class Meta:
        model = models.Goal
        exclude = ('user',)