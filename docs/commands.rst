Management Commands
===================

.. highlight:: console

.. compilejsi18n:

compilejsi18n
-------------

Collect Javascript catalog files in a single location.

Some commonly used options are:

``-l LOCALE`` or ``--locale=LOCALE``
    The locale to process. Default is to process all.

``-d DOMAIN`` or ``--domain=DOMAIN``
    Override the gettext domain. By default, the command uses the djangojs
    gettext domain.

``-p PACKAGES`` or ``-packages=PACKAGES``
    A list of packages to check for translations. Default is 'django.conf'.
    Use multiple times to add more.

``-o OUPUT_DIR`` or ``--output=OUTPUT_DIR``
    Output directory to store generated catalogs. Defaults to static/jsi18n.

For a full list of options, refer to the compilejsi18n management command help
by running::

   $ python manage.py compilejsi18n --help

