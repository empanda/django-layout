.. _requirements:

============
Requirements
============

`pip`_ uses a requirements file to install specified versions of a project
from the `Python Package Index (PyPI)`_.

.. _pip: http://www.pip-installer.org/
.. _Python Package Index (PYPI): http://pypi.python.org/

We use a ``pip`` to ensure that we can reproduce exact python environments
with specific versions of specific packages.

The exact format of the requirements file can be found in ``pip``'s
`documentation <http://www.pip-installer.org/en/latest/requirements.html>`_.


.. _default-requirements-file:

Default Requirements File
=========================

The default requirements file is broken into sections to make reading it
clearer.


.. _python-requirements:

Python
------

These packages are just general packages that make working with Python in
general easier.


.. _ipython-requirement:

``ipython``
^^^^^^^^^^^

IPython is a replacement Python shell that adds a bunch of useful features
that are lacking in the default shell. The features that I find most
useful are tab completion, class/module help using ``object_name?``, and
history. You can find more out about more features in `the official
documentation`_.

.. _the official documentation: http://ipython.org/ipython-doc/stable/interactive/tutorial.html

.. seealso::


    Documentation
        http://ipython.org/ipython-doc/stable/index.html

    Homepage
        http://ipython.org/

    PyPI
        http://pypi.python.org/pypi/ipython


.. _nose-requirement:

``nose``
^^^^^^^^

nose is a test discoverer and runner for Python code. It makes writing and
running test simple and fast. It also has a vast array of plugins that
extend it's functionality to `capture stdout/stderr`_ and `capture
logging`_, `code coverage reports`_, `test tagging`_ and `skipping`_. nose
has `many other features`_ and I encourage you to experiment with them to
make your testing experience better and faster.

.. _capture stdout/stderr: https://nose.readthedocs.org/en/latest/plugins/capture.html

.. _capture logging: https://nose.readthedocs.org/en/latest/plugins/logcapture.html

.. _code coverage reports: https://nose.readthedocs.org/en/latest/plugins/cover.html

.. _test tagging: https://nose.readthedocs.org/en/latest/plugins/attrib.html

.. _skipping: https://nose.readthedocs.org/en/latest/plugins/skip.html

.. _many other features: https://nose.readthedocs.org/en/latest/plugins/builtin.html

.. seealso::

    Documentation
        https://nose.readthedocs.org/

    PyPI
        http://pypi.python.org/pypi/nose


.. _mock-requirement:

``mock``
^^^^^^^^

mock is a mocking library for Python tests. It is simple to use and very
handy when writing fast tests.

.. seealso::

    Documentation
        http://www.voidspace.org.uk/python/mock/

    PyPI
        http://pypi.python.org/pypi/mock


.. _documentation-requirements:

Documentation
-------------

These packages are used to document your project. They make the writing
and publishing documentation fun and easy.


.. _sphinx-requirement:

``Sphinx``
^^^^^^^^^^

Sphinx is main documentation platform for this project. It is simple to
use, with advanced features available when needed. It uses
`reStructuredText`_ as the backing text format and it is able to produce
output in a bunch of different formats including HTML, PDF, ePub and
others.

.. _reStructuredText: http://sphinx-doc.org/rest.html

.. seealso::

    Documentation
        http://sphinx-doc.org/contents.html

    Homepage
        http://sphinx-doc.org/

    PyPI
        http://pypi.python.org/pypi/Sphinx


.. _jinja-requirement:

``Jinja``
^^^^^^^^^

Jinja is a dependency of Sphinx. It is the package that Sphinx uses as a
templating engine for the HTML output.

.. seealso::

    Documentation
        http://jinja.pocoo.org/docs/

    Homepage
        http://jinja.pocoo.org/

    PyPI
        http://pypi.python.org/pypi/Jinja


.. _pygments-requirement:

``Pygments``
^^^^^^^^^^^^

Pygments is a dependency of Sphinx. It is the package that Sphinx uses to
highlight source code.

.. seealso::

    Documentation
        http://pygments.org/docs/

    Homepage
        http://pygments.org/

    PyPI
        http://pypi.python.org/pypi/Pygments


.. _docutils-requirement:

``docutils``
^^^^^^^^^^^^

docutils is a dependency of Sphinx. It is the package that Sphinx uses to
parse the reStructuredText markup.

.. seealso::

    Documentation
        http://docutils.sourceforge.net/docs/index.html

    Homepage
        http://docutils.sourceforge.net/

    PyPI
        http://pypi.python.org/pypi/docutils


.. _django-requirements:

Django
------

These requirements make Django work at it's best.


.. _django-requirement:

``django``
^^^^^^^^^^

It's Django, nuf said.

.. seealso::

    Documentation
        https://docs.djangoproject.com/en/1.4/

    Homepage
        https://www.djangoproject.com/

    PyPI
        http://pypi.python.org/pypi/Django


.. _pytz-requirement:

``pytz``
^^^^^^^^

pytz is a dependency of Django. It is the package that Django uses to
support timezone lookup and conversion when timezone support is enabled.


.. seealso::

    Documentation
        http://pytz.sourceforge.net/

    PyPI
        http://pypi.python.org/pypi/pytz/


.. _py-bcrypt-requirement:

``py-bcrypt``
^^^^^^^^^^^^^

py-bcrypt is used as an interface to the `bcrypt`_ library to allow for
bcrypt hashing for passwords. It is not a direct dependency of Django, but
we use it with Django's `BCryptPasswordHasher`_.

.. _bcrypt: http://bcrypt.sourceforge.net/

.. _BCryptPasswordHasher: https://docs.djangoproject.com/en/1.4/topics/auth/#using-bcrypt-with-django

.. seealso::

    Homepage
        http://www.mindrot.org/projects/py-bcrypt/

    PyPI
        http://pypi.python.org/pypi/py-bcrypt/


.. _django-utility-apps-requirements:

Django Utility Apps
-------------------

These apps make writing Django applications and site easier.


.. _south-requirement:

``South``
^^^^^^^^^

South enables migrations for Django models. It has become the de-facto
standard for migrations in the Django world. It supports both schema and
data migrations.

.. seealso::

    Documentation:
        http://south.readthedocs.org/en/latest/

    Homepage
        http://south.aeracode.org/

    PyPI
        http://pypi.python.org/pypi/South


.. _django-secure-requirement:

``django-secure``
^^^^^^^^^^^^^^^^^

django-secure is a package containing utilities and a `linter` to help
make your Django site more secure. It provides additional settings to
apply easy security wins usually through the use of specific headers. It
works best with sites that use SSL, but it also provides some benefit for
those who don't.

.. seealso::

    Documentation
        http://django-secure.readthedocs.org/en/latest/

    Homepage
        https://github.com/carljm/django-secure

    PyPI
        http://pypi.python.org/pypi/django-secure


.. _django-debug-toolbar-requirement:

``django-debug-toolbar``
^^^^^^^^^^^^^^^^^^^^^^^^

django-debug-toolbar is a package that adds a lot of additional useful
information to the HTML pages that Django produces while ``DEBUG = True``.
It has panels showing information about SQL queries, templates, settings,
etc.

.. seealso::

    Documentation
        https://github.com/django-debug-toolbar/django-debug-toolbar

    PyPI
        http://pypi.python.org/pypi/django-debug-toolbar


.. _django-nose-requirement:

``django-nose``
^^^^^^^^^^^^^^^

django-nose is a simple package that provides a Django test runner that
will use nose under the covers. It makes sure that nose will correctly
setup and tear down the test database.

.. seealso::

    Documentation
        https://github.com/jbalogh/django-nose

    PyPI
        http://pypi.python.org/pypi/django-nose


.. _factory-boy-requirement:

``factory_boy``
^^^^^^^^^^^^^^^

factory_boy is a package that simplifies the writing of Django model
factories for using in tests. It can be used to create a complex set of
related models which can then be tested against. It is a good alternative
to fixtures.

.. seealso::

    Documentation
        https://factoryboy.readthedocs.org/en/latest/

    Homepage
        https://github.com/dnerdy/factory_boy

    PyPI
        http://pypi.python.org/pypi/factory_boy


.. _django-model-utils-requirement:

``django-model-utils``
^^^^^^^^^^^^^^^^^^^^^^

django-model-utils is a package of handy utility classes for working with
Django models. It incorperates the logic of a lot of different common
model uses, ie ``TimeFramedModel``, ``StatusModel``, and
``TimeStampedModel``.

.. seealso::

    Documentation
        https://github.com/carljm/django-model-utils

    PyPI
        http://pypi.python.org/pypi/django-model-utils


.. _django-apps-requirements:

Django Apps
-----------

These reusable Django apps, get your Django site up and running quickly.


.. _django-compressor-requirement:

``django_compressor``
^^^^^^^^^^^^^^^^^^^^^

django_compressor is a package that extends Django's handling of static
assets. It will combine and minify your CSS and JS assets into files with
unique names that can be cached forever on the client. 

.. seealso::

    Documentation
        http://django_compressor.readthedocs.org/en/latest/

    Homepage
        https://github.com/jezdez/django_compressor

    PyPI
        http://pypi.python.org/pypi/django_compressor


.. _django-appconf-requirement:

``django-appconf``
^^^^^^^^^^^^^^^^^^

django-appconf is a dependency of django_compressor. It provides a unified
way for reusable Django apps to handle settings.

.. seealso::

    Documentation
        https://django-appconf.readthedocs.org/en/latest/

    Homepage
        https://github.com/jezdez/django-appconf

    PyPI
        http://pypi.python.org/pypi/django-appconf


.. _lxml-requirement:

``lxml``
^^^^^^^^

lxml is a dependency of django_compressor. It is an extremely fast HTML
and XML parser.

.. seealso::

    Documentation
        http://lxml.de/index.html#documentation

    Homepage
        http://lxml.de/

    PyPI
        http://pypi.python.org/pypi/lxml


.. _beautifulsoup-requirement:

``BeautifulSoup``
^^^^^^^^^^^^^^^^^

BeautifulSoup is a dependency of django_compressor. It is a slow but very
forgiving HTML and XML parser.

.. seealso::

    Documentation
        http://www.crummy.com/software/BeautifulSoup/bs4/doc/

    Homepage
        http://www.crummy.com/software/BeautifulSoup/

    PyPI
        http://pypi.python.org/pypi/BeautifulSoup


.. _django-waffle-requirement:

``django-waffle``
^^^^^^^^^^^^^^^^^

django-waffle is a package for using feature flipping in Django. It
provides a way to turn features of your app on and off depending on a set
of rules. The rules can be as simple as a switch, or more based on more
complicated logic like staff status or a weighted percentage.

.. seealso::

    Documentation
        http://waffle.readthedocs.org/en/latest/index.html

    Homepage
        https://github.com/jsocol/django-waffle

    PyPI
        http://pypi.python.org/pypi/django-waffle


.. _adding-requirements:

Adding Requirements
===================

When you need new packages to the ``requirements.pip`` file you can follow
these simple steps.

1. Run ``pip freeze > requirements.pip.before`` to record the package
   state as it is now.

#. Install the new package using ``pip install -v package``. Note the
   output towards the bottom that tells you which packages where installed
   to meet all the requirements of the package you installed.

#. Run ``pip freeze > requirements.pip.after`` to record the new package
   state.

#. Run ``diff requirements.pip.before requirements.pip.after`` to see all
   the new lines show which packages and versions that were installed.

#. Manually add the new lines to the ``requirements.pip`` file, placing
   them in the correct section.

#. Run ``rm requirements.pip.before requirements.pip.after`` to cleanup
   the temporary files that were created.

#. **Document the addition in the commit message.** Remember, other
   developers will now need to run ``pip install -v -r requirements.pip``
   to satisfy the additional package requirements.
