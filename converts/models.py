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
    name = models.CharField(u'Название', max_length=200)
    periodicity = models.CharField(u'Периодичность', choices=PERIODICITY_CHOICES, max_length=50, default='f')
    size = models.DecimalField(u'Размер(NZD)', default=0, max_digits=20, decimal_places=2)
    start_date = models.DateField(u'Дата начала', default=datetime.date.today())
    end_date = models.DateField(u'Дата окончания', blank=True, null=True)


class Expense(models.Model):
    user = models.ForeignKey(User, related_name='expenses')
    name = models.CharField(max_length=200)
    periodicity = models.CharField(choices=PERIODICITY_CHOICES, max_length=50)
    size = models.DecimalField(max_digits=20, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
