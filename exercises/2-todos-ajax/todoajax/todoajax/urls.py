from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todoajax.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^todos/', include('todos_api.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
