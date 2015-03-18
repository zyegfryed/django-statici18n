Changelog
=========

v1.1.2 (2015 Mar 18)
--------------------

* Updated dependencies
* Added Python 3.2 and Django 1.7 test support
* Updated requirements to include the newest version of appconf and changed
  setup.py to reflect appconf requirement (thanks Nicholas Lockhart)

v1.1.1 (2014 Nov 17)
--------------------

* Added empty catalog entry to troubleshooting section (thanks @eduardo-matos)

v1.1 (2014 Jan 12)
-------------------

* Added i18ninline template tag (thanks @jezdez)
* Added RequireJS entry to the FAQ (thanks @Ewjoachim)

v1.0.1 (2013 Nov 20)
--------------------

* Improved documentation clarity and cross-references
* Updated classifiers

v1.0.0 (2013 Nov 18)
--------------------

* Added Django 1.6 support (thanks @ryanbutterfield)
* Improved documentation
* Added full test suite

.. warning::

   The following changes are backward-incompatible with the previous release.

* Now use ``STATIC_ROOT`` as default value for ``STATICI18N_ROOT``.

v0.4.5 (2013 Jun 13)
--------------------

* Fixed ImportError exception.

v0.4.4 (2013 Jun 12)
--------------------

* Fixed issue in  filename function now using language code instead of
  locale name. Thanks Marc Kirkwood.
* Fixed Django documentation URLs to use 1.5 release.
* Improved the overall documentation.

v0.4.3 (2013 Jun 10)
--------------------

* Updated documentation reference to Django 1.5.
* Fixed a typo in documentation.

v0.4.2 (2013 Feb 04)
--------------------

* Fixing compiling the JS formats for non-default languages. Thanks @jezdez.

v0.4.1 (2012 Oct 17)
--------------------

* Worked around an issue with unescaped string literals in Django JavaScript
  i18n code. Thanks @jezdez.

v0.4.0 (2012 Apr 04)
--------------------

* Added statici18n template tag.

v0.3.1 (2012 Apr 03)
--------------------

* Added license

* Fixed installation error due to missing manifests file.


v0.3.0 (2012 Apr 03)
--------------------

* Added Sphinx documentation.

* Added many settings managed with django-appconf.

v0.2.0 (2012 Apr 02)
--------------------

.. warning::

   The following changes are backward-incompatible with the previous release.

* Renamed ``collecti18n`` command to ``compilejsi18n``.

* Now use current static directory instead of ``STATIC_ROOT`` for sane defaults.

v0.1.0 (2012 Apr 02)
--------------------

* Initial commit.
