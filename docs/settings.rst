Settings
========

.. currentmodule:: django.conf.settings

.. attribute:: STATICI18N_DOMAIN

    :default: ``'djangojs'``

    The gettext domain to use when generating static files.

    Can be overrided with the ``-d/--domain`` option of ``compilejsi18n`` command.

    Usually you don't want to do that, as JavaScript messages go to the
    ``djangojs`` domain. But this might be needed if you deliver your JavaScript
    source from Django templates.

.. attribute:: STATICI18N_PACKAGES

    :default: ``('django.conf')``

    A list of packages to check for translations.

    Can be overrided with the ``-p/--package`` option of :ref:`compilejsi18n`
    command.

    Each string in packages should be in Python dotted-package syntax (the
    same format as the strings in ``INSTALLED_APPS``) and should refer to a
    package that contains a locale directory. If you specify multiple
    packages, all those catalogs are merged into one catalog. This is useful
    if you have JavaScript that uses strings from different applications.

.. attribute:: STATICI18N_ROOT

    :default: ``STATIC_ROOT``

    Controls the file path that catalog files will be written into.

.. attribute:: STATICI18N_OUTPUT_DIR

    :Default: ``'jsi18n'``

    Controls the directory inside :attr:`STATICI18N_ROOT` that generated files
    will be written into.

.. attribute:: STATICI18N_FILENAME_FUNCTION

    :default: ``'statici18n.utils.default_filename'``

    The dotted path to the function that creates the filename.

    The function receives two parameters:

    * ``locale``: a string representation of the locale currently processed

    * ``domain``: a string representation of the gettext domain used to check
      for translations

    By default, the function returns the path ``'<locale>/<domain>.js'``.

    The final filename is resulted by joining :attr:`STATICI18N_ROOT`,
    :attr:`STATICI18N_OUTPUT_DIR` and :attr:`STATICI18N_FILENAME_FUNCTION`.

    For example, with default settings in place and ``STATIC_ROOT = 'static'``,
    the JavaScript catalog generated for the ``en_GB`` locale is:
    ``'static/jsi18n/en_GB/djangojs.js'``.

    Use the legacy function ``statici18n.utils.legacy_filename`` to
    generate a filename with the language code derived from the
    ``django.utils.translation.trans_real import to_language``.

.. attribute:: STATICI18N_NAMESPACE

    :default: ``None``

    Javascript identifier to use as namespace. This is useful when we want to
    have separate translations for the global and the namespaced contexts.
    The final gettext will be put under `window.<namespace>.gettext` rather
    than the `window.gettext`. Useful for pluggable modules that need JS i18n.
