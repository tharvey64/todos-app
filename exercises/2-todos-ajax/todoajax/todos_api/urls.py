from django.conf.urls import patterns, include, url
from django.contrib import admin
import todos_api.views as view

urlpatterns = patterns('',
    url(r'^$', view.index_view, name='index-view'),
    url(r'^get_incomplete/(?P<key>[0-9a-z]+)/$', view.incomplete, name='incomplete'),
    url(r'^get_todos/(?P<key>[0-9a-z]+)/$', view.list, name='list-view'),
    url(r'^add_todo/(?P<key>[0-9a-z]+)/$', view.add, name='add-view'),
    url(r'^get_todos/(?P<key>[0-9a-z]+)/(?P<date>[\d]{1,2}[-][\d]{1,2}[-][\d]{4})$', view.date, name='date-view'),
    url(r'^update/(?P<key>[0-9a-z]+)/(?P<task_id>[0-9]+)/$', view.update, name='update-view'),
    url(r'^delete/(?P<key>[0-9a-z]+)/(?P<task_id>[0-9]+)/$', view.delete, name='delete'),
    url(r'^done/(?P<key>[0-9a-z]+)/(?P<task_id>[0-9]+)/$', view.done, name='done'),
    url(r'^new_user/$', view.new_user, name='new-user'),
    url(r'^sign_in/$', view.sign_in, name='sign-in'),
    url(r'^log_out/$', view.log_out, name='log-out'),
    url(r'^[.]+', view.invalid_url, name='invalid-url'),
)