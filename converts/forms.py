from django import forms
from converts import models
from django.contrib.auth.models import User


class SettingsForm(forms.ModelForm):
    class Meta:
        model = models.Settings
        exclude = ('user',)


class IncomeForm(forms.ModelForm):
    class Meta:
        model = models.Income
        exclude = ('user',)


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = models.Expense
        exclude = ('user',)


class FundForm(forms.ModelForm):
    class Meta:
        model = models.Fund
        exclude = ('user',)


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')