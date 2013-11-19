from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from converts.models import Income
from converts.forms import NewIncomeForm


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


def income_post(request):
    name = Income(name=request.POST['name'])
    return render(request, 'income_post.html')
