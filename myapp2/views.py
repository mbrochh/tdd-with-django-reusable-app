"""
Views for the ``myapp2`` application.

Before implementing anything here, you would first create
``tests/implementation_tests/views_tests.py`` and try to call this view via
``self.client.get``. Then you would do the "TDD Dance" and gradually follow
the instructions the failing tests give you. You would add the view to the
``urls.py``, you would import the view in the ``urls.py``, you would finally
implement the view in this file and then add the missing template.

This is a great example how TDD will guide you during your implementation

"""
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'myapp2/home.html'

    def dispatch(self, *args, **kwargs):
        return super(HomeView, self).dispatch(*args, **kwargs)
