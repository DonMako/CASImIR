from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'django.shortcuts.render', {'template_name': 'index.html'}),
)