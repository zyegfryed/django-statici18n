from statici18n import utils


def test_default_filename():
    filename = utils.default_filename('en', 'djangojs')
    assert filename == 'en/djangojs.js'


def test_default_filename_with_locale():
    filename = utils.default_filename('en_GB', 'djangojs')
    assert filename == 'en-gb/djangojs.js'
