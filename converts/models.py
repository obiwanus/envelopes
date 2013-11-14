from django.db import models


class Income(models.Model):
    PERIODICITY_CHOICES = (
        ('W', 'weekly'),
        ('F', 'fortnightly'),
        ('M', 'monthly')
    )

    # TODO: add user
    name = models.CharField("Income name", max_length=200)
    start_date = models.DateTimeField("Date start")
    size = models.DecimalField("Income size (NZD)", max_digits=20, decimal_places=2)
    periodicity = models.CharField(choices=PERIODICITY_CHOICES, max_length=50)


class Expense(models.Model):
    pass
