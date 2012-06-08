"""Views for appname application."""
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'myapp2/home.html'
