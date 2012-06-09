"""
Factories for the ``myapp2`` app.

Always provide factories for all your models. They allow you to setup fixtures
for each test, often in the ``setUp`` method of your test in a very fast and
efficient manner.

"""
import factory

from myapp2.models import Example


class ExampleFactory(factory.Factory):
    FACTORY_FOR = Example

    text = 'Foobar'
