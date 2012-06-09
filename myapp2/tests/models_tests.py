"""
Tests for the models of the ``myapp2`` app.

The first thing I usually test is just the creation of the model. If you can
instanciate it and it has a primary key, creation and saving has obviously
worked fine.

After that I would add tests for each method of the model to make sure that
coverage stays at 100%.

"""
from django.test import TestCase

from myapp2.tests.factories import ExampleFactory


class ExampleTestCase(TestCase):
    """Tests for the ``Example`` model class."""
    def test_model(self):
        obj = ExampleFactory()
        self.assertTrue(obj.pk)
