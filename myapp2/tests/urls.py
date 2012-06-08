from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(r'^example/', include('myapp2.urls')),
)
