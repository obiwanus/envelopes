from django.contrib import admin
from converts.models import Income, Expense, Goal, ActualExpense, Settings


class IncomeAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'size', 'periodicity')


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'size', 'periodicity')


class GoalAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'saved', 'payment_size', 'payment_periodicity')


class ActualExpenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'size', 'date', 'regular_expense')


class SettingsAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_date', 'period_length')


admin.site.register(Income, IncomeAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(ActualExpense, ActualExpenseAdmin)
admin.site.register(Settings, SettingsAdmin)
