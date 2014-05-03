from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from converts import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^incomes/$', views.regular_incomes_list, name='incomes'),
    url(r'^incomes/add/$', views.regular_income_add, name='regular_income_add'),
    url(r'^expenses/$', views.regular_expenses_list, name='expenses'),
    url(r'^expenses/add/$', views.regular_expense_add, name='regular_expense_add'),
    url(r'^funds/$', views.funds_list, name='funds'),
    url(r'^funds/add/$', views.fund_add, name='fund_add'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
