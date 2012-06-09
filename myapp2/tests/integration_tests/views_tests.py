"""
Tests for the models of the myapp application.

Even just stupidly calling every view and checking for status code 200 can be
a life saver. You could, for example, insert a bad use of a template filter
which would cause an exeption when rendering your template. Your unit tests
would never be able to find this, but by just calling the view here you will
force it's template to render itself and you would be aware of such tricky
bugs.

"""
from django.test import TestCase
from django.core.urlresolvers import reverse


class ExampleTestCase(TestCase):
    """Tests for Example model class."""

    def test_view(self):
        resp = self.client.get(reverse('myapp2_home'))
        self.assertEqual(resp.status_code, 200)
