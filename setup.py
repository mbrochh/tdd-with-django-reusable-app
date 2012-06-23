"""
The purpose of this setup.py is to upload this reusable app to the Python
package index so that your potential users can easily install it via
``easy_install`` or ``pip`.  However, you might never need to use this since
you can just host your app on github or bitbucket and use ``pip`` to install it
from there.

In order to test this package with an existing Django project, activate that
project's virtualenv and run::

    python setup.py develop

This will build the app in the same folder and just add a reference to your
virtualenv's easy-install.pth file.

When you are ready for a release you can register your desired package name and
upload yout work.  You need an account at pypi.python.org for this::

    python setup.py register
    python setup.py sdist upload

For more information please see this guide:
http://guide.python-distribute.org/quickstart.html

Replace all occurrences of ``your-app-name``, ``package_name``, ``Your Name``,
``your-name``.

"""
import os
from setuptools import setup, find_packages
import package_name


def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''


setup(
    name="your-app-name",
    version=package_name.__version__,
    description=read('DESCRIPTION'),
    long_description=read('README.rst'),
    license='The MIT License',
    platforms=['OS Independent'],
    keywords='django, app',
    author='Your Name',
    author_email='your-name@gmail.com',
    url="https://github.com/your-name/your-app-name",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django',
    ],
    tests_require=[
        'django-nose',
        'coverage',
        'django-coverage',
    ],
    test_suite='package_name.tests.runtests.runtests',
)
