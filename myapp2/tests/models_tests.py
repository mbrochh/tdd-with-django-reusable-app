"""Tests for the models of the ``myapp`` app."""
from django.test import TestCase

from myapp2.tests.factories import ExampleFactory


class ExampleTestCase(TestCase):
    """Tests for the ``Example`` model class."""
    def test_model(self):
        obj = ExampleFactory()
        self.assertTrue(obj.pk)
