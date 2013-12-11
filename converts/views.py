# coding: utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from converts.models import Income, Expense, Goal
from converts.forms import IncomeForm, ExpenseForm, GoalForm


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
