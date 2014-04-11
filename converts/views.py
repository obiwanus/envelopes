# coding: utf-8
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from converts.models import Income, Expense, Goal, Settings
from converts.forms import IncomeForm, ExpenseForm, GoalForm, NewUserForm, SettingsForm


@login_required
def index(request):
    return render(request, 'index.html')


# Доходы
@login_required
def incomes(request):
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
def expenses(request):
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
def goals(request):
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