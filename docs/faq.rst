FAQ
===

.. _staticfiles-configuration:

How to configure static files with ``django-statici18n``?
---------------------------------------------------------

Due to the modularity of :mod:`django.contrib.staticfiles` it's easy to use
the storage facility provided by tweaking some settings.

There's two solution leveraging the :django:setting:`STATICFILES_FINDERS`
setting:

* using a dedicated application, or,

* using a dedicated directory to hold the catalog files.

In the next sections, we'll detail with examples how to use both solutions.
Choose the one that best fits your needs and/or taste.

See `static files management`_ for more information.

Once setup is in place, run the :djadmin:`compilejsi18n` command to
compile/update the Javascript catalog files followed by the
:djadmin:`collectstatic` command to generate the static files::

    # compile/update Javascript catalog files...
    $ python manage.py compilejsi18n

    # then, collect static files.
    $ python manage.py collectstatic


.. _static files management: http://django.readthedocs.org/en/1.6.x/ref/contrib/staticfiles/


.. _staticfiles-app-configuration:

Using a placeholder app
~~~~~~~~~~~~~~~~~~~~~~~

You need to have the ``AppDirectoriesFinder`` finder enabled (the default).

Create a minimal app with a ``static`` subdirectory. For example, let's create
an app named **ì18n** to hold the generated catalogs::

    cd /path/to/your/django/project
    mkdir -p i18n/static
    touch i18n/__init__.py i18n/models.py

Your project layout should then looks like the following::

    example_project
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
    |   |-- __init__.py
    |   |-- models.py          <-- A placeholder file to enable app loading
    |   `-- static             <-- The output directory of catalog files
    |       `-- jsi18n
    |-- manage.py
    |-- project
    |   |-- __init__.py
    |   |-- locale
    |   |-- settings.py
    |   |-- templates
    |   `-- urls.py
    `-- public
        `-- static             <-- The output directory of collected
            `-- jsi18n             static files for deployment

Then update your settings accordingly. Following the previous example::

    # project/settings.py

    # ... the rest of your settings here ...

    INSTALLED_APPS = (
        'django.contrib.staticfiles',
        # ...
        'statici18n',
        'i18n',
    )

    STATIC_ROOT = os.path.join(BASE_DIR, "public", "static")
    STATICI18N_ROOT = os.path.join(BASE_DIR, "i18n", "static")


.. _staticfiles-directory-configuration:

Using a placeholder directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This approach extends the :django:setting:`STATICFILES_DIRS` setting.
You need to have the ``FileSystemFinder`` finder enabled (the default).

Following is an example project layout::

    example_project
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
    |   |-- static             <-- Directory holding catalog files
    |   |   `-- jsi18n
    |   |-- templates
    |   `-- urls.py
    `-- public
        `-- static             <-- The output directory of collected
                                   static files for deployment

Then update your settings accordingly. Following the previous example::

    # project/settings.py

    # ... the rest of your settings here ...

    INSTALLED_APPS = (
        'django.contrib.staticfiles',
        # ...
        'statici18n',
    )

    STATIC_ROOT = os.path.join(BASE_DIR, "public", "static")
    STATICI18N_ROOT = os.path.join(BASE_DIR, "project", "static")
    STATICFILES_DIRS += (STATICI18N_ROOT,)


Can I use the generated catalog with RequireJS_?
------------------------------------------------

Yes. You just need some boilerplate configuration to export the object
reference, like the following::

    # settings.py
    STATICI18N_ROOT = os.path.join(BASE_DIR, "project", "static")
    STATICFILES_DIRS += (STATICI18N_ROOT,)

    # app.js
    require.config({
            baseUrl: "static/js",
            paths: {
                    "jsi18n": "../jsi18n/{{ LANGUAGE_CODE }}/djangojs",
            },
            shim: {
                    "jsi18n":
                    {
                            exports: 'django'
                    },
            }
    })

    // Usage
    require(["jquery", "jsi18n"], function($, jsi18n) {
        console.log(jsi18n.gettext('Internationalization is fun !'));
            // > "L’internationalisation, c'est cool !"
    })

.. _RequireJS: http://requirejs.org/
