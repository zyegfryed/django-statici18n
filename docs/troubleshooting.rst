Troubleshooting
===============

Files are not served during development
---------------------------------------

By default ``django-statici18n`` doesn't rely on
:mod:`django.contrib.staticfiles`, so you have to serve the generated catalogs
files with the Django dev server. For example::

    # urls.py
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = patterns('',
        # ... the rest of your URLconf goes here ...
    ) + static(settings.STATIC_URL, document_root=settings.STATICI18N_ROOT)

However, when using the :mod:`statici18n` template tag you should first
integrate ``django-static18n`` with :mod:`django.contrib.staticfiles`. See
:ref:`staticfiles-configuration` for more information.

.. note::

    Even if the setup looks a bit more tedious at first sight, using the
    :mod:`statici18n` template tag is the recommended way and it will make
    your life easier in the long run.


Catalog is empty
----------------

``django-statici18n`` requires that the locale paths are available in the settings.
So just add :django:setting:`LOCALE_PATHS=('/path/to/your/locale/directory',)` to the settings file.

For more information on how Django discovers translations, refer to the `official documentation`_.

.. _official documentation: https://docs.djangoproject.com/en/1.7/topics/i18n/translation/#how-django-discovers-translations

