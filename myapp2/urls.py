"""URLs for the myapp application."""
from django.conf.urls.defaults import *

from myapp2.views import HomeView


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='myapp2_home'),
)
