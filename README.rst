Test Driven Development with Django Reusable Apps
=================================================

This is the code for my talk at PyCon APAC 2012 about test driven development
with Django reusable apps.

Video: https://www.youtube.com/watch?v=bAo9HcLt8NQ

Slides: https://speakerdeck.com/u/mbrochh/p/tdd-with-django

There is another repository that covers the code for Django projects:
https://github.com/mbrochh/tdd-with-django-project

This is an example repository structure that should show how you can layout a
Django reusable app so that if fulfills the following criteria:

* is ready for test driven development
* can be tested on travis.ci.org
* can be uploaded to the Python package index

This code can be used by anyone for anything! I am using this code as a
template for reusable apps myself, therefore I included a LICENSE file. Just
replace ``Your Name`` with your name when you kickstart a new reusable app from
this code.

Also, you might want to delete all the above text and kickstart your real
README with the content below:

Replace all occurrences of ``your-name``,  ``your-app-name``, ``package_name``,
``your-url``

Installation
------------

If you want to install the latest stable release from PyPi::

    $ pip install your-app-name

If you feel adventurous and want to install the latest commit from GitHub::

    $ pip install -e git://github.com/yourname/your-app-name.git#egg=package_name

Add ``package_name`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'package_name',
    )

Hook this app into your ``urls.py``::

    urlpatterns = patterns('',
        ...
        url(r'^your-url/$', include('package_name.urls')),
    )

Usage
-----

TODO: Describe usage, for example:

* ``./manage.py syncdb --migrate``
* ``./manage.py collectstatic``

Contribute
----------

If you want to contribute to this project, please perform the following steps::

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 django-online-docs
    $ pip install -r requirements.txt
    $ ./online_docs/tests/runtests.sh
    # You should get no failing tests

    $ git co -b feature_branch master
    # Implement your feature and tests
    $ git add . && git commit
    $ git push origin feature_branch
    # Send us a pull request for your feature branch

Whenever you run the tests a coverage output will be generated in
``tests/coverage/index.html``. When adding new features, please make sure that
you keep the coverage at 100%.

Oh and... if you submit patches that make our tests fail, you will be publicly
humiliated on http://travis-ci.org/#!/yourname/your-app-name ;)

If you are making changes that need to be tested in a browser (i.e. to the
CSS or JS files), you might want to setup a Django project, follow the
installation instructions above, then run ``python setup.py develop``. This
will just place an egg-link to your cloned fork in your project's virtualenv.

Roadmap
-------

See the issue list on GitHub for features that are planned for the next
milestone.
