=================
django-statici18n
=================

A Django app that provides helper for generating Javascript catalog to static
files.

When dealing with internationalization in Javascript code, Django provides the
`javascript_catalog view`_ which sends out a JavaScript code library with
functions that mimic the gettext interface, plus an array of translation
strings.

At first glance, it works well and everything is fine. But, because
`javascript_catalog view`_ is generating Javascript catalog dynamically on
each request, it's adding an overhead that can be an issue with site growth.

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

- Add ``'statici18n'`` to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = [
        # ...
        'statici18n',
    ]

- Once you have `translated`_ and `compiled`_ your messages, use the
  ``compilejsi18n``   management command::

    python manage.py compilejsi18n

By default, the generated catalogs are stored to ``static/jsi18n``.

(Optionnal)

The following steps assumes you're using either ``django.contrib.staticfiles``
or ``django-statcifles``.

.. note::

  Although the usage of ``django.contrib.staticfiles`` or ``django-statcifles``
  is not required, django-statici18n really shines when used with those apps.

- Add the ``django.core.context_processors.i18n`` context processor to your
  ``TEMPLATE_CONTEXT_PROCESSORS`` setting - already set by Django by default::

    TEMPLATE_CONTEXT_PROCESSORS = (
      # ...
      'django.core.context_processors.i18n',
    )

- Edit your templates and replace the dynamically generated script by the
  statically generated script like this::

    <script src="{{ STATIC_URL }}jsi18n/{{ LANGUAGE_CODE }}/djangojs.js"></script>

.. _github.com/zyegfryed/django-statici18n: http://github.com/zyegfryed/django-statici18n
.. _PyPI: http://pypi.python.org/pypi/django-statici18n
.. _translated: http://docs.djangoproject.com/en/1.4/topics/i18n/translation/#message-files
.. _compiled: http://docs.djangoproject.com/en/1.4/topics/i18n/translation/#compiling-message-files
