from django.conf.urls import patterns, include, url
from django.contrib import admin
from deafgrandpa.views import GrandpaView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', GrandpaView.as_view(), name='index'),
)
