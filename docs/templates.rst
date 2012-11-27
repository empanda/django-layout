=========
Templates
=========

This project comes with three built-in templates.

``base.html``
=============

``base.html`` is the base template that all other templates inherit from.

The following is a line by line walk through of the template.

<head>
------

charset
^^^^^^^

.. code-block:: html

    <meta charset="utf-8">

Sets the character set for the rest of the file to ``utf-8``. The server
should also be sending the HTML pages as ``utf-8``, but specifying it
again here isn't a bad thing.

X-UA-Compatible
^^^^^^^^^^^^^^^

.. code-block:: html

    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">

Tells IE to use the most up to date rendering engine. Also, if `Google
Chrome Frame`_ is installed, it is used.

.. _Google Chrome Frame: https://developers.google.com/chrome/chrome-frame/

title
^^^^^

.. code-block:: django

    <title>{% block title %}{% endblock %}</title>

The ``<title>`` element contents can be set using the ``title`` block.

description
^^^^^^^^^^^

.. code-block:: django

    <meta name="description" content="{% block meta_description %}{% endblock %}">

The meta description can be set using the ``meta_description`` block.

author
^^^^^^

.. code-block:: django

    <meta name="author" content="{% block meta_author %}{% endblock %}">

The meta author can be set using the ``meta_author`` block.

viewport
^^^^^^^^

.. code-block:: html

    <meta name="viewport" content="width=device-width">

The viewport is set to be compatible with mobile devices while using
Twitter Bootstrap.

bootstrap.css
^^^^^^^^^^^^^

.. code-block:: django

    {% compress css %}
      <link rel="stylesheet" href="{{ STATIC_URL }}vendor/css/bootstrap.css">
      <link rel="stylesheet" href="{{ STATIC_URL }}vendor/css/bootstrap-responsive.css">
    {% endcompress %}

Django compressor is used to combine and minify the Twitter Bootstrap
files. This way we can use the development versions while in development
and then painlessly switch to a joined, minified and compressed version
automatically in production.

main.css
^^^^^^^^

.. code-block:: django

    {% compress css %}
      <link rel="stylesheet" href="{{ STATIC_URL }}css/main.css">
    {% endcompress %}

Django Compressor is also used when referencing our CSS files internally.

Because we Django Compressor here you should aim to keep your CSS in
logical files and not just include all the properties in ``main.css``.  To
include additional CSS files, just list them after ``main.css`` inside the
``{% compress css %}`` block.

HTML5 Shiv
^^^^^^^^^^

.. code-block:: html

    <!--[if lt IE 9]>
    {% compress js %}
      <script src="{{ STATIC_URL }}vendor/js/html5shiv-printshiv.js"></script>
    {% endcompress %}
    <![endif]-->

Use the html5shiv for IE 8. This allows us to use HTML5 elements without
worry.

REQUEST_ID
^^^^^^^^^^

.. code-block:: django

    <script>var REQUEST_ID='{{ request.id }}';</script>

The unique ``request.id`` attribute for the request. This can be useful
for debugging and error reporting.

icons
^^^^^

.. code-block:: django

    <link rel="shortcut icon" href="{{ STATIC_URL }}ico/favicon.ico">
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="{{ STATIC_URL }}ico/apple-touch-icon-144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="{{ STATIC_URL }}ico/apple-touch-icon-114-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="{{ STATIC_URL }}ico/apple-touch-icon-72-precomposed.png">
    <link rel="apple-touch-icon-precomposed" href="{{ STATIC_URL }}ico/apple-touch-icon-57-precomposed.png">


<body>
------

``404.html``
============

``404.html`` is the template that is used to render ``404`` errors.

``500.html``
============

``500.html`` is the template that is used to render ``500`` errors.

.. note::

    This template is not provided with any context. So you can't use any
    variables inside it, including common ones like ``{{ STATIC_URL }}``.
