from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from converts import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^incomes/$', views.incomes, name='incomes'),
    url(r'^incomes/add/$', views.income_add, name='income_add'),
    url(r'^expenses/$', views.expenses, name='expenses'),
    url(r'^expenses/add/$', views.expense_add, name='expense_add'),
    url(r'^goals/$', views.goals, name='goals'),
    url(r'^goals/add/$', views.goal_add, name='goal_add'),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
