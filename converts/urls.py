from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from converts import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^income/$', views.income, name='income'),
    url(r'^expense/$', views.expense, name='expense'),
    url(r'^income/add/$', views.income_add, name='income_add'),
    url(r'^expense/add/$', views.expense_add, name='expense_add'),
    # url(r'^converts/', include('converts.foo.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
