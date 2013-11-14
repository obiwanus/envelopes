from django.shortcuts import render

from converts.models import Income


def income(request):
    context = {'incomes': Income.objects.all()}
    return render(request, 'income.html', context)


def income_add(request):
    return render(request, 'income_add.html')


def income_post(request):
    name = Income(name=request.POST['name'])
    return render(request, 'income_post.html')
