# coding: utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from converts.models import Income, Expense
from converts.forms import NewIncomeForm, NewExpenseForm


def index(request):
    return render(request, 'index.html')


# Доходы
def income(request):
    context = {'incomes': Income.objects.all()}
    return render(request, 'income.html', context)


@login_required(login_url='/admin/')
def income_add(request):
    form = NewIncomeForm(request.POST or None)
    if form.is_valid():
        income = form.save(commit=False)
        income.user = request.user
        income.save()
        return redirect('income')
    return render(request, 'income_add.html', {'form': form})


# Расходы
def expense(request):
    context = {'expenses': Expense.objects.all()}
    return render(request, 'expense.html', context)


@login_required(login_url='/admin/')
def expense_add(request):
    form = NewExpenseForm(request.POST or None)
    if form.is_valid():
        expense = form.save(commit=False)
        expense.user = request.user
        expense.save()
        return redirect('expense')
    return render(request, 'expense_add.html', {'form': form})
