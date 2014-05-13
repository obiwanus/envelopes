# coding: utf-8
import datetime
from django.db import models


PERIODICITY_CHOICES = (
    ('d', 'Ежедневно'),
    ('w', 'Еженедельно'),
    ('f', 'Раз в две недели'),
    ('4w', 'Раз в четыре недели'),
    ('m', 'Ежемесячно'),
)


class Category(models.Model):
    name = models.CharField('Название', max_length=255)


class Income(models.Model):
    name = models.CharField('Название', max_length=200, db_index=True)
    periodicity = models.CharField('Периодичность', choices=PERIODICITY_CHOICES, max_length=50, default='f')
    size = models.DecimalField('Размер (NZD)', default=0, max_digits=20, decimal_places=2)
    start_date = models.DateField('Дата начала', default=datetime.date.today())
    end_date = models.DateField('Дата окончания', blank=True, null=True)


class Expense(models.Model):
    name = models.CharField('Название', max_length=200, db_index=True)
    periodicity = models.CharField('Периодичность', choices=PERIODICITY_CHOICES, max_length=50, default='f')
    size = models.DecimalField('Размер (NZD)', default=0, max_digits=20, decimal_places=2)
    start_date = models.DateField('Дата начала', default=datetime.date.today())
    end_date = models.DateField('Последняя трата не позднее', blank=True, null=True)

    def __str__(self):
        return '%s (%s)' % (self.name, self.size)


class Fund(models.Model):
    """ Sum of money saved on a particular purpose """
    name = models.CharField('Название', max_length=200, db_index=True)
    price = models.DecimalField('Стоимость', default=0, max_digits=20, decimal_places=2)
    saved = models.DecimalField('Уже накоплено', default=0, max_digits=20, decimal_places=2)
    start_date = models.DateField('Дата начала накопления', default=datetime.date.today())
    end_date = models.DateField('Цель надо достигнуть к', blank=True, null=True)
    payment_size = models.DecimalField('Размер начислений', default=0, max_digits=20, decimal_places=2)
    payment_periodicity = models.CharField('Периодичность начислений', blank=True, null=True,
                                           choices=PERIODICITY_CHOICES, max_length=50, default='f')


class ActualExpense(models.Model):
    name = models.CharField('Название', max_length=255, default='', db_index=True)
    size = models.DecimalField('Размер (NZD)', default=0, max_digits=20, decimal_places=2)
    date = models.DateField('Дата', default=datetime.date.today())
    regular_expense = models.ForeignKey(Expense, related_name='actual_expenses', blank=True, null=True)
