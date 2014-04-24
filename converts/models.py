# coding: utf-8
from django.contrib.auth.models import User
from django.db import models

import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver


PERIODICITY_CHOICES = (
    ('d', 'Ежедневно'),
    ('w', 'Еженедельно'),
    ('f', 'Раз в две недели'),
    ('4w', 'Раз в четыре недели'),
    ('m', 'Ежемесячно'),
)


class Settings(models.Model):
    user = models.OneToOneField(User, related_name='settings')
    start_date = models.DateField('Начало первого расчетного периода', default=datetime.date.today())
    period_length = models.CharField(
        'Длина периода',
        max_length=2,
        default='f',
        choices=(('w', 'Неделя'), ('f', '2 недели'), ('4w', '4 недели'), ('m', 'Месяц')),
    )


@receiver(post_save, sender=User)
def create_settings(sender, instance, created=False, **kwargs):
    """ Creates default settings for a user """
    if created:
        Settings.objects.create(user=instance)


class Income(models.Model):
    user = models.ForeignKey(User, related_name='incomes')
    name = models.CharField('Название', max_length=200, db_index=True)
    periodicity = models.CharField('Периодичность', choices=PERIODICITY_CHOICES, max_length=50, default='f')
    size = models.DecimalField('Размер (NZD)', default=0, max_digits=20, decimal_places=2)
    start_date = models.DateField('Дата начала', default=datetime.date.today())
    end_date = models.DateField('Дата окончания', blank=True, null=True)


class Expense(models.Model):
    user = models.ForeignKey(User, related_name='expenses')
    name = models.CharField('Название', max_length=200, db_index=True)
    periodicity = models.CharField('Периодичность', choices=PERIODICITY_CHOICES, max_length=50, default='f')
    size = models.DecimalField('Размер (NZD)', default=0, max_digits=20, decimal_places=2)
    start_date = models.DateField('Дата начала', default=datetime.date.today())
    end_date = models.DateField('Последняя трата не позднее', blank=True, null=True)

    def __str__(self):
        return '%s (%s)' % (self.name, self.size)


class Fund(models.Model):
    """ Sum of money saved on a particular purpose """
    user = models.ForeignKey(User, related_name='funds')
    name = models.CharField('Название', max_length=200, db_index=True)
    price = models.DecimalField('Стоимость', default=0, max_digits=20, decimal_places=2)
    saved = models.DecimalField('Уже накоплено', default=0, max_digits=20, decimal_places=2)
    start_date = models.DateField('Дата начала накопления', default=datetime.date.today())
    end_date = models.DateField('Цель надо достигнуть к', blank=True, null=True)
    payment_size = models.DecimalField('Размер начислений', default=0, max_digits=20, decimal_places=2)
    payment_periodicity = models.CharField('Периодичность начислений',
                                           choices=PERIODICITY_CHOICES, max_length=50, default='f')


class ActualExpense(models.Model):
    user = models.ForeignKey(User, related_name='actual_expenses')
    name = models.CharField('Название', max_length=255, default='', db_index=True)
    size = models.DecimalField('Размер (NZD)', default=0, max_digits=20, decimal_places=2)
    date = models.DateField('Дата', default=datetime.date.today())
    regular_expense = models.ForeignKey(Expense, related_name='actual_expenses', blank=True, null=True)
