from django.conf.urls import patterns, url

urlpatterns = patterns('dbsettings.views',
    (r'^$', 'site_settings'),
    (r'^(?P<app_label>[^/]+)/$', 'app_settings'),
)
