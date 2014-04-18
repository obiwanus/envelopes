# coding: utf-8
from datetime import datetime
from dateutil import rrule
from dateutil.relativedelta import relativedelta
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from converts.models import Income, Expense, Goal, Settings
from converts.forms import IncomeForm, ExpenseForm, GoalForm, NewUserForm, SettingsForm


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


def get_user_periods(user):
    """
    Returns the user's rrule of periods based on settings
    """
    return get_dates(user.settings.start_date, periodicity=user.settings.period_length)


def get_relativedelta(periodicity):
    params = {
        'd': dict(days=1),
        'w': dict(weeks=1),
        'f': dict(weeks=2),
        '4w': dict(weeks=4),
        'm': dict(months=1),
    }
    return relativedelta(**params[periodicity])


@login_required
def index(request):
    today = datetime.today()
    user = request.user
    try:
        selected_date = datetime.strptime(request.GET.get('d'), '%Y-%m-%d')
    except (ValueError, TypeError):
        # Today by default
        selected_date = today
    if selected_date.date() < request.user.settings.start_date:
        # There's nothing to show before the start date
        return redirect('index')

    # Get the user's periods info
    periods = get_user_periods(request.user)
    period_start = periods.before(selected_date + relativedelta(days=1))
    period_end = period_start + get_relativedelta(request.user.settings.period_length) + relativedelta(days=-1)

    # Get all regular expenses for this period
    expenses = user.expenses.filter(Q(start_date__lte=period_end.date()) | Q(end_date__gte=period_start.date()))

    # Get each day of the current period
    days = []
    for dt in rrule.rrule(rrule.DAILY, dtstart=period_start, until=period_end):
        day = {
            'date': dt,
            'status': '' if dt > today else 'today' if dt.date() == today.date() else 'passed',
            'expenses': [e for e in expenses if dt in list(get_dates(e.start_date, e.periodicity).between(period_start, period_end, inc=True))],
            'incomes': [],
            'goals': [],
        }
        days.append(day)

    return render(request, 'index.html', {
        'period_start': period_start,
        'period_end': period_end,
        'next': periods.after(selected_date),
        'prev': periods.before(period_start),
        'days': days,
    })


# Доходы
@login_required
def user_incomes(request):
    ctx = {'incomes': Income.objects.all()}
    return render(request, 'incomes.html', ctx)


@login_required
def income_add(request):
    form = IncomeForm(request.POST or None)
    if form.is_valid():
        income = form.save(commit=False)
        income.user = request.user
        income.save()
        return redirect('incomes')
    return render(request, 'income_add.html', {'form': form})


# Расходы
@login_required
def regular_expenses(request):
    ctx = {'expenses': Expense.objects.all()}
    return render(request, 'expenses.html', ctx)


@login_required
def expense_add(request):
    form = ExpenseForm(request.POST or None)
    if form.is_valid():
        expense = form.save(commit=False)
        expense.user = request.user
        expense.save()
        return redirect('expenses')
    return render(request, 'expense_add.html', {'form': form})


@login_required
def user_goals(request):
    ctx = {'goals': Goal.objects.all()}
    return render(request, 'goals.html', ctx)


@login_required
def goal_add(request):
    form = GoalForm(request.POST or None)
    if form.is_valid():
        goal = form.save(commit=False)
        goal.user = request.user
        goal.save()
        return redirect('goals')
    return render(request, 'goal_add.html', {'form': form})


def register(request):
    form = NewUserForm(request.POST or None)
    if form.is_valid():
        email, password = form.cleaned_data['email'], form.cleaned_data['password']
        User.objects.create_user(email, email, password)
        return redirect('index')
    return render(request, 'register.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('index')


@never_cache
def user_login(request):
    form = NewUserForm(request.POST or None)
    if form.is_valid():
        email, password = form.cleaned_data['email'], form.cleaned_data['password']
        user = authenticate(email=email, password=password)
        if user:
            login(request, user)
        else:
            messages.error(request, "Не удалось залогиниться")
            return redirect('login')
        return redirect('index')
    return render(request, 'login.html', {'form': form})


@login_required
def user_settings(request):
    settings, created = Settings.objects.get_or_create(user=request.user)
    form = SettingsForm(request.POST or None, instance=settings)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'settings.html', {'form': form})