django-statici18n
=================

.. image:: https://travis-ci.org/zyegfryed/django-statici18n.png?branch=master
   :alt: Build Status
   :target: https://travis-ci.org/zyegfryed/django-statici18n

.. image:: https://coveralls.io/repos/zyegfryed/django-statici18n/badge.png?branch=master
  :target: https://coveralls.io/r/zyegfryed/django-statici18n?branch=master

A Django app that provides helper for generating JavaScript catalog to static
files.

Overview
--------

When dealing with internationalization in JavaScript code, Django provides the
`javascript_catalog view`_ which sends out a JavaScript code library with
functions that mimic the gettext interface, plus an array of translation
strings.

At first glance, it works well and everything is fine. But, because
`javascript_catalog view`_ is generating JavaScript catalog dynamically on
each request, it's `adding an overhead`_ that can be an issue with site growth.

That's what ``django-statici18n`` is for:

    Collecting JavaScript catalogs from each of your Django apps (and any other
    place you specify) into a single location that can easily be served in
    production.

The main website for ``django-statici18n`` is
`github.com/zyegfryed/django-statici18n`_ where you can also file tickets.

.. _javascript_catalog view: https://docs.djangoproject.com/en/1.6/topics/i18n/translation/#module-django.views.i18n
.. _adding an overhead: https://docs.djangoproject.com/en/1.6/topics/i18n/translation/#note-on-performance
.. _github.com/zyegfryed/django-statici18n: https://github.com/zyegfryed/django-statici18n

Supported Django Versions
-------------------------

django-statici18n works with all the Django versions officially supported by the
Django project. At the time of writing, these are the 1.8 (LTS), 1.9 and 1.10
series.

Installation
------------

1. Use your favorite Python packaging tool to install ``django-statici18n``
   from `PyPI`_, e.g.::

    pip install django-statici18n

2. Add ``'statici18n'`` to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = [
        # ...
        'statici18n',
    ]

3. Once you have `translated`_ and `compiled`_ your messages, use the
   ``compilejsi18n`` management command::

    python manage.py compilejsi18n

4. Add the ``django.core.context_processors.i18n`` context processor to the
   ``context_processors`` section for your backend in the ``TEMPLATES`` setting
   — it should have already been set by Django::

    TEMPLATES = [
      {
        # ...
        'OPTIONS': {
          'context_processors': {
            # ...
            'django.core.context_processors.i18n',
          },
        },
      },
    ]

5. Edit your template(s) and replace the `dynamically generated script`_ by the
   statically generated one:

  .. code-block:: html+django

    <script src="{{ STATIC_URL }}jsi18n/{{ LANGUAGE_CODE }}/djangojs.js"></script>

.. note::

    By default, the generated catalogs are stored to ``STATIC_ROOT/jsi18n``.
    You can modify the output path and more options by tweaking
    ``django-statici18n`` settings.

**(Optional)**

The following step assumes you're using `django.contrib.staticfiles`_.

5. Edit your template(s) and use the provided template tag:

  .. code-block:: html+django

    {% load statici18n %}
    <script src="{% statici18n LANGUAGE_CODE %}"></script>

6. Or inline the JavaScript directly in your template:

  .. code-block:: html+django

    {% load statici18n %}
    <script>{% inlinei18n LANGUAGE_CODE %}</script>

.. _PyPI: http://pypi.python.org/pypi/django-statici18n
.. _translated: https://docs.djangoproject.com/en/1.10/topics/i18n/translation/#message-files
.. _compiled: https://docs.djangoproject.com/en/1.10/topics/i18n/translation/#compiling-message-files
.. _dynamically generated script: https://docs.djangoproject.com/en/1.10/topics/i18n/translation/#using-the-javascript-translation-catalog
.. _django.contrib.staticfiles: https://docs.djangoproject.com/en/1.10/ref/contrib/staticfiles/
