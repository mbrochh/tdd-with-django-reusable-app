import os
from setuptools import setup, find_packages
import myapp2


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="myapp2",
    version=myapp2.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    keywords='test, demo, django, app',
    packages=find_packages(),
    author='Martin Brochhaus',
    author_email='mbrochh@gmail.com',
    url="https://github.com/mbrochh/tdd-with-django",
    include_package_data=True,
    test_suite='myapp2.tests.runtests.runtests',
)
