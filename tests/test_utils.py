import pytest

from statici18n import utils


###############################################################################

def test_default_filename_with_language():
    filename = utils.default_filename('en', 'djangojs')
    assert filename == 'en/djangojs.js'

    filename = utils.default_filename('en-us', 'djangojs')
    assert filename == 'en-us/djangojs.js'


def test_default_filename_with_locale():
    filename = utils.default_filename('en_GB', 'djangojs')
    assert filename == 'en-gb/djangojs.js'


###############################################################################

def test_get_filename_default():
    filename = utils.get_filename('fr-CH', 'djangojs')
    assert filename == 'fr-ch/djangojs.js'


def js_filename(locale, domain):
    return "{0}-{1}.js".format(locale, domain)


def test_get_filename_custom(settings):
    settings.STATICI18N_FILENAME_FUNCTION = 'test_utils.js_filename'

    filename = utils.get_filename('es', 'djangojs')
    assert filename == 'es-djangojs.js'


def test_get_filename_not_exists(settings):
    settings.STATICI18N_FILENAME_FUNCTION = 'my_filename'

    with pytest.raises(ImportError):
        utils.get_filename('es', 'djangojs')
