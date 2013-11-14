from django.contrib import admin
from converts.models import Income


class IncomeAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'size', 'periodicity')

admin.site.register(Income, IncomeAdmin)