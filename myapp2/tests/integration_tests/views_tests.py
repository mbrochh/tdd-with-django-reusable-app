"""Tests for the models of the myapp application."""
from django.test import TestCase
from django.core.urlresolvers import reverse


class ExampleTestCase(TestCase):
    """Tests for Example model class."""

    def test_view(self):
        resp = self.client.get(reverse('myapp2_home'))
        self.assertEqual(resp.status_code, 300)
