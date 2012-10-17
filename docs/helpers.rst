=======
Helpers
=======

.. module:: statici18n
   :synopsis: An app for handling Javascript catalog.

Template tags
=============

.. highlight:: html+django

statici18n
----------

.. function:: templatetags.statici18n.statici18n(locale)

.. versionadded:: 0.4

.. warning::

   Behind the scenes, it's a thin wrapper around staticfiles's `static template
   tag`_. Therefore, it requires either django-staticfiles>=1.1 or Django=>1.4
   to work.

Builds the full Javascript catalog URL for the given locale, by joining the
STATICI18N_OUTPUT_DIR and STATICI18N_FILENAME_FUNCTION settings::

    {% load statici18n %}
    <script src="{% statici18n LANGUAGE_CODE %}"></script>

This is especially useful when using a non-local storage backend to `deploy
files to a CDN`_ or when using `cache busting`_ to serve files.

.. _`static template tag`: https://docs.djangoproject.com/en/1.4/ref/contrib/staticfiles/#static
.. _`deploy files to a CDN`: https://docs.djangoproject.com/en/dev/howto/static-files/#serving-static-files-from-a-cloud-service-or-cdn
.. _`cache busting`: http://django-staticfiles.readthedocs.org/en/latest/helpers/#cachedstaticfilesstorage
