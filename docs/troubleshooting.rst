Troubleshooting
===============

Files are not served during development
---------------------------------------

Because ``django-statici18n`` relies on static files, you have to serve them with the Django dev server. To do so, refer to the Django documentation about `serving static files during development`_.

In case you're not using ``staticfiles`` app, you might want to use something like the following::

    # urls.py
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = patterns('',
        # ... the rest of your URLconf goes here ...
    ) + static(settings.STATIC_URL, document_root=settings.STATICI18N_ROOT)

.. _serving static files during development: https://docs.djangoproject.com/en/1.6/howto/static-files/#serving-static-files-during-development
