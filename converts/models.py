from django.contrib.auth.models import User
from django.db import models


PERIODICITY_CHOICES = (
    ('d', 'daily'),
    ('w', 'weekly'),
    ('f', 'fortnightly'),
    ('m', 'monthly'),
)


class Income(models.Model):
    user = models.ForeignKey(User, related_name='incomes')
    name = models.CharField(max_length=200)
    periodicity = models.CharField(choices=PERIODICITY_CHOICES, max_length=50)
    size = models.DecimalField(max_digits=20, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Expense(models.Model):
    user = models.ForeignKey(User, related_name='expenses')
    name = models.CharField(max_length=200)
    periodicity = models.CharField(choices=PERIODICITY_CHOICES, max_length=50)
    size = models.DecimalField(max_digits=20, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
