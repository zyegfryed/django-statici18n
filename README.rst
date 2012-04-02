=================
django-statici18n
=================

This is a Django app that provides helper for generating Javascript catalog
to static files.

When dealing with internationalization in Javascript code, Django provides the
`javascript_catalog view`_ which sends out a JavaScript code library with
functions that mimic the gettext interface, plus an array of translation
strings.

At first glance, it works well and everything is fine. However, for a given
language, each request will generates the same identical catalog.

That's what ``statici18n`` is for:

    Collecting Javascript catalogs from each of your Django apps (and any other
    place you specify) into a single location that can easily be served in
    production.

The main website for django-staticfiles is
`github.com/zyegfryed/django-statici18n`_ where you can also file tickets.

.. _javascript_catalog view: http://docs.djangoproject.com/en/1.4/topics/i18n/translation/#module-django.views.i18n

Installation
------------

- Use your favorite Python packaging tool to install ``statici18n``
  from `PyPI`_, e.g.::

    pip install django-statici18n

- Added ``'statici18n'`` to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = [
        # ...
        'statici18n',
    ]

- Once you have translated and compiled your messages, use the ``collecti18n``
  management command::

    python manage.py collecti18n

By default, the generated catalogs are stored to ``STATIC_ROOT``.

- Edit your templates and replace the dynamically generated script by the
  statically generated script like this::

    <script src="{{ STATIC_URL }}jsi18n/{{ LANGUAGE_CODE }}/djangojs.js"></script>

.. _github.com/zyegfryed/django-statici18n: http://github.com/zyegfryed/django-statici18n
.. _PyPI: http://pypi.python.org/pypi/django-statici18n
.. _Apache: http://httpd.apache.org/
.. _Lighttpd: http://www.lighttpd.net/
.. _Nginx: http://wiki.nginx.org/
.. _Cherokee: http://www.cherokee-project.com/
