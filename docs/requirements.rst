============
Requirements
============

`pip`_ uses a requirements file to install specified versions of a project
from the `Python Package Index (PYPI)`_.

.. _pip: http://www.pip-installer.org/
.. _Python Package Index (PYPI): http://pypi.python.org/

We use a ``pip`` to ensure that we can reproduce exact python environments
with specific versions of specific packages.

The exact format of the requirements file can be found in ``pip``'s
`documentation <http://www.pip-installer.org/en/latest/requirements.html>`_.


Default Requirements File
=========================

The default requirements file is broken into sections to make reading it
clearer.


Python
------

``ipython``
^^^^^^^^^^^

``nose``
^^^^^^^^

Documentation
-------------

``Sphinx``
^^^^^^^^^^

``Jinja``
^^^^^^^^^

``Pygments``
^^^^^^^^^^^^

``docutils``
^^^^^^^^^^^^

Django
------

``django``
^^^^^^^^^^

``pytz``
^^^^^^^^

``py-bcrypt``
^^^^^^^^^^^^^

Django Util Apps
----------------

``South``
^^^^^^^^^

``django-secure``
^^^^^^^^^^^^^^^^^

``django-debug-toolbar``
^^^^^^^^^^^^^^^^^^^^^^^^

``django-nose``
^^^^^^^^^^^^^^^

``factory-boy``
^^^^^^^^^^^^^^^

``django-model-utils``
^^^^^^^^^^^^^^^^^^^^^^

Django Apps
-----------

``django-compressor``
^^^^^^^^^^^^^^^^^^^^^

``django-appconf``
^^^^^^^^^^^^^^^^^^

``lxml``
^^^^^^^^

``BeautifulSoup``
^^^^^^^^^^^^^^^^^

``django-waffle``
^^^^^^^^^^^^^^^^^


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
