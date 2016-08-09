import pytest

from statici18n import utils


def test_default_filename_with_language():
    filename = utils.get_filename('en', 'djangojs', 'js')
    assert filename == 'en/djangojs.js'

    filename = utils.get_filename('en-us', 'djangojs', 'js')
    assert filename == 'en-us/djangojs.js'


def test_default_filename_with_locale():
    filename = utils.get_filename('en_GB', 'djangojs', 'js')
    assert filename == 'en-gb/djangojs.js'


def test_default_filename_with_outputformat():
    filename = utils.get_filename('en', 'djangojs', 'js')
    assert filename == 'en/djangojs.js'

    filename = utils.get_filename('en', 'djangojs', 'json')
    assert filename == 'en/djangojs.json'

    filename = utils.get_filename('en', 'djangojs', 'yaml')
    assert filename == 'en/djangojs.yaml'


def custom_func(locale, domain):
    return "{0}-{1}.js".format(locale, domain)


def test_filename_with_custom_func(settings):
    settings.STATICI18N_FILENAME_FUNCTION = 'test_utils.custom_func'

    filename = utils.get_filename('es', 'djangojs')
    assert filename == 'es-djangojs.js'


def test_filename_with_no_func(settings):
    settings.STATICI18N_FILENAME_FUNCTION = 'no_func'

    with pytest.raises(ImportError):
        utils.get_filename('es', 'djangojs')
