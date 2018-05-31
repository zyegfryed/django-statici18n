Management commands
===================

.. highlight:: console

.. _compilejsi18n:

compilejsi18n
-------------

Collect JavaScript catalog files in a single location.

Some commonly used options are:

``-l LOCALE`` or ``--locale=LOCALE``
    The locale to process. Default is to process all but if for some reason I18N
    features are disabled, only `settings.LANGUAGE_CODE` will be processed.

``-d DOMAIN`` or ``--domain=DOMAIN``
    Override the gettext domain. By default, the command uses the ``djangojs``
    gettext domain.

``-p PACKAGES`` or ``-packages=PACKAGES``
    A list of packages to check for translations. Default is ``'django.conf'``.
    Use multiple times to add more.

``-o OUPUT_DIR`` or ``--output=OUTPUT_DIR``
    Output directory to store generated catalogs. Defaults to the joining path
    of :attr:`~django.conf.settings.STATICI18N_ROOT` and
    :attr:`~django.conf.settings.STATICI18N_OUTPUT_DIR`.

``-f OUTPUT_FORMAT`` or ``--format=OUTPUT_FORMAT``
    Format of the output catalog. Options are:
        * ``js``,
        * ``json``.

    Defaults to ``js``.

``-n NAMESPACE`` or ``--namespace=NAMESPACE``
    The final gettext will be put with window.SpecialBlock.gettext rather
    than the window.gettext. This is useful for pluggable modules which
    need Javascript i18n.

    Defaults to ``None``.

For a full list of options, refer to the ``compilejsi18n`` management command
help by running::

   $ python manage.py compilejsi18n --help


.. note::

    Missing directories will be created on-the-fly by the command when invoked.
