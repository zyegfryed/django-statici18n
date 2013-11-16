=================
django-statici18n
=================

.. image:: https://travis-ci.org/zyegfryed/django-statici18n.png?branch=master
   :alt: Build Status
   :target: https://travis-ci.org/zyegfryed/django-statici18n

.. image:: https://coveralls.io/repos/zyegfryed/django-statici18n/badge.png?branch=master
  :target: https://coveralls.io/r/zyegfryed/django-statici18n?branch=master

A Django app that provides helper for generating JavaScript catalog to static
files.

When dealing with internationalization in JavaScript code, Django provides the
`javascript_catalog view`_ which sends out a JavaScript code library with
functions that mimic the gettext interface, plus an array of translation
strings.

At first glance, it works well and everything is fine. But, because
`javascript_catalog view`_ is generating JavaScript catalog dynamically on
each request, it's adding an overhead that can be an issue with site growth.

That's what ``django-statici18n`` is for:

    Collecting JavaScript catalogs from each of your Django apps (and any other
    place you specify) into a single location that can easily be served in
    production.

The main website for ``django-statici18n`` is
`github.com/zyegfryed/django-statici18n`_ where you can also file tickets.

.. _javascript_catalog view: http://docs.djangoproject.com/en/1.5/topics/i18n/translation/#module-django.views.i18n
.. _github.com/zyegfryed/django-statici18n: https://github.com/zyegfryed/django-statici18n

Installation
------------

- Use your favorite Python packaging tool to install ``django-statici18n``
  from `PyPI`_, e.g.::

    pip install django-statici18n

- Add ``'statici18n'`` to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = [
        # ...
        'statici18n',
    ]

- Once you have `translated`_ and `compiled`_ your messages, use the
  ``compilejsi18n``   management command::

    python manage.py compilejsi18n

By default, the generated catalogs are stored to ``static/jsi18n``. You can modify it with the ``django-statici18n`` settings.

**(Optionnal)**

The following steps assumes you're using either ``django.contrib.staticfiles``
or ``django-staticfiles``.

.. note::

  Although the usage of ``django.contrib.staticfiles`` or ``django-staticfiles``
  is not required, ``django-statici18n`` really shines when used with those apps.

- Add the ``django.core.context_processors.i18n`` context processor to your
  ``TEMPLATE_CONTEXT_PROCESSORS`` setting - already set by Django by default::

    TEMPLATE_CONTEXT_PROCESSORS = (
      # ...
      'django.core.context_processors.i18n',
    )

- Edit your templates and replace either the dynamically generated script by the
  statically generated one like this::

    <script src="{{ STATIC_URL }}jsi18n/{{ LANGUAGE_CODE }}/djangojs.js"></script>

  or use the provided template tag like this::

    {% load statici18n %}
    <script src="{% statici18n LANGUAGE_CODE %}"></script>

.. _PyPI: http://pypi.python.org/pypi/django-statici18n
.. _translated: http://docs.djangoproject.com/en/1.5/topics/i18n/translation/#message-files
.. _compiled: http://docs.djangoproject.com/en/1.5/topics/i18n/translation/#compiling-message-files
