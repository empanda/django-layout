============
Installation
============

Pre-Requisites
===============

* `setuptools <http://pypi.python.org/pypi/setuptools>`_
* `virtualenv <http://pypi.python.org/pypi/virtualenv>`_
* `PostgreSQL <http://www.postgresql.org/>`_


Creating the Virtual Environment
================================

First, create a clean base environment using virtualenv::

    virtualenv --no-site-packages --distribute {{ project_name }}
    cd {{ project_name }}
    source bin/activate


Installing the Project
======================

Install the requirements and the project source::

    cd path/to/your/{{ project_name }}/repository
    pip install -r requirements.pip
    pip install -e .


Configuring a Local Environment
===============================

If you're just checking the project out locally, you can copy some example
configuration files to get started quickly::

    cp {{ project_name }}/settings/local.py.example {{ project_name }}/settings/local.py

You'll need to configure the DATABASES setting in ``{{ project_name
}}/settings/local.py``. Change ``db_user`` and ``db_password`` as needed.

.. code-block:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': '{{ project_name }}',
            'USER': 'db_user',
            'PASSWORD': 'db_password',
            'HOST': '',
            'PORT': '',
        }
    }

.. note::
    ``HOST`` defaults to ``localhost`` and ``PORT`` defaults to ``5432``.
    You can leave those options blank to just use the defaults.

Lastly, sync the database and run all the database migrations::

    manage.py syncdb --migrate


Building Documentation
======================

Documentation is available in ``docs`` and can be built into a number of 
formats using `Sphinx <http://pypi.python.org/pypi/Sphinx>`_. To get started::

    cd docs
    make html

This creates the documentation in HTML format at ``docs/_build/html``.
