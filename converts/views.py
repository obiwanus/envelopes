# coding: utf-8
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from converts.models import Income, Expense, Goal
from converts.forms import IncomeForm, ExpenseForm, GoalForm, NewUserForm


def index(request):
    return render(request, 'index.html')


# Доходы
@login_required(login_url='/admin/')
def incomes(request):
    ctx = {'incomes': Income.objects.all()}
    return render(request, 'incomes.html', ctx)


@login_required(login_url='/admin/')
def income_add(request):
    form = IncomeForm(request.POST or None)
    if form.is_valid():
        income = form.save(commit=False)
        income.user = request.user
        income.save()
        return redirect('incomes')
    return render(request, 'income_add.html', {'form': form})


# Расходы
@login_required(login_url='/admin/')
def expenses(request):
    ctx = {'expenses': Expense.objects.all()}
    return render(request, 'expenses.html', ctx)


@login_required(login_url='/admin/')
def expense_add(request):
    form = ExpenseForm(request.POST or None)
    if form.is_valid():
        expense = form.save(commit=False)
        expense.user = request.user
        expense.save()
        return redirect('expenses')
    return render(request, 'expense_add.html', {'form': form})


@login_required(login_url='/admin/')
def goals(request):
    ctx = {'goals': Goal.objects.all()}
    return render(request, 'goals.html', ctx)


@login_required(login_url='/admin/')
def goal_add(request):
    form = GoalForm(request.POST or None)
    if form.is_valid():
        goal = form.save(commit=False)
        goal.user = request.user
        goal.save()
        return redirect('goals')
    return render(request, 'goal_add.html', {'form': form})


def user_add(request):
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