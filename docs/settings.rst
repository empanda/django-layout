.. _settings:

========
Settings
========

This file outlines the settings and setting files used in this project.

The settings files are all located inside the ``settings`` package at the
top level of the project.

This package contains two settings files by default, ``base.py`` and
``local.py.example``.

.. _base-settings-file:

``base.py``
===========

This is the base settings file for the project. It contains all of the
default settings across all the different environments.

It is split into logical sections:

.. _directory-setup-settings:

Directory setup
---------------

A lot of settings in Django require full paths instead of relative paths.
We can use some tricks inside the settings file to enable us to determine
the location of the project and then use relative paths from there.


.. attribute:: PROJECT_DIR

:py:const:`PROJECT_DIR` is the absolute path to the package for the project.

.. code-block:: python

    PROJECT_DIR = os.path.dirname(os.path.realpath(project_module.__file__))


.. attribute:: PROJECT_ROOT

:py:const:`PROJECT_ROOT` is the absolute path to the root directory of the project.

.. code-block:: python

    PROJECT_ROOT = os.path.dirname(PROJECT_DIR)


.. attribute:: VAR_ROOT

:py:const:`VAR_ROOT` is the absolute path to the ``var/`` directory inside
the root directory of the project.

.. code-block:: python

    VAR_ROOT = os.path.join(PROJECT_ROOT, 'var')


.. attribute:: BIN_ROOT

:py:const:`BIN_ROOT` is the absolute path to the ``bin/`` directory inside
the root directory of the project.

.. code-block:: python

    BIN_ROOT = os.path.join(PROJECT_ROOT, 'bin')


.. _generic-django-project-settings:

Generic Django project settings
-------------------------------

.. attribute:: SITE_ID

:py:const:`SITE_ID` is a unique ID for each Django site. It's used as part
of the ``django.contrib.sites`` application.

.. code-block:: python

    SITE_ID = 1

See also, Django's documentation for :py:const:`SITE_ID`
    https://docs.djangoproject.com/en/1.4/ref/settings/#site-id


.. _admin-managers-settings:

Admin/managers
--------------

.. attribute:: ADMINS

:py:const:`ADMINS` is the list of administrators for the site. You should
change this to be your name and email address. These are the people who
will see the error traceback emails.

.. code-block:: python

    ADMINS = (
        ('You', 'your@email'),
    )

See also, Django's documentation for :py:const:`ADMINS`
    https://docs.djangoproject.com/en/1.4/ref/settings/#admins


.. attribute:: MANAGERS

:py:const:`MANAGERS` is the list of managers for the site. By default
Django only uses this emails to send 404 error emails. However the sending
of 404 error emails if off by default. By default this is just set to
the same as :py:const:`ADMINS`.

.. code-block:: python

    MANAGERS = ADMINS

See also, Django's documentation for :py:const:`MANAGERS`
    https://docs.djangoproject.com/en/1.4/ref/settings/#managers


.. _localization-settings:

Localization settings
---------------------

.. attribute:: TIME_ZONE

:py:const:`TIME_ZONE` specifies the default timezone for the installation.

.. code-block:: python

    TIME_ZONE = 'America/Los_Angeles'


See also, Django's documentation for :py:const:`TIME_ZONE`
        https://docs.djangoproject.com/en/1.4/ref/settings/#time-zone


.. attribute:: USE_TZ

Setting :py:const:`USE_TZ` to ``True`` enables timezone support and use
timezone aware datetimes. Timezones help give context to datetimes and it
makes sense to always use them to reduce ambiguity.

.. code-block:: python

    USE_TZ = True

See also, Django's documentation for :py:const:`USE_TZ`
    https://docs.djangoproject.com/en/1.4/ref/settings/#use-tz


.. attribute:: USE_I18N

Setting :py:const:`USE_I18N` to ``True`` enables Django's
internationalization support.

.. code-block:: python

    USE_I18N = True

See also, Django's documentation for :py:const:`USE_I18N`
    https://docs.djangoproject.com/en/1.4/ref/settings/#use-i18n


.. attribute:: USE_L10N

Setting :py:const:`USE_L10N` to ``True`` enables Django's localization
support.

.. code-block:: python

    USE_L10N = True

See also, Django's documentation for :py:const:`USE_L10N`
    https://docs.djangoproject.com/en/1.4/ref/settings/#use-l10n


.. attribute:: LANGUAGE_CODE

:py:const:`LANGUAGE_CODE` controls the default language for the site. We
set it to English by default.

.. code-block:: python

    LANGUAGE_CODE = 'en'

See also, Django's documentation for :py:const:`LANGUAGE_CODE`
    https://docs.djangoproject.com/en/1.4/ref/settings/#language-code


.. attribute:: LANGUAGES

:py:const:`LANGUAGES` is a list of all the languages that this site
supports. By default since many of our sites don't use anything other than
English, it is just set to English.

If your site supports other languages you can add them here.

.. note::

    Django supports many languages out of the box, and all of Django's UI
    is translated into those languages. However since the rest of your site
    isn't translated, it tends to be a better user experience to just list the
    languages that your entire site supports.

.. code-block:: python

    LANGUAGES = (
        ('en', 'English'),
    )

See also, Django's documentation for :py:const:`LANGUAGES`
    https://docs.djangoproject.com/en/1.4/ref/settings/#languages

Django's supported languages
    https://github.com/django/django/blob/stable/1.4.x/django/conf/global_settings.py#L47

.. _installed-apps-settings:

Installed apps
--------------

.. attribute:: INSTALLED_APPS

:py:const:`INSTALLED_APPS` is the list of installed Django applications
for the site. This list is separated into sections to make it clear where
the app is from.

.. code-block:: python

    INSTALLED_APPS = (
        # Local Apps
        # '{{ project_name }}.apps.',

        # Third Party Apps
        'south',
        'compressor',
        'waffle',
        'django_nose',
        'djangosecure',
        'djcelery',

        # Django Apps
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.admin',
        'django.contrib.admindocs',
    )

See also, Django's documentation for :py:const:`INSTALLED_APPS`
    https://docs.djangoproject.com/en/1.4/ref/settings/#installed-apps


.. _project-urls-and-media-settings:

Project URLS and media settings
-------------------------------

.. attribute:: ROOT_URLCONF

:py:const:`ROOT_URLCONF` is the python path to the root URL module to use
for the project.

.. code-block:: python

    ROOT_URLCONF = '{{ project_name }}.urls'

See also, Django's documentation for :py:const:`ROOT_URLCONF`
    https://docs.djangoproject.com/en/1.4/ref/settings/#root-urlconf


.. attribute:: LOGIN_URL

:py:const:`LOGIN_URL` is the URL which points to the login view. This
setting is used primarily to redirect to the login page when a view comes
across a permissions error.

.. code-block:: python

    LOGIN_URL = '/login/'

See also, Django's documentation for :py:const:`LOGIN_URL`
    https://docs.djangoproject.com/en/1.4/ref/settings/#login-url


.. attribute:: LOGOUT_URL

:py:const:`LOGOUT_URL` is the URL which points to the logout view.

.. code-block:: python

    LOGOUT_URL = '/logout/'

See also, Django's documentation for :py:const:`LOGOUT_URL`
    https://docs.djangoproject.com/en/1.4/ref/settings/#logout-url


.. attribute:: LOGIN_REDIRECT_URL

:py:const:`LOGIN_REDIRECT_URL` points the URL that the user should be
redirected to after a successful login where no ``next`` parameter is
provided to the login view.

.. code-block:: python

    LOGIN_REDIRECT_URL = '/'

See also, Django's documentation for :py:const:`LOGIN_REDIRECT_URL`
    https://docs.djangoproject.com/en/1.4/ref/settings/#login-redirect-url


.. attribute:: STATIC_URL

:py:const:`STATIC_URL` is the URL where static files are served from.

.. note::

    By default we use the relative URL ``/static/``, but this setting can
    take a complete URL such as ``http://static.example.com/``. This is
    handy when you are using a CDN or other file hosting provider.

.. code-block:: python

    STATIC_URL = '/static/'

See also, Django's documentation for :py:const:`STATIC_URL`
    https://docs.djangoproject.com/en/1.4/ref/settings/#static-url


.. attribute:: MEDIA_URL

:py:const:`MEDIA_URL` is the URL where uploaded media will be served from.

.. note::

    By default we use the relative URL ``/uploads/``, but this setting can
    take a complete URL such as ``http://uploads.example.com/``. This is
    handy when you are using a CDN or other file hosting provider.

.. code-block:: python

    MEDIA_URL = '/uploads/'

See also, Django's documentation for :py:const:`MEDIA_URL`
    https://docs.djangoproject.com/en/1.4/ref/settings/#media-url


.. attribute:: STATIC_ROOT

:py:const:`STATIC_ROOT` is the absolute path to where the
``django.contrib.staticfiles`` app will place the files it finds when
running the ``collectstatic`` management command.

By default it's ``var/static/``.

.. code-block:: python

    STATIC_ROOT = os.path.join(VAR_ROOT, 'static')

See also, Django's documentation for :py:const:`STATIC_ROOT`
    https://docs.djangoproject.com/en/1.4/ref/settings/#static-root


.. attribute:: MEDIA_ROOT

:py:const:`MEDIA_ROOT` is the absolute path to where Django will store
uploaded files when using the default file storage system.

By default it's ``var/uploads/``.

.. code-block:: python

    MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')

See also, Django's documentation for :py:const:`MEDIA_ROOT`
    https://docs.djangoproject.com/en/1.4/ref/settings/#media-root


.. attribute:: STATICFILES_DIRS

:py:const:`STATICFILES_DIRS` lists the directories that the
``django.contrib.staticfiles`` app will look for files.

By default it's ``{{ project_name }}/static/``.

.. code-block:: python

    STATICFILES_DIRS = (
        os.path.join(PROJECT_DIR, 'static'),
    )

See also, Django's documentation for :py:const:`STATICFILES_DIRS`
    https://docs.djangoproject.com/en/1.4/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS


.. attribute:: STATICFILES_FINDERS

:py:const:`STATICFILES_FINDERS` is a list of classes that find static
files for the ``django.contrib.staticfiles`` app. We are adding the Django
Compressor finder to the list.

.. code-block:: python

    STATICFILES_FINDERS += (
        'compressor.finders.CompressorFinder',
    )

See also, Django's documentation for :py:const:`STATICFILES_FINDERS`
    https://docs.djangoproject.com/en/1.4/ref/contrib/staticfiles/#std:setting-STATICFILES_FINDERS


.. _templates-settings:

Templates
---------

Settings that control where Django finds templates and how they are
rendered.

.. attribute:: TEMPLATE_DIRS

:py:const:`TEMPLATE_DIRS` is a list of directories that Django will look
in for templates.

By default it will only look in ``{{ project_name }}/templates/``.

.. code-block:: python

    TEMPLATE_DIRS = (
        os.path.join(PROJECT_DIR, 'templates'),
    )

See also, Django's documentation for :py:const:`TEMPLATE_DIRS`
    https://docs.djangoproject.com/en/1.4/ref/settings/#template-dirs


.. attribute:: TEMPLATE_CONTEXT_PROCESSORS

:py:const:`TEMPLATE_CONTEXT_PROCESSORS` is a list of functions that modify
every template context that is rendered with :py:class:`RequestContext`.

.. code-block:: python

    TEMPLATE_CONTEXT_PROCESSORS += (
        'django.core.context_processors.request',
    )

See also, Django's documentation for :py:const:`TEMPLATE_CONTEXT_PROCESSORS`
    https://docs.djangoproject.com/en/1.4/ref/settings/#template-context-processors

Django's documentation for :py:func:`django.core.context_processors.request`
    https://docs.djangoproject.com/en/1.4/ref/templates/api/#django-core-context-processors-request


.. _middleware-settings:

Middleware
----------

.. attribute:: MIDDLEWARE_CLASSES

:py:const:`MIDDLEWARE_CLASSES` is a list of classes that act on each
request and response.

By default we use ten pieces of middleware.

.. py:data:: {{ project_name }}.utils.middleware.request_id.RequestIdMiddleware

Adds a unique ``request.id`` attribute to each request.

This middleware is useful when trying to trace a request through the logs.

If you are using the
:py:class:`{{ project_name }}.utils.logging.formatters.JSONFormatter`
for logging and you include a request object in your ``extra`` dictionary
passed to logging calls, this ID will be displayed in the final JSON
output.

.. py:data:: django.middleware.common.CommonMiddleware

Performs URL rewriting based on the :py:const:`APPEND_SLASH` and
:py:const:`PREPEND_WWW` settings.

If :py:const:`APPEND_SLASH` is ``True`` and the initial URL doesn't end
with a slash, and it is not found in the URLconf, then a new URL is formed
by appending a slash at the end. If this new URL is found in the URLconf,
then Django redirects the request to this new URL. Otherwise, the initial
URL is processed as usual.

For example, ``foo.com/bar`` will be redirected to ``foo.com/bar/`` if you
don't have a valid URL pattern for ``foo.com/bar`` but do have a valid
pattern for ``foo.com/bar/``.

See also, Django's documentation for :py:data:`django.middleware.common.CommonMiddleware`
    https://docs.djangoproject.com/en/1.4/ref/middleware/#django.middleware.common.CommonMiddleware

.. py:data:: django.contrib.sessions.middleware.SessionMiddleware

Enables Django's sessions application. Handles the creation of the session
cookie and session storage.

See also, Django's documentation for :py:data:`django.contrib.sessions.middleware.SessionMiddleware`
    https://docs.djangoproject.com/en/1.4/ref/middleware/#django.contrib.sessions.middleware.SessionMiddleware

.. py:data:: django.middleware.transaction.TransactionMiddleware

Handles database transactions based on the Django request/response cycle.

It starts a new transaction at the begging of a request and commits the
transaction once the request has been completed successfully. If the
request fails for any reason it performs a rollback on the transaction.

See also, Django's documentation for :py:data:`django.middleware.transaction.TransactionMiddleware`
    https://docs.djangoproject.com/en/1.4/ref/middleware/#django.middleware.transaction.TransactionMiddleware

.. py:data:: django.middleware.csrf.CsrfViewMiddleware

Handles CSRF verifcation on POST requests.

See also, Django's documentation for :py:data:`django.middleware.csrf.CsrfViewMiddleware`
    https://docs.djangoproject.com/en/1.4/ref/middleware/#django.middleware.csrf.CsrfViewMiddleware

.. py:data:: django.contrib.auth.middleware.AuthenticationMiddleware

Adds the :py:attr:`user` attribute, representing the currently-logged-in user, to every incoming :py:class:`HttpRequest` object.

See also, Django's documentation for :py:data:`django.contrib.auth.middleware.AuthenticationMiddleware`
    https://docs.djangoproject.com/en/1.4/ref/middleware/#django.contrib.auth.middleware.AuthenticationMiddleware

.. py:data:: django.contrib.messages.middleware.MessageMiddleware

Enables cookie- and session-based message support.

See also, Django's documentation for :py:data:`django.contrib.messages.middleware.MessageMiddleware`
    https://docs.djangoproject.com/en/1.4/ref/middleware/#django.contrib.messages.middleware.MessageMiddleware

.. py:data:: djangosecure.middleware.SecurityMiddleware

Enables all the features of ``django-secure``. Primarily it adds headers
to the response for additional security.

See also, Django Secure's documentation for :py:data:`djangosecure.middleware.SecurityMiddleware`
    https://django-secure.readthedocs.org/en/latest/middleware.html#securitymiddleware

.. py:data:: django.middleware.clickjacking.XFrameOptionsMiddleware

Adds the ``X-Frame-Options`` header to each request. See the
:py:const:`X_FRAME_OPTIONS` setting.

See also, Django's documentation for :py:data:`django.middleware.clickjacking.XFrameOptionsMiddleware`
    https://docs.djangoproject.com/en/1.4/ref/middleware/#django.middleware.clickjacking.XFrameOptionsMiddleware

.. py:class:: waffle.middleware.WaffleMiddleware

Enables all of the features of ``django_waffle``. Primarily it handles the
cookies that ``django_waffle`` uses.

.. code-block:: python

    MIDDLEWARE_CLASSES = (
        '{{ project_name }}.utils.middleware.request_id.RequestIdMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.transaction.TransactionMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'djangosecure.middleware.SecurityMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'waffle.middleware.WaffleMiddleware',
    )

See also, Django's documentation for :py:const:`MIDDLEWARE_CLASSES`
    https://docs.djangoproject.com/en/1.4/ref/settings/#middleware-classes


.. _security-settings:

Security settings
-----------------

.. attribute:: X_FRAME_OPTIONS

:py:const:`X_FRAME_OPTIONS` controls the contents of the ``X-Frame-Options``
header that is set when using the
:py:class:`django.middleware.clickjacking.XFrameOptionsMiddleware` middleware.

This header controls whether or not a browser will show the page in an
iframe. This can be used to prevent `clickjacking`_.

.. _clickjacking: https://docs.djangoproject.com/en/1.4/ref/clickjacking/#an-example-of-clickjacking

It can either be ``SAMEORIGIN`` or ``DENY``.

``SAMEORIGIN`` allows for the page to put into a frame if it's on the same
site.

``DENY`` never allows the page to be shown in a frame.

We set it to ``DENY`` for all pages as it is the most secure option.

If you need to override this for a specific, view Django provides
decorators to turn it off for just that view. See `Django's documentation
on clickjacking`_.

.. _Django's documentation on clickjacking: https://docs.djangoproject.com/en/1.4/ref/clickjacking/#how-to-use-it

.. code-block:: python

    X_FRAME_OPTIONS = 'DENY'

See also, Django's documentation for :py:const:`X_FRAME_OPTIONS`
    https://docs.djangoproject.com/en/1.4/ref/settings/#x-frame-options


.. attribute:: INTERNAL_IPS

:py:const:`INTERNAL_IPS` controls which IP addresses Django sees as being
`internal`.

The Django Debug Toolbar app will only show the toolbar when the request
originates from a IP address listed in :py:const:`INTERNAL_IPS`.

.. code-block:: python

    INTERNAL_IPS = ('127.0.0.1',)

See also, Django's documentation for :py:const:`INTERNAL_IPS`
    https://docs.djangoproject.com/en/1.4/ref/settings/#internal-ips


.. attribute:: SESSION_COOKIE_HTTPONLY

Setting :py:const:`SESSION_COOKIE_HTTPONLY` to ``True`` sets the Django
session cookie to use the ``HttpOnly`` flag on the cookie. This disables
access to the cookie via Javascript. It reduces the risk of session
hijacking because no Javascript on the page, malicious or otherwise, will
have access to the session cookie.

.. code-block:: python

    SESSION_COOKIE_HTTPONLY = True

See also, Django's documentation for :py:const:`SESSION_COOKIE_HTTPONLY`
    https://docs.djangoproject.com/en/1.4/ref/settings/#session-cookie-httponly

    Learn more about the HttpOnly flag
        https://en.wikipedia.org/wiki/HTTP_cookie#HttpOnly_cookie


.. attribute:: SECURE_CONTENT_TYPE_NOSNIFF

Some browsers will try to guess the content types of the assets that they
fetch, overriding the ``Content-Type`` header. While this can help display
sites with improperly configured servers, it can also pose a security
risk.

If your site serves user-uploaded files, a malicious user could upload a
specially-crafted file that would be interpreted as HTML or Javascript by
the browser when you expected it to be something harmless.

To learn more about this header and how the browser treats it, you can
read about it on the `IE Security Blog`_.

.. _IE Security Blog: http://blogs.msdn.com/b/ie/archive/2008/09/02/ie8-security-part-vi-beta-2-update.aspx

To prevent the browser from guessing the content type, and force it to
always use the type provided in the ``Content-Type`` header, you can pass
the ``X-Content-Type-Options: nosniff`` header.

Setting :py:const:`SECURE_CONTENT_TYPE_NOSNIFF` to ``True`` adds this
header to all requests.

.. code-block:: python

    SECURE_CONTENT_TYPE_NOSNIFF = True

See also, Django Secure's Documentation for :py:const:`SECURE_CONTENT_TYPE_NOSNIFF`
    http://django-secure.readthedocs.org/en/latest/settings.html#secure-content-type-nosniff


.. attribute:: SECURE_BROWSER_XSS_FILTER

Some browsers have to ability to block content that appears to be an `XSS
attack`_. They work by looking for Javascript content in the GET or POST
parameters of a page. If the Javascript is replayed in the server's
response the page is blocked from rendering and a error page is shown
instead.

The `X-XSS-Protection header`_ is used to control the operation of the
XSS filter.

To enable the XSS filter in the browser, and force it to always block
suspected XSS attacks, you can pass the ``X-XSS-Protection: 1; mode=block``
header.

Setting :py:const:`SECURE_BROWSER_XSS_FILTER` to ``True`` will add this
header to all requests.

.. warning::
    The XSS filter does not prevent XSS attacks on your site, and you
    should ensure that you are taking all other possible mesaures to
    prevent XSS attacks. The most obvious of these is validating and
    sanitizing all input.

.. _XSS attack: http://en.wikipedia.org/wiki/Cross-site_scripting
.. _X-XSS-Protection header: http://blogs.msdn.com/b/ie/archive/2008/07/02/ie8-security-part-iv-the-xss-filter.aspx


.. code-block:: python

    SECURE_BROWSER_XSS_FILTER = True

See also, Django Secure's Documentation for :py:const:`SECURE_BROWSER_XSS_FILTER`
    http://django-secure.readthedocs.org/en/latest/settings.html#secure-browser-xss-filter


.. attribute:: PASSWORD_HASHERS

:py:const:`PASSWORD_HASHERS` is a list of classes that Django will use to
hash passwords as part of it's authentication system.

The top class of the list is the hasher that is used. The other hasher are
listed so that Django can upgrade users with old hashes to default hasher.

We change the default password hasher to
:py:class:`django.contrib.auth.hashers.BCryptPasswordHasher` so that our
passwords will be hashed using the ``bcrypt``.

`bcrypt`_ is a hashing algorithm based on the `blowfish encryption
cipher`_. It is specifically designed to slow and hard to compute so that
brute force attacks are less effective.

.. warning::

    :py:class:`django.contrib.auth.hashers.BCryptPasswordHasher` requires
    the :ref:`py-bcrypt-requirement` package to work.
    :ref:`py-bcrypt-requirement` is a C package and may not be available
    on all hosting platforms.

.. _bcrypt: http://en.wikipedia.org/wiki/Bcrypt

.. _blowfish encryption cipher: http://en.wikipedia.org/wiki/Blowfish_(cipher)

.. code-block:: python

    PASSWORD_HASHERS = (
        'django.contrib.auth.hashers.BCryptPasswordHasher',
        'django.contrib.auth.hashers.PBKDF2PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
        'django.contrib.auth.hashers.SHA1PasswordHasher',
        'django.contrib.auth.hashers.MD5PasswordHasher',
        'django.contrib.auth.hashers.CryptPasswordHasher',
    )

See also, Django's documentation for :py:const:`PASSWORD_HASHERS`
    https://docs.djangoproject.com/en/dev/topics/auth/#how-django-stores-passwords


.. _test-settings:

Test settings
-------------

.. attribute:: TEST_RUNNER

:py:const:`TEST_RUNNER` controls which test runner Django will use when
``manage.py test`` is used.

We change it to use the :py:class:`django_nose.NoseTestSuiteRunner` so
that Django will use :ref:`nose-requirement` to find and run our tests.

.. code-block:: python

    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

See also, Django's documentation for :py:const:`TEST_RUNNER`
    https://docs.djangoproject.com/en/1.4/ref/settings/#test-runner


.. _email-settings-base:

Email settings
--------------

.. attribute:: DEFAULT_FROM_EMAIL

:py:const:`DEFAULT_FROM_EMAIL` sets the default ``From:`` address on
emails sent via Django.

You should change this to ``no-reply@DOMAIN_NAME.com`` where
``DOMAIN_NAME`` is your websites domain.

.. code-block:: python

    DEFAULT_FROM_EMAIL = 'no-reply@localhost'

See also, Django's documentation for :py:const:`DEFAULT_FROM_EMAIL`
    https://docs.djangoproject.com/en/1.4/ref/settings/#default-from-email


.. attribute:: SERVER_EMAIL

:py:const:`SERVER_EMAIL` sets the ``From:`` email address that Django uses
to send it's error traceback emails. By default we just set it to the same
as :py:const:`DEFAULT_FROM_EMAIL`.

.. code-block:: python

    SERVER_EMAIL = DEFAULT_FROM_EMAIL

See also, Django's documentation for :py:const:`SERVER_EMAIL`
    https://docs.djangoproject.com/en/1.4/ref/settings/#server-email


.. attribute:: EMAIL_SUBJECT_PREFIX

:py:const:`EMAIL_SUBJECT_PREFIX` is the string that Django will prefix the
subject of the error traceback emails.

.. code-block:: python

    EMAIL_SUBJECT_PREFIX = '[Django - {{ project_name }}] '


See also, Django's documentation for :py:const:`EMAIL_SUBJECT_PREFIX`
    https://docs.djangoproject.com/en/1.4/ref/settings/#email-subject-prefix


.. _django-compressor-settings:

Django Compressor settings
--------------------------

.. attribute:: COMPRESS_PARSER

:py:const:`COMPRESS_PARSER` controls which HTML parser Django Compressor
will use when parsing ``{% templatetag openblock %} compress {% templatetag closeblock %}`` template blocks.

We set it to ``lxml`` because it's a super fast XML/HTML parser.

.. warning::

    :py:class:`compressor.parser.LxmlParser` requires the
    :ref:`lxml-requirement` package to work.  :ref:`lxml-requirement` is a
    C package and may not be available on all hosting platforms.

.. code-block:: python

    COMPRESS_PARSER = 'compressor.parser.LxmlParser'

See also, Django Compressor's Documentation for :py:const:`COMPRESS_PARSER`
    https://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_PARSER


.. attribute:: COMPRESS_STORAGE

:py:const:`COMPRESS_STORAGE` controls the storage backend that Django
Compressor will use when writing out the final compressed files.

We set it to :py:class:`compressor.storage.GzipCompressorFileStorage`
which is a simple extension of the default file storage sys. It simply
creates two copies of each compressed file. One is the regular file and
one it a gzip compressed version.

For example, it would create ``main.ae413.css`` and ``main.ae413.css.gz``.

This allow a web server (when configured correctly) to server the gzipped
version of the file directly to clients that support gzip. It can reduce
server load and also can work well with a CDN that may not support
on-the-fly gzip compression.

.. code-block:: python

    COMPRESS_STORAGE = 'compressor.storage.GzipCompressorFileStorage'

See also, Django Compressor's Documentation for :py:const:`COMPRESS_STORAGE`
    https://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_STORAGE


.. attribute:: COMPRESS_OFFLINE

:py:const:`COMPRESS_OFFLINE` controls the mode that Django Compressor runs
in. We use Django Compressor in `offline` mode to reduce server load and
to ease transition to multiple servers or a CDN.

.. note::

    As an alternative to `offline` mode you can use `online` mode. In
    `online` mode Django Compressor will build and cache the compressed
    static files during the request/response cycle. While this mode is
    simpler to setup initially, it quickly becomes a problem when using
    multiple servers or a CDN. We avoid any later transition issue by just
    using `offline` mode from the start.


In `offline` mode you have to run ``manage.py compress`` before each
deploy. This command will parse through your templates and build the
cached CSS and JS files.

Compressing the static files in `offline` mode does have some limitations.
You have to specify the context variables that you want available inside
``{% templatetag openblock %} compress {% templatetag closeblock %}`` template tags explicitly. See the
`COMPRESS_OFFLINE_CONTEXT`_ setting.

.. note::

    By default the :py:const:`COMPRESS_OFFLINE_CONTEXT` contains only the
    :py:const:`STATIC_URL` context variable.

.. _COMPRESS_OFFLINE_CONTEXT: http://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE_CONTEXT

.. code-block:: python

    COMPRESS_OFFLINE = True

See also, Django Compressor's Documentation for :py:const:`COMPRESS_OFFLINE`
    https://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OFFLINE


.. attribute:: COMPRESS_CSS_FILTERS

:py:const:`COMPRESS_CSS_FILTERS` is the list of filters that Django
Compressor will use when compressing CSS files.

By default we enable three filters.

:py:class:`compressor.filters.css_default.CssAbsoluteFilter` parses CSS
files for ``url()`` properties and replaces relative URLS with absolute
ones.

:py:class:`compressor.filters.datauri.CssDataUriFilter` parses CSS for
images referenced by ``url()`` and if the image is smaller than
:py:const:`COMPRESS_DATA_URI_MAX_SIZE` it will compile the image into a
`data URI`_ directly inside the CSS file.

Using data URIs instead of referencing images via URLs reduces the number
of HTTP requests that the client has to make to render the page. Less HTTP
requests means less round-trips and faster page load times.

Also, data URIs can alleviate some of the need of CSS sprite images, because it
allows small images to be embedded directly into the CSS file.

.. warning::

    Data URIs aren't supported in every browser. Most notably IE 6 and 7
    don't support them at all. If support for IE 6 or 7 is important to
    you, remove :py:class:`compressor.filters.datauri.CssDataUriFilter`
    from the list. Also, more obscure browsers may not support data URIs.
    Using CSS image sprites many be a good fallback option. For a full
    list of browsers that support data URIs see
    http://caniuse.com/datauri.

:py:class:`compressor.filters.cssmin.CSSMinFilter` runs the entire CSS
file through a CSS minifier to remove whitespace and comments. This
reduces the size of the final CSS output.

.. _data URI: http://en.wikipedia.org/wiki/Data_URI_scheme

.. code-block:: python

    COMPRESS_CSS_FILTERS = (
        'compressor.filters.css_default.CssAbsoluteFilter',
        'compressor.filters.datauri.CssDataUriFilter',
        'compressor.filters.cssmin.CSSMinFilter',
    )

See also, Django Compressor's Documentation for :py:const:`COMPRESS_CSS_FILTERS`
    https://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_CSS_FILTERS


.. attribute:: COMPRESS_CSS_HASHING_METHOD

:py:const:`COMPRESS_CSS_HASHING_METHOD` controls how Django Compressor
determines if a CSS file has new changes. By default it
uses the mtime of the files.

By setting it to ``content`` we change this to hash the contents of the
files. Hashing the contents of the files is slower, but more accurate and
works better across multiple servers and/or developer workstations. Also,
because we are using Django Compressor in `offline` mode the slowness
really has no effect.

.. code-block:: python

    COMPRESS_CSS_HASHING_METHOD = 'content'

See also, Django Compressor's Documentation for :py:const:`COMPRESS_CSS_HASHING_METHOD`
    https://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_CSS_HASHING_METHOD


.. attribute:: COMPRESS_DATA_URI_MAX_SIZE

:py:const:`COMPRESS_DATA_URI_MAX_SIZE` controls the size of files that
will be converted into data URIs inside the CSS files. By default we set
it to 30KB to avoid the IE 8 issue.

See :py:class:`compressor.filters.datauri.CssDataUriFilter` in the
:py:const:`COMPRESS_CSS_FILTERS` setting.

.. warning::

    IE 8 doesn't support `data URIs larger than 32KB`_. IE versions 9+
    support data URIs up to 4GB in size.

.. _data URIs larger than 32KB: http://msdn.microsoft.com/en-us/library/cc848897(v=vs.85).aspx

.. code-block:: python

    COMPRESS_DATA_URI_MAX_SIZE = 30 * 1024  # 30KB

See also, Django's documentation for :py:const:`COMPRESS_DATA_URI_MAX_SIZE`
    https://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_DATA_URI_MAX_SIZE


.. attribute:: COMPRESS_JS_FILTERS

:py:const:`COMPRESS_JS_FILTERS` is the list of filters that Django
Compressor will apply to Javascript files. By default we only use one
filter.

:py:class:`compressor.filters.closure.ClosureCompilerFilter` will pass the
contents of the JS files into `Google Closure Compiler`_ for JS
minification. This minifier requires the Google Closure Compiler binary,
see the :py:const:`COMPRESS_CLOSURE_COMPILER_BINARY` setting.

.. _Google Closure Compiler: https://developers.google.com/closure/compiler/

.. code-block:: python

    COMPRESS_JS_FILTERS = (
        'compressor.filters.closure.ClosureCompilerFilter',
    )

See also, Django's documentation for :py:const:`COMPRESS_JS_FILTERS`
    https://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_JS_FILTERS


.. attribute:: COMPRESS_CLOSURE_COMPILER_BINARY

:py:const:`COMPRESS_CLOSURE_COMPILER_BINARY` tells Django Compressor where
to find the Google Closure Compiler binarywhen using the
:py:class:`compressor.filters.closure.ClosureCompilerFilter` filter.

We include Google Closure Compiler binary with the project distribution at
``bin/closure_compiler.jar``. All you need is `Java`_ to run it.

.. _Java: http://www.java.com/en/

.. code-block:: python

    COMPRESS_CLOSURE_COMPILER_BINARY = 'java -jar %s' % os.path.join(
        BIN_ROOT, 'closure_compiler.jar')

See also, Django's documentation for :py:const:`COMPRESS_CLOSURE_COMPILER_BINARY`
    https://django_compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_CLOSURE_COMPILER_BINARY

.. _celery-settings:

Celery settings
---------------

Settings for the celery distributed task queue. Below is the
initialization of celery for Django.

.. code-block:: python

    import djcelery
    djcelery.setup_loader()


.. attribute:: CELERY_TIMEZONE

:py:const:`CELERY_TIMEZONE` sets the timezone that celery will use. We set
it to use the same timezone as Django.

.. code-block:: python

    CELERY_TIMEZONE = TIME_ZONE

See also, Celery's documentation for :py:const:`CELERY_TIMEZONE`
    http://docs.celeryproject.org/en/latest/configuration.html#celery-timezone

.. attribute:: CELERYD_HIJACK_ROOT_LOGGER

Setting :py:const:`CELERYD_HIJACK_ROOT_LOGGER` to ``False`` tells celery
to not override our logging configuration. See the :py:const:`LOGGING`
setting.

.. code-block:: python 

    CELERYD_HIJACK_ROOT_LOGGER = False

See also, Celery's documentation for :py:const:`CELERYD_HIJACK_ROOT_LOGGER`
    http://docs.celeryproject.org/en/latest/configuration.html#celeryd-hijack-root-logger

.. _miscellaneous-project-settings:

Miscellaneous project settings
------------------------------

This is the section where you should put additional project settings. Make
sure to document any new settings.

.. _local-settings-file:

``local.py.example``
====================

``local.py.exmaple`` is a settings file that extends the ``base.py``
settings file. It its meant to be used for local development. A new
developer will copy ``local.py.example`` to ``local.py`` so make sure that
the settings in here make sense for local development.

.. _debug-settings:

Debug settings
--------------

The :py:const:`DEBUG` flag controls whether or not Django will operate in
`DEBUG` mode. This should be off when in production.

.. attribute:: DEBUG

.. code-block:: python

    DEBUG = True

See also, Django's documentation for :py:const:`DEBUG`
    https://docs.djangoproject.com/en/1.4/ref/settings/#debug


.. attribute:: TEMPLATE_DEBUG

The :py:const:`TEMPLATE_DEBUG` flag controls whether or not Django will
render tempaltes in `DEBUG` mode. By default this is set to the same value
as :py:const:`DEBUG`. This should be off when in production.

.. code-block:: python

    TEMPLATE_DEBUG = DEBUG

See also, Django's documentation for :py:const:`TEMPLATE_DEBUG`
    https://docs.djangoproject.com/en/1.4/ref/settings/#template-debug


.. attribute:: DEBUG_TOOLBAR

The :py:const:`DEBUG_TOOLBAR` flag controls whether or not the Django
Debug Toolbar is active. This setting meant to make turning on and off
the toolbar easy. See :ref:`DEBUG_TOOLBAR in the Conditional settings
section<if-debug-toolbar-setting>`.

.. code-block:: python

    DEBUG_TOOLBAR = DEBUG


.. attribute:: COMPRESS_ENABLED

The :py:const:`COMPRESS_ENABLED` flag controls whether or not Django
Compressor serves the compressed content or not. By default this option is
set to the same as :py:const:`DEBUG`. You can enable this while
:py:const:`DEBUG` remains ``False`` to test the Django Compression output.

.. code-block:: python

    COMPRESS_ENABLED = DEBUG


.. _database-settings:

Database settings
-----------------

.. attribute:: DATABASES

:py:const:`DATABASES` is a dictionary mapping the different databases that
Django will use.

By default we use `PostgreSQL`_ as the default database. PostgreSQL is a
great :abbr:`RDMS (Relational Database Management System)`. It supports a
ton of features and is generally better than MySQL.

.. _PostgreSQL: http://www.postgresql.org/

.. code-block:: python

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': '{{ project_name }}',
            'USER': '{{ project_name }}',
            'PASSWORD': '',
            'PORT': '',
            'HOST': '',
        }
    }

See also, Django's documentation for :py:const:`DATABASES`
    https://docs.djangoproject.com/en/1.4/ref/settings/#databases

.. _cache-settings-local:

Cache settings
--------------

.. attribute:: CACHES

:py:const:`CACHES` is a dictionary mapping the caches that Django will
use.

By default we just use a dummy cache that accepts any writes, but ignores
them and always returns misses for cache reads.

We set ``KEY_PREFIX`` to the name of the project to reduce the chance of
cache key collisions.

In production this should be set to use `Memcached`_.

.. _Memcached: http://memcached.org/

.. code-block:: python

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
            'KEY_PREFIX': '{{ project_name }}'
        }
    }

See also, Django's documentation for :py:const:`CACHES`
    https://docs.djangoproject.com/en/1.4/ref/settings/#caches

.. _email-settings-local:

Email settings
--------------

.. attribute:: EMAIL_HOST

:py:const:`EMAIL_HOST` is the host that Django will connect to to send
email. If you're just going to send emails directly and not use a email
delivery service you should install a local email server, which Django can
offload email handling to. `Postfix`_ is a good option.

.. _Postfix: http://www.postfix.org/

.. code-block:: python

    EMAIL_HOST = 'localhost'

See also, Django's documentation for :py:const:`EMAIL_HOST`
    https://docs.djangoproject.com/en/1.4/ref/settings/#email-host


.. _logging-settings:

Logging settings
----------------

.. attribute:: LOGGING

:py:const:`LOGGING` is a dictionary configuration for the `Python logging
system`_.

.. _Python logging system: http://docs.python.org/2/library/logging.html

    .. attribute:: version

    This is the version of the dictionary schema. ``1`` is the only valid
    option at this point.

    .. attribute:: disable_existing_loggers

    Setting this to ``True`` will disable any previously registered loggers
    and only use the loggers from this configuration.

    .. attribute:: formatters

    The formatters are used to format log entires for the handler.

        .. attribute:: verbose

        This is the verbose format for the console logger.

        The Python code:

        .. code-block:: python

            logger = logging.getLogger('myapp.tasks')
            logger.info('the task with id #%d failed', 101)

        Produces the log message:

        ``[2012-11-20 12:53:58,503] [INFO] [myapp.tasks] the task with id
        #101 failed``

        .. attribute:: json

        The JSON formatter outputs all the log records fields using JSON.
        This makes it a breeze to parse the log files later.

        The schema used is defined in
        :py:class:`{{ project_name }}.logging.utils.formatters.JSONFormatter`.

        One of the handy features of the JSON formatter is that it will
        output all of the ``extra`` logging information by default without
        you having to specify it in the format beforehand.

        .. note::

            By default the file produced isn't valid JSON. It's just a
            file with a valid JSON object on each line. You can process
            the JSON log file several ways.

            You can add commas at the end of each line except the last
            line and add brackets ``[`` ``]`` at the beginning and end of
            file. This makes the whole file valid JSON and you can just
            run ``json.load('app.json.log')`` to load all the entries.

            The other option you have is to parse the file line by line.
            For example:

            .. code-block:: python

                with open('app.json.log') as logfile:
                    for line in logfile:
                        logline = json.loads(line)

            I tend to prefer this method because it doesn't require
            creating objects for the entire JSON file in memory before you
            can do any processing.

        .. note::

            Just because the file contains JSON data doesn't mean that you
            can only process it using JSON tools.

            The file is also just a text file with one log entry per line.
            This means that you can still do processing with all the
            normal text manipulation and filtering tools that you are
            used to. ``grep`` still works just fine for filtering.

        .. warning::

            The JSON formatter is quite verbose and stores a lot of data
            by default. Each log line will be at between 500 - 1,000 bytes
            in length.

            Disk space is cheap and verbose logging can be critical when
            trying to debug a production system.

            Normally this won't be a problem because it still means you
            can store about 100,000 log messages per 100MB of disk space.
            Also, because of the verbosity of JSON, the log files will
            compress down really well with a 15-30x compression ratio.
            Meaning you could store 3,000,000 log messages per 100MB when
            compressed.

        The Python code:

        .. code-block:: python

            logger = logging.getLogger('myapp.tasks')
            logger.info('the task with id #%d failed', 101, extra={'ip': '127.0.0.1', 'id': 10)

        Produces the log message:

        .. note::

            The message here is shown as multiple lines for
            readability, normally the log message will appear all on one
            line.

        .. code-block:: javascript

            {
                "extra": {
                    "ip": "127.0.0.1",
                    "id": 10
                },
                "process": {
                    "process": 9168,
                    "processName": "MainProcess",
                    "threadName": "MainThread",
                    "thread": 140735211397504
                },
                "file": {
                    "funcName": "main",
                    "pathname": "test.py",
                    "lineno": 116,
                    "module": "test",
                    "filename": "test.py"
                },
                "time": {
                    "relativeCreated": 13.112068176269531,
                    "asctime": "2012-11-21T10:02:06.612837Z",
                    "created": 1353492126.612837
                },
                "logger": {
                    "levelno": 10,
                    "name": "main",
                    "levelname": "DEBUG"
                },
                "message": {
                    "msg": "the task with id #%d failed",
                    "message": "the task with id #101 failed",
                    "args": [101]
                }
            }

    .. attribute:: filters

    Filters filter log records before they are sent to the handler.

        .. attribute:: require_debug_false

        Only lets log records through when :py:const:`DEBUG` is set to
        ``False``. This is a handy filter to use when you only want a
        handler to work in production.

    .. attribute:: handlers

    Handlers decide how formatted log records are handled. They can write
    log records to disk or send them out over the network. There are many
    built in handlers, you can see them all at
    http://docs.python.org/2/library/logging.handlers.html.

        .. attribute:: null

        The :py:const:`null` handler just discards all log records. It's
        useful when you need a handler that does nothing.

        .. attribute:: console

        The :py:const:`console` handler prints log records out to
        ``stderr`` using the :py:const:`verbose` formatter.

        .. attribute:: rotating_file

        The :py:const:`rotating_file` handler writes log records out to
        the file ``var/log/app.json.log`` using the :py:const:`json`
        formatter.

        Additionally it will rotate the log file when it reaches 50MB
        in size. It will keep one file back as for some history. This
        means that it will use a maximum of 100MB for logging.

        .. attribute:: watched_file

        The :py:const:`watched_file` handler writes log records out to the
        file ``var/log/app.json.log`` using the JSON formatter,
        additionally it will reopen the file handle if the file is
        moved.

        This is useful when you are using programs like ``logrotate`` to
        do automatic log rotation and compression. Once the file is
        rotated this handler will a new file and continue writing out log
        records.

        .. attribute:: mail_admins

        The :py:const:`mail_admins` handler will email the
        :py:const:`ADMINS` of the site with the log record.

        This is mostly useful as a poor mans exception and error
        reporting.

        By default this handler will only log records that are ``ERROR``
        level or higher and will only log records when :py:const:`DEBUG`
        is ``False``.

    .. attribute:: loggers

    Here is where you can tie specific loggers to handlers. By default we
    only put handlers on the :py:const:`root` logger, but you can be more
    selective for your own needs.

        .. attribute:: root

        We hook the :py:const:`root` logger up to the
        :py:const:`mail_admins`, :py:const:`console` and
        :py:const:`rotating_file` handlers by default.


.. code-block:: python

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'verbose': {
                'format': '[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s',
            },
            'json': {
                '()': '{{ project_name }}.utils.logging.formatters.JSONFormatter',
            },
        },
        'filters': {
            'require_debug_false': {
                '()': 'django.utils.log.RequireDebugFalse',
            },
        },
        'handlers': {
            'null': {
                'class': 'django.utils.log.NullHandler',
            },
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose',
            },
            'rotating_file': {
                'level': 'DEBUG',
                'filters': [],
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'json',
                'encoding': 'utf8',
                'filename': os.path.join(VAR_ROOT, 'log', 'app.json.log'),
                'maxBytes': (1024 * 1024) * 10,  # 50MB
                'backupCount': 1,
            },
            'watched_file': {
                'level': 'DEBUG',
                'filters': [],
                'class': 'logging.handlers.WatchedFileHandler',
                'formatter': 'json',
                'encoding': 'utf8',
                'filename': os.path.join(VAR_ROOT, 'log', 'app.json.log'),
            },
            'mail_admins': {
                'level': 'ERROR',
                'filters': ['require_debug_false'],
                'class': 'django.utils.log.AdminEmailHandler'
            },
        },
        'root': {
            'handlers': ['mail_admins', 'console', 'rotating_file'],
            'level': 'DEBUG',
        },
        'loggers': {
            # Define more specific logger here
        },
    }

See also, Django's documentation for :py:const:`LOGGING`
    https://docs.djangoproject.com/en/1.4/ref/settings/#logging

.. _security-settings-local:

Security settings
-----------------

.. attribute:: SECRET_KEY

The :py:const:`SECRET_KEY` is a string of characters that Django will use
in it's security mechanisms (like password hashing) to improve security.

It should be random, secret, and static. You should use a different one
for each environment.

.. code-block:: python

    SECRET_KEY = 'some auto-generated random characters'

See also, Django's documentation for :py:const:`SECRET_KEY`
    https://docs.djangoproject.com/en/1.4/ref/settings/#secret-key


.. attribute:: SSL

If you are using ``SSL`` for your entire site you should set this to
``True``, otherwise leave it at ``False``. It changes a bunch of settings
to take advantage of your ``SSL`` secured site. See :ref:`Conditional SSL<if-ssl-setting>`
for more information.

.. code-block:: python

    SSL = False

.. _http-proxy-settings-local:

HTTP proxy settings
-------------------

.. attribute:: SECURE_PROXY_SSL_HEADER

:py:const:`SECURE_PROXY_SSL_HEADER` is the header and value of the header
that Django should use to determine if the request was made over
``HTTPS``.

Most Django sites sit behind a reverse proxy (like `Nginx`_) that does HTTP and SSL
negotiation for them. This makes the site scale better and be more robust.
However it also makes it impossible for Django to know if a request was
made securely over ``SSL``.

.. _Nginx: http://wiki.nginx.org/Main

Most web servers can be configured to set a header when the site is
accessed over ``SSL``. This setting controls which header Django can look
at to get that information.

.. warning::

    Using this setting can open up your site to a security issue. If you
    turn this on you'll need to confirm that end users can control the
    value of the header that your using. For more information see the
    `warning that Django gives`_ about this setting.

.. _warning that Django gives: https://docs.djangoproject.com/en/1.4/ref/settings/#secure-proxy-ssl-header

.. code-block:: python

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

See also, Django's documentation for :py:const:`SECURE_PROXY_SSL_HEADER`
    https://docs.djangoproject.com/en/1.4/ref/settings/#secure-proxy-ssl-header


.. _celery-settings-local:

Celery settings
---------------

Celery settings that should be defined differently for each environment.

.. attribute:: BROKER_URL

:py:const:`BROKER_URL` is the configuration URL for the celery message
broker. By default we set it to use redis on localhost.

.. code-block:: python

        BROKER_URL = 'redis://'

See also, Celery's documentation for :py:const:`BROKER_URL`
    http://docs.celeryproject.org/en/latest/configuration.html#broker-url

.. attribute:: CELERY_RESULT_BACKEND

:py:const:`CELERY_RESULT_BACKEND` is the configuration URL for the celery
results backend. By default we set it to use redis on localhost.

.. code-block:: python

    CELERY_RESULT_BACKEND = 'redis://'

See also, Celery's documentation for :py:const:`CELERY_RESULT_BACKEND`
    http://docs.celeryproject.org/en/latest/configuration.html#celery-result-backend

.. attribute:: CELERY_ALWAYS_EAGER

:py:const:`CELERY_ALWAYS_EAGER` controls when the tasks are executed.
Setting it to ``True`` disabled out of process execution and the tasks run
like normal Python functions.

We set it to the same as :py:const:`DEBUG` so that when developing and
testing you don't have to wait for tasks to queue and run asynchronously.

.. code-block:: python

    CELERY_ALWAYS_EAGER = DEBUG

See also, Celery's documentation for :py:const:`CELERY_ALWAYS_EAGER`
    http://docs.celeryproject.org/en/latest/configuration.html#celery-always-eager

.. attribute:: CELERY_EAGER_PROPAGATES_EXCEPTIONS

:py:const:`CELERY_EAGER_PROPAGATES_EXCEPTIONS` controls how exception
handling works when :py:const:`CELERY_ALWAYS_EAGER` is set to ``True``.

:py:const:`CELERY_EAGER_PROPAGATES_EXCEPTIONS` is set to ``True``
exceptions that are raised inside tasks will propagate up to your code and
cause 500 errors. This is what you want when developing so that exceptions
don't pass silently. Also this is needed during tests.

By default we also set this to be ``True`` when
:py:const:`CELERY_ALWAYS_EAGER` is ``True``.

.. code-block:: python

    CELERY_EAGER_PROPAGATES_EXCEPTIONS = CELERY_ALWAYS_EAGER

See also, Celery's documentation for :py:const:`CELERY_EAGER_PROPAGATES_EXCEPTIONS`
    http://docs.celeryproject.org/en/latest/configuration.html#celery-eager-propagates-exceptions


.. _conditional-settings-local:

Conditional settings
--------------------

These settings are controlled via flags earlier in the file. Here we
define what those flags actually do.

.. _if-debug-toolbar-setting:

:py:const:`DEBUG_TOOLBAR`
^^^^^^^^^^^^^^^^^^^^^^^^^

When :py:const:`DEBUG_TOOLBAR` is ``True`` we add debug-toolbar to the
installed apps and middleware settings. This enables Django Debug Toolbar.

.. code-block:: python

    if DEBUG_TOOLBAR:
        INSTALLED_APPS += ('debug_toolbar',)
        MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)


.. _if-ssl-setting:

:py:const:`SSL`
^^^^^^^^^^^^^^^

If :py:const:`SSL` is ``True`` we enable a bunch of additional settings to
improve our use of ``SSL``.

.. code-block:: python

    if SSL:
        SESSION_COOKIE_SECURE = True
        CSRF_COOKIE_SECURE = True
        SECURE_SSL_REDIRECT = True
        WAFFLE_SECURE = True
        # SECURE_HSTS_SECONDS =


.. attribute:: SESSION_COOKIE_SECURE

Setting :py:const:`SESSION_COOKIE_SECURE` to ``True`` adds the ``secure``
flag to the session cookie. This means that the browser will only send
that cookie when the request it made via ``SSL``.

.. code-block:: python

    SESSION_COOKIE_SECURE = True

See also, Django's documentation for :py:const:`SESSION_COOKIE_SECURE`
    https://docs.djangoproject.com/en/1.4/ref/settings/#session-cookie-secure


.. attribute:: CSRF_COOKIE_SECURE

Setting :py:const:`CSRF_COOKIE_SECURE` to ``True`` adds the ``secure``
flag to the CSRF cookie. This means that the browser will only send
that cookie when the request it made via ``SSL``.

.. code-block:: python

    CSRF_COOKIE_SECURE = True

See also, Django's documentation for :py:const:`CSRF_COOKIE_SECURE`
    https://docs.djangoproject.com/en/1.4/ref/settings/#csrf-cookie-secure


.. attribute:: SECURE_SSL_REDIRECT

Setting :py:const:`SECURE_SSL_REDIRECT` to ``True`` enables Django Secure
to redirect any requests that don't come via ``SSL`` to the ``SSL``
version of the URL.

.. code-block:: python

    SECURE_SSL_REDIRECT = True

See also, Django Secure's documentation for :py:const:`SECURE_SSL_REDIRECT`
    http://django-secure.readthedocs.org/en/v0.1.2/settings.html#secure-ssl-redirect


.. attribute:: WAFFLE_SECURE

Setting :py:const:`WAFFLE_SECURE` to ``True`` adds the ``secure``
flag to the waffle cookie. This means that the browser will only send
that cookie when the request it made via ``SSL``.

.. code-block:: python

    WAFFLE_SECURE = True

See also, Django Waffle's documentation for :py:const:`WAFFLE_SECURE`
    http://waffle.readthedocs.org/en/latest/usage.html#global-settings


.. attribute:: SECURE_HSTS_SECONDS

Setting :py:const:`SECURE_HSTS_SECONDS` to a non-zero integer value,
causes Django Secure to set the `HTTP Strict Transport Security header`_
on all responses that do not already have that header.

.. _HTTP Strict Transport Security header: http://django-secure.readthedocs.org/en/v0.1.2/middleware.html#http-strict-transport-security

This will force the browser to only make ``SSL`` connections to that
domain for the number of seconds you have listed.

You should set this to a low number while testing ``SSL``, and then raise
it to a higher number after testing is complete.

You can find out more `HSTS on Wikipedia`_.

.. _HSTS on Wikipedia: http://en.wikipedia.org/wiki/Strict_Transport_Security

.. code-block:: python

    SECURE_HSTS_SECONDS = 120

See also, Django Secure's documentation for :py:const:`SECURE_HSTS_SECONDS`
    http://django-secure.readthedocs.org/en/v0.1.2/settings.html#secure-hsts-seconds


.. _miscellaneous-project-settings-local:

Miscellaneous project settings
------------------------------

This is a section for miscellaneous project specific settings. Each
setting should be documented in full.


.. _additional-environments-settings:

Additional Environments Settings
================================

Each different environment that you application runs in should have a
different settings file based on ``local.py.example``.
