from django.contrib import admin
from converts.models import Income, Expense, Fund, ActualExpense


class IncomeAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'size', 'periodicity')


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'size', 'periodicity')


class FundAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'saved', 'payment_size', 'payment_periodicity')


class ActualExpenseAdmin(admin.ModelAdmin):
    list_display = ('size', 'date', 'regular_expense')


class SettingsAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'period_length')


admin.site.register(Income, IncomeAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Fund, FundAdmin)
admin.site.register(ActualExpense, ActualExpenseAdmin)
