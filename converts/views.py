# coding: utf-8
from datetime import datetime
from dateutil import rrule
from dateutil.relativedelta import relativedelta
from django.db.models import Q
from django.shortcuts import render, redirect
from django.conf import settings
from converts.models import Income, Expense, Fund
from converts.forms import IncomeForm, ExpenseForm, FundForm


def get_dates(start, periodicity, end=None):
    """ Returns an rrule based on provided parameters """
    freq, interval = rrule.WEEKLY, 1
    if periodicity == 'd':
        freq = rrule.DAILY
    elif periodicity == 'w':
        freq = rrule.WEEKLY
    elif periodicity == 'f':
        freq, interval = rrule.WEEKLY, 2
    elif periodicity == '4w':
        freq, interval = rrule.WEEKLY, 4
    elif periodicity == 'm':
        freq = rrule.MONTHLY
    return rrule.rrule(freq, interval=interval, dtstart=start, until=end)


def get_periods():
    """
    Returns the rrule of periods based on settings
    """
    return get_dates(settings.START_DATE, periodicity=settings.PERIOD_LENGTH)


def get_relativedelta(periodicity):
    params = {
        'd': dict(days=1),
        'w': dict(weeks=1),
        'f': dict(weeks=2),
        '4w': dict(weeks=4),
        'm': dict(months=1),
    }
    return relativedelta(**params[periodicity])


def index(request):
    today = datetime.today()
    try:
        selected_date = datetime.strptime(request.GET.get('d'), '%Y-%m-%d')
    except (ValueError, TypeError):
        # Today by default
        selected_date = today
    if selected_date.date() < settings.START_DATE:
        # There's nothing to show before the start date
        return redirect('index')

    # Get the periods info
    periods = get_periods()
    period_start = periods.before(selected_date + relativedelta(days=1))
    period_end = period_start + get_relativedelta(settings.PERIOD_LENGTH) + relativedelta(days=-1)

    # Get all regular expenses for this period
    expenses = Expense.objects.filter(Q(start_date__lte=period_end.date()) | Q(end_date__gte=period_start.date()))

    # Get each day of the current period
    days = []
    for dt in rrule.rrule(rrule.DAILY, dtstart=period_start, until=period_end):
        day = {
            'date': dt,
            'status': '' if dt > today else 'today' if dt.date() == today.date() else 'passed',
            'expenses': [e for e in expenses if dt in list(get_dates(e.start_date, e.periodicity).between(period_start, period_end, inc=True))],
            'incomes': [],
            'funds': [],
        }
        days.append(day)

    return render(request, 'index.html', {
        'period_start': period_start,
        'period_end': period_end,
        'next': periods.after(selected_date),
        'prev': periods.before(period_start),
        'days': days,
    })


def regular_incomes_list(request):
    ctx = {'incomes': Income.objects.all()}
    return render(request, 'incomes.html', ctx)


def regular_income_add(request):
    form = IncomeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('incomes')
    return render(request, 'income_add.html', {'form': form})


def regular_expenses_list(request):
    ctx = {'expenses': Expense.objects.all()}
    return render(request, 'expenses.html', ctx)


def regular_expense_add(request):
    form = ExpenseForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('expenses')
    return render(request, 'expense_add.html', {'form': form})


def funds_list(request):
    ctx = {'funds': Fund.objects.all()}
    return render(request, 'funds.html', ctx)


def fund_add(request):
    form = FundForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('funds')
    return render(request, 'fund_add.html', {'form': form})
