Changelog
=========

v2.1.1 (2021 Nov 2)
-------------------

* [PR#52] Fix deprecation warning for AppConfig in Django version 3.2 or
  above (thanks @DmytroLitvinov)

v2.1.0 (2021 May 17)
--------------------

* [PR#50] Fix test under Django 3.2 (thanks @mbakke)
* Add Django 3.2 support
* Drop Django 3.0 support
* Add Python 3.9 support

v2.0.1 (2020 Oct 18)
--------------------

* Switch to codecov as coverage service
* Remove no longer used compatibility code
* Simplify tooling, rely only on tox
* Remove six dependency
* Fix Django and django-appconf minimum version
* Fix Python versions suppport
* Add project URL

v2.0.0 (2020 Sep 18)
--------------------

* [PR#49] Change `force_text` to `force_str` (thanks @bullfest)
* Add Django 3.1 support
* Drop Django 1.8 support
* Drop Django 1.9 support
* Drop Django 1.10 support
* Drop Django 1.11 support
* Drop Django 2.0 support
* Drop Django 2.1 support
* Fix linting issues
* Use Python 3.8 as default version
* Fix travis matrix definition
* Upgrade Sphinx configuration

v1.9.0 (2020 Jan 11)
--------------------

* [PR#48] Update django-appconf, thanks @zetaab
* Add Django 2.2 support
* Add Django 3.0 support
* Drop Python 3.3 support (reached EOL)
* Drop Python 3.4 support (reached EOL)

v1.8.3 (2019 Mar 03)
--------------------

* [PR#44] Fix python3 compatibility about inlinei18n (thanks @outloudvi)
* Add Django 2.1 support
* Fix warning for static templatetag in Django 2.1
* Fix deprecation warning on collections module
* Compress tox matrix definition
* Change travis to use tox under the hood

v1.8.2 (2018 Jun 29)
--------------------

This is a maintenance release due to CI issues.

* Add Python 3.7 classifier
* Fix Travis matrix definition
* Remove Python 3.7 support for Travis

v1.8.1 (2018 Jun 29)
--------------------

* Fix #42: regression issue with packages (thanks @classifaddict)
* Update to latest Python versions
* Add Python 3.7 support

v1.8.0 (2018 May 31)
--------------------

* [PR#39] Serialize packages before giving it to Django (thanks @askoretskiy)
* [PR#41] Add the namespace parameter (thanks @afzaledx and @pomegranited)

v1.7.0 (2018 Feb 11)
--------------------

* Fix documentation (thanks @philipbelesky and @pre101)

.. warning::

   The following changes are backward-incompatible with the previous release.

* Use the plain locale for filename by default (thanks @genonfire)
  For legacy behavior, set ``STATICI18N_FILENAME_FUNCTION`` setting with
  ``'statici18n.utils.legacy_filename'``.

v1.6.1 (2018 Jan 20)
--------------------

* Use ASCII character instead of UTF-8 one to fix build with Python
  3 (thanks @sunpoet)

v1.6.0 (2018 Jan 12)
--------------------

* Add Django 2.0 support (thanks Martin Pauly)
* Drop Python 3.2 support
* Add Python 3.6 support

v1.5.0 (2017 Dec 08)
--------------------

* Load statici18n conf via Django's `AppConfig` (thanks @julen)

v1.4.0 (2017 Jun 22)
--------------------

* Add Django 1.11 support (thanks @bmedx)

v1.3.0 (2017 Jan 19)
--------------------

* Pass language name instead of locale name on Django 1.10 (thanks @quantum5)
* Fix circle-ci builds

v1.2.1 (2016 Aug 20)
--------------------

* Fix Django links to use version 1.10

v1.2.0 (2016 Aug 20)
--------------------

* #17: Mark inlinei18n output as safe (thanks @quantum5)
* #23: Added support for JSON format in command-line based catalog generation
  (thanks @rarguelloF)
* #18: Added support for Django 1.9 and 1.10; this change also drops
  support for Django 1.4, 1.5, 1.6 and 1.7 as they are not officially
  supported by the DSF anymore (thanks @julen)
* #19: Added support for `USE_18N = False` (thanks @julen)

v1.1.5 (2015 Aug 7)
-------------------

* New release due to missing changelog in previous one

v1.1.4 (2015 Aug 7)
---------------------

* Fix #14: compilejsi18n command should skip system checks
  (thanks @bubenkoff and @xolox)
* Update python2.7 to 2.7.10

v1.1.3 (2015 Apr 19)
--------------------

* Add django 1.8 support
* Fix deprecation warning from django.utils.importlib (thanks @ogai)

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
