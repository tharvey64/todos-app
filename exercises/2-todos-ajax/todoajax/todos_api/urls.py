from django.conf.urls import patterns, include, url
from django.contrib import admin
import todos_api.views as view

urlpatterns = patterns('',
    url(r'^$', view.index_view, name='index-view'),
    url(r'^get_incomplete/$', view.incomplete, name='incomplete'),
    url(r'^get_todos/$', view.list, name='list-view'),
    url(r'^add_todo/(?P<key>[0-9a-z]+)/$', view.add, name='add-view'),
    url(r'^get_todos/$', view.date, name='date-view'),
    url(r'^update/$', view.update, name='update-view'),
    url(r'^delete/$', view.delete, name='delete'),
    url(r'^done/$', view.done, name='done'),
    url(r'^new_user/$', view.new_user, name='new-user'),
    url(r'^sign_in/$', view.sign_in, name='sign-in'),
    url(r'^log_out/$', view.log_out, name='log-out'),
    url(r'^[.]+', view.invalid_url, name='invalid-url'),
)