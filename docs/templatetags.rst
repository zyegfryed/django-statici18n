.. module:: statici18n
   :synopsis: An app for handling JavaScript catalog.

Template tags
=============

.. highlight:: html+django

statici18n
----------

.. function:: templatetags.statici18n.statici18n(locale)

.. versionadded:: 0.4

.. warning::

   Behind the scenes, it's a thin wrapper around the `static template tag`_.
   Therefore, ensure that ``django.contrib.staticfiles`` is enabled - i.e is
   added to your ``INSTALLED_APPS`` - before proceeding.

Builds the full JavaScript catalog URL for the given locale, by joining the
``STATICI18N_OUTPUT_DIR`` and ``STATICI18N_FILENAME_FUNCTION`` settings::

    {% load statici18n %}
    <script src="{% statici18n LANGUAGE_CODE %}"></script>

This is especially useful when using a non-local storage backend to
`deploy files to a CDN`_ or when using `cache busting`_ to serve files.

.. _static template tag: https://docs.djangoproject.com/en/1.6/ref/contrib/staticfiles/#static
.. _deploy files to a CDN: https://docs.djangoproject.com/en/1.6/howto/static-files/#serving-static-files-from-a-cloud-service-or-cdn
.. _cache busting: https://docs.djangoproject.com/en/1.6/ref/contrib/staticfiles/#cachedstaticfilesstorage
