.. module:: statici18n
   :synopsis: An app for handling JavaScript catalog.

Template tags
=============

.. highlight:: html+django

statici18n
----------

.. function:: templatetags.statici18n.statici18n(locale)

.. versionadded:: 0.4

Builds the full JavaScript catalog URL for the given locale by joining the
:attr:`~django.conf.settings.STATICI18N_OUTPUT_DIR` and
:attr:`~django.conf.settings.STATICI18N_FILENAME_FUNCTION` settings::

    {% load statici18n %}
    <script src="{% statici18n LANGUAGE_CODE %}"></script>

This is especially useful when using a non-local storage backend to
:ref:`deploy files to a CDN <django:staticfiles-from-cdn>` or when using :class:`~django.contrib.staticfiles.storage.CachedStaticFilesStorage` storage to serve files.

.. note::

   Behind the scenes, it's a thin wrapper around the :django:ttag:`static`
   template tag. Therefore, ensure that :mod:`django.contrib.staticfiles` is
   configured before proceeding. See :ref:`staticfiles-configuration` for more
   information.
