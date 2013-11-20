# coding: utf-8
from django.contrib.auth.models import User
from django.db import models

import datetime


PERIODICITY_CHOICES = (
    ('d', 'Ежедневно'),
    ('w', 'Еженедельно'),
    ('f', 'Раз в две недели'),
    ('m', 'Ежемесячно'),
)


class Income(models.Model):
    user = models.ForeignKey(User, related_name='incomes')
    name = models.CharField('Название', max_length=200)
    periodicity = models.CharField('Периодичность', choices=PERIODICITY_CHOICES, max_length=50, default='f')
    size = models.DecimalField('Размер (NZD)', default=0, max_digits=20, decimal_places=2)
    start_date = models.DateField('Дата начала', default=datetime.date.today())
    end_date = models.DateField('Дата окончания', blank=True, null=True)


class Expense(models.Model):
    user = models.ForeignKey(User, related_name='expenses')
    name = models.CharField('Название', max_length=200)
    periodicity = models.CharField('Периодичность', choices=PERIODICITY_CHOICES, max_length=50)
    size = models.DecimalField('Размер (NZD)', max_digits=20, decimal_places=2)
    start_date = models.DateField('Дата начала', default=datetime.date.today())
    end_date = models.DateField('Последняя трата не позднее', blank=True, null=True)


class Goal(models.Model):
    user = models.ForeignKey(User, related_name='goals')
    name = models.CharField('Название', max_length=200)
    price = models.DecimalField('Стоимость', default=0, max_digits=20, decimal_places=2)
    saved = models.DecimalField('Уже накоплено', default=0, max_digits=20, decimal_places=2)
    start_date = models.DateField('Дата начала накопления', default=datetime.date.today())
    end_date = models.DateField('Цель надо достигнуть к', blank=True, null=True)
    payment_size = models.DecimalField('Размер начислений', default=0, max_digits=20, decimal_places=2)
    payment_periodicity = models.CharField('Периодичность', choices=PERIODICITY_CHOICES, max_length=50, default='f')


class ActualExpense(models.Model):
    user = models.ForeignKey(User, related_name='actual_expenses')
    size = models.DecimalField('Размер (NZD)', default=0, max_digits=20, decimal_places=2)
    date = models.DateField('Дата', default=datetime.date.today())
    description = models.CharField('Описание', max_length=255)
    regular_expense = models.ForeignKey(Expense, related_name='actual_expenses', blank=True, null=True)
