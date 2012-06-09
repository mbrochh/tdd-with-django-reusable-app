"""URLs for the myapp2 application."""
from django.conf.urls.defaults import patterns, url

from myapp2.views import HomeView


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='myapp2_home'),
)
