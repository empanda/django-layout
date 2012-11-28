=========
Templates
=========

This project comes with three built-in templates.

``base.html``
=============

``base.html`` is the base template that all other templates inherit from.

The template is setup to use `Twitter Bootstrap`_ in the responsive mode.
Twitter Bootstrap will provide your project with a simple grid system and
a lot of handy CSS modules.

.. _Twitter Bootstrap: http://twitter.github.com/bootstrap/

The template is also setup to use Django Compressor to join and minify CSS
and JS assets. It's important to use the smallest number of groups that
make sense to reduce the number of HTTP requests that have to be made to
render the page.

CSS files are placed in the head and JS files are placed at the very
bottom of the document to increase page load time.

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

The list of icons for the site. This includes the ``favicon.ico`` as well
as all the mobile touch icons.

<body>
------

nav
^^^

.. code-block:: html

    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </a>

          <a class="brand" href="#">Project name</a>

          <div class="nav-collapse collapse">

            <ul class="nav">
              <li class="active"><a href="#">Home</a></li>
              <li><a href="#about">About</a></li>
              <li><a href="#contact">Contact</a></li>
              <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown">Dropdown <b class="caret"></b></a>
                <ul class="dropdown-menu">
                    <li><a href="#">Action</a></li>
                    <li><a href="#">Another action</a></li>
                    <li><a href="#">Something else here</a></li>
                    <li class="divider"></li>
                    <li class="nav-header">Nav header</li>
                    <li><a href="#">Separated link</a></li>
                    <li><a href="#">One more separated link</a></li>
                </ul>
              </li>
            </ul>

            <form class="navbar-form pull-right">
              <input class="span2" type="text" placeholder="Email">
              <input class="span2" type="password" placeholder="Password">
              <button type="submit" class="btn">Sign in</button>
            </form>

          </div>
        </div>
      </div>
    </div>

The navigation block for Twitter Bootstrap. Change this to meet your
needs.

content
^^^^^^^

.. code-block:: html

    <div class="container">
      {% block content %}
        <div class="hero-unit">
          <h1>Hello, world!</h1>
          <p>This is a template for a simple marketing or informational website. It includes a large callout called the hero unit and three supporting pieces of content. Use it as a starting point to create something more unique.</p>
          <p><a class="btn btn-primary btn-large">Learn more &raquo;</a></p>
        </div>
        <div class="row">
          <div class="span4">
            <h2>Heading</h2>
            <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>
            <p><a class="btn" href="#">View details &raquo;</a></p>
          </div>
          <div class="span4">
            <h2>Heading</h2>
            <p>Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus. Etiam porta sem malesuada magna mollis euismod. Donec sed odio dui. </p>
            <p><a class="btn" href="#">View details &raquo;</a></p>
          </div>
          <div class="span4">
            <h2>Heading</h2>
            <p>Donec sed odio dui. Cras justo odio, dapibus ac facilisis in, egestas eget quam. Vestibulum id ligula porta felis euismod semper. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
            <p><a class="btn" href="#">View details &raquo;</a></p>
          </div>
        </div>
      {% endblock %}


footer
^^^^^^

.. code-block:: html

    <hr>

    <footer>
      {% block  %}
        <p>&copy; Company 2012</p>
      {% endblock %}
    </footer>

jQuery
^^^^^^

.. code-block:: html

    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="{{ STATIC_URL }}vendor/js/jquery-1.8.2.min.js"><\/script>')</script>

bootstrap.js
^^^^^^^^^^^^

.. code-block:: html

    {% compress js %}
      <script src="{{ STATIC_URL }}vendor/js/bootstrap.js"></script>
    {% endcompres %}

main.js
^^^^^^^

.. code-block:: html

    {% compress js %}
      <script src="{{ STATIC_URL }}js/ga.js"></script>
      <script src="{{ STATIC_URL }}js/main.js"></script>
    {% endcompres %}


``404.html``
============

``404.html`` is the template that is used to render ``404`` errors.

This template is just a simple extension on the ``base.html`` template. It
provides a basic `not found` page.

``500.html``
============

``500.html`` is the template that is used to render ``500`` errors.

.. note::

    This template is not provided with any context. So you can't use any
    variables inside it, including common ones like ``{{ STATIC_URL }}``.

This template cannot extend ``base.html`` because it doesn't have access
to any context variables.

By default it's just a very simple error page. Hopefully your users won't
see this much.
