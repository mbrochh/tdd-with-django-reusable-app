"""Factories for the ``myapp`` app."""
import factory

from myapp2.models import Example


class ExampleFactory(factory.Factory):
    FACTORY_FOR = Example

    text = 'Foobar'
