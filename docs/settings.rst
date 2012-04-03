Settings
========

.. currentmodule:: django.conf.settings

.. attribute:: STATICI18N_DOMAIN

    :default: ``'djangojs'``

    The gettext domain to use when generating static files.

    Can be overrided with the -d/--domain option of ``compilejsi18n` command.

    Usually you don't want to do that, as JavaScript messages
    go to the djangojs domain. But this might be needed if you
    deliver your JavaScript source from Django templates.

.. attribute:: STATICI18N_PACKAGES

    :default: ``('django.conf')``

    A list of packages to check for translations.

    Can be overrided with the -p/--package option of ``compilejsi18n`` command.

    Each string in packages should be in Python dotted-package syntax (the
    same format as the strings in INSTALLED_APPS) and should refer to a
    package that contains a locale directory. If you specify multiple
    packages, all those catalogs are merged into one catalog. This is useful
    if you have JavaScript that uses strings from different applications.

.. attribute:: STATICI18N_ROOT

    :default: ``'static'``

    Controls the file path that static files will be written into.

    By default, the file path is relative to the current directory you're
    calling the compilejsi8n command. Thus, it will generally be the static
    directory of your project, and the same one you're delaing with
    django.contrib.staticfiles.


.. attribute:: STATICI18N_OUTPUT_DIR

    :Default: ``'jsi18n'``

    Controls the directory inside STATICI18N_ROOT that generated files will
    be written to.


.. attribute:: STATICI18N_FILENAME_FUNCTION

    :default: ``'statici18n.utils.default_filename'``

    The dotted path to the function that creates the filename.

    The function receives two parameters:

    * ``locale``: a string representation of the locale currently processed

    * ``domain``: a string representation of the gettext domain used to check
      for translations

    By default, the function returns the path ``<locale>/<domain>.js``.

    The final filename is obtained by joining STATICI18N_ROOT,
    STATICI18N_OUTPUT_DIR and STATICI18N_FILENAME_FUNCTION.

    For example, with default settings in place, the Javascript catalog
    generated for the ``en`` locale is the following:
    ``static/jsi18n/en/djangojs.js``

    Missing directories will be created when missing.
