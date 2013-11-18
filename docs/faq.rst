FAQ
===

How to use static storage with ``django-statici18n``?
-----------------------------------------------------

Due to the modularity of ``django.contrib.staticfiles`` it's easy to use the
storage facility provided by tweaking some settings.

There's two solution leveraging the ``STATICFILES_FINDERS`` setting:

* using a dedicated application, or,

* using a dedicated directory to hold the catalog files.

In the next sections, we'll detail with examples how to use both solutions.
Choose the one that best fits your needs and/or taste.

To kown more about the static files app refer to the documentation related to
`static files management`_.

.. _static files management: https://docs.djangoproject.com/en/1.6/ref/contrib/staticfiles/

Using a placeholder app
~~~~~~~~~~~~~~~~~~~~~~~

You need to have the ``AppDirectoriesFinder`` finder enabled (the default).

Create a minimal app with a ``static`` subdirectory. For example, let's create
an app named **ì18n** to hold the generated catalogs::

    mkdir -p i18n/static
    touch i18n/models.py

Your project layout should then looks like the following::

    .
    |-- app
    |   |-- __init__.py
    |   |-- admin.py
    |   |-- locale
    |   |-- models.py
    |   |-- static
    |   |-- templates
    |   |-- tests.py
    |   `-- views.py
    |-- i18n                   <-- Your dedicated app
    |   |-- models.py          <-- A placeholder file to enable app loading
    |   `-- static             <-- The output directory of catalog files
    |-- manage.py
    `-- project
        |-- __init__.py
        |-- locale
        |-- settings.py
        |-- static
        |-- templates
        `-- urls.py

Then update your settings accordingly. Following the previous example::

    # project/settings.py
    [...]
    INSTALLED_APPS += ('i18n',)
    STATICI18N_ROOT = os.path.join(BASE_DIR, "i18n", "static")


Using a placeholder directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This approach extends the ``STATICFILES_DIRS`` setting. You need
to have the ``FileSystemFinder`` finder enabled (the default).

Following is an example project layout::

    .
    |-- app
    |   |-- __init__.py
    |   |-- admin.py
    |   |-- locale
    |   |-- models.py
    |   |-- tests.py
    |   `-- views.py
    |-- manage.py
    |-- project
    |   |-- __init__.py
    |   |-- locale
    |   |-- settings.py
    |   |-- static
    |   |-- templates
    |   `-- urls.py
    `-- static_i18n            <-- Directory holding catalog files

Then update your settings accordingly. Following the previous example::

    # project/settings.py
    [...]
    STATICI18N_ROOT = os.path.join(BASE_DIR, 'static_i18n')
    STATICFILES_DIRS += (STATICI18N_ROOT,)
