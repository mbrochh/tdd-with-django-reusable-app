"""
Models for the ``myapp2`` application.

Before implementing anything in this file, you would create
``tests/factories.py`` and ``tests/models_tests.py``. You would use the factory
to test the creation of your model, which will fail, because the model does not
exist, then you would implement your model here.

"""
from django.db import models


class Example(models.Model):
    """Example model class."""
    text = models.TextField(blank=True, null=True)
